---
aid: factory-i-o
name: FACTORY I/O
description: FACTORY I/O is a software simulation tool that allows users to create and simulate industrial automation systems in a virtual environment. It provides a realistic and interactive platform for training, testing, and troubleshooting automation processes without the need for physical equipment. Users can design their own control systems, program PLCs, and observe the behavior of machines and processes in real-time.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Industrial Automation
  - Simulations
  - Software Simulation
url: https://raw.githubusercontent.com/api-evangelist/factory-i-o/refs/heads/main/apis.yml
created: '2025-03-01'
modified: '2026-04-28'
position: Consumer
access: 3rd-Party
specificationVersion: '0.19'
apis:
  - aid: factory-i-o:factory-i-o
    name: FACTORY I/O Web API
    description: 'The web server in Factory I/O exposes a REST API for reading and writing simulation values from external clients. The web server uses conventional HTTP response codes to indicate success or failure: 2xx for success, 4xx for client errors, and 5xx for errors in Factory I/O.'
    humanURL: https://docs.factoryio.com/manual/web-api/
    tags:
      - Industrial Automation
      - Simulations
      - Software Simulation
    properties:
      - type: Documentation
        url: https://docs.factoryio.com/manual/web-api/
      - type: GitHub Organization
        url: https://github.com/RealGames
common:
  - type: Website
    url: https://factoryio.com
  - type: Documentation
    url: https://docs.factoryio.com/
  - type: Blog
    url: https://factoryio.com/blog
  - type: GitHub Organization
    url: https://github.com/RealGames
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
