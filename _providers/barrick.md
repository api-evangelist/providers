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
  href: https://artifacts.apis.io/barrick/hosts/barrick-hosts.yml
  title: ''
  type: Hosts
  url: hosts/barrick-hosts.yml
- group: other
  href: https://artifacts.apis.io/barrick/vendors/barrick-vendors.yml
  title: ''
  type: Vendors
  url: vendors/barrick-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.barrick.com/
- group: auth
  href: https://artifacts.apis.io/barrick/security/barrick-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/barrick-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.barrick.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.barrick.com/English/careers/default.aspx
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.barrick.com/English/investors/default.aspx
- group: company
  title: ''
  type: Newsroom
  url: https://www.barrick.com/English/news/default.aspx
coverage:
  checked: '2026-11-02'
  detail: Barrick Mining is a mining corporation with no public developer API.
  evidence:
  - status: 200
    url: https://www.barrick.com
  reason: not-a-software-company
  state: none
created: '2026-11-02'
description: Barrick Mining Corporation is a leading global gold and copper mining company, operating mines and projects across the Americas, Africa, and the Middle East. The company focuses on sustainable mining practices, community development, and delivering value to shareholders. Its website provides extensive information on operations, governance, sustainability initiatives, investor relations, and career opportunities.
layout: provider
modified: '2026-11-02'
name: Barrick Mining
nav: Providers
network: true
overview: 'Barrick Mining is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mining, Gold, Resources, and Sustainability.


  Barrick Mining''s developer surface includes support and 7 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 45.5
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Barrick Domain Security
  slug: barrick-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: barrick
tags:
- Company
- Mining
- Gold
- Resources
- Sustainability
- Investor
website: https://www.barrick.com/
---
