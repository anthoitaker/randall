# Randall

[![favicon](http://randallcode.es/static/favicon.ico)](http://randallcode.es/static/favicon.ico)

[![CircleCI](https://circleci.com/gh/anthoitaker/randall.svg?style=svg&circle-token=ccc41d9970e9e34d740a2ff56314395f95d85087)](https://circleci.com/gh/anthoitaker/randall)

Randall is a website with an API that allows you to identify and understand [Diagnostic Trouble Codes](https://en.wikipedia.org/wiki/On-board_diagnostics#EOBD_fault_codes).
When your car has some trouble you can check what is the error code with a code reader. Then you can use randall to understand what is the problem and to find possible solutions.

***

## Data

All the information is taken from [Códigos DTC](https://codigosdtc.com/) through [Scrapy](https://scrapy.org/) to provide a free to use API.

![Admin image](http://randallcode.es/static/admin.png)

## Usage

The API has 6 endpoints:

- [List Troubles](#list-troubles)
- [Get Trouble](#get-trouble)
- [List Systems](#list-systems)
- [List Trouble Symptoms](#list-trouble-symptoms)
- [List Trouble Causes](#list-trouble-causes)
- [List Trouble Solutions](#list-trouble-solutions)

### List Troubles

* Endpoint: http://randallcode.es/api/troubles/

* Optional Parameters:

  | Name     | Type          | Values                     | Default |
  |:--------:|:-------------:|:--------------------------:|:-------:|
  | page     | integer       | -                          | 1       |
  | size     | integer       | -                          | 5       |
  | order    | enum          | code, -code, title, system | code    |
  | mode     | enum          | simple, extended           | simple  |

* Example: http://randallcode.es/api/troubles/?page=1&size=2&order=code&mode=simple

### Get Trouble

* Endpoint: http://randallcode.es/api/troubles/{code}/

* Required Parameters:

  | Name     | Regex          | Values  | Default |
  |:--------:|:--------------:|:-------:|:-------:|
  | code     | [A-Za-z0-9]{5} | -       | -       |

* Optional Parameters:

  | Name     | Type          | Values           | Default |
  |:--------:|:-------------:|:----------------:|:-------:|
  | mode     | enum          | simple, extended | simple  |

* Example: http://randallcode.es/api/troubles/p0300/?mode=extended

### List Systems

* Endpoint: http://randallcode.es/api/systems/

* Optional Parameters:

  | Name     | Type          | Values           | Default |
  |:--------:|:-------------:|:----------------:|:-------:|
  | page     | integer       | -                | 1       |
  | size     | integer       | -                | 5       |
  | order    | enum          | name, -name      | name    |

* Example: http://randallcode.es/api/systems/?page=1&size=3&order=name

### List Trouble Symptoms

* Endpoint: http://randallcode.es/api/troubles/{code}/symptoms/

* Required Parameters:

  | Name     | Regex          | Values  | Default |
  |:--------:|:--------------:|:-------:|:-------:|
  | code     | [A-Za-z0-9]{5} | -       | -       |

* Example: http://randallcode.es/api/troubles/p0300/symptoms/

### List Trouble Causes

* Endpoint: http://randallcode.es/api/troubles/{code}/causes/

* Required Parameters:

  | Name     | Regex          | Values  | Default |
  |:--------:|:--------------:|:-------:|:-------:|
  | code     | [A-Za-z0-9]{5} | -       | -       |

* Example: http://randallcode.es/api/troubles/p0300/causes/

### List Trouble Solutions

* Endpoint: http://randallcode.es/api/troubles/{code}/solutions/

* Required Parameters:

  | Name     | Regex          | Values  | Default |
  |:--------:|:--------------:|:-------:|:-------:|
  | code     | [A-Za-z0-9]{5} | -       | -       |

* Example: http://randallcode.es/api/troubles/p0300/solutions/
