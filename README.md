# Sing-Color-Web-Development-

I built this online store application for my friends to sell their products. This is a handicraft online store. I used Flask, which is a framework of Python, to build the back-end for this application. The front-end was built by HTML5, CSS3, SASS, and Javascript . This online store allows users to make payments and receive the email confirmation. On the other hand, the seller will receive the order email as well. The order data are stored in SQLite locally or PostgreSQL remotely. 


## Architecture:
```
├── Pipfile
├── Pipfile.lock
├── README.md
└── src
    ├── app.py
    ├── application.py
    ├── config.py
    ├── data.sqlite
    ├── models
    │   ├── order.py
    │   └── user.py
    ├── static
    │   ├── css
    │   │   ├── fonts
    │   │   │   ├── linea-basic-10.eot
    │   │   │   ├── linea-basic-10.svg
    │   │   │   ├── linea-basic-10.ttf
    │   │   │   └── linea-basic-10.woff
    │   │   ├── icon-font.css
    │   │   └── style.css
    │   ├── img
    │   │   ├── 74007.jpg
    │   │   ├── booking.jpg
    │   │   ├── man.jpg
    │   │   ├── new_background.jpg
    │   │   ├── pic-1.jpg
    │   │   ├── pic-2.jpg
    │   │   ├── pic-3.jpg
    │   │   ├── popup1.jpg
    │   │   ├── popup2.jpg
    │   │   └── sing_logo.png
    │   ├── package-lock.json
    │   ├── package.json
    │   └── sass
    │       ├── abstracts
    │       │   ├── _mixins.scss
    │       │   └── _variables.scss
    │       ├── base
    │       │   ├── _animations.scss
    │       │   ├── _base.scss
    │       │   ├── _typography.scss
    │       │   └── _utilities.scss
    │       ├── components
    │       │   ├── _button.scss
    │       │   ├── _card.scss
    │       │   ├── _composition.scss
    │       │   ├── _feature-box.scss
    │       │   └── _form.scss
    │       ├── layout
    │       │   ├── _footer.scss
    │       │   ├── _grid.scss
    │       │   ├── _header.scss
    │       │   └── _navigation.scss
    │       ├── main.scss
    │       └── pages
    │           ├── _checkout.scss
    │           ├── _confirmation.scss
    │           ├── _home.scss
    │           └── _order.scss
    └── templates
        ├── checkout.html
        ├── confirmation.html
        ├── home.html
        ├── layout.html
        └── order.html
```