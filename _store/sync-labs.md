---
aid: sync-labs
name: Sync Labs
description: Sync Labs (sync.so) provides a suite of studio-grade AI lip-sync and visual dubbing APIs. Their technology synchronizes video lip movements with any audio track using state-of-the-art models, enabling professional video dubbing, content localization, and personalized video generation at scale. Models include sync-3, lipsync-2-pro, lipsync-2, lipsync-1.9, and react-1, with support for batch processing (up to 500 videos), webhooks, Python and TypeScript SDKs, Adobe Premiere plugin, and ComfyUI integration. Backed by Y Combinator.
image: https://sync.so/favicon.ico
tags:
  - Artificial Intelligence
  - Content Localization
  - Dubbing
  - Lip Sync
  - Media
  - Video
  - Visual AI
type: Index
position: Consumer
access: 3rd-Party
created: '2026-05-03'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/sync-labs/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: sync-labs:sync-labs-api
    name: Sync Labs API
    description: The Sync Labs REST API provides programmatic access to AI lip-sync and visual dubbing capabilities. Submit video and audio inputs to generate studio-grade synchronized output videos. Supports single generation, batch processing of up to 500 videos, asset management, cost estimation, and webhook notifications. Rate limited to 60 requests/min for generation endpoints.
    humanURL: https://sync.so/api
    baseURL: https://api.sync.so/v2
    tags:
      - Artificial Intelligence
      - Batch Processing
      - Dubbing
      - Lip Sync
      - Media Processing
      - Video
      - Webhooks
    properties:
      - type: Documentation
        url: https://sync.so/docs/introduction
      - type: OpenAPI
        url: openapi/sync-labs-openapi.yml
      - type: Pricing
        url: https://sync.so/pricing
      - type: Quickstart
        url: https://sync.so/docs/quickstart
  - aid: sync-labs:sync-labs-python-sdk
    name: Sync Labs Python SDK
    description: Official Python SDK for integrating the Sync Labs lip-sync API into Python applications. Supports Python 3.8+. Install via pip install syncsdk.
    humanURL: https://sync.so/docs/introduction
    tags:
      - Python
      - SDK
    properties:
      - type: Documentation
        url: https://sync.so/docs/introduction
      - type: PyPI
        url: https://pypi.org/project/syncsdk/
  - aid: sync-labs:sync-labs-typescript-sdk
    name: Sync Labs TypeScript SDK
    description: Official TypeScript/Node.js SDK for integrating the Sync Labs API. Supports Node.js 18+. Install via npm install @sync.so/sdk.
    humanURL: https://sync.so/docs/introduction
    tags:
      - JavaScript
      - Node.js
      - SDK
      - TypeScript
    properties:
      - type: Documentation
        url: https://sync.so/docs/introduction
      - type: NPM
        url: https://www.npmjs.com/package/@sync.so/sdk
common:
  - type: Website
    url: https://sync.so
  - type: Documentation
    url: https://sync.so/docs/introduction
  - type: Quickstart
    url: https://sync.so/docs/quickstart
  - type: Pricing
    url: https://sync.so/pricing
  - type: API Keys
    url: https://sync.so/settings/api-keys
  - type: Sign Up
    url: https://sync.so/sign-up
  - type: Contact
    url: mailto:hello@sync.so
  - type: Y Combinator
    url: https://www.ycombinator.com/companies/sync-2
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
