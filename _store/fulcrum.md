---
aid: fulcrum
name: Fulcrum
description: Fulcrum is a field data collection and inspection platform used by teams to build mobile forms, capture geospatial records, attach photos, videos, audio, and signatures, and synchronize the resulting data with back-office systems. The Fulcrum REST API exposes programmatic access to forms, records, media, choice lists, classification sets, projects, layers, memberships, roles, webhooks, ad hoc SQL queries, and changesets.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-13'
modified: '2026-04-28'
position: Consumer
tags:
  - Data Collection
  - Field Data
  - Geospatial
  - Process Management
  - Mobile
url: https://raw.githubusercontent.com/api-evangelist/fulcrum/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: fulcrum:fulcrum-api
    name: Fulcrum API
    description: The Fulcrum API is a RESTful HTTP API that provides programmatic access to all Fulcrum resources. It supports CRUD operations on forms (apps) and records, uploads of photo, video, audio, and signature media tied to records, management of choice lists and classification sets, project and layer configuration, account memberships and roles, outbound webhooks, and ad hoc SQL queries against a read-only mirror of the customer data. All requests authenticate using an X-ApiToken header and exchange JSON bodies.
    humanURL: https://docs.fulcrumapp.com/reference/
    baseURL: https://api.fulcrumapp.com/api/v2
    tags:
      - Data Collection
      - Field Data
      - Geospatial
      - Forms
      - Records
      - Media
      - Webhooks
    properties:
      - type: Documentation
        url: https://docs.fulcrumapp.com/reference/
      - type: Getting Started
        url: https://docs.fulcrumapp.com/docs
      - type: OpenAPI
        url: openapi/fulcrum-api-openapi.yml
common:
  - type: Website
    url: https://www.fulcrumapp.com/
  - type: Documentation
    url: https://docs.fulcrumapp.com/
  - type: GettingStarted
    url: https://docs.fulcrumapp.com/docs
  - type: Pricing
    url: https://www.fulcrumapp.com/pricing/
  - type: Login
    url: https://web.fulcrumapp.com/users/sign_in
  - type: SignUp
    url: https://web.fulcrumapp.com/users/sign_up
  - type: PrivacyPolicy
    url: https://www.fulcrumapp.com/privacy/
  - type: TermsOfService
    url: https://www.fulcrumapp.com/terms/
  - type: Support
    url: https://www.fulcrumapp.com/support/
  - type: Blog
    url: https://www.fulcrumapp.com/blog/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
