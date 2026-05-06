---
aid: johnson-and-johnson
name: Johnson & Johnson
description: Johnson & Johnson is a multinational pharmaceutical and medical devices corporation. Operating today as Johnson & Johnson Innovative Medicine and MedTech, J&J has historically connected health platforms and APIs through subsidiaries such as LifeScan (OneTouch blood glucose monitoring), which was divested to Platinum Equity in 2018 and continues to operate the LifeScan developer portal referenced here. Consumer health brands (Tylenol, Listerine, Neutrogena, Band-Aid) were spun out as Kenvue in 2023 and are tracked in a separate kenvue index.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Healthcare
  - Medical Devices
  - Diabetes
  - Blood Glucose
  - Pharmaceuticals
created: '2026-03-21'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/johnson-and-johnson/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: johnson-and-johnson:lifescan-api
    name: Johnson & Johnson LifeScan API
    description: The Johnson & Johnson LifeScan API provides programmatic access to blood glucose monitoring data and diabetes management tools. LifeScan, historically a Johnson & Johnson company (divested in 2018), develops products like the OneTouch brand of blood glucose meters. The API enables developers to integrate glucose monitoring data into health applications and wellness platforms.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://github.com/bulltonic/lifescan-apiportal
    baseURL: https://api.lifescan.com
    tags:
      - Blood Glucose
      - Diabetes
      - Healthcare
      - Medical Devices
    properties:
      - type: Documentation
        url: https://github.com/bulltonic/lifescan-apiportal
      - type: OpenAPI
        url: openapi/johnson-and-johnson-lifescan-api-openapi.yml
common:
  - type: Website
    url: https://www.jnj.com/
  - type: Portal
    url: https://github.com/johnsonandjohnson
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
