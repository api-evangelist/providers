---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: 'Live production API host operated by Blockskye, discovered by probe. The host answers as a Fastify service behind AWS API Gateway: GET /health returns 200 with a JSON status/bootId payload, every othe'
  name: Blockskye API
  slug: blockskye-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.blockskye.com/
- group: other
  title: ''
  type: Platform
  url: https://www.blockskye.com/blockskye-platform
- group: company
  title: ''
  type: About
  url: https://www.blockskye.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.blockskye.com/latestnews
- group: operate
  title: ''
  type: Support
  url: https://www.blockskye.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.blockskye.com/support/home
- group: start
  title: ''
  type: Login
  url: https://horizon.blockskye.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blockskye.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blockskye.com/privacy-policy
- group: company
  title: ''
  type: Careers
  url: https://www.blockskye.com/careers
- group: other
  title: ''
  type: Glossary
  url: https://www.blockskye.com/glossary
- group: build
  title: ''
  type: Library
  url: https://www.blockskye.com/resources/library
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blockskye-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/blockskye-llms.txt
coverage:
  checked: '2026-08-07'
  detail: Blockskye runs a live production API at api.blockskye.com whose /health endpoint answers 200 anonymously, but the only Blockskye documentation that exists sits in a Freshworks-backed knowledge base where /support/solutions chains 302 to /support/home to /support/login and out to a blockskye.myfreshworks.com OAuth authorize URL, so the reference is reachable only by an existing customer tenant.
  evidence:
  - status: 302
    url: https://support.blockskye.com/support/solutions
  - status: 302
    url: https://support.blockskye.com/support/login
  - status: 200
    url: https://api.blockskye.com/health
  - status: 404
    url: https://api.blockskye.com/openapi.json
  - status: 404
    url: https://api.blockskye.com/documentation/json
  - status: 404
    url: https://www.blockskye.com/llms.txt
  - status: 404
    url: https://www.blockskye.com/.well-known/security.txt
  - status: 200
    url: https://horizon.blockskye.com/login
  reason: customer-only-docs
  state: gated
created: '2026-08-07'
description: 'Blockskye is an enterprise travel management and payments platform for large corporate travel programs, founded in 2017 and headquartered in New York. It combines a consumer-grade online booking tool sourced through direct supplier and NDC connectivity, BMAX direct settlement that wires a customer''s ERP straight to travel suppliers so booked travel bypasses corporate cards and expense reports, B360 for capturing personal co-brand card loyalty on business trips while holding policy compliance, and real-time reporting across every booking channel, with transactions recorded to a tamper-resistant distributed ledger. Blockskye delivers an end-to-end corporate travel solution in partnership with KAYAK for Business. The platform is sold and operated as an enterprise service: the booking, servicing and settlement application runs at horizon.blockskye.com behind a customer login and the knowledge base sits behind a Freshworks OAuth login. Blockskye operates a live production API host
  at api.blockskye.com but publishes no public developer portal, API reference, or machine-readable API contract.'
image: https://static1.squarespace.com/static/68efa9e7e26dde07bc4331ce/t/690a135f62cc1b156338a90e/1778097079157/SEOblockskye.jpg?format=1500w
layout: provider
modified: '2026-08-07'
name: Blockskye
nav: Providers
network: true
overview: 'Blockskye publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Corporate Travel, Travel Management, Payments, and Settlement.


  Blockskye''s developer surface includes engineering blog, support, and 12 more developer resources.'
random_paper: 73
rate_limits:
- limit_count: 1
  name: Blockskye Rate Limits
  slug: blockskye-rate-limits
score:
  band: emerging
  composite: 15.7
  delta: -3.3
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 19.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blockskye/refs/heads/main/screenshots/blockskye-2026-08-07T162631.png
security:
- kind: domain-security
  name: Blockskye Domain Security
  slug: blockskye-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blockskye
tags:
- Travel
- Corporate Travel
- Travel Management
- Payments
- Settlement
- Expense Management
- Booking
- Blockchain
- Distributed Ledger
- Enterprise
website: https://www.blockskye.com/
---
