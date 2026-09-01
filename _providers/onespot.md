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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/onespot-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/onespot-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/onespot-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/onespot-rate-limits.yml
- group: company
  title: ''
  type: Website
  url: https://onespot.com
coverage:
  checked: '2026-08-12'
  detail: OneSpot is fully absorbed into IgniteTech — every path on onespot.com and its api., developer. and app. subdomains answers a blanket HTTP 302 to https://ignitetech.ai/, the acquirer's marketing homepage, and IgniteTech's own software library does not list OneSpot as a current product; even the OneSpot page-tag host the Segment integration loads (d3xl0zyjyljwa.cloudfront.net) no longer resolves in DNS.
  evidence:
  - status: 302
    url: https://api.onespot.com/openapi.json
  - status: 302
    url: https://developer.onespot.com/
  - status: 302
    url: https://onespot.com/.well-known/agent-card.json
  - status: 200
    url: https://ignitetech.ai/wp-json/wp/v2/search?search=onespot
  reason: defunct
  state: none
created: '2026-07-17'
description: OneSpot was an Austin, Texas adtech and content-marketing startup that built a machine-learning platform to personalize and sequence branded content across websites, email, and paid media. Founded around 2010 and backed by early investors including 500 Startups, RSL Venture Partners, and Austin angels, it raised multiple venture rounds before being acquired. The onespot.com domain (and its developer, api, and app subdomains) now redirects to IgniteTech, and the company no longer operates an independent public developer API, documentation, or SDK surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/onespot.png
layout: provider
modified: '2026-08-12'
name: OneSpot
nav: Providers
network: true
overview: OneSpot is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AdTech, Content Marketing, Marketing Technology, and Personalization.
plans:
- name: Onespot Plans Pricing
  plan_count: 0
  slug: onespot-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Onespot Rate Limits
  slug: onespot-rate-limits
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/onespot/refs/heads/main/screenshots/onespot-2026-08-07T190349.png
security:
- kind: domain-security
  name: Onespot Domain Security
  slug: onespot-domain-security
  summary_line: TLSv1.2 · DMARC
slug: onespot
tags:
- Company
- AdTech
- Content Marketing
- Marketing Technology
- Personalization
- Advertising
- Machine-Learning
- Austin
website: https://onespot.com
---
