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
- group: other
  href: https://artifacts.apis.io/dispatch-bio/hosts/dispatch-bio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dispatch-bio-hosts.yml
- group: other
  href: https://artifacts.apis.io/dispatch-bio/vendors/dispatch-bio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dispatch-bio-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dispatch-bio/security/dispatch-bio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dispatch-bio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dispatchbio.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dispatchbio.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://dispatchbio.com/contact-us/
- group: other
  title: ''
  type: ExpandedAccessPolicy
  url: https://dispatchbio.com/EAP/
- group: docs
  title: ''
  type: Documentation
  url: https://dispatchbio.com/science/
- group: docs
  title: ''
  type: APIReference
  url: https://dispatchbio.com/pipeline/
- group: company
  title: ''
  type: Blog
  url: https://dispatchbio.com/news/
coverage:
  checked: '2026-10-23'
  detail: The provider's documentation pages are rendered via JavaScript, preventing machine‑readable contract discovery.
  evidence:
  - status: 200
    url: https://dispatchbio.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-23'
description: Dispatch Bio is a biotech company focused on engineering a groundbreaking immunotherapy platform, Flare, to treat solid tumors. Founded in 2022 as a Penn spin‑out, the firm aims to overcome targeting and resistance challenges in cancer treatment, advancing its pipeline through pre‑clinical and early clinical studies. The company is backed by investors including Bristol Myers Squibb and seeks to create universal cancer therapies.
layout: provider
modified: '2026-10-23'
name: Dispatch Bio
nav: Providers
network: true
overview: 'Dispatch Bio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Immunotherapy, Cancer, Platform, and Startups.


  Dispatch Bio''s developer surface includes support, documentation, API reference, engineering blog, and 6 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 6.8
  coverage:
    artifact_dirs: 12
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.7
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/dispatch-bio/dispatch-bio-2026-11-03T130757.png
security:
- kind: domain-security
  name: Dispatch Bio Domain Security
  slug: dispatch-bio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dispatch-bio
tags:
- Biotechnology
- Immunotherapy
- Cancer
- Platform
- Startups
website: https://dispatchbio.com
---
