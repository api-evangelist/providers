---
aid: figma
url: https://raw.githubusercontent.com/apis-json/artisanal/main/apis/figma.yml
apis:
  - aid: figma:figma-api
    name: Figma API
    tags:
      - Files
      - Nodes
      - Images
      - Teams
      - Projects
      - Versions
      - Comments
      - Reactions
      - Me
      - Users
      - Components
      - Keys
      - Component_sets
      - Styles
      - Webhooks
      - Activity  Logs
      - Payments
      - Variables
      - Local
      - Published
      - Dev_resources
      - Dev  Resources
      - Analytics
      - Libraries
      - Actions
      - Library  Analytics
      - Usages
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://www.figma.com/developers
    overlays: []
    properties:
      - url: properties/figma-api-openapi.yml
        type: OpenAPI
    description: |-

      Figma allows designers to create and prototype their digital experiences -
      together in real-time and in one place - helping them turn their ideas and
      visions into products, faster. Figma's mission is to make design
      accessible to everyone. The Figma API is one of the ways we aim to do
      that.
name: Figma
tags: []
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
common:
  - url: https://www.figma.com/developers/api#authentication
    type: Authentication
  - url: https://www.figma.com/developers/api#webhooks_v2
    type: Webhooks
  - url: https://www.figma.com/developers/api#errors
    type: Errors
  - url: https://www.figma.com/developers/api#changelog
    type: Change Log
  - url: https://www.figma.com/login
    type: Login
  - url: https://www.figma.com/signup
    type: Sign Up
  - url: https://www.figma.com/blog
    type: Blog
  - url: https://www.figma.com/summary-of-policy
    type: Terms of Service
  - url: https://www.figma.com/contact
    type: Contact
  - url: https://www.figma.com/security
    type: Security
  - url: https://www.figma.com/login?cont=/developers/api
    name: Login
    type: Login
  - url: https://www.figma.com/signup?cont=/developers/api
    name: SignUp
    type: SignUp
  - url: https://www.figma.com/developers
    name: Portal
    type: Portal
  - url: https://www.figma.com/pricing/
    name: Pricing
    type: Pricing
  - url: https://www.figma.com/blog/
    name: Blog
    type: Blog
  - url: https://status.figma.com/
    name: Status
    type: Status
  - url: https://help.figma.com/hc/en-us
    name: Support
    type: Support
  - url: https://www.figma.com/product-integrations/
    name: Integrations
    type: Integrations
  - url: https://github.com/figma/rest-api-spec
    name: OpenAPI Specifications
    type: Specifications
created: 2023/11/22
modified: '2024-12-26'
description: |-

  Figma's mission is to make design accessible to everyone. Our two products
  help people from different backgrounds and roles express their ideas visually
  and make things together.
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
specificationVersion: '0.16'
---