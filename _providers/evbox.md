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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/evbox/well-known/evbox-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/evbox-well-known.yml
- group: other
  href: https://artifacts.apis.io/evbox/hosts/evbox-hosts.yml
  title: ''
  type: Hosts
  url: hosts/evbox-hosts.yml
- group: build
  href: https://artifacts.apis.io/evbox/packages/evbox-packages.yml
  title: ''
  type: SDKs
  url: packages/evbox-packages.yml
- group: build
  href: https://artifacts.apis.io/evbox/packages/evbox-packages.yml
  title: ''
  type: Packages
  url: packages/evbox-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/evbox
- group: auth
  href: https://artifacts.apis.io/evbox/security/evbox-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/evbox-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://evbox.com/
- group: company
  title: ''
  type: Blog
  url: https://evbox.com/en/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://evbox.com/en/
- group: operate
  title: ''
  type: Support
  url: https://evbox.com/en/support/
- group: company
  title: ''
  type: Partners
  url: https://evbox.com/en/partners/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://evbox.com/en/privacy-policy/
- group: commercial
  title: ''
  type: LegalNotice
  url: https://evbox.com/en/legal-notice/
created: '2026-10-27'
description: EVBox provides smart electric vehicle (EV) charging solutions, including hardware chargers and cloud‑based software platforms for managing charging stations, energy usage, and fleet operations. The company serves businesses, municipalities, and consumers worldwide, offering scalable, interoperable charging infrastructure and services that integrate with renewable energy sources and grid management.
image: https://evbox.com/app/uploads/2025/07/cropped-logo.png
layout: provider
modified: '2026-10-27'
name: EVBox
nav: Providers
network: true
overview: 'EVBox is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, EV Charging, Hardware, Software, and Energy.


  EVBox''s developer surface includes engineering blog, documentation, support, and 10 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.3
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 48.2
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 12.4
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 11.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/evbox/evbox-2026-11-03T131647.png
security:
- kind: domain-security
  name: Evbox Domain Security
  slug: evbox-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: evbox
tags:
- Company
- EV Charging
- Hardware
- Software
- Energy
website: https://evbox.com/
---
