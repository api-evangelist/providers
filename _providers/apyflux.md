---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: bearer
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: GraphQL API for accessing Apyflux marketplace data.
  name: Apyflux GraphQL API
  slug: apyflux-graphql-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/apyflux/conventions/apyflux-conventions.yml
  title: ''
  type: Conventions
  url: conventions/apyflux-conventions.yml
- group: auth
  href: https://artifacts.apis.io/apyflux/authentication/apyflux-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apyflux-authentication.yml
- group: other
  href: https://artifacts.apis.io/apyflux/hosts/apyflux-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apyflux-hosts.yml
- group: auth
  href: https://artifacts.apis.io/apyflux/security/apyflux-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apyflux-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.apyflux.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.apyflux.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.apyflux.com/docs/getting-started/how-to-publish-api-on-apyflux
- group: operate
  title: ''
  type: Support
  url: https://www.apyflux.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apyflux.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.apyflux.com/privacy
created: '2026-10-19'
description: Apyflux is an API marketplace that connects API providers with developers, offering a curated catalog of APIs across various industries. The platform enables seamless API publishing, discovery, and monetization, providing tools for documentation, analytics, and billing. It aims to simplify integration for businesses and empower developers to find and use high‑quality APIs efficiently.
image: https://storageapyfluxprod.blob.core.windows.net/staticmaterial/apyflux_logo.webp
layout: provider
modified: '2026-10-19'
name: Apyflux
nav: Providers
network: true
overview: 'Apyflux is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Marketplace, Developer Tools, Integration, Monetization, and Software-as-a-Service.


  Apyflux''s developer surface includes authentication, getting-started guide, support, and 7 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 13.8
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.3
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 25.0
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 19.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/apyflux/apyflux-2026-11-03T121048.png
security:
- kind: authentication
  name: Apyflux Authentication
  slug: apyflux-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Apyflux Domain Security
  slug: apyflux-domain-security
  summary_line: TLSv1.3 · DMARC
slug: apyflux
tags:
- API Marketplace
- Developer Tools
- Integration
- Monetization
- Software-as-a-Service
website: https://www.apyflux.com/
---
