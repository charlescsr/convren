# imgconvren [![CircleCI](https://circleci.com/gh/charlescsr/imgconvren.svg?style=svg)](https://circleci.com/gh/mlabouardy/circleci-heroku-flask) [![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)
A package to convert and rename images easily

Example in action
```
import convren

path = 'file path'

r = convren.Renamer()
r.conv_ren(path, 'jpeg', 'test')
```
