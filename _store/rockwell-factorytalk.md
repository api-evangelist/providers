---
aid: rockwell-factorytalk
url: https://raw.githubusercontent.com/api-evangelist/rockwell-factorytalk/refs/heads/main/apis.yml
apis:
- aid: rockwell-factorytalk:factorytalk-optix-rest-api
  name: Rockwell FactoryTalk Optix REST API
  tags:
  - Automation
  - HMI
  - Manufacturing
  - REST
  image: https://raw.githubusercontent.com/api-evangelist/rockwell-factorytalk/refs/heads/main/image.png
  humanURL: https://docs.rockwellautomation.com/en/products/software/factorytalk/factorytalk-optix.html
  baseURL: https://api.factorytalk.example.com
  properties:
  - url: https://docs.rockwellautomation.com/en/products/software/factorytalk/factorytalk-optix.html
    type: Documentation
  - url: openapi/rockwell-factorytalk-optix-openapi.yml
    type: OpenAPI
  description: Rockwell Automation FactoryTalk Optix REST API provides programmatic access to HMI and SCADA visualization applications, enabling external system integration, tag read/write, alarm management, and runtime control of FactoryTalk Optix applications.
- aid: rockwell-factorytalk:factorytalk-hub-api
  name: Rockwell FactoryTalk Hub API
  tags:
  - Automation
  - Cloud
  - Manufacturing
  - REST
  image: https://raw.githubusercontent.com/api-evangelist/rockwell-factorytalk/refs/heads/main/image.png
  humanURL: https://www.rockwellautomation.com/en-us/products/software/factorytalk.html
  baseURL: https://api.factorytalk.example.com
  properties:
  - url: https://www.rockwellautomation.com/en-us/products/software/factorytalk.html
    type: Documentation
  - url: asyncapi/rockwell-factorytalk-realtime-asyncapi.yml
    type: AsyncAPI
  description: Rockwell FactoryTalk Hub provides cloud-based industrial API services for connecting FactoryTalk software applications, enabling centralized identity management, software licensing, and connected factory services.
- aid: rockwell-factorytalk:logix-designer-api
  name: Rockwell FactoryTalk Logix Designer API
  tags:
  - Automation
  - Manufacturing
  - PLC
  - Programming
  - REST
  image: https://raw.githubusercontent.com/api-evangelist/rockwell-factorytalk/refs/heads/main/image.png
  humanURL: https://github.com/rockwellautomation/ra-logix-designer-vcs-custom-tools
  baseURL: https://api.factorytalk.example.com
  properties:
  - url: https://github.com/rockwellautomation/ra-logix-designer-vcs-custom-tools
    type: Documentation
  - url: https://github.com/rockwellautomation/ra-logix-cicd
    type: SDKs
  description: Rockwell Automation FactoryTalk Logix Designer provides programmatic access to Logix controller programming, allowing version control integration, CI/CD pipeline automation, and export of L5X controller files for PLC program management.
name: Rockwell Factorytalk
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Rockwell FactoryTalk is a portfolio of software products by Rockwell Automation that supports the design, operation, and maintenance of industrial control systems and connected manufacturing operations.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

