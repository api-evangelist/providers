---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 8.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Canopy API provides Amazon product data via REST, GraphQL, and MCP interfaces. Documentation is hosted at docs.canopyapi.co.
  name: Canopy API
  slug: canopy-api
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/canopyapi-co/authentication/canopyapi-co-authentication.yml
  title: ''
  type: Authentication
  url: authentication/canopyapi-co-authentication.yml
- group: agent
  href: https://artifacts.apis.io/canopyapi-co/llms/canopyapi-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/canopyapi-co-llms.txt
- group: agent
  href: https://artifacts.apis.io/canopyapi-co/well-known/canopyapi-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/canopyapi-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/canopyapi-co/hosts/canopyapi-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/canopyapi-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/canopyapi-co/vendors/canopyapi-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/canopyapi-co-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.canopyapi.co/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.canopyapi.co/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://www.canopyapi.co/signin
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/canopy-api
- group: company
  title: ''
  type: Blog
  url: https://www.canopyapi.co/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.canopyapi.co/
- group: auth
  href: https://artifacts.apis.io/canopyapi-co/security/canopyapi-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/canopyapi-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://canopyapi.co/
coverage:
  checked: '2026-10-30'
  detail: Docs site renders via Next.js and provides no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://docs.canopyapi.co/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: Canopy API provides developers with real-time Amazon product data, including pricing, reviews, and sales estimates, via REST, GraphQL, and MCP interfaces. The service offers a single API key to access comprehensive product information without the need for web scraping, supporting AI agents and applications. It targets developers building e‑commerce tools, price‑tracking services, and market analysis platforms, delivering up to 100 free requests for new users and scalable plans for higher volume.
image: https://www.canopyapi.co/api/og
layout: provider
modified: '2026-10-30'
name: canopyapi-co
nav: Providers
network: true
overview: 'canopyapi-co is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Amazon, Data, API, and E-commerce.


  canopyapi-co''s developer surface includes authentication, engineering blog, documentation, and 10 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 18.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Canopyapi Co Authentication
  slug: canopyapi-co-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Canopyapi Co Domain Security
  slug: canopyapi-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: canopyapi-co
tags:
- Company
- Amazon
- Data
- API
- E-commerce
- Pricing
website: https://canopyapi.co/
---
