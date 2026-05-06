---
aid: picpurify
name: PicPurify
description: PicPurify provides image and video moderation services including gun and knife weapon detection, nudity, drug, gore, hate sign, age, gender, and other content moderation tasks. Pictures showing someone posing with a firearm or holding a knife can offend visitors, shock young minds and displease advertisers - PicPurify detects these images so they can be filtered before publication.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Image Moderation
  - Content Moderation
  - Computer Vision
  - Weapon Detection
created: '2025-02-17'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/picpurify/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: picpurify:picpurify
    name: PicPurify Moderation API
    description: PicPurify image and video moderation API supporting gun detection, knife detection, weapon moderation, porn moderation, drug moderation, gore moderation, hate sign detection, money detection, age detection, gender detection, and other tasks. Submit an image or video by file upload or URL, receive a moderation decision (OK/KO) along with confidence scores.
    humanURL: https://www.picpurify.com/
    baseURL: https://www.picpurify.com
    tags:
      - Image Moderation
      - Content Moderation
      - Weapon Detection
    properties:
      - type: Documentation
        url: https://www.picpurify.com/api-services.html
      - type: GunDetection
        url: https://www.picpurify.com/gun-detection.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/picpurify/refs/heads/main/openapi/picpurify-openapi.yaml
common:
  - type: Website
    url: https://www.picpurify.com/
  - type: Documentation
    url: https://www.picpurify.com/api-services.html
  - type: Pricing
    url: https://www.picpurify.com/buying.html
  - type: SignUp
    url: https://www.picpurify.com/inscription.html
  - type: SDKs
    url: https://github.com/Picpurify
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
