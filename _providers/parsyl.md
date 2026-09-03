---
access_model:
  confidence: low
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: 'Parsyl offers custom API integration into the Parsyl Platform so customers and Data Partner Program vendors can push or pull shipment, sensor and condition data. Documentation is served from Parsyl''s '
  name: Parsyl Platform API
  slug: parsyl-platform-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/parsyl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.parsyl.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.parsyl.com/
- group: company
  title: ''
  type: Blog
  url: https://www.parsyl.com/media
- group: operate
  title: ''
  type: Support
  url: https://www.parsyl.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.parsyl.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.parsyl.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/parsyl
- group: design
  title: ''
  type: Conformance
  url: conformance/parsyl-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/parsyl-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/parsyl-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/parsyl-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/parsyl-llms.txt
coverage:
  checked: '2026-08-26'
  detail: Parsyl's API reference lives on its own docs host, docs.parsyl.com, but every path there — including /openapi.json and /.well-known/* — 302s to /auth/login and into an Amazon Cognito user pool named parsyl-api-docs, so the contract is readable only by an authenticated Parsyl customer.
  evidence:
  - status: 302
    url: https://docs.parsyl.com/openapi.json
  - status: 302
    url: https://docs.parsyl.com/auth/login
  - status: 403
    url: https://api.parsyl.io/openapi.json
  - status: 404
    url: https://www.parsyl.com/llms.txt
  reason: customer-only-docs
  state: gated
created: '2026-08-26'
description: Parsyl Inc. is a Denver, Colorado based technology-enabled cargo insurance company for perishable and temperature-sensitive supply chains, with an office in London and underwriting capacity placed at Lloyd's of London. It pairs IoT temperature and condition sensors with a data platform that turns shipment telemetry into risk insight, and sells that insight back as connected marine cargo insurance products — ColdCover cargo insurance, stock throughput, excess stock, legal liability, a small-business program, and the cargo market's first parametric spoilage policy. Customers include food, seafood, pharmaceutical, vaccine and semiconductor shippers, plus global health programs such as Africa CDC and PFSCM. Parsyl runs a Data Partner Program that ingests telemetry from third-party monitoring vendors (Berlinger, Copeland, Roambee, Sensitech, Tive) and offers custom API integration so customers can pull their own systems' data into the Parsyl Platform. The API surface is real but
  is documented only to authenticated customers at docs.parsyl.com; no OpenAPI, AsyncAPI, MCP server or agent card is published publicly.
image: https://www.parsyl.com/hubfs/favicon.ico
layout: provider
modified: '2026-08-26'
name: Parsyl
nav: Providers
network: true
overview: 'Parsyl publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Cargo Insurance, Supply Chain, and Cold Chain.


  Parsyl''s developer surface includes documentation, engineering blog, support, and 10 more developer resources.'
plans:
- name: Parsyl Plans Pricing
  plan_count: 0
  slug: parsyl-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Parsyl Rate Limits
  slug: parsyl-rate-limits
score:
  band: emerging
  composite: 17.8
  coverage:
    artifact_dirs: 10
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 17.8
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 36.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/parsyl/refs/heads/main/screenshots/parsyl-2026-09-02T150909.png
security:
- kind: domain-security
  name: Parsyl Domain Security
  slug: parsyl-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: parsyl
tags:
- Company
- Insurance
- Cargo Insurance
- Supply Chain
- Cold Chain
- Logistics
- Internet of Things
- Sensors
- Risk Management
- Food Safety
- Pharmaceuticals
- Global Health
website: https://www.parsyl.com/
---
