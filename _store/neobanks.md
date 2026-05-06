---
aid: neobanks
name: Neobanks
description: A collection of APIs from leading neobanks and digital banking platforms including Revolut, Monzo, Starling Bank, N26, Nubank, Bunq, and others that offer modern banking services through developer-friendly APIs.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Digital Banking
  - Fintech
  - Mobile Banking
  - Neobank
  - Open Banking
url: https://raw.githubusercontent.com/api-evangelist/neobanks/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: neobanks:revolut
    name: Revolut API
    description: Digital banking platform offering accounts, payments, and financial services.
    humanURL: https://developer.revolut.com
    baseURL: https://api.revolut.com
    tags:
      - Banking
      - Fintech
      - Neobank
      - Payments
    properties:
      - type: Documentation
        url: https://developer.revolut.com/docs
      - type: Authentication
        url: https://developer.revolut.com/docs/api-authentication
  - aid: neobanks:monzo
    name: Monzo API
    description: UK-based digital bank with API-first approach.
    humanURL: https://docs.monzo.com
    baseURL: https://api.monzo.com
    tags:
      - Banking
      - Neobank
      - Open Banking
      - UK
    properties:
      - type: Documentation
        url: https://docs.monzo.com
  - aid: neobanks:starling-bank
    name: Starling Bank API
    description: UK digital bank with comprehensive developer platform.
    humanURL: https://developer.starlingbank.com
    baseURL: https://api.starlingbank.com
    tags:
      - Banking
      - Neobank
      - Open Banking
      - UK
    properties:
      - type: Documentation
        url: https://developer.starlingbank.com/docs
      - type: Getting Started
        url: https://developer.starlingbank.com/get-started
  - aid: neobanks:bunq
    name: Bunq API
    description: European neobank with extensive API capabilities.
    humanURL: https://doc.bunq.com
    baseURL: https://api.bunq.com
    tags:
      - Banking
      - Europe
      - Neobank
    properties:
      - type: Documentation
        url: https://doc.bunq.com
      - type: Reference
        url: https://doc.bunq.com/api-reference
      - type: GitHub Organization
        url: https://github.com/bunq
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
