---
aid: maileroo
name: Maileroo
description: Maileroo provides transactional and marketing email delivery via a developer-friendly REST API with high deliverability, SMTP relay support, email tracking, and SDKs for popular programming languages. Trusted by businesses of all sizes to handle millions of emails every month.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Email
  - Email Delivery
  - Marketing Email
  - SMTP
  - Transactional Email
url: https://raw.githubusercontent.com/api-evangelist/maileroo/refs/heads/main/apis.yml
created: '2025-02-06'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: maileroo:maileroo-email-api
    name: Maileroo Email API
    description: The Maileroo REST API allows sending transactional and marketing emails via JSON requests with high deliverability. Supports HTML and plain text emails, attachments, tracking, and templates.
    humanURL: https://maileroo.com/email-for-developers
    baseURL: https://smtp.maileroo.com
    tags:
      - Email
      - REST API
      - Transactional Email
    properties:
      - type: Documentation
        url: https://maileroo.com/docs/email-api/introduction/
      - type: Getting Started
        url: https://maileroo.com/docs/introduction/
      - type: Reference
        url: https://maileroo.com/docs/email-api/send-basic-email/
      - type: SDKs
        url: https://maileroo.com/docs/email-api/libraries-and-sdks/
      - type: OpenAPI
        url: openapi/maileroo-email-api-openapi.yml
common:
  - type: Portal
    url: https://maileroo.com/email-for-developers
  - type: Documentation
    url: https://maileroo.com/docs/
  - type: Sign Up
    url: https://app.maileroo.com/register
  - type: Login
    url: https://app.maileroo.com/login
  - type: GitHub Organization
    url: https://github.com/maileroo
  - type: Pricing
    url: https://maileroo.com/pricing
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
