---
aid: inbox
name: Inbox
description: Inbox is an API Evangelist index of email and inbox-oriented API platforms that developers use to send, receive, parse, route, schedule, and verify email messages. The index focuses on transactional and conversational email providers exposing programmatic access to message lifecycle, deliverability, and inbox automation primitives.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Email
  - Inbox
  - Messaging
  - Deliverability
  - Transactional Email
url: https://raw.githubusercontent.com/api-evangelist/inbox/refs/heads/main/apis.yml
created: '2024-12-25'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: inbox:mailgun-email-api
    name: Mailgun Email API
    description: Mailgun provides a programmable email API for sending, receiving, tracking, and validating email at scale. Endpoints cover messages, domains, suppressions, mailing lists, webhooks, inbound routes, event streams, and inbox placement testing for deliverability monitoring.
    humanURL: https://www.mailgun.com/
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Email
      - Transactional Email
      - Deliverability
      - Inbound Parsing
    properties:
      - type: Documentation
        url: https://documentation.mailgun.com/docs/mailgun/api-reference/intro/
      - type: Reference
        url: https://documentation.mailgun.com/docs/mailgun/api-reference/openapi-final/tag/Introduction/
      - type: Pricing
        url: https://www.mailgun.com/pricing/
      - type: SignUp
        url: https://signup.mailgun.com/new/signup
  - aid: inbox:nylas-email-api
    name: Nylas Email API
    description: Nylas exposes a unified REST API for email, calendar, contacts, and scheduling across Google, Microsoft, iCloud, and IMAP providers. Developers can read, send, and thread messages, manage folders and labels, handle attachments, and subscribe to webhook notifications without integrating each provider individually.
    humanURL: https://www.nylas.com/products/email-api/
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Email
      - Unified API
      - IMAP
      - Webhooks
    properties:
      - type: Documentation
        url: https://developer.nylas.com/docs/v3/email/
      - type: Reference
        url: https://developer.nylas.com/docs/api/v3/ecc/
      - type: Pricing
        url: https://www.nylas.com/pricing/
      - type: SignUp
        url: https://dashboard-v3.nylas.com/register
common:
  - type: Website
    url: https://apievangelist.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
