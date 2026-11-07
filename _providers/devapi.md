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
api_count: 1
apis:
- description: Developer API portal for TIVIT services.
  name: TIVIT DevAPI
  slug: tivit-devapi
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/devapi/vendors/devapi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/devapi-vendors.yml
- group: other
  href: https://artifacts.apis.io/devapi/hosts/devapi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/devapi-hosts.yml
- group: company
  title: ''
  type: Blog
  url: https://tivit.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.devapi.com.br/
- group: auth
  href: https://artifacts.apis.io/devapi/security/devapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/devapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://devapi.com.br/
coverage:
  checked: '2026-10-20'
  detail: The developer portal at https://tivit.com/devapi/ loads content via JavaScript, preventing machine‑readable discovery of OpenAPI specifications.
  evidence:
  - status: 200
    url: https://tivit.com/devapi/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-20'
description: 'TIVIT is a company surfaced via the API Evangelist harvest backlog (source: g2-catalog) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-20'
name: TIVIT
nav: Providers
network: true
overview: 'TIVIT is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Integration Platform, API Management, iPaaS, Digital Transformation, and Workflow Automation.


  TIVIT''s developer surface includes engineering blog, documentation, and 4 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.2
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 44.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 5.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/devapi/devapi-2026-11-03T130559.png
security:
- kind: domain-security
  name: Devapi Domain Security
  slug: devapi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: devapi
tags:
- Integration Platform
- API Management
- iPaaS
- Digital Transformation
- Workflow Automation
website: https://devapi.com.br/
---
