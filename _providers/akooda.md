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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/akooda/well-known/akooda-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/akooda-well-known.yml
- group: other
  href: https://artifacts.apis.io/akooda/vendors/akooda-vendors.yml
  title: ''
  type: Vendors
  url: vendors/akooda-vendors.yml
- group: other
  href: https://artifacts.apis.io/akooda/hosts/akooda-hosts.yml
  title: ''
  type: Hosts
  url: hosts/akooda-hosts.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developer.tulip.co/
- group: company
  title: ''
  type: Website
  url: https://www.akooda.co/
- group: auth
  href: https://artifacts.apis.io/akooda/security/akooda-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/akooda-domain-security.yml
coverage:
  checked: '2026-10-24'
  detail: The website redirects to Tulip AI with no developer documentation or API references.
  evidence:
  - status: 200
    url: https://akooda.co
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Akooda provides a platform that enables businesses to integrate and manage their digital services through a unified API ecosystem. Founded by a collective of experienced entrepreneurs, the company focuses on delivering scalable, secure, and developer-friendly solutions for various industries. Their offerings include API management, analytics, and support tools designed to accelerate product development and improve operational efficiency. Akooda aims to empower organizations to innovate faster while maintaining high standards of security and compliance.
layout: provider
modified: '2026-10-24'
name: Akooda
nav: Providers
network: true
overview: 'Akooda is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include API Management, Integration, Platform, Security, and Analytics.


  Akooda''s developer surface includes documentation and 5 more developer resources.'
random_paper: 23
score:
  band: minimal
  composite: 5.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 44.6
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 6.3
  provenance:
    mcp: unknown
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
screenshot: https://apis.io/screenshots/akooda/akooda-2026-11-03T120558.png
security:
- kind: domain-security
  name: Akooda Domain Security
  slug: akooda-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: akooda
tags:
- API Management
- Integration
- Platform
- Security
- Analytics
website: https://www.akooda.co/
---
