---
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/traxcn-com/plans/traxcn-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/traxcn-com-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/traxcn-com/hosts/traxcn-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/traxcn-com-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tracxn.com/privacypolicy
- group: commercial
  title: ''
  type: Pricing
  url: https://tracxn.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://tracxn.com/p/media
- group: start
  title: ''
  type: Login
  url: https://tracxn.com/login
- group: auth
  href: https://artifacts.apis.io/traxcn-com/security/traxcn-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/traxcn-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.traxcn.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: http://www.traxcn.com
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Tracxn provides technology and data intelligence for venture capitalists, private equity firms, investment banks, and corporations, helping them track innovative companies and emerging sectors worldwide. Their platform aggregates comprehensive company information, market trends, and analytics to support investment decisions and corporate development strategies.
image: https://cdn.tracxn.com/images/static/social/homepage.webp
layout: provider
modified: '2026-10-21'
name: Tracxn
nav: Providers
network: true
overview: 'Tracxn is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Intelligence, Venture-Capital, and Analytics.


  Tracxn''s developer surface includes pricing and 7 more developer resources.'
plans:
- name: Traxcn Com Plans Pricing
  plan_count: 6
  slug: traxcn-com-plans-pricing
random_paper: 12
score:
  band: emerging
  composite: 18.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Traxcn Com Domain Security
  slug: traxcn-com-domain-security
  summary_line: TLSv1.3
slug: traxcn-com
tags:
- Company
- Data
- Intelligence
- Venture-Capital
- Analytics
website: http://www.traxcn.com
---
