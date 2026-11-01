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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Public API for Fizz social platform
  name: Fizz API
  slug: fizz-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Security
  url: https://fizz.social/legal/vulnerability-disclosure
- group: agent
  href: https://artifacts.apis.io/fizzsocial-app/llms/fizzsocial-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fizzsocial-app-llms.txt
- group: auth
  href: https://artifacts.apis.io/fizzsocial-app/well-known/fizzsocial-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/fizzsocial-app-security.txt
- group: agent
  href: https://artifacts.apis.io/fizzsocial-app/well-known/fizzsocial-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fizzsocial-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/fizzsocial-app/hosts/fizzsocial-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fizzsocial-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/fizzsocial-app/vendors/fizzsocial-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fizzsocial-app-vendors.yml
- group: auth
  href: https://artifacts.apis.io/fizzsocial-app/security/fizzsocial-app-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/fizzsocial-app-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/fizzsocial-app/security/fizzsocial-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fizzsocial-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fizz.social
- group: company
  title: ''
  type: Blog
  url: https://fizz.social/blog
- group: docs
  title: ''
  type: Documentation
  url: https://fizz.social
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fizz.social
- group: start
  title: ''
  type: GettingStarted
  url: https://fizz.social
- group: operate
  title: ''
  type: Support
  url: https://fizz.social/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fizz.social/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fizz.social/legal/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/fizzsocial/workspace
coverage:
  checked: '2026-10-26'
  detail: OpenAPI JSON endpoint returned HTTP 500, and no other machine-readable contract was found despite probing common spec locations.
  evidence:
  - status: 500
    url: https://fizz.social/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-25'
description: Fizz is a Gen Z focused social networking platform that connects college students across over 800 campuses. The app provides an authentic, unfiltered conversation space where verified .edu users can share posts, join communities, and engage with campus life. Fizz also offers advertising solutions for brands targeting the college demographic, with robust safety guidelines and legal policies to ensure a secure environment.
image: https://fizz.social/opengraph-image
layout: provider
modified: '2026-10-25'
name: Fizz
nav: Providers
network: true
overview: 'Fizz is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Social, GenZ, College, and Advertising.


  Fizz''s developer surface includes engineering blog, documentation, getting-started guide, support, and 13 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 20.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Fizzsocial App Domain Security
  slug: fizzsocial-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Fizzsocial App Vulnerability Disclosure
  slug: fizzsocial-app-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: fizzsocial-app
tags:
- Company
- Social
- GenZ
- College
- Advertising
website: https://fizz.social
---
