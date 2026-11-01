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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/mozza/hosts/mozza-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mozza-hosts.yml
- group: other
  href: https://artifacts.apis.io/mozza/vendors/mozza-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mozza-vendors.yml
- group: auth
  href: https://artifacts.apis.io/mozza/security/mozza-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mozza-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mozzafoods.com
- group: operate
  title: ''
  type: Support
  url: https://www.mozzafoods.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mozzafoods.com/termsandconditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mozzafoods.com/privacy-policy
coverage:
  checked: '2026-10-29'
  detail: Mozza Foods provides a plant‑based protein product and does not expose a public API.
  evidence:
  - status: 404
    url: https://www.mozzafoods.com/openapi.json
  reason: not-a-software-company
  state: none
created: '2026-10-29'
description: Mozza Foods develops real dairy casein produced in soybean plants, offering a drop‑in ingredient for dairy manufacturers that replaces traditional cow‑derived protein. Founded in 2018 by software engineer Adam Tarshis, the company leverages two decades of engineering expertise to build a sustainable, plant‑based protein platform. Headquartered in Los Angeles, Mozza aims to transform the dairy supply chain by providing a scalable, plant‑grown casein that reduces reliance on livestock, lowers greenhouse‑gas emissions, and supports the growing demand for dairy‑free products. The technology uses existing global soybean farming infrastructure, enabling rapid scale‑up and integration into existing dairy manufacturing processes.
image: http://static1.squarespace.com/static/69c12a88e7de68600157c378/t/69d8eea25d7ce64472554cf5/1775824546095/MOZZA-SOCIALS_post3-5.png?format=1500w
layout: provider
modified: '2026-10-29'
name: Mozza
nav: Providers
network: true
overview: 'Mozza is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include FoodTech, Biotechnology, Sustainable Agriculture, Plant-Based Protein, and Dairy Alternative.


  Mozza''s developer surface includes support and 6 more developer resources.'
plans:
- name: Mozza Plans Pricing
  plan_count: 0
  slug: mozza-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Mozza Rate Limits
  slug: mozza-rate-limits
scopes:
- name: Mozza Scopes
  scope_count: 0
  slug: mozza-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Mozza Authentication
  slug: mozza-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Mozza Domain Security
  slug: mozza-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mozza
tags:
- FoodTech
- Biotechnology
- Sustainable Agriculture
- Plant-Based Protein
- Dairy Alternative
website: https://www.mozzafoods.com
---
