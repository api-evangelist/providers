---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/ceres-imaging/hosts/ceres-imaging-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ceres-imaging-hosts.yml
- group: other
  href: https://artifacts.apis.io/ceres-imaging/vendors/ceres-imaging-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ceres-imaging-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ceres.ai/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://support.ceresimaging.net/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ceres.ai/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://ceres.ai/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://ceres.ai/press
- group: company
  title: ''
  type: Blog
  url: https://ceres.ai/blog
- group: docs
  title: ''
  type: Documentation
  url: https://dev.ceresimaging.net/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ceresimaging
- group: auth
  href: https://artifacts.apis.io/ceres-imaging/security/ceres-imaging-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ceres-imaging-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ceresimaging.net
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://www.ceresimaging.net/mcp
  - status: 200
    url: https://www.ceresimaging.net
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: 'Ceres Imaging is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by lemnos-labs) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-22'
name: Ceres Imaging
nav: Providers
network: true
overview: 'Ceres Imaging is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Agribusiness, Sustainability, Insurance, Lending, and Farm Management.


  Ceres Imaging''s developer surface includes support, pricing, engineering blog, documentation, and 8 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.9
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 36.6
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 13.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 12.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ceres-imaging/ceres-imaging-2026-11-03T123725.png
security:
- kind: domain-security
  name: Ceres Imaging Domain Security
  slug: ceres-imaging-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ceres-imaging
tags:
- Agribusiness
- Sustainability
- Insurance
- Lending
- Farm Management
- Risk Management
website: https://www.ceresimaging.net
---
