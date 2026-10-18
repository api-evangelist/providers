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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/made-in-cookware/refs/heads/main/llms/made-in-cookware-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/made-in-cookware-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/made-in-cookware/refs/heads/main/well-known/made-in-cookware-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/made-in-cookware-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/made-in-cookware/refs/heads/main/hosts/made-in-cookware-hosts.yml
  title: ''
  type: Hosts
  url: hosts/made-in-cookware-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/made-in-cookware/refs/heads/main/vendors/made-in-cookware-vendors.yml
  title: ''
  type: Vendors
  url: vendors/made-in-cookware-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.madeincookware.com/privacy-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/made-in-cookware/refs/heads/main/security/made-in-cookware-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/made-in-cookware-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://madeincookware.com
- group: docs
  title: ''
  type: Documentation
  url: https://madeincookware.com/pages/our-story
- group: company
  title: ''
  type: About
  url: https://madeincookware.com/pages/our-story
- group: operate
  title: ''
  type: Contact
  url: https://madeincookware.com/pages/contact-us
- group: company
  title: ''
  type: Blog
  url: https://madeincookware.com/blogs
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://privacy.madeincookware.com/mcp
  - status: 200
    url: https://madeincookware.com
  reason: no-developer-program
  state: none
created: '2026-10-12'
description: Made In Cookware designs and sells professional-quality cookware, non-stick, carbon steel, and knives. The company offers a range of kitchen sets, individual pieces, and accessories, focusing on durability and performance. Their products are sold directly to consumers through their online store and are marketed as premium kitchen tools for home chefs.
image: https://cdn.sanity.io/images/fr9flhkd/main/506a210bae8bd9cc71256ee37d0aca092540b1c4-1920x1080.jpg?fit=crop&h=630&q=75&w=1200
layout: provider
modified: '2026-10-12'
name: Made In Cookware
nav: Providers
network: true
overview: 'Made In Cookware is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Cookware, E-Commerce, Direct to Consumer, Kitchenware, and Premium.


  Made In Cookware''s developer surface includes documentation, engineering blog, and 9 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Made In Cookware Domain Security
  slug: made-in-cookware-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: made-in-cookware
tags:
- Cookware
- E-Commerce
- Direct to Consumer
- Kitchenware
- Premium
website: https://madeincookware.com
---
