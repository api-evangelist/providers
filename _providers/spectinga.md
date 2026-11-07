---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/spectinga/hosts/spectinga-hosts.yml
  title: ''
  type: Hosts
  url: hosts/spectinga-hosts.yml
- group: other
  href: https://artifacts.apis.io/spectinga/vendors/spectinga-vendors.yml
  title: ''
  type: Vendors
  url: vendors/spectinga-vendors.yml
- group: auth
  href: https://artifacts.apis.io/spectinga/security/spectinga-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/spectinga-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://spectinga.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://spectinga.com/signup
- group: operate
  title: ''
  type: Support
  url: https://spectinga.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://spectinga.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spectinga
- group: operate
  title: ''
  type: Roadmap
  url: https://spectinga.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://spectinga.com/
- group: start
  title: ''
  type: SignUp
  url: https://spectinga.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://spectinga.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://spectinga.com/privacy-policy
coverage:
  checked: '2026-10-29'
  detail: Spectinga is a marketplace for buying and selling machinery and does not provide a public API.
  evidence:
  - status: 200
    url: https://spectinga.com/
  reason: not-a-software-company
  state: none
created: '2026-10-29'
description: Spectinga is an online marketplace for buying and selling agricultural and construction machinery. It offers dealer‑only prices, vetted trader access, inspection services, logistics handling, and dedicated support. Users can browse exclusive stock, make offers, and have machines delivered worldwide. The platform emphasizes transparent pricing, no hidden fees, and a secure transaction process.
image: https://spectinga.com/favicon.ico
layout: provider
modified: '2026-10-29'
name: Spectinga
nav: Providers
network: true
overview: 'Spectinga is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Marketplace, Agriculture, Construction, Machinery, and B2B.


  Spectinga''s developer surface includes getting-started guide, support, engineering blog, pricing, signup flow, and 8 more developer resources.'
random_paper: 22
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 18.7
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/spectinga/spectinga-2026-11-03T143618.png
security:
- kind: domain-security
  name: Spectinga Domain Security
  slug: spectinga-domain-security
  summary_line: TLSv1.3 · DMARC
slug: spectinga
tags:
- Marketplace
- Agriculture
- Construction
- Machinery
- B2B
website: https://spectinga.com/
---
