---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Token-authenticated REST API for Anvyl's supply chain / production platform. Resources are served under https://api.anvyl.com/api/v1 (e.g. purchase orders); unauthenticated requests return 401. Docume
  name: Anvyl API
  slug: anvyl-api
artifact_total: 5
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/sage/
- group: docs
  title: ''
  type: Documentation
  url: https://anvyl.stoplight.io/docs/anvyl-api
- group: docs
  title: ''
  type: APIReference
  url: https://anvyl.stoplight.io/docs/anvyl-api
- group: auth
  title: ''
  type: Authentication
  url: authentication/anvyl-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/anvyl-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/anvyl-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.sage.com/en-gb/trust-security/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/anvyl-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/anvyl-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/anvyl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.anvyl.com/
created: '2026-07-17'
description: 'Anvyl is a supply chain and production management platform (a "Production Hub") for consumer-brand and e-commerce companies, connecting brands with their suppliers to manage the purchase-order and manufacturing lifecycle in one place: issuing and tracking purchase orders, coordinating production milestones and tasks, managing suppliers and SKUs/products, and monitoring inbound shipments and logistics. Anvyl was acquired by Sage and now operates under the Sage umbrella. It exposes a token-authenticated REST API (api.anvyl.com/api/v1) documented via Stoplight, with resources such as purchase orders. This profile was surfaced as a portfolio company of Redpoint Ventures and enriched by the API Evangelist pipeline from Anvyl''s live public developer surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/anvyl.png
layout: provider
modified: '2026-07-17'
name: Anvyl
nav: Providers
network: true
overview: 'Anvyl publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Logistics, Supply Chain, Procurement, and Purchase Orders.


  Anvyl''s developer surface includes documentation, API reference, authentication, and 8 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 15.5
  coverage:
    artifact_dirs: 4
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 15.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/anvyl/refs/heads/main/screenshots/anvyl-2026-07-25T200445.png
security:
- kind: authentication
  name: Anvyl Authentication
  slug: anvyl-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Anvyl Domain Security
  slug: anvyl-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Anvyl Vulnerability Disclosure
  slug: anvyl-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Anvyl Trust Center
  slug: anvyl-trust-center
  summary_line: trust center published
slug: anvyl
tags:
- Company
- Logistics
- Supply Chain
- Procurement
- Purchase Orders
- Manufacturing
- Production Management
website: https://www.anvyl.com/
---
