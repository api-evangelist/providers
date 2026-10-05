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
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: GraphQL endpoint for Bluestonelane shop.
  name: Bluestonelane GraphQL API
  slug: bluestonelane-graphql-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bluestonelane/refs/heads/main/llms/bluestonelane-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bluestonelane-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bluestonelane/refs/heads/main/well-known/bluestonelane-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bluestonelane-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bluestonelane/refs/heads/main/hosts/bluestonelane-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bluestonelane-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bluestonelane/refs/heads/main/vendors/bluestonelane-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bluestonelane-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bluestonelane.com/policies/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bluestonelane.com/policies/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://bluestonelane.com/press/
- group: start
  title: ''
  type: Login
  url: https://shop.bluestonelane.com/account/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bluestonelane/refs/heads/main/security/bluestonelane-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bluestonelane-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bluestonelane.com
- group: company
  title: ''
  type: Blog
  url: https://bluestonelane.com/blog/
- group: company
  title: ''
  type: About
  url: https://bluestonelane.com/about/
- group: company
  title: ''
  type: Careers
  url: https://bluestonelane.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://bluestonelane.com/contact/
created: '2026-09-29'
description: Bluestone Lane is an Australian‑origin coffee brand operating cafés across the United States. It offers ethically‑sourced, meticulously‑roasted coffee beans, a subscription service, wholesale programs, and a loyalty app that rewards frequent customers. The company emphasizes sustainable packaging, community‑centric café experiences, and corporate coffee solutions for businesses. While it runs a robust retail e‑commerce site and provides corporate coffee services, it does not currently expose a public API for external developers. The brand focuses on quality, sustainability, and a distinctive Australian café culture brought to American neighborhoods.
image: https://bluestonelane.com/wp-content/uploads/2022/02/BL201218306777-1-scaled.jpg
layout: provider
modified: '2026-09-29'
name: Bluestonelane
nav: Providers
network: true
overview: 'Bluestonelane publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Coffee, Retail, Subscription, and Sustainability.


  Bluestonelane''s developer surface includes engineering blog and 13 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 15.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 82.1
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
  name: Bluestonelane Domain Security
  slug: bluestonelane-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bluestonelane
tags:
- Company
- Coffee
- Retail
- Subscription
- Sustainability
website: https://bluestonelane.com
---
