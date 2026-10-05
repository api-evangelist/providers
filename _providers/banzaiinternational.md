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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/banzaiinternational/refs/heads/main/hosts/banzaiinternational-hosts.yml
  title: ''
  type: Hosts
  url: hosts/banzaiinternational-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/banzaiinternational/refs/heads/main/vendors/banzaiinternational-vendors.yml
  title: ''
  type: Vendors
  url: vendors/banzaiinternational-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.banzai.io/newsroom
- group: start
  title: ''
  type: Login
  url: https://www.banzai.io/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/banzaiinternational/refs/heads/main/security/banzaiinternational-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/banzaiinternational-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.banzai.io
- group: company
  title: ''
  type: Blog
  url: https://www.banzai.io/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.banzai.io/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.banzai.io/legal/privacy-policy
- group: docs
  title: ''
  type: Documentation
  url: https://www.banzai.io/blog
- group: operate
  title: ''
  type: Support
  url: https://www.banzai.io/contact
coverage:
  checked: '2026-09-27'
  detail: Developer pages return 404 and the site is built on Webflow with no public API documentation.
  evidence:
  - status: 404
    url: https://www.banzai.io/developers
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: Banzaiinternational, operating as Banzai, provides data‑driven demand generation solutions through a platform that includes webinar hosting, video creation, and audience engagement tools. The company helps marketers boost event registrations, generate leads, and measure ROI with products like Demio, OpenReel, and its own Banzai suite. It serves B2B customers seeking to improve pipeline conversion and customer engagement across digital channels.
image: https://cdn.prod.website-files.com/61967dbb50eec57a4e7fde97/66463303e4783a19ea8cb2e2_Banzai_OG.jpg
layout: provider
modified: '2026-09-27'
name: Banzaiinternational
nav: Providers
network: true
overview: 'Banzaiinternational is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Demand Generation, Webinar, and Video-Content.


  Banzaiinternational''s developer surface includes engineering blog, documentation, support, and 8 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 14.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
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
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Banzaiinternational Domain Security
  slug: banzaiinternational-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: banzaiinternational
tags:
- Company
- Marketing
- Demand Generation
- Webinar
- Video-Content
website: https://www.banzai.io
---
