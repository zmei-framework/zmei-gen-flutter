# Flutter plugin for [Zmei generator](https://github.com/zmei-framework/generator)
[![Maintainability](https://api.codeclimate.com/v1/badges/d63e77220053cccf31ec/maintainability)](https://codeclimate.com/github/zmei-framework/zmei-gen-flutter/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/d63e77220053cccf31ec/test_coverage)](https://codeclimate.com/github/zmei-framework/zmei-gen-flutter/test_coverage)
[![Build Status](https://travis-ci.org/zmei-framework/zmei-gen-flutter.svg?branch=master)](https://travis-ci.org/zmei-framework/zmei-gen-flutter)

This is Zmei generator plugin that adds flutter generator support.

## Features

- Generate pages
- Generate menus
- Automatically fetch data from django page
- Automatically connect to websocket streams if any

## Installation 

Generator is written in python. Install with pip python packaging tool (preferably in virtual environment):

`pip install zmei-gen-flutter`
 
## Quick start

Just add @flutter to any page:

    [index: /]
    @flutter
    
Also you may mark all subpages as flutter as well:

    [base]
    @flutter(child: true)
    
    [base->index]
    
Plugin understand two types of menu: 
    
    // this is drawer menu
       
    @menu.flutter_drawer(
        [transition=inFromRight, color=green] "Заказчик": page(client.index)
        [transition=inFromRight, color=orange] "Перевозчик": page(carrier.index)
        [transition=inFromRight, color=blue] "Водитель": page(driver.index)
    
        [icon=settings] "Настройки": page(settings)
        [icon=power_settings_new] "Выход": page(logout)
    )
    
    // this is bottom menu
    
    @menu.flutter_bottom(
        "Home": page(index)
        "Profile": page(profile)
    )
    
## Contribution

Contributions are highly appreciated. Project is huge and it is hard to develop it alone.

You can contribute by:
- Improve documentation
- Test, write bug reports, propose features
- Add new features
- Fix bugs, improve code base, add your features
- Write articles, blog-posts with your experience using the generator
- Write plugins, improve existing ones


## Development

    pip install -r requirements-dev.txt
    pip install -e .
    zmei build
    py.test


## Authors

### Conributors

- Alex Rudakov @ribozz (maintainer)

### Thanks to

...

## LEGAL NOTICE

Source code is distributed under GNU General Public License v3.0 licence. Full licence text is available in LICENSE file.

In-short about GPLv3:
- All software that use Zmei-generator as it's part **MUST** be open-sourced as well: plugins, other generators
 based on it, etc.
- You **CAN NOT** take Zmei-generator and sell it as a paid service without open-sourcing it
- But, you **CAN** use Zmei generator as a tool to write any software including private closed source software
 

Software is free for non-commercial use. For commercial use ask for dual-licensing options. 
