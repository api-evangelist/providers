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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/dimhour-com/llms/dimhour-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dimhour-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dimhour-com/well-known/dimhour-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dimhour-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dimhour-com/hosts/dimhour-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dimhour-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dimhour-com/vendors/dimhour-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dimhour-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dimhour-com/security/dimhour-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dimhour-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dimhour.com/
- group: operate
  title: ''
  type: Support
  url: https://dimhour.com/support.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dimhour.com/privacy.html
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://dimhour.com/
  reason: no-developer-program
  state: none
created: '2026-11-05'
description: Dim Hour is a city guide with a point of view — places to eat and drink, plus hotels, museums and landmarks across 26 cities, chosen rather than crowdsourced. The catalog is built with curated selections, data verification, and a deliberate editorial stance, offering travelers trusted recommendations for each location.
image: https://dimhour.com/icons/og-card.png
layout: provider
modified: '2026-11-05'
name: Dim Hour
nav: Providers
network: true
overview: 'Dim Hour is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, City Guide, Travel, Recommendations, and Editorial.


  Dim Hour''s developer surface includes support and 7 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 8.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dimhour Com Domain Security
  slug: dimhour-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dimhour-com
tags:
- Company
- City Guide
- Travel
- Recommendations
- Editorial
website: https://dimhour.com/
---
