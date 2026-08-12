---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 31
  human_in_the_loop: 0
  name: Celcoin Agentic Access
  operation_count: 45
  slug: celcoin-agentic-access
  summary_line: 45 operations · 31 acting
api_count: 15
apis:
- description: APIs for white-label card account creation and management, card issuance and tracking, transaction simulation, post-paid invoice management, recurring subscriptions, and webhook-driven card event noti
  name: Celcoin Card Solutions API
  slug: cards
- description: Embedded payment APIs covering bill payments, mobile recharges, vehicle debit, payment gateway with multi-acquirer support, Pix instant payments, withdrawals and deposits, and Payment Initiation (ITP)
  name: Celcoin Payments API
  slug: payments
- description: Open Finance and Open Banking APIs for Payment Initiation (ITP with and without redirect), account linking with FIDO biometrics, data sharing and consent management, and sweeping accounts for intellig
  name: Celcoin Open Finance API
  slug: open-finance
- description: The AnnotationCompetenceCalendar API from Celcoin — 1 operation(s) for annotationcompetencecalendar.
  name: Celcoin AnnotationCompetenceCalendar API
  slug: celcoin-annotationcompetencecalendar-api
- description: The BankCorrespondentAgent API from Celcoin — 2 operation(s) for bankcorrespondentagent.
  name: Celcoin BankCorrespondentAgent API
  slug: celcoin-bankcorrespondentagent-api
- description: The Consignee API from Celcoin — 1 operation(s) for consignee.
  name: Celcoin Consignee API
  slug: celcoin-consignee-api
- description: The Files API from Celcoin — 1 operation(s) for files.
  name: Celcoin Files API
  slug: celcoin-files-api
- description: The Guarantee API from Celcoin — 21 operation(s) for guarantee.
  name: Celcoin Guarantee API
  slug: celcoin-guarantee-api
- description: The LegacyGuarantee API from Celcoin — 1 operation(s) for legacyguarantee.
  name: Celcoin LegacyGuarantee API
  slug: celcoin-legacyguarantee-api
- description: The LegalPerson API from Celcoin — 1 operation(s) for legalperson.
  name: Celcoin LegalPerson API
  slug: celcoin-legalperson-api
- description: The NaturalPerson API from Celcoin — 2 operation(s) for naturalperson.
  name: Celcoin NaturalPerson API
  slug: celcoin-naturalperson-api
- description: The OutstandingBalance API from Celcoin — 4 operation(s) for outstandingbalance.
  name: Celcoin OutstandingBalance API
  slug: celcoin-outstandingbalance-api
- description: The Proposal API from Celcoin — 2 operation(s) for proposal.
  name: Celcoin Proposal API
  slug: celcoin-proposal-api
- description: The Settlement API from Celcoin — 2 operation(s) for settlement.
  name: Celcoin Settlement API
  slug: celcoin-settlement-api
- description: The TaggingJourney API from Celcoin — 1 operation(s) for taggingjourney.
  name: Celcoin TaggingJourney API
  slug: celcoin-taggingjourney-api
artifact_total: 22
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/celcoin-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/celcoin-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/celcoin-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.celcoin.com.br/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.celcoin.com.br/docs
- group: docs
  title: ''
  type: Reference
  url: https://developers.celcoin.com.br/reference
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/celcoincell
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/celcoin-financial-hub/
- group: company
  title: ''
  type: Blog
  url: https://www.celcoin.com.br/articles/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.celcoin.com.br/developers/
- group: operate
  title: ''
  type: StatusPage
  url: https://redecelcoin.statuspage.io/
- group: other
  title: ''
  type: X
  url: https://x.com/celcoinbr
- group: commercial
  title: ''
  type: Plans
  url: plans/celcoin-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/celcoin-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/celcoin-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/celcoin-vocabulary.json
- group: build
  title: ''
  type: Examples
  url: examples/celcoin-examples.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/celcoin-jsonld.json
created: '2026-06-13'
description: Celcoin is a Brazilian Banking-as-a-Service (BaaS) infratech platform that provides REST APIs for Pix, boleto, TED transfers, bill payments, prepaid and post-paid cards, digital account opening, open banking integration, and credit operations. Processing over R$30 billion monthly across 6,000+ clients, Celcoin enables fintechs, digital banks, and enterprises to embed financial services without a banking license.
examples:
- key_count: 1
  name: Celcoin Examples
  slug: celcoin-examples
finops:
- name: Celcoin Finops
  service_category: ''
  slug: celcoin-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/celcoin.png
layout: provider
modified: '2026-06-13'
name: Celcoin
nav: Providers
network: true
overview: 'Celcoin publishes 12 APIs on the [APIs.io](https://apis.io/) network, including AnnotationCompetenceCalendar API, BankCorrespondentAgent API, Consignee API, and 9 more. Tagged areas include Banking as a Service, BaaS, Pix, Boleto, and TED.


  Celcoin''s developer surface includes authentication, documentation, engineering blog, pricing, code examples, and 13 more developer resources.'
plans:
- name: Celcoin Plans Pricing
  plan_count: 4
  slug: celcoin-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 0
  name: Celcoin Rate Limits
  slug: celcoin-rate-limits
score:
  band: thin
  composite: 36.4
  delta: -0.4
  facets:
    commercial_clarity: 50.0
    contract_quality: 48.1
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 10.4
    operational_transparency: 21.1
  previous_composite: 36.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 21.5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/celcoin/refs/heads/main/screenshots/celcoin-2026-06-20T174114.png
security:
- kind: authentication
  name: Celcoin Authentication
  slug: celcoin-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Celcoin Domain Security
  slug: celcoin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: celcoin
tags:
- Banking as a Service
- BaaS
- Pix
- Boleto
- TED
- Bill Payments
- Prepaid Cards
- Digital Accounts
- Open Banking
- Open Finance
- Credit
- Fintech
- Brazil
- Financial Infrastructure
website: https://www.celcoin.com.br/
---
