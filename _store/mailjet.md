---
aid: mailjet
name: Mailjet
description: Mailjet is an email service provider offering a powerful REST API for sending transactional and marketing emails. It provides an easy-to-integrate API with support for PHP, Python, Ruby, Java, Node.js, C#, and Go, along with SMTP relay and real-time email tracking.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Email
  - Email Delivery
  - Marketing Email
  - SMTP
  - Transactional Email
url: https://raw.githubusercontent.com/api-evangelist/mailjet/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: mailjet:mailjet-email-api
    name: Mailjet Email API
    description: The Mailjet REST API allows sending transactional and marketing emails programmatically using HTTP GET and POST requests with JSON, XML, or other supported formats. Includes send API, contact management, campaign management, statistics, and event tracking.
    humanURL: https://dev.mailjet.com/
    baseURL: https://api.mailjet.com/v3
    tags:
      - Email
      - Marketing Email
      - Transactional Email
    properties:
      - type: Documentation
        url: https://dev.mailjet.com/email/guides/
      - type: Reference
        url: https://dev.mailjet.com/email/reference/
      - type: Getting Started
        url: https://dev.mailjet.com/email/guides/send-api-V3/
      - type: Authentication
        url: https://dev.mailjet.com/email/guides/#authentication
      - type: OpenAPI
        url: openapi/mailjet-email-api-openapi.yml
common:
  - type: Portal
    url: https://dev.mailjet.com/
  - type: Sign Up
    url: https://app.mailjet.com/signup
  - type: Login
    url: https://app.mailjet.com/
  - type: GitHub Organization
    url: https://github.com/mailjet
  - type: Support
    url: https://documentation.mailjet.com/hc/en-us
  - type: Pricing
    url: https://www.mailjet.com/pricing/
  - type: Status
    url: https://mailjetstatus.com/
  - type: Terms of Service
    url: https://www.mailjet.com/legal/terms/
  - type: Privacy Policy
    url: https://www.mailjet.com/legal/privacy-policy/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
