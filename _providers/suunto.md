---
agent_readiness:
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.4
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: GraphQL API providing access to Suunto data and services.
  name: Suunto GraphQL API
  slug: suunto-graphql-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Security
  url: https://www.suunto.com/Privacy-Policy/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/suunto/refs/heads/main/llms/suunto-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/suunto-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/suunto/refs/heads/main/well-known/suunto-suunto-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/suunto-suunto-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/suunto/refs/heads/main/well-known/suunto-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/suunto-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/suunto/refs/heads/main/well-known/suunto-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/suunto-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/suunto/refs/heads/main/hosts/suunto-hosts.yml
  title: ''
  type: Hosts
  url: hosts/suunto-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/suunto/refs/heads/main/vendors/suunto-vendors.yml
  title: ''
  type: Vendors
  url: vendors/suunto-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.suunto.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/suunto/refs/heads/main/security/suunto-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/suunto-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/suunto/refs/heads/main/security/suunto-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/suunto-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.suunto.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.suunto.com/Support/User-guides/
- group: operate
  title: ''
  type: Support
  url: https://www.suunto.com/Support/Suunto-Webshop/
- group: company
  title: ''
  type: Blog
  url: https://www.suunto.com/News/?category=news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.suunto.com/Terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.suunto.com/Privacy-Policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.suunto.com/Products/sports-watches/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.suunto.com/Support/User-guides/
- group: start
  title: ''
  type: SignUp
  url: https://www.suunto.com/Redirects/For-navigation/Contact-information/
coverage:
  checked: '2026-10-14'
  detail: GraphQL endpoint returned a schema unrelated to Suunto, preventing verification of ownership.
  evidence:
  - status: 200
    url: https://tactical.suunto.com/api/graphql
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-14'
description: Suunto is a Finnish company that designs and manufactures sports watches, dive computers, compasses and accessories for outdoor enthusiasts. Founded in 1936, Suunto combines precision engineering with modern technology to provide reliable tools for athletes, adventurers and professionals. Their product range includes GPS-enabled watches, dive computers, heart rate monitors, and navigation instruments, all built to withstand harsh environments and support performance tracking.
layout: provider
modified: '2026-10-14'
name: Suunto
nav: Providers
network: true
overview: 'Suunto is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sports, Wearables, Outdoor, and Navigation.


  Suunto''s developer surface includes documentation, support, engineering blog, pricing, getting-started guide, signup flow, and 13 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 32.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 29.8
    developer_ergonomics: 28.6
    discoverability: 60.7
    operational_transparency: 26.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Suunto Domain Security
  slug: suunto-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Suunto Vulnerability Disclosure
  slug: suunto-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: suunto
tags:
- Company
- Sports
- Wearables
- Outdoor
- Navigation
website: https://www.suunto.com
---
