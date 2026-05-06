---
aid: mailtrap
name: Mailtrap
description: Mailtrap provides a RESTful email infrastructure API with high deliverability rates, an email sandbox for safe testing, and actionable analytics. It offers SDKs for smooth integration and supports both transactional sending and bulk email delivery.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Email
  - Email Delivery
  - Email Sandbox
  - Email Testing
  - Transactional Email
url: https://raw.githubusercontent.com/api-evangelist/mailtrap/refs/heads/main/apis.yml
created: '2025-02-06'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: mailtrap:mailtrap-email-api
    name: Mailtrap Email Sending API
    description: The Mailtrap Email Sending API allows sending transactional and bulk emails with high deliverability. It follows REST principles and supports authentication via API tokens, with all requests sent over HTTPS.
    humanURL: https://mailtrap.io/email-api/
    baseURL: https://send.api.mailtrap.io
    tags:
      - Email
      - REST API
      - Transactional Email
    properties:
      - type: Documentation
        url: https://docs.mailtrap.io/developers
      - type: Reference
        url: https://api-docs.mailtrap.io/
      - type: Getting Started
        url: https://docs.mailtrap.io/docs/sending-emails-overview
      - type: OpenAPI
        url: openapi/mailtrap-email-api-openapi.yml
  - aid: mailtrap:mailtrap-email-sandbox
    name: Mailtrap Email Sandbox API
    description: The Mailtrap Email Sandbox API provides a safe email testing environment to inspect and debug emails before sending to real recipients. Supports switching between sandbox and production modes in official SDKs.
    humanURL: https://mailtrap.io/automated-email-testing/
    baseURL: https://sandbox.api.mailtrap.io
    tags:
      - Email Testing
      - QA
      - Sandbox
    properties:
      - type: Documentation
        url: https://docs.mailtrap.io/docs/email-sandbox-overview
      - type: OpenAPI
        url: openapi/mailtrap-email-sandbox-openapi.yml
common:
  - type: Portal
    url: https://mailtrap.io/
  - type: Documentation
    url: https://docs.mailtrap.io/
  - type: Sign Up
    url: https://mailtrap.io/register/signup
  - type: Login
    url: https://mailtrap.io/users/sign_in
  - type: Pricing
    url: https://mailtrap.io/pricing/
  - type: Status
    url: https://status.mailtrap.io/
  - type: Support
    url: https://help.mailtrap.io/
  - type: Terms of Service
    url: https://mailtrap.io/terms-of-use/
  - type: Privacy Policy
    url: https://mailtrap.io/privacy-policy/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
