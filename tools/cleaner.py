from tkinter import Tk, Text, BOTH, W, N, E, S
from tkinter.ttk import Frame, Button, Label, Style
import argparse
from glob import glob
import os
from PIL import Image, ImageTk
import shutil
import json
import numpy as np
import cv2


def draw_bbox(path, bbox, category_id, class_names, colors):
    """Draws bounding boxes for the image and returns a PIL Image

    Args:
        path (str): Path to image
        bbox (list): List containing all the bbox for the image
        category_id (list): List containing all the category_ids for the image
        class_names (dict): Dictionary containing category_ids as keys and names as values
        colors (dict): Dictionary containing category_ids as keys and colors as values

    Returns:
        img (PIL.Image)
    """
    assert len(bbox) == len(category_id)

    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    for id, bb in zip(category_id, bbox):
        x, y, w, h = map(int, bb)
        r, g, b = map(int, colors[id])

        start_point = (x, y)
        end_point = (x + w, y + h)
        img = cv2.rectangle(img, start_point, end_point, (r, g, b), 2)
        text = f'{class_names[id]}'
        img = cv2.putText(img, text, (x+5, y + 10),
                          cv2.FONT_HERSHEY_SIMPLEX, 0.5, (r, g, b), 2)

    # Scale image for better view
    img = cv2.resize(img, (1000, 1000))

    img = Image.fromarray(img)
    return img


class Cleaner(Frame):
    def __init__(self, folder, images, bbox, category_id, class_names):
        super().__init__()
        self.folder = folder
        self.images = images
        self.bbox = bbox
        self.category_id = category_id
        self.class_names = class_names
        self.colors = {}

        for class_id, _ in self.class_names.items():
            self.colors[class_id] = tuple(np.random.randint(
                0, 255, size=(3), dtype="uint8"))

        # Maintain a file containing deleted images
        self.deleted = open('deleted.txt', 'a')

        if len(self.images) == 0:
            print('Empty Image List')
            exit(0)

        self.current_index = 0
        self.current_image = self.load_image()
        self.initUI()

    def initUI(self):
        self.master.title('Cleaner')
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(4, pad=7)

        lbl = Label(self, text=f'Path: {self.folder}')
        lbl.grid(sticky=W, pady=4, padx=5)

        self.imgarea = Label(self, image=self.current_image)
        self.imgarea.grid(row=1, column=0, columnspan=2, rowspan=4,
                          padx=5, sticky=E+W+S+N)

        fbtn = Button(self, text="Keep",
                      command=lambda: self.handle_btn_click(False))
        fbtn.grid(row=1, column=3)

        dbtn = Button(self, text="Delete",
                      command=lambda: self.handle_btn_click(True))
        dbtn.grid(row=3, column=3,)

        cbtn = Button(self, text="Close", command=lambda: self.quit())
        cbtn.grid(row=4, column=3)

    def load_image(self):
        image_dict = self.images[self.current_index]
        image_id = image_dict['id']
        bbox = self.bbox[image_id]
        category_id = self.category_id[image_id]
        path = os.path.join(
            self.folder, image_dict['file_name'])

        img = draw_bbox(path, bbox, category_id, self.class_names, self.colors)
        img = ImageTk.PhotoImage(img)
        return img

    def handle_btn_click(self, delete):
        if delete:
            print(self.images[self.current_index]['id'], file=self.deleted)

        self.current_index += 1

        if self.current_index > len(self.images)-1:
            print('Done!')
            exit(0)

        self.current_image = self.load_image()
        self.imgarea.configure(image=self.current_image)
        self.imgarea.image = self.current_image

    def quit(self):
        self.deleted.close()
        exit(0)


def main(args):
    print('Parsing annotation data...')
    with open(args.annot) as f:
        annotation_data = json.load(f)

    # Load annotation data in the given range
    images = annotation_data['images'][args.start:args.end]
    bbox = {}  # {'image_id': ['bbox']}
    category_id = {}  # {'image_id': ['category_id']}

    for annotation in annotation_data['annotations']:
        image_id = annotation['image_id']
        if image_id in bbox and image_id in category_id:
            bbox[image_id].append(annotation['bbox'])
            category_id[image_id].append(annotation['category_id'])
        else:
            bbox[image_id] = [annotation['bbox']]
            category_id[image_id] = [annotation['category_id']]

    class_names = {}
    for category in annotation_data['categories']:
        id = category['id']
        class_name = category['name']
        class_names[id] = class_name

    root = Tk()
    root.geometry("1100x1100")
    app = Cleaner(args.folder, images, bbox, category_id, class_names)
    root.mainloop()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--folder", help="Enter image directory",
                        action="store", dest="folder")
    parser.add_argument("-a", "--annotation", help="Enter path to your annotation JSON",
                        action="store", dest="annot")
    parser.add_argument("-s", "--start_range", help="Start Range",
                        action="store", dest="start", type=int)
    parser.add_argument("-e", "--end_range", help="End Range",
                        action="store", dest="end", type=int)
    args = parser.parse_args()
    main(args)
