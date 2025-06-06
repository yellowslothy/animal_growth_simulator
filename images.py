def get_cat_image_path(level):
    if level < 3:
        return "images/cat_baby.png"
    elif level < 5:
        return "images/cat_teen.png"
    else:
        return "images/cat_adult.png"
