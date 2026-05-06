---
aid: lightning-labs
name: Lightning Labs
description: At Lightning Labs, we develop software that powers the Lightning Network. Our open source, secure, and scalable Lightning systems enable users to send and receive money more efficiently than ever before. We also offer a series of verifiable, non-custodial Lightning-based financial services. We bridge the world of open source software and the next-generation of bitcoin financial software.
type: Contract
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Bitcoin
  - Crypto
  - Lightning Network
  - Payments
created: '2024-11-08'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/lightning-labs/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: lightning-labs:lightning-labs
    name: Lightning Labs LND API
    description: REST API for the Lightning Network Daemon (lnd) by Lightning Labs, providing programmatic access to Lightning Network nodes for sending and receiving Bitcoin payments, channel management, wallet operations, and routing.
    humanURL: https://lightning.engineering/api-docs/api/lnd/
    tags:
      - Bitcoin
      - Crypto
      - Lightning Network
      - Payments
    properties:
      - type: Documentation
        url: https://lightning.engineering/api-docs/api/lnd/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/lightning-labs/refs/heads/main/openapi/lightning-labs-openapi.json
common:
  - type: GitHubOrganization
    url: https://github.com/lightningnetwork
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
