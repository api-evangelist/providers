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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quantum-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://quantums.com.sa
- group: start
  title: ''
  type: Login
  url: https://app.one.quantums.com.sa
- group: commercial
  title: ''
  type: Plans
  url: plans/quantum-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/quantum-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/quantum-llms.txt
coverage:
  checked: '2026-08-12'
  detail: Quantum's only API surface is an /apikeys screen inside the login-gated Quantum One tenant app at app.one.quantums.com.sa; the marketing site is a single WordPress page with no developer section, and every contract and /.well-known path 404s on all four Quantum hosts.
  evidence:
  - status: 200
    url: https://app.one.quantums.com.sa/apikeys
  - status: 404
    url: https://quantums.com.sa/openapi.json
  - status: 404
    url: https://quantums.com.sa/.well-known/api-catalog
  - status: 404
    url: https://app.one.quantums.com.sa/.well-known/agent-card.json
  reason: customer-only-docs
  state: gated
created: '2026-07-17'
description: Quantum is a Saudi Arabian advertising-technology (adtech) enabler that bridges online publishers and advertisers with data and technology. Its Quantum One omnichannel platform connects online and offline retail experiences across programmatic ads, in-app media buying, e-sampling, on-ground activations, influencer marketing, and out-of-home media, with goal-attainment tracking, ROI measurement, customer-engagement analytics, and conversion-rate analysis. As of this enrichment pass the company publishes no public developer API, documentation, or developer portal; the Quantum One tenant application does carry an API-key management screen, so the platform issues keys to signed-in customers, but no contract, reference, or machine-readable spec is published anywhere.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quantum.png
layout: provider
modified: '2026-08-12'
name: Quantum
nav: Providers
network: true
overview: Quantum is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, AdTech, Marketing, and Programmatic.
plans:
- name: Quantum Plans Pricing
  plan_count: 0
  slug: quantum-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Quantum Rate Limits
  slug: quantum-rate-limits
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 5
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
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Quantum Domain Security
  slug: quantum-domain-security
  summary_line: TLSv1.3 · DMARC
slug: quantum
tags:
- Company
- Advertising
- AdTech
- Marketing
- Programmatic
- Omnichannel
- Retail Media
- Saudi Arabia
website: https://quantums.com.sa
---
