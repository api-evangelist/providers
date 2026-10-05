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
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/angel-studios/refs/heads/main/well-known/angel-studios-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/angel-studios-clarity-security.txt
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/angel-studios/refs/heads/main/llms/angel-studios-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/angel-studios-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/angel-studios/refs/heads/main/well-known/angel-studios-ir-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/angel-studios-ir-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/angel-studios/refs/heads/main/well-known/angel-studios-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/angel-studios-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/angel-studios/refs/heads/main/hosts/angel-studios-hosts.yml
  title: ''
  type: Hosts
  url: hosts/angel-studios-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/angel-studios/refs/heads/main/vendors/angel-studios-vendors.yml
  title: ''
  type: Vendors
  url: vendors/angel-studios-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.angel.com/legal/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://support.angel.com/hc
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.angel.com/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.angel.com/guild/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.angel.com/press
- group: start
  title: ''
  type: Login
  url: https://www.angel.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.angel.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/angel-studios/refs/heads/main/security/angel-studios-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/angel-studios-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/angel-studios/refs/heads/main/security/angel-studios-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/angel-studios-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.angel.com/
created: '2026-09-24'
description: Angel Studios operates a streaming platform that offers uplifting movies and TV shows for families and individuals seeking inspirational content. The service combines a subscription-based model with a community-driven guild where members can support filmmakers, vote on projects, and access exclusive content. Angel Studios emphasizes purpose-driven storytelling, providing a diverse library across genres such as drama, comedy, documentary, and faith-based programming, while also offering theatrical releases and a marketplace for merchandise.
image: https://images.angelstudios.com/image/upload/c_fill,f_auto,h_630,q_auto,w_1200/v1778524911/angel-studios/seo/angel-opengraph.png
layout: provider
modified: '2026-09-24'
name: Angel Studios
nav: Providers
network: true
overview: 'Angel Studios is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Streaming, Media, Community, and Faith.


  Angel Studios'' developer surface includes support, pricing, engineering blog, and 14 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 18.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    mcp: unknown
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
  name: Angel Studios Domain Security
  slug: angel-studios-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Angel Studios Vulnerability Disclosure
  slug: angel-studios-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: angel-studios
tags:
- Company
- Streaming
- Media
- Community
- Faith
website: https://www.angel.com/
---
