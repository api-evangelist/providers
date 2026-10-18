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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/memmo/refs/heads/main/hosts/memmo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/memmo-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/memmo/refs/heads/main/vendors/memmo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/memmo-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/memmo/refs/heads/main/security/memmo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/memmo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://memmo.me/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://business.memmo.me/
- group: docs
  title: ''
  type: Documentation
  url: https://memmo.me/global/en/docs
- group: docs
  title: ''
  type: APIReference
  url: https://memmo.me/global/en/api
- group: start
  title: ''
  type: GettingStarted
  url: https://memmo.me/global/en/enroll
- group: operate
  title: ''
  type: Support
  url: https://memmo.me/global/en/faq
- group: company
  title: ''
  type: Blog
  url: https://memmo.me/global/en/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://memmo.me/global/en/pricing
- group: start
  title: ''
  type: SignUp
  url: https://memmo.me/global/en/enroll
- group: commercial
  title: ''
  type: TermsOfService
  url: https://memmo.me/global/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://memmo.me/global/en/privacy
coverage:
  checked: '2026-10-15'
  detail: No public developer documentation or API contract was found for memmo.
  evidence:
  - status: 200
    url: https://memmo.me/
  reason: no-developer-program
  state: none
created: '2026-10-15'
description: Memmo is a platform that enables users to request personalized video messages from celebrities, athletes, and influencers. It offers a marketplace where talent can record custom greetings, birthday wishes, and promotional content, with secure payment processing, fast delivery, and a global audience. The service caters to both individual consumers and businesses seeking unique marketing or engagement tools.
image: https://memmo.me/_next/static/images/og-share-default-2dd195c8fdda8a6509171c86cd8767f5.jpg
layout: provider
modified: '2026-10-15'
name: memmo
nav: Providers
network: true
overview: 'memmo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Video, Marketplace, Celebrities, and Personalized.


  memmo''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 7 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 22.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 48.2
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
  name: Memmo Domain Security
  slug: memmo-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: memmo
tags:
- Company
- Video
- Marketplace
- Celebrities
- Personalized
website: https://memmo.me/
---
