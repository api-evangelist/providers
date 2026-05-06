---
aid: contensis
url: https://raw.githubusercontent.com/api-evangelist/contensis/refs/heads/main/apis.yml
name: Contensis
description: Contensis is an enterprise-level Content Management System (CMS) developed by Zengenti, designed to help organizations create, manage, and deliver digital content across multiple platforms and devices through HTTP, JavaScript, and .Net APIs.
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
position: Consuming
tags:
  - CMS
  - Content
  - Headless CMS
created: '2024-11-13'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: contensis:delivery-api
    name: Contensis Delivery API
    tags:
      - Content Delivery
      - Headless CMS
      - REST
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.contensis.com/help-and-docs/apis/delivery-http
    properties:
      - url: https://www.contensis.com/help-and-docs/apis/delivery-http
        type: Documentation
      - url: https://www.contensis.com/help-and-docs/apis/delivery-js
        type: JavaScript
      - url: https://www.contensis.com/help-and-docs/apis/delivery-net
        type: .Net
    description: The Contensis Delivery API focuses on delivering content created in content types and entries to websites and applications. It is a read-only HTTP API designed for high-performance content retrieval, with official JavaScript and .Net client wrappers available for integration into modern front-end frameworks.
  - aid: contensis:management-api
    name: Contensis Management API
    tags:
      - Content Management
      - CRUD
      - Headless CMS
      - REST
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.contensis.com/help-and-docs/apis/management-http
    properties:
      - url: https://www.contensis.com/help-and-docs/apis/management-http
        type: Documentation
      - url: https://www.contensis.com/help-and-docs/apis/management-js
        type: JavaScript
      - url: https://www.contensis.com/help-and-docs/apis/management-net
        type: .Net
    description: The Contensis Management API allows developers to import and manage content within content types and entries. It provides full CRUD access to content models, entries, projects, and related resources, enabling headless content workflows, migrations, and integrations with editorial tooling.
  - aid: contensis:image-api
    name: Contensis Image API
    tags:
      - Asset Delivery
      - Images
      - Media
      - Transformation
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.contensis.com/help-and-docs/apis/image-api
    properties:
      - url: https://www.contensis.com/help-and-docs/apis/image-api
        type: Documentation
      - url: https://www.contensis.com/community/blog/developing-with-the-contensis-image-api
        type: Blog
    description: The Contensis Image API provides real-time image manipulation and optimization features as part of the Delivery API. It supports on-the-fly transformations such as resizing, cropping, format conversion, and quality adjustment via URL query parameters, and is designed to speed up image delivery for responsive, multi-device experiences.
common:
  - type: Website
    url: https://www.contensis.com/
  - type: Documentation
    url: https://www.contensis.com/help-and-docs/apis
  - type: Blog
    url: https://www.contensis.com/community/blog
  - type: Community
    url: https://www.contensis.com/community
  - type: Support
    url: https://www.contensis.com/help-and-docs
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
