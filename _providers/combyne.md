---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Combyne provides a grain accounting and marketing platform for farmers and advisors.
  name: Combyne API
  slug: combyne-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/combyne/plans/combyne-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/combyne-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/combyne/hosts/combyne-hosts.yml
  title: ''
  type: Hosts
  url: hosts/combyne-hosts.yml
- group: other
  href: https://artifacts.apis.io/combyne/vendors/combyne-vendors.yml
  title: ''
  type: Vendors
  url: vendors/combyne-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://dev.combyne.ag/
- group: auth
  href: https://artifacts.apis.io/combyne/security/combyne-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/combyne-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://combyne.ag/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://welcome.combyne.ag/
- group: company
  title: ''
  type: Blog
  url: https://www.combyne.ag/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://welcome.combyne.ag/pricing/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/combyne
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.combyne.ag/hc/en-ca
coverage:
  checked: '2026-10-28'
  detail: The developer portal at https://welcome.combyne.ag/ renders content via JavaScript and provides no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://welcome.combyne.ag/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: Combyne is a complete grain accounting and marketing platform for farmers and their advisors. It simplifies tracking of sold positions, grain contracts, and brokerage trades while ensuring both parties work with unified, accurate data. This synergy allows for informed decisions, making crop marketing and risk management more efficient.
image: https://combyneprod.s3.amazonaws.com/static/image-preview-2x.png
layout: provider
modified: '2026-10-28'
name: Combyne
nav: Providers
network: true
overview: 'Combyne is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture, Grain, Farming, Software-as-a-Service, and AgTech.


  Combyne''s developer surface includes documentation, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Combyne Plans Pricing
  plan_count: 2
  slug: combyne-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Combyne Rate Limits
  slug: combyne-rate-limits
scopes:
- name: Combyne Scopes
  scope_count: 0
  slug: combyne-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.0
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 57.1
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 18.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/combyne/combyne-2026-11-03T124911.png
security:
- kind: authentication
  name: Combyne Authentication
  slug: combyne-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Combyne Domain Security
  slug: combyne-domain-security
  summary_line: TLSv1.3 · DMARC
slug: combyne
tags:
- Agriculture
- Grain
- Farming
- Software-as-a-Service
- AgTech
website: https://combyne.ag/
---
