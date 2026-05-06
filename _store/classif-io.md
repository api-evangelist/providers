---
aid: classif-io
name: Classif.io
url: https://raw.githubusercontent.com/api-evangelist/classif-io/refs/heads/main/apis.yml
created: '2025-03-01'
modified: '2026-04-23'
type: Index
access: 3rd-Party
position: Consumer
specificationVersion: '0.19'
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Apparel
  - Classification
  - Computer Vision
  - Fashion
  - Image Recognition
  - Machine Learning
  - Recommendation
description: Classif.io provides machine-learning-powered classification APIs that identify and label visual content. The flagship offering is a Fashion Style Classification API that detects clothing items, categorizes shirts, pants, dresses, and accessories from images, and supports outfit recommendation, retail product matching, virtual fitting room, social media tagging, and e-commerce styling use cases. APIs are delivered as REST endpoints and authenticated with API keys.
apis:
  - aid: classif-io:fashion-style-classification-api
    name: Classif.io Fashion Style Classification API
    tags:
      - Apparel
      - Classification
      - Fashion
      - Recommendation
      - Style
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.classif.io/fashion-style-classification-api/
    properties:
      - url: https://www.classif.io/fashion-style-classification-api/
        type: Documentation
    description: The Fashion Style Classification API detects and categorizes clothing items from images, including shirts, pants, dresses, and accessories, and produces stylistic labels suitable for personal styling, retail recommendation, virtual fitting room, social media tagging, and e-commerce styling use cases.
common:
  - type: Website
    url: https://www.classif.io/
  - type: Documentation
    url: https://www.classif.io/fashion-style-classification-api/
  - type: JSON-LD
    url: json-ld/classif-io-context.jsonld
  - type: Spectral
    url: rules/classif-io-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/classif-io-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
