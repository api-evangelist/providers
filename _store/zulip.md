---
aid: zulip
name: Zulip
description: Zulip is an open-source team chat application with a unique topic-based threading model. Zulip's APIs power the web and mobile apps and provide REST endpoints, incoming webhooks, outgoing webhooks, and event-driven integrations to connect Zulip with external services.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Collaboration
  - Messaging
  - Team Chat
  - Webhooks
created: '2026-01-02'
modified: '2026-03-16'
url: https://raw.githubusercontent.com/api-evangelist/zulip/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: zulip:rest-api
    name: Zulip REST API
    description: The Zulip REST API powers the Zulip web and mobile apps. It provides programmatic access to messages, streams, users, organizations, and all other Zulip functionality. Anything you can do in Zulip, you can do with the REST API.
    humanURL: https://zulip.com/api/rest
    tags:
      - Messaging
      - REST
      - Team Chat
    properties:
      - type: Documentation
        url: https://zulip.com/api/rest
      - type: Reference
        url: https://zulip.com/api/
  - aid: zulip:webhooks
    name: Zulip Webhooks
    description: Zulip supports both incoming webhooks (allowing third-party services to push data to Zulip) and outgoing webhooks (allowing Zulip to send HTTP POST payloads to external services when messages are sent).
    humanURL: https://zulip.com/api/incoming-webhooks-overview
    tags:
      - Events
      - Integrations
      - Webhooks
    properties:
      - type: Documentation
        url: https://zulip.com/api/incoming-webhooks-overview
      - type: Reference
        url: https://zulip.com/api/outgoing-webhooks
common:
  - url: https://zulip.com/
    name: Zulip - Team Chat
    type: Website
    description: 'null'
  - url: https://zulip.com/api/
    name: Zulip API Documentation
    type: Documentation
    description: 'null'
  - url: https://zulip.com/api/integrations-overview
    name: Zulip Integrations Overview
    type: Integrations
    description: 'null'
  - url: https://github.com/zulip
    name: Zulip GitHub Organization
    type: GitHubOrganization
    description: 'null'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
