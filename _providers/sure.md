---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: REST APIs for the full embedded insurance lifecycle including quoting, rating, binding, policy management, claims intake through settlement, premium payments (card, ACH, bank rail, escrow), and compli
  name: Sure Platform API
  slug: sure-platform-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sure-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sureapp.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.sureapp.com/solutions/platform/apis
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/sureapp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sure-insurance
- group: company
  title: ''
  type: Blog
  url: https://www.sureapp.com/resources/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sureapp.com/contact
- group: operate
  title: ''
  type: StatusPage
  url: https://www.sureapp.com/solutions/platform/apis
- group: other
  title: ''
  type: X
  url: https://x.com/surehq
- group: commercial
  title: ''
  type: Plans
  url: plans/sure-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sure-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sure-finops.yml
created: '2026-06-13'
description: Sure is an embedded insurance platform providing purpose-built REST APIs for distributing insurance products through digital channels. The platform enables brands, carriers, MGAs, and marketplaces to build, launch, and scale digital insurance programs covering quoting, binding, policy management, claims processing, payments, and compliance workflows across all 50 US states.
finops:
- name: Sure Finops
  service_category: ''
  slug: sure-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sure.png
layout: provider
modified: '2026-06-13'
name: Sure
nav: Providers
network: true
overview: 'Sure publishes 1 API on the [APIs.io](https://apis.io/) network: Platform API. Tagged areas include Insurance, Embedded Insurance, Insurtech, Policy Management, and Claims.


  Sure''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Sure Plans Pricing
  plan_count: 2
  slug: sure-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Sure Rate Limits
  slug: sure-rate-limits
score:
  band: emerging
  composite: 23.8
  coverage:
    artifact_dirs: 7
    catalog_gap: 67.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 26.7
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 23.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sure/refs/heads/main/screenshots/sure-2026-06-20T194803.png
security:
- kind: domain-security
  name: Sure Domain Security
  slug: sure-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sure
tags:
- Insurance
- Embedded Insurance
- Insurtech
- Policy Management
- Claims
- Payments
- Compliance
website: https://www.sureapp.com
---
