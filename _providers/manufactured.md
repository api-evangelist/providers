---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://manufactured.com
- group: start
  title: ''
  type: Login
  url: https://app.manufactured.com
- group: auth
  title: ''
  type: DomainSecurity
  url: security/manufactured-domain-security.yml
created: '2026-07-17'
description: Manufactured is a supply-chain and production platform for hardware and consumer-product brands, backed by Bullpen Capital. Its web application (app.manufactured.com) helps teams run overseas production end to end — issuing sourcing requests to vendors, managing supplier and vendor profiles, negotiating order estimates and contracts under master procurement agreements, tracking production timelines and calendars, and financing purchase orders through production and repayment terms. The product also embeds an AI assistant built on LangChain. At the time of enrichment the public marketing site and the api/docs/developer subdomains were unreachable, and the GraphQL, Lambda and bot backends are private and authentication-gated (introspection blocked), so no public API specification, developer portal, or documentation could be harvested. This profile captures the real, observable surface only.
image: https://app.manufactured.com/logo192.png
layout: provider
modified: '2026-07-20'
name: Manufactured
nav: Providers
network: true
overview: Manufactured is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Manufacturing, Supply Chain, Sourcing, and Procurement.
random_paper: 19
score:
  band: minimal
  composite: 6.3
  coverage:
    artifact_dirs: 1
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Manufactured Domain Security
  slug: manufactured-domain-security
  summary_line: DNSSEC · DMARC
slug: manufactured
tags:
- Company
- Manufacturing
- Supply Chain
- Sourcing
- Procurement
- Hardware
- Production Financing
- Vendor Management
- AI Assistant
website: https://manufactured.com
---
