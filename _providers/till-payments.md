---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.6
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Till Payments Agentic Access
  operation_count: 35
  slug: till-payments-agentic-access
  summary_line: 35 operations · 32 acting
api_count: 4
apis:
- description: The Till Payments Gateway V3 API for processing card-present and card-not-present transactions — debit, preauthorize, capture, void, refund, payout, registration/tokenization, recurring schedules, tra
  name: Till Payments Gateway API
  slug: till-payments-gateway
- description: The Till Payments Direct PCI-enabled Payment Platform V3 API for merchants that are PCI DSS certified to collect and transmit raw cardholder data. Requests are sent over HTTPS (TLS 1.2+) with JSON bod
  name: Till Payments Direct PCI-enabled API
  slug: till-payments-direct-pci
- description: The Till Payments Pay By Link API for generating shareable hosted payment links, documented on the Till developer documentation site. No downloadable OpenAPI specification was published for this produ
  name: Till Payments Pay By Link API
  slug: till-payments-pay-by-link
- description: Terminal Connect is Till Payments' in-person integration surface for connecting point-of-sale software to Till payment terminals, documented via getting-started and integration guides on the Till deve
  name: Till Payments Terminal Connect API
  slug: till-payments-terminal-connect
arazzos:
- description: Preauthorize a card payment, then capture the reserved funds, on the Till Payments Gateway V3 API.
  name: Till Payments — authorize and capture
  slug: till-payments-authorize-and-capture
- description: Register (tokenize) a payment instrument, then charge it with a debit using the returned transactionToken.
  name: Till Payments — tokenize and charge
  slug: till-payments-tokenize-and-charge
artifact_total: 13
asyncapis:
- description: ''
  name: Till Payments Callbacks Webhooks
  slug: till-payments-callbacks-webhooks
collections:
- collection_type: open
  name: tillpayments.com Payment Platform
  slug: open-till-payments-direct-pci
- collection_type: open
  name: Till Payments Gateway
  slug: open-till-payments-gateway
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/till-payments-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/till-payments-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/till-payments-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/till-payments-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/till-payments-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/till-payments-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/till-payments-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/till-payments-callbacks-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/till-payments-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/till-payments-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/till-payments-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/till-payments-authorize-and-capture.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/till-payments-tokenize-and-charge.yml
- group: company
  title: ''
  type: Website
  url: https://tillpayments.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://tillpayments.com/developer-hub
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tillpayments.com/guides
- group: docs
  title: ''
  type: APIReference
  url: https://gateway.tillpayments.com/documentation/apiv3
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tillpayments
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tillpayments.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://tillpayments.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://tillpayments.com/blog
- group: operate
  title: ''
  type: Support
  url: https://tillpayments.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tillpayments.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tillpayments.com/privacy-policy
created: '2026-07-24'
description: 'Till Payments is a Sydney, Australia founded merchant acquirer and payment technology company (established 2012), focused on integrated payments for independent software vendors, platforms, and omnichannel merchants across online, in-person, and unattended channels. Its product family spans a card-present and card-not-present processing Gateway, a PCI-enabled Direct API for merchants handling raw card data, Pay By Link, and Terminal Connect for in-person device integrations. Till was acquired by Nuvei in 2024 and now operates as part of Nuvei''s global platform while retaining its Australian home market and developer surface. Its API posture is genuinely API-first: a public developer hub, hosted V3 reference documentation, and two downloadable OpenAPI 3.0 specifications (the Gateway API and the Direct PCI-enabled Payment Platform), both authenticated with HTTP Basic credentials over TLS 1.2+.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: till-payments-mcp.yml
  slug: till-payments-mcpyml
modified: '2026-07-24'
name: Till Payments
nav: Providers
network: true
overview: 'Till Payments publishes 2 APIs on the [APIs.io](https://apis.io/) network: Gateway API and Direct PCI-enabled API. Tagged areas include Payments, Australia, Payment Gateway, Payment Processing, and Acquiring.


  The Till Payments catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Till Payments'' developer surface includes authentication, documentation, API reference, pricing, engineering blog, support, and 19 more developer resources.'
random_paper: 22
score:
  band: thin
  composite: 38.2
  delta: -4.1
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 16.7
    contract_quality: 60.8
    developer_ergonomics: 39.9
    discoverability: 72.2
    governance: 16.7
    operational_transparency: 26.3
  previous_composite: 42.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/till-payments/refs/heads/main/screenshots/till-payments-2026-08-17T082354.png
security:
- kind: authentication
  name: Till Payments Authentication
  slug: till-payments-authentication
  summary_line: http · 3 schemes
- kind: domain-security
  name: Till Payments Domain Security
  slug: till-payments-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: till-payments
tags:
- Payments
- Australia
- Payment Gateway
- Payment Processing
- Acquiring
- Merchant Services
- Card Payments
- In-Person Payments
website: https://tillpayments.com/
---
