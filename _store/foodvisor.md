---
aid: foodvisor
name: Foodvisor
description: Foodvisor is a mobile nutrition platform whose Vision API uses computer vision and AI to identify food items from photographs and return nutritional information including calories, macronutrients, and serving estimates. The Vision API is offered to enterprise developers under a commercial agreement.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-03-01'
modified: '2026-04-28'
position: Consumer
tags:
  - AI
  - Computer Vision
  - Food
  - Health
  - Nutrition
  - Mobile
url: https://raw.githubusercontent.com/api-evangelist/foodvisor/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: foodvisor:vision
    name: Foodvisor Vision API
    tags:
      - AI
      - Food Recognition
      - Nutrition
    humanURL: https://www.foodvisor.io/en/vision/
    description: The Foodvisor Vision API performs food detection and nutritional analysis from images. It is provisioned under a commercial agreement; endpoint and authentication details are shared with customers and no public OpenAPI specification is published.
    properties:
      - type: Documentation
        url: https://www.foodvisor.io/en/vision/
      - type: ContactSales
        url: https://www.foodvisor.io/en/vision/#contact
common:
  - type: Website
    url: https://www.foodvisor.io/
  - type: Documentation
    url: https://www.foodvisor.io/en/vision/
  - type: ContactSales
    url: https://www.foodvisor.io/en/vision/#contact
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
