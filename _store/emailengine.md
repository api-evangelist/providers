---
aid: emailengine
name: EmailEngine
description: EmailEngine is a self-hosted email automation platform that provides a unified REST API for accessing email accounts via IMAP, SMTP, the Gmail API, and the Microsoft Graph API. It exposes JSON payloads, real-time webhooks, OAuth2 integration, an IMAP/SMTP proxy, hosted authentication forms, low-code custom integrations, Prometheus monitoring, and bounce detection so developers can build modern email functionality without paying per-account fees.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
tags:
  - Email
  - Email API
  - IMAP
  - SMTP
  - Webhooks
url: https://raw.githubusercontent.com/api-evangelist/emailengine/refs/heads/main/apis.yml
created: '2025-02-06'
modified: '2026-04-28'
specificationVersion: '0.19'
access: 3rd-Party
position: Consumer
apis:
  - aid: emailengine:emailengine
    name: EmailEngine API
    description: EmailEngine API exposes a unified REST interface for sending and receiving email through IMAP, SMTP, Gmail, and Microsoft Graph. Developers can manage mailboxes, send messages, work with attachments, configure webhooks, and automate OAuth2 token renewal across consumer and enterprise email providers.
    humanURL: https://emailengine.app/
    baseURL: https://api.emailengine.app
    tags:
      - Email
      - Email API
      - IMAP
      - SMTP
    properties:
      - url: https://emailengine.app/
        type: Documentation
      - url: https://learn.emailengine.app/docs/api/emailengine-api
        type: API Reference
      - url: https://learn.emailengine.app/
        type: Documentation
      - url: https://github.com/postalsys/emailengine
        type: SourceCode
      - url: https://emailengine.app/webhooks
        type: Webhooks
    contact:
      - FN: EmailEngine Support
        email: info@postalsys.com
common:
  - name: EmailEngine Documentation
    url: https://learn.emailengine.app/
    type: Documentation
  - name: API Reference
    url: https://learn.emailengine.app/docs/api/emailengine-api
    type: API Reference
  - name: Webhooks
    url: https://emailengine.app/webhooks
    type: Webhooks
  - name: GitHub Repository
    url: https://github.com/postalsys/emailengine
    type: SourceCode
  - name: Blog
    url: https://blog.emailengine.app/
    type: Blog
  - name: FAQ
    url: https://emailengine.app/#faq
    type: FAQ
  - name: Pricing
    url: https://postalsys.com/plans
    type: Pricing
  - name: Terms of Service
    url: https://postalsys.com/tos
    type: TermsOfService
  - name: Privacy Policy
    url: https://emailengine.app/privacy-policy
    type: PrivacyPolicy
  - name: Support
    url: https://emailengine.app/support
    type: Support
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
