---
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/arrive/refs/heads/main/llms/arrive-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arrive-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/arrive/refs/heads/main/well-known/arrive-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arrive-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arrive/refs/heads/main/hosts/arrive-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arrive-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arrive/refs/heads/main/vendors/arrive-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arrive-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://arrive.com/en/newsroom
- group: company
  title: ''
  type: Blog
  url: https://arrive.com/en/newsroom/blog/white-paper
- group: docs
  title: ''
  type: Documentation
  url: https://developer.arrive.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arrive/refs/heads/main/security/arrive-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arrive-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arrive.com
- group: operate
  title: ''
  type: Support
  url: https://arrive.com/en/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arrive.com/en/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arrive.com/en/privacy-policy
coverage:
  checked: '2026-09-26'
  detail: Access to the developer documentation requires a login, preventing retrieval of the OpenAPI spec.
  evidence:
  - status: 200
    url: https://developer.arrive.com/openapi.json
  reason: sales-gate
  state: gated
created: '2026-09-26'
description: Arrive provides smart mobility solutions for cities, helping operators, decision‑makers and businesses improve urban transportation through smarter parking, public transit integration, and fleet management. Their platform enables cities to reduce congestion, enhance user experience, and optimize mobility services, delivering data‑driven insights and seamless payment experiences across parking operators and transport providers.
image: https://a.storyblok.com/f/333594/4500x3000/2568baf1c1/22-square_05-article.png/m/1200x630/filters:quality(75)
layout: provider
modified: '2026-09-26'
name: Arrive
nav: Providers
network: true
overview: 'Arrive is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Mobility, Smart Cities, Parking, Transportation, and Software-as-a-Service.


  Arrive''s developer surface includes engineering blog, documentation, support, and 9 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 13.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Arrive Domain Security
  slug: arrive-domain-security
  summary_line: TLSv1.3 · DMARC
slug: arrive
tags:
- Mobility
- Smart Cities
- Parking
- Transportation
- Software-as-a-Service
- Company
website: https://arrive.com
---
