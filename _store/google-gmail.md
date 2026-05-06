---
aid: google-gmail
name: Google Gmail
description: The Gmail API lets you view and manage Gmail mailbox data like threads, messages, and labels. It provides RESTful access to Gmail mailboxes, supporting message sending, drafting, organizing with labels, managing settings, and push notifications for mailbox changes. The API uses OAuth 2.0 for authorization and supports both user and service account authentication for Google Workspace domains.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-gmail/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Drafts
  - Email
  - Gmail
  - Google
  - Google Workspace
  - Labels
  - Messaging
  - Threads
apis:
  - name: Google Gmail API
    description: The Gmail API provides programmatic access to Gmail mailboxes. It supports typical mailbox operations like reading, composing, and sending messages, managing drafts, labels, threads, and configuring account settings including forwarding, filters, and delegates.
    humanURL: https://developers.google.com/workspace/gmail/api/guides
    baseURL: https://gmail.googleapis.com
    tags:
      - Drafts
      - Email
      - Gmail
      - Labels
      - Messages
      - Threads
    properties:
      - type: Documentation
        url: https://developers.google.com/workspace/gmail/api/reference/rest
      - type: OpenAPI
        url: openapi/openapi.yml
      - type: Authentication
        url: https://developers.google.com/workspace/gmail/api/auth/about-auth
      - type: Getting Started
        url: https://developers.google.com/workspace/gmail/api/guides
      - type: JSONSchema
        url: json-schema/json-schema.yml
      - type: JSONLD
        url: json-ld/json-ld.jsonld
common:
  - type: Portal
    url: https://developers.google.com/workspace/gmail
  - type: Getting Started
    url: https://developers.google.com/workspace/gmail/api/guides
  - type: Documentation
    url: https://developers.google.com/workspace/gmail/api
  - type: Authentication
    url: https://developers.google.com/workspace/gmail/api/auth/about-auth
  - type: Pricing
    url: https://developers.google.com/workspace/gmail/api/guides/quota
  - type: Terms of Service
    url: https://developers.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://status.cloud.google.com/
  - type: Support
    url: https://developers.google.com/workspace/gmail/api/support
  - type: JSONLD
    url: json-ld/json-ld.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
