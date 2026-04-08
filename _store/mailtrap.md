---
aid: mailtrap
url: https://raw.githubusercontent.com/api-evangelist/mailtrap/refs/heads/main/apis.yml
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
name: Mailtrap
tags:
- Email
- Email Delivery
- Email Sandbox
- Email Testing
- Transactional Email
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-02-06'
modified: '2026-04-07'
position: Consumer
description: Mailtrap provides a RESTful email infrastructure API with high deliverability rates, an email sandbox for safe testing, and actionable analytics. It offers SDKs for smooth integration and supports both transactional sending and bulk email delivery.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

