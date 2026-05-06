---
aid: trioptima
url: https://raw.githubusercontent.com/api-evangelist/trioptima/refs/heads/main/apis.yml
name: Trioptima
description: Trioptima provides post-trade infrastructure services for the OTC derivatives market, including portfolio compression (triReduce), portfolio reconciliation (triResolve), and risk mitigation services. Originally founded in 2000, Trioptima became part of OSTTRA in 2021 — a joint venture combining MarkitServ, Traiana, TriOptima, and Reset to form a comprehensive post-trade services platform. Trioptima's services help financial institutions reduce counterparty risk, optimize capital requirements, and meet regulatory obligations across interest rate, credit, FX, and equity derivatives.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - CME Group
  - Derivatives
  - Financial Services
  - OSTTRA
  - Portfolio Compression
  - Post-Trade Services
  - Reconciliation
  - Risk Management
created: '2026-05-03'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: trioptima:trireduce-api
    name: Trioptima triReduce API
    tags:
      - Compression
      - Derivatives
      - Portfolio Optimization
      - Risk Reduction
    humanURL: https://osttra.com/services/optimisation/portfolio-compression/
    baseURL: https://rates.trireduce.com
    properties:
      - url: https://www.cmegroup.com/education/brochures-and-handbooks/trireduce-api
        type: Documentation
      - url: openapi/trioptima-trireduce-api-openapi.yml
        type: OpenAPI
      - url: rules/trioptima-rules.yml
        type: SpectralRules
      - url: vocabulary/trioptima-vocabulary.yml
        type: Vocabulary
    description: The triReduce API provides machine-to-machine access to TriOptima's portfolio compression cycles for OTC derivatives. The API allows cycle participants to automate participation in compression cycles, submit trade and risk data, and retrieve cycle results. Available for rates (IRS, OIS) and credit derivatives compression. Authentication uses OAuth 2.0 with read-only access for development and full access for production. Documentation available at https://rates.trireduce.com/api/v1/doc.
  - aid: trioptima:triresolve
    name: Trioptima triResolve Portfolio Reconciliation
    tags:
      - Collateral Management
      - Derivatives
      - Disputes
      - Reconciliation
      - Risk Management
    humanURL: https://osttra.com/services/trade-lifecycle-services/portfolio-reconciliation/
    baseURL: https://triResolve.com
    properties:
      - url: https://osttra.com/services/trade-lifecycle-services/portfolio-reconciliation/
        type: Documentation
    description: Trioptima triResolve is a web-based portfolio reconciliation service for OTC derivatives. It normalizes trade data, reconciles all fields using an algorithmic match engine, and provides break workflow for identifying, tracking, investigating, and resolving discrepancies. Over 1,500 firms use triResolve for bilateral and cleared portfolio reconciliation. Data submission via SFTP API file transfer or manual upload (QuickPort).
common:
  - type: Website
    url: https://osttra.com
    name: OSTTRA (TriOptima Parent)
  - type: Website
    url: https://osttra.com/login/trioptima-logins/
    name: TriOptima Logins
  - type: Documentation
    url: https://www.cmegroup.com/education/brochures-and-handbooks/trireduce-api
    name: triReduce API Documentation
  - type: Documentation
    url: https://osttra.com/services/optimisation/portfolio-compression/
    name: Portfolio Compression Service
  - type: Documentation
    url: https://osttra.com/services/trade-lifecycle-services/portfolio-reconciliation/
    name: Portfolio Reconciliation Service
  - type: GitHub
    url: https://github.com/TriOptima
    name: TriOptima GitHub Organization
  - type: GitHub
    url: https://github.com/osttra
    name: OSTTRA GitHub Organization
  - url: json-ld/trioptima-context.jsonld
    name: Trioptima JSON-LD Context
    type: JSONLDContext
  - url: json-schema/trioptima-compression-cycle-schema.json
    name: Compression Cycle JSON Schema
    type: JSONSchema
  - url: json-schema/trioptima-trade-schema.json
    name: Trade JSON Schema
    type: JSONSchema
  - url: vocabulary/trioptima-vocabulary.yml
    name: Trioptima Vocabulary
    type: Vocabulary
  - name: Features
    type: Features
    data:
      - name: Portfolio Compression (triReduce)
      - name: Portfolio Reconciliation (triResolve)
      - name: Collateral Management (triResolve Margin)
      - name: Risk Mitigation
      - name: Multilateral Compression
      - name: Bilateral Compression
      - name: Cleared IRS Compression
      - name: Credit Default Swap Compression
      - name: FX Forward Compression
      - name: Break Workflow Management
      - name: Dispute Resolution
      - name: SWIFT Integration
      - name: SFTP Data Transfer
      - name: OAuth 2.0 Authentication
  - name: Solutions
    type: Solutions
    data:
      - name: Interest Rate Derivatives Post-Trade
      - name: Credit Derivatives Post-Trade
      - name: FX Derivatives Post-Trade
      - name: Regulatory Compliance (EMIR, Dodd-Frank)
      - name: Capital Optimization
      - name: Counterparty Risk Reduction
  - name: Integrations
    type: Integrations
    data:
      - name: SWIFT
      - name: CLS (FX compression)
      - name: LCH
      - name: CME Clearing
      - name: Eurex
      - name: Bloomberg
      - name: Traiana
      - name: MarkitServ
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
