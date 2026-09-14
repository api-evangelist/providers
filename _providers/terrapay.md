---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
api_count: 1
apis:
- description: GSMA Mobile Money API profile for account validation, FX quotations, and multi-rail money movement (wallet/bank/card) across international corridors.
  name: TerraPay API Suite
  slug: terrapay-api-suite
artifact_total: 4
asyncapis:
- description: ''
  name: Terrapay Notifications Webhooks
  slug: terrapay-notifications-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.terrapay.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.terrapay.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.terrapay.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.terrapay.com/apiReference.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.terrapay.com/getStarted.html
- group: auth
  title: ''
  type: Authentication
  url: authentication/terrapay-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/terrapay-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/terrapay-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/terrapay-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/terrapay-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/terrapay-lifecycle.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/terrapay-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/terrapay-llms.txt
- group: start
  title: ''
  type: Sandbox
  url: sandbox/terrapay-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/terrapay-notifications-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/terrapay-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/terrapay-domain-security.yml
created: '2026-07-17'
description: TerraPay is a global cross-border payments and digital-wallet infrastructure company connecting banks, mobile wallets, money-transfer operators, merchants, and card networks into a single interoperable network for real-time international money movement. Its partner API Suite follows the GSMA Mobile Money API, exposing account validation, FX quotations, and multi-rail transactions (wallet, bank account, and card) across global remittance corridors, with compliance, monitoring, reconciliation, and reporting built into the platform. Partners authenticate with signed request headers over mutual TLS across Sandbox, UAT, and LIVE environments. Added to the API Evangelist network from the Partech portfolio and enriched from TerraPay's public developer portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/terrapay.png
layout: provider
modified: '2026-07-21'
name: TerraPay
nav: Providers
network: true
overview: 'TerraPay publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Payments, Cross-Border Payments, and Remittances.


  The TerraPay catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  TerraPay''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, and 12 more developer resources.'
random_paper: 11
screenshot: https://raw.githubusercontent.com/api-evangelist/terrapay/refs/heads/main/screenshots/terrapay-2026-09-02T163159.png
security:
- kind: authentication
  name: Terrapay Authentication
  slug: terrapay-authentication
  summary_line: apiKey/custom-signed-headers/mutualTLS · 6 schemes
- kind: domain-security
  name: Terrapay Domain Security
  slug: terrapay-domain-security
  summary_line: TLSv1.3 · DMARC
slug: terrapay
tags:
- Company
- Financial-Services
- Payments
- Cross-Border Payments
- Remittances
- Mobile Money
- Digital Wallet
- Money Transfer
- Fintech
- GSMA Mobile Money API
website: https://www.terrapay.com/
---
