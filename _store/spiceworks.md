---
aid: spiceworks
url: https://raw.githubusercontent.com/api-evangelist/spiceworks/refs/heads/main/apis.yml
apis:
  - aid: spiceworks:spiceworks-cloud-apps-api
    name: Spiceworks Cloud Apps API
    tags:
      - Cloud Apps
      - Community
      - Help Desk
      - IT Management
      - Ticketing
    humanURL: https://spiceworks.github.io/developers.spiceworks.com/documentation/cloud-apps/
    properties:
      - url: https://spiceworks.github.io/developers.spiceworks.com/documentation/cloud-apps/
        type: Documentation
      - url: https://spiceworks.github.io/developers.spiceworks.com/documentation/cloud-apps/authentication/
        type: Authentication
      - url: https://spiceworks.github.io/developers.spiceworks.com/documentation/cloud-apps/reference/helpdesk/
        type: Documentation
      - url: https://github.com/spiceworks/spiceworks-js-sdk
        type: SDKs
      - url: https://github.com/spiceworks/spiceworks-js-sdk/tree/master/examples/hello-world
        type: Examples
      - url: openapi/spiceworks-cloud-apps-openapi.yml
        type: OpenAPI
      - url: rules/spiceworks-rules.yml
        type: SpectralRules
      - url: capabilities/shared/cloud-apps.yaml
        type: NaftikoCapabilities
    description: The Spiceworks Cloud Apps API provides a JavaScript SDK for building integrated apps within the Spiceworks platform, with access to Help Desk ticketing data, device inventory, and user information. It allows developers to create custom apps embedded in the Spiceworks interface with access to IT management data.
name: Spiceworks
tags:
  - Community
  - Enterprise IT
  - IT Management
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
common:
  - url: https://community.spiceworks.com/
    name: Spiceworks Community Website
    type: Website
  - url: https://community.spiceworks.com/register
    name: Sign Up
    type: SignUp
  - url: https://community.spiceworks.com/login
    name: Login
    type: Login
  - url: https://spiceworks.github.io/developers.spiceworks.com/
    name: Developer Portal
    type: Portal
  - url: https://spiceworks.github.io/developers.spiceworks.com/documentation/cloud-apps/
    name: Developer Documentation
    type: Documentation
  - url: https://github.com/spiceworks/spiceworks-js-sdk
    name: Spiceworks JavaScript SDK
    type: SDKs
  - url: https://community.spiceworks.com/help
    name: Help Center
    type: Support
  - url: https://community.spiceworks.com/legal/terms
    name: Terms of Service
    type: TermsOfService
  - url: https://community.spiceworks.com/legal/privacy
    name: Privacy Policy
    type: PrivacyPolicy
  - url: https://community.spiceworks.com/blog
    name: Spiceworks Blog
    type: Blog
  - url: https://twitter.com/spiceworks
    name: Spiceworks on X (Twitter)
    type: X
  - url: https://www.linkedin.com/company/spiceworks
    name: Spiceworks on LinkedIn
    type: LinkedIn
  - url: https://www.facebook.com/Spiceworks
    name: Spiceworks on Facebook
    type: Facebook
  - url: https://www.youtube.com/spiceworks
    name: Spiceworks on YouTube
    type: YouTube
  - url: https://github.com/spiceworks
    name: Spiceworks on GitHub
    type: GitHub
  - url: openapi/spiceworks-cloud-apps-openapi.yml
    name: Spiceworks Cloud Apps OpenAPI
    type: OpenAPI
  - url: rules/spiceworks-rules.yml
    name: Spiceworks Spectral Rules
    type: SpectralRules
  - url: vocabulary/spiceworks-vocabulary.yml
    name: Spiceworks Vocabulary
    type: Vocabulary
  - url: capabilities/it-management.yaml
    name: Spiceworks IT Management Capabilities
    type: NaftikoCapabilities
description: Spiceworks is an online community and marketplace where IT professionals can find advice, manage their networks, and discover and purchase IT products and services. The Spiceworks Cloud Apps API enables developers to build integrated applications within the Spiceworks platform, accessing Help Desk ticketing, device inventory, and user management data through a JavaScript SDK with OAuth-based authentication.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
