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
- description: Search and book flights from any AI agent. One URL. Real prices. Human backup.
  name: RunRelay Flights API
  slug: runrelay-flights-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/runrelay-io/plans/runrelay-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/runrelay-io-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/runrelay-io/authentication/runrelay-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/runrelay-io-authentication.yml
- group: other
  href: https://artifacts.apis.io/runrelay-io/hosts/runrelay-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/runrelay-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/runrelay-io/vendors/runrelay-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/runrelay-io-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.runrelay.io/blog
- group: auth
  href: https://artifacts.apis.io/runrelay-io/security/runrelay-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/runrelay-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://runrelay.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.runrelay.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.runrelay.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.runrelay.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.runrelay.io/#quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.runrelay.io/#pricing
- group: operate
  title: ''
  type: Support
  url: mailto:info@runrelay.io
coverage:
  checked: '2026-10-31'
  detail: Documentation is public but no machine-readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://docs.runrelay.io/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: RunRelay provides a real-time travel execution platform that enables banks, fintechs, and AI agents to search, book, and manage flights, hotels, payments, and logistics through a single API. The service combines automated booking with human concierge support 24/7, offering white-label solutions that can be integrated quickly into banking and platform products. RunRelay’s API delivers live pricing, reservation management, and ancillary services such as eSIM travel, insurance, and lounge access, all backed by a human fallback for complex edge cases. The platform is built for high-volume, enterprise-grade integrations and supports compliance and security standards required by financial institutions.
image: https://www.runrelay.io/favicon.svg
layout: provider
modified: '2026-10-31'
name: runrelay-io
nav: Providers
network: true
overview: 'runrelay-io is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Fintech, API, and Concierge.


  runrelay-io''s developer surface includes authentication, engineering blog, documentation, API reference, getting-started guide, pricing, support, and 6 more developer resources.'
plans:
- name: Runrelay Io Plans Pricing
  plan_count: 4
  slug: runrelay-io-plans-pricing
random_paper: 15
score:
  band: emerging
  composite: 23.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.2
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 38.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 57.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 9.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Runrelay Io Authentication
  slug: runrelay-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Runrelay Io Domain Security
  slug: runrelay-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: runrelay-io
tags:
- Company
- Travel
- Fintech
- API
- Concierge
- Banking
website: https://runrelay.io/
---
