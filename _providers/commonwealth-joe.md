---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
  score: 4.5
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/commonwealth-joe/refs/heads/main/llms/commonwealth-joe-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/commonwealth-joe-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/commonwealth-joe/refs/heads/main/well-known/commonwealth-joe-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/commonwealth-joe-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/commonwealth-joe/refs/heads/main/hosts/commonwealth-joe-hosts.yml
  title: ''
  type: Hosts
  url: hosts/commonwealth-joe-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/commonwealth-joe/refs/heads/main/vendors/commonwealth-joe-vendors.yml
  title: ''
  type: Vendors
  url: vendors/commonwealth-joe-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://commonwealthjoe.com/pages/press
- group: start
  title: ''
  type: Login
  url: https://commonwealthjoe.com/account/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/commonwealth-joe/refs/heads/main/security/commonwealth-joe-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/commonwealth-joe-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://commonwealthjoe.com
- group: company
  title: ''
  type: About
  url: https://commonwealthjoe.com/pages/about
- group: company
  title: ''
  type: Blog
  url: https://commonwealthjoe.com/blogs/blog
- group: operate
  title: ''
  type: Contact
  url: https://commonwealthjoe.com/pages/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://commonwealthjoe.com/pages/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://commonwealthjoe.com/pages/terms-conditions
coverage:
  checked: '2026-10-09'
  detail: Commonwealth Joe provides no public developer program or API documentation.
  evidence:
  - status: 200
    url: https://commonwealthjoe.com/api/graphql
  reason: no-developer-program
  state: none
created: '2026-10-09'
description: Commonwealth Joe Coffee Roasters is a specialty coffee company based in Washington, D.C., offering freshly roasted beans, cold brew, and coffee‑as‑a‑service for offices and retail customers. They operate retail cafés, an online shop, and wholesale programs, emphasizing sustainability and community values. Their website provides product catalogs, subscription options, a blog, and corporate information, but no public API documentation is currently available.
image: http://commonwealthjoe.com/cdn/shop/files/Image_11-4-25_at_7.35_PM_1200x1200.jpg?v=1762303040
layout: provider
modified: '2026-10-09'
name: Commonwealth Joe
nav: Providers
network: true
overview: 'Commonwealth Joe is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Coffee, Retail, Subscription, and Wholesale.


  Commonwealth Joe''s developer surface includes engineering blog and 12 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Commonwealth Joe Domain Security
  slug: commonwealth-joe-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: commonwealth-joe
tags:
- Company
- Coffee
- Retail
- Subscription
- Wholesale
- WashingtonDC
website: https://commonwealthjoe.com
---
