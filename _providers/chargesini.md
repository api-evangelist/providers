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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/chargesini/llms/chargesini-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chargesini-llms.txt
- group: other
  href: https://artifacts.apis.io/chargesini/hosts/chargesini-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chargesini-hosts.yml
- group: other
  href: https://artifacts.apis.io/chargesini/vendors/chargesini-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chargesini-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.chargesini.com/news
- group: auth
  href: https://artifacts.apis.io/chargesini/security/chargesini-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chargesini-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.chargesini.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.chargesini.com/about-us/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.chargesini.com/for-business/
- group: operate
  title: ''
  type: Support
  url: https://www.chargesini.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.chargesini.com/news/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.chargesini.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chargesini.com/privacy-policy/
coverage:
  checked: '2026-10-27'
  detail: The website provides only marketing pages and no developer documentation or machine‑readable API specifications.
  evidence:
  - status: 200
    url: https://www.chargesini.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: ChargeSini is a Malaysian electric vehicle (EV) charging network operator that installs, operates, and bills public and private chargers across Malaysia. It offers a mobile app for locating, reserving, and paying for charging sessions, supports fast DC charging up to 120 kW, and provides solutions for condos, businesses, and malls. The company emphasizes sustainability, offers subscription plans, and partners with local businesses to expand EV infrastructure.
image: https://www.chargesini.com/assets/og-image.jpg?v=2
layout: provider
modified: '2026-10-27'
name: Chargesini
nav: Providers
network: true
overview: 'Chargesini is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, EVCharging, Malaysia, Sustainability, and MobileApp.


  Chargesini''s developer surface includes documentation, getting-started guide, support, engineering blog, and 8 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chargesini Domain Security
  slug: chargesini-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chargesini
tags:
- Company
- EVCharging
- Malaysia
- Sustainability
- MobileApp
website: https://www.chargesini.com/
---
