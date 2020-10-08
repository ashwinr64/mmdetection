_base_ = [
    '../_base_/models/mask_rcnn_r50_fpn.py',
    '../_base_/datasets/coco_instance.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]
classes = ('water', 'pear', 'egg', 'grapes', 'butter', 'bread-white', 'jam', 'bread-whole-wheat', 'apple', 'tea-green', 'white-coffee-with-caffeine', 'tea-black', 'mixed-salad-chopped-without-sauce', 'cheese', 'tomato-sauce', 'pasta-spaghetti', 'carrot', 'onion', 'beef-cut-into-stripes-only-meat', 'rice-noodles-vermicelli', 'salad-leaf-salad-green', 'bread-grain', 'espresso-with-caffeine', 'banana', 'mixed-vegetables', 'bread-wholemeal', 'savoury-puff-pastry', 'wine-white', 'dried-meat', 'fresh-cheese', 'red-radish', 'hard-cheese', 'ham-raw', 'bread-fruit', 'oil-vinegar-salad-dressing', 'tomato', 'cauliflower', 'potato-gnocchi', 'wine-red', 'sauce-cream', 'pasta-linguini-parpadelle-tagliatelle', 'french-beans', 'almonds', 'dark-chocolate', 'mandarine', 'semi-hard-cheese', 'croissant', 'sushi', 'berries', 'biscuits', 'thickened-cream-35', 'corn', 'celeriac', 'alfa-sprouts', 'chickpeas', 'leaf-spinach', 'rice', 'chocolate-cookies', 'pineapple', 'tart', 'coffee-with-caffeine', 'focaccia', 'pizza-with-vegetables-baked', 'soup-vegetable', 'bread-toast', 'potatoes-steamed', 'spaetzle', 'frying-sausage', 'lasagne-meat-prepared', 'boisson-au-glucose-50g', 'ma1-4esli', 'peanut-butter', 'chips-french-fries', 'mushroom', 'ratatouille', 'veggie-burger', 'country-fries', 'yaourt-yahourt-yogourt-ou-yoghourt-natural', 'hummus', 'fish', 'beer', 'peanut', 'pizza-margherita-baked', 'pickle', 'ham-cooked', 'cake-chocolate', 'bread-french-white-flour', 'sauce-mushroom', 'rice-basmati', 'soup-of-lentils-dahl-dhal', 'pumpkin', 'witloof-chicory', 'vegetable-au-gratin-baked', 'balsamic-salad-dressing', 'pasta-penne', 'tea-peppermint', 'soup-pumpkin', 'quiche-with-cheese-baked-with-puff-pastry', 'mango', 'green-bean-steamed-without-addition-of-salt', 'cucumber', 'bread-half-white', 'pasta', 'beef-filet', 'pasta-twist', 'pasta-wholemeal', 'walnut', 'soft-cheese', 'salmon-smoked', 'sweet-pepper', 'sauce-soya', 'chicken-breast', 'rice-whole-grain', 'bread-nut', 'green-olives', 'roll-of-half-white-or-white-flour-with-large-void', 'parmesan', 'cappuccino', 'flakes-oat', 'mayonnaise', 'chicken', 'cheese-for-raclette', 'orange', 'goat-cheese-soft', 'tuna', 'tomme', 'apple-pie', 'rosti', 'broccoli', 'beans-kidney', 'white-cabbage', 'ketchup', 'salt-cake-vegetables-filled', 'pistachio', 'feta', 'salmon', 'avocado', 'sauce-pesto', 'salad-rocket', 'pizza-with-ham-baked', 'gruya-re', 'ristretto-with-caffeine',
           'risotto-without-cheese-cooked', 'crunch-ma1-4esli', 'braided-white-loaf', 'peas', 'chicken-curry-cream-coconut-milk-curry-spices-paste', 'bolognaise-sauce', 'bacon-frying', 'salami', 'lentils', 'mushrooms', 'mashed-potatoes-prepared-with-full-fat-milk-with-butter', 'fennel', 'chocolate-mousse', 'corn-crisps', 'sweet-potato', 'bircherma1-4esli-prepared-no-sugar-added', 'beetroot-steamed-without-addition-of-salt', 'sauce-savoury', 'leek', 'milk', 'tea', 'fruit-salad', 'bread-rye', 'salad-lambs-ear', 'potatoes-au-gratin-dauphinois-prepared', 'red-cabbage', 'praline', 'bread-black', 'black-olives', 'mozzarella', 'bacon-cooking', 'pomegranate', 'hamburger-bread-meat-ketchup', 'curry-vegetarian', 'honey', 'juice-orange', 'cookies', 'mixed-nuts', 'breadcrumbs-unspiced', 'chicken-leg', 'raspberries', 'beef-sirloin-steak', 'salad-dressing', 'shrimp-prawn-large', 'sour-cream', 'greek-salad', 'sauce-roast', 'zucchini', 'greek-yaourt-yahourt-yogourt-ou-yoghourt', 'cashew-nut', 'meat-terrine-pata-c', 'chicken-cut-into-stripes-only-meat', 'couscous', 'bread-wholemeal-toast', 'craape-plain', 'bread-5-grain', 'tofu', 'water-mineral', 'ham-croissant', 'juice-apple', 'falafel-balls', 'egg-scrambled-prepared', 'brioche', 'bread-pita', 'pasta-haprnli', 'blue-mould-cheese', 'vegetable-mix-peas-and-carrots', 'quinoa', 'crisps', 'beef', 'butter-spread-puree-almond', 'beef-minced-only-meat', 'hazelnut-chocolate-spread-nutella-ovomaltine-caotina', 'chocolate', 'nectarine', 'ice-tea', 'applesauce-unsweetened-canned', 'syrup-diluted-ready-to-drink', 'sugar-melon', 'bread-sourdough', 'rusk-wholemeal', 'gluten-free-bread', 'shrimp-prawn-small', 'french-salad-dressing', 'pancakes', 'milk-chocolate', 'pork', 'dairy-ice-cream', 'guacamole', 'sausage', 'herbal-tea', 'fruit-coulis', 'water-with-lemon-juice', 'brownie', 'lemon', 'veal-sausage', 'dates', 'roll-with-pieces-of-chocolate', 'taboula-c-prepared-with-couscous', 'croissant-with-chocolate-filling', 'eggplant', 'sesame-seeds', 'cottage-cheese', 'fruit-tart', 'cream-cheese', 'tea-verveine', 'tiramisu', 'grits-polenta-maize-flour', 'pasta-noodles', 'artichoke', 'blueberries', 'mixed-seeds', 'caprese-salad-tomato-mozzarella', 'omelette-plain', 'hazelnut', 'kiwi', 'dried-raisins', 'kolhrabi', 'plums', 'beetroot-raw', 'cream', 'fajita-bread-only', 'apricots', 'kefir-drink', 'bread', 'strawberries', 'wine-rosa-c', 'watermelon-fresh', 'green-asparagus', 'white-asparagus', 'peach')

# Use r101 model
model = dict(
    pretrained='torchvision://resnet101',
    backbone=dict(depth=101),
    roi_head=dict(
        bbox_head=dict(num_classes=len(classes)),
        mask_head=dict(num_classes=len(classes))))

data_root = 'data/'
data = dict(
    train=dict(
        ann_file=data_root+'train/annotations.json',
        img_prefix=data_root+'train',
        classes=classes),
    val=dict(
        ann_file=data_root+'val/annotations.json',
        img_prefix=data_root+'val',
        classes=classes),
    test=dict(
        ann_file=data_root+'val/annotations.json',
        img_prefix=data_root+'val',
        classes=classes))

load_from = 'http://download.openmmlab.com/mmdetection/v2.0/mask_rcnn/mask_rcnn_r101_fpn_1x_coco/mask_rcnn_r101_fpn_1x_coco_20200204-1efe0ed5.pth'
