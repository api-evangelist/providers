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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/craftsvilla-domain-security.yml
created: '2026-07-17'
description: 'Craftsvilla was an India-based online marketplace for ethnic and handcrafted products — sarees, ethnic apparel, jewelry, footwear, accessories, beauty and home decor sourced from artisans, weavers and small sellers across India. Founded in 2011 and headquartered in Mumbai, it was backed by Lightspeed Venture Partners, Sequoia Capital, Nexus Venture Partners and Global Founders Capital before winding down its consumer operations around 2019 amid financial difficulties. It was surfaced as a Lightspeed portfolio company and added to the API Evangelist network as a stub for enrichment. Enrichment found no live public developer surface: the storefront domain now serves a broken AWS S3 redirect (www.craftsvilla.com is NXDOMAIN) and there is no API, developer portal, documentation, /.well-known/ discovery, or llms.txt to harvest.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/craftsvilla.png
layout: provider
modified: '2026-07-18'
name: Craftsvilla
nav: Providers
network: true
overview: Craftsvilla is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Marketplace, Retail, and Fashion.
random_paper: 3
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 1
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
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 5.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
security:
- kind: domain-security
  name: Craftsvilla Domain Security
  slug: craftsvilla-domain-security
  summary_line: no transport/DNS hardening detected
slug: craftsvilla
tags:
- Company
- E-Commerce
- Marketplace
- Retail
- Fashion
- Ethnic Wear
- Handcrafted
- India
---
