---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
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
  scored_at: '2026-09-02'
api_count: 1
artifact_total: 6
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Carbon Direct API
  slug: open-carbon-direct
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carbon-direct-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/carbon-direct
- group: company
  title: ''
  type: Website
  url: https://www.carbon-direct.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.carbon-direct.com/platform
- group: commercial
  title: ''
  type: Plans
  url: plans/carbon-direct-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/carbon-direct-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/carbon-direct-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.carbon-direct.com/insights
- group: other
  title: ''
  type: Sustainability
  url: https://www.carbon-direct.com/company
- group: other
  title: ''
  type: Sustainability
  url: https://www.carbon-direct.com/insights/carbon-direct-acquires-pachama
- group: other
  title: ''
  type: Sustainability
  url: https://www.carbon-direct.com/solutions/report
created: '2026-06-20'
description: Carbon Direct is a science-first carbon management company that pairs an enterprise carbon management platform with a team of 70+ scientists. The platform helps organizations measure emissions, set science-based targets, reduce, and procure high-quality carbon dioxide removal (CDR), with monitoring, reporting, and verification (MRV) capabilities expanded through its 2025 acquisition of Pachama. Carbon Direct is an enterprise SaaS and advisory offering and does not publish a public developer API as of this profile.
finops:
- name: Carbon Direct Finops
  service_category: Carbon Management and Sustainability
  slug: carbon-direct-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/carbon-direct.png
layout: provider
modified: '2026-07-25'
name: Carbon Direct
nav: Providers
network: true
overview: 'Carbon Direct publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Carbon Management, Carbon Removal, CDR, MRV, and Climate.


  Carbon Direct''s developer surface includes documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Carbon Direct Plans Pricing
  plan_count: 1
  slug: carbon-direct-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Carbon Direct Rate Limits
  slug: carbon-direct-rate-limits
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 8
    catalog_gap: 77.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/carbon-direct/refs/heads/main/screenshots/carbon-direct-2026-06-20T173954.png
security:
- kind: domain-security
  name: Carbon Direct Domain Security
  slug: carbon-direct-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: carbon-direct
tags:
- Carbon Management
- Carbon Removal
- CDR
- MRV
- Climate
- Sustainability
website: https://www.carbon-direct.com
---
