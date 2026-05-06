---
aid: constant-contact
name: Constant Contact
url: https://raw.githubusercontent.com/api-evangelist/constant-contact/refs/heads/main/apis.yml
tags:
  - Campaigns
  - Contacts
  - Email Marketing
  - Events
  - Reporting
  - SMS
  - Surveys
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-03-01'
modified: '2026-05-04'
position: Consumer
specificationVersion: '0.19'
x-type: company
description: Constant Contact is a small-business email and digital marketing platform offering email campaigns, automation, SMS, contact management, surveys, and events. The Constant Contact V3 API is a REST + JSON, OAuth2-protected service published at api.cc.email/v3 covering accounts, contacts, lists, tags, custom fields, segments, email campaigns, A/B tests, schedules and tests, bulk activities (CSV/JSON import, export, list and tag mutations), events with registration and check-in, reporting, and partner provisioning.
apis:
  - aid: constant-contact:v3
    name: Constant Contact V3 API
    tags:
      - Campaigns
      - Contacts
      - Email Marketing
      - Events
      - OAuth2
      - REST
      - SMS
    humanURL: https://developer.constantcontact.com/
    baseURL: https://api.cc.email/v3
    properties:
      - url: https://developer.constantcontact.com/
        type: Documentation
      - url: https://developer.constantcontact.com/api_guide/index.html
        type: Getting Started
      - url: https://developer.constantcontact.com/api_guide/auth_overview.html
        type: Authentication
      - url: https://api.cc.email/v3/swagger.yaml
        type: OpenAPI
      - url: openapi/constant-contact-v3-openapi.yml
        type: OpenAPI
    description: Production REST API for Constant Contact's email marketing, SMS, and events platform. OAuth2 authorization (auth code, PKCE, and JWT-bearer flows) gates all endpoints across account services, contacts, contact lists, tags, custom fields, segments, email campaigns and activities (with A/B tests, schedules, and tests), bulk activities for high-volume mutations, events (registrations, tracks, check-in, payment status), contact reporting, landing pages, and partner technology-account provisioning.
common:
  - type: Website
    url: https://www.constantcontact.com/
  - type: Portal
    url: https://developer.constantcontact.com/
  - type: Getting Started
    url: https://developer.constantcontact.com/api_guide/index.html
  - type: Authentication
    url: https://developer.constantcontact.com/api_guide/auth_overview.html
  - type: API Reference
    url: https://developer.constantcontact.com/api_reference/index.html
  - type: OpenAPI
    url: https://api.cc.email/v3/swagger.yaml
  - type: Status
    url: https://status.constantcontact.com/
  - type: Support
    url: https://www.constantcontact.com/help
  - type: Community
    url: https://community.constantcontact.com/
  - type: Blog
    url: https://blogs.constantcontact.com/
  - type: GitHub Organization
    url: https://github.com/constantcontact
  - type: Privacy Policy
    url: https://www.constantcontact.com/legal/privacy-statement
  - type: Terms of Service
    url: https://www.constantcontact.com/legal/terms-of-use
  - type: JSON-LD
    url: json-ld/constant-contact-context.jsonld
  - type: JSONSchema
    url: json-schema/constant-contact-contact-schema.json
  - type: JSONSchema
    url: json-schema/constant-contact-campaign-schema.json
  - type: Spectral
    url: rules/constant-contact-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/constant-contact-capabilities.yml
  - type: Features
    data:
      - 'Lite: $12/mo for 500 contacts (jumps to $50/mo at 1K)'
      - 'Standard: mid-tier with A/B testing, segmentation'
      - 'Premium: $80/mo at 500 contacts with 24x email ratio'
      - 'Email overages: $0.002 per additional email'
      - REST API v3 at api.cc.email/v3
      - 'API limit: 4 req/sec, 10K req/day per app'
      - OAuth 2.0
      - Webhooks for contact and campaign events
      - Contacts, lists, segments, custom fields
      - Email Templates and Drag-and-Drop editor
      - Marketing Automation (Standard+)
      - Surveys, landing pages, social media posts
      - Reporting on opens, clicks, bounces, conversions
      - E-commerce integrations (Shopify, WooCommerce, etc.)
      - Event marketing and registration
      - List building tools and lead capture
    sources:
      - https://www.constantcontact.com/pricing
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
