---
aid: logmeal
name: LogMeal
description: LogMeal provides a Food Recognition Image API that detects foods, drinks, vegetables, fruits and prepared dishes from images. The platform offers semantic tagging including food group, dish and ingredients recognition, as well as nutritional information analysis with 35+ nutritional indicators and user intake history tracking.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Computer Vision
  - Food
  - Image Recognition
  - Nutrition
  - Semantic Tagging
created: '2025-03-01'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/logmeal/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: logmeal:food-recognition-api
    name: LogMeal Food Recognition API
    description: The LogMeal API is a RESTful service that recognizes foods from images, returns ingredient lists, computes nutritional information and tracks user intake history.
    humanURL: https://logmeal.com/api/
    baseURL: https://api.logmeal.com
    tags:
      - Computer Vision
      - Food
      - Image Recognition
      - Nutrition
    properties:
      - type: Documentation
        url: https://docs.logmeal.com
      - type: SignUp
        url: https://logmeal.com/api/
      - type: OpenAPI
        url: openapi/logmeal-food-recognition-api-openapi.yml
common:
  - type: Website
    url: https://logmeal.com
  - type: Documentation
    url: https://docs.logmeal.com
  - type: Portal
    url: https://logmeal.com/api/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
