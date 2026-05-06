---
aid: traiana
url: https://raw.githubusercontent.com/api-evangelist/traiana/refs/heads/main/apis.yml
apis:
  - aid: traiana:harmony-trade-processing
    name: Traiana Harmony Trade Processing API
    tags:
      - Fintech
      - Foreign Exchange
      - Post-Trade Processing
      - Trade Matching
    humanURL: https://www.cmegroup.com/services/traiana.html
    properties:
      - url: https://www.cmegroup.com/services/traiana.html
        type: Documentation
      - url: openapi/traiana-harmony-trade-processing-openapi.yml
        type: OpenAPI
      - url: json-schema/trade.json
        type: JSONSchema
      - url: json-schema/allocation.json
        type: JSONSchema
      - url: json-schema/give-up.json
        type: JSONSchema
      - url: json-ld/traiana-context.jsonld
        type: JSONLD
    description: The Traiana Harmony Trade Processing API provides cross-asset post-trade processing capabilities through the Harmony network. It enables automated trade allocation, matching, confirmation, give-up messaging, and reporting across FX, equities, equity derivatives, and exchange-traded derivatives. Harmony connects over 1,000 firms and supports 15,000 cross-asset trading relationships, handling $2 trillion in daily transaction volume.
  - aid: traiana:harmony-creditlink
    name: Traiana Harmony CreditLink API
    tags:
      - Credit Risk
      - Fintech
      - Foreign Exchange
      - Risk Management
    humanURL: https://www.cmegroup.com/services/traiana.html
    properties:
      - url: https://www.cmegroup.com/services/traiana.html
        type: Documentation
      - url: openapi/traiana-harmony-creditlink-openapi.yml
        type: OpenAPI
      - url: json-schema/credit-limit.json
        type: JSONSchema
      - url: json-ld/traiana-context.jsonld
        type: JSONLD
    description: The Traiana Harmony CreditLink API provides real-time pre-trade and post-trade credit risk management across prime-brokered, cleared, and bilateral relationships. CreditLink is composed of the Designation Notice Manager (DNM), Tri-Party Limit Manager (TPL), and ECN Limit Manager (ELM), enabling limit monitoring, breach detection, credit line modification, and trading termination in real time through integration with exchange APIs.
  - aid: traiana:harmony-netlink
    name: Traiana Harmony NetLink API
    tags:
      - Fintech
      - Netting
      - Settlement
      - Trade Compression
    humanURL: https://www.cmegroup.com/services/traiana.html
    properties:
      - url: https://www.cmegroup.com/services/traiana.html
        type: Documentation
      - url: openapi/traiana-harmony-netlink-openapi.yml
        type: OpenAPI
      - url: json-schema/netting-session.json
        type: JSONSchema
      - url: json-schema/settlement.json
        type: JSONSchema
      - url: json-ld/traiana-context.jsonld
        type: JSONLD
    description: The Traiana Harmony NetLink API provides netting, settlement orchestration, and trade compression services. NetLink enables counterparties to perform on-demand intraday netting of FX transactions, pre-settlement netting for equities, and trade compression between retail brokers and executing brokers. It reduces settlement risk and optimizes intraday liquidity through PvP settlement orchestration, including same-day settlement.
name: Traiana
tags:
  - Fintech
  - Foreign Exchange
  - Post-Trade Processing
  - Risk Management
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://www.cmegroup.com/services/traiana.html
    name: Traiana Trade Lifecycle Processing
    type: Documentation
    description: 'null'
  - url: https://osttra.com/services/post-trade-processing/trade-processing/
    name: OSTTRA Trade Processing
    type: Documentation
    description: 'null'
  - url: https://osttra.com/support/
    name: OSTTRA Support
    type: Support
    description: 'null'
  - type: Spectral
    url: rules/traiana-rules.yml
  - type: Vocabulary
    url: vocabulary/traiana-vocabulary.yml
created: '2025-01-01'
modified: '2026-05-03'
position: Consumer
description: Traiana, part of CME Group and now operating under OSTTRA, is a leading market infrastructure technology provider offering pre-trade risk monitoring and automated post-trade processing for listed and OTC trading. Its Harmony network connects over 1,000 firms via a cloud-based platform supporting 15,000 cross-asset trading relationships and handling $2 trillion in daily transaction volume across FX, equities, equity derivatives, and exchange-traded derivatives.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
