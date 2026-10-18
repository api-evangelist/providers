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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.7
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API for managing EV charging schedules, retrieving vehicle status, creating charging plans, and accessing billing information.
  name: Jedlix API
  slug: jedlix-api
artifact_total: 4
asyncapis:
- description: ''
  name: Jedlix Webhooks
  slug: jedlix-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/jedlix/refs/heads/main/vendors/jedlix-vendors.yml
  title: ''
  type: Vendors
  url: vendors/jedlix-vendors.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jedlix/refs/heads/main/asyncapi/jedlix-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/jedlix-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jedlix/refs/heads/main/conventions/jedlix-conventions.yml
  title: ''
  type: Conventions
  url: conventions/jedlix-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/jedlix/refs/heads/main/sandbox/jedlix-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/jedlix-sandbox.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/jedlix/refs/heads/main/authentication/jedlix-authentication.yml
  title: ''
  type: Authentication
  url: authentication/jedlix-authentication.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/jedlix/refs/heads/main/lifecycle/jedlix-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/jedlix-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jedlix/refs/heads/main/lifecycle/jedlix-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/jedlix-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/jedlix/refs/heads/main/errors/jedlix-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/jedlix-problem-types.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/jedlix/refs/heads/main/hosts/jedlix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jedlix-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/jedlix/refs/heads/main/packages/jedlix-packages.yml
  title: ''
  type: SDKs
  url: packages/jedlix-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/jedlix/refs/heads/main/packages/jedlix-packages.yml
  title: ''
  type: Packages
  url: packages/jedlix-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.jedlix.com/docs/quickstart-guide
- group: docs
  title: ''
  type: Documentation
  url: https://developer.jedlix.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jedlix
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/jedlix/refs/heads/main/security/jedlix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jedlix-domain-security.yml
coverage:
  checked: '2026-10-14'
  detail: Documentation is provided as markdown pages without a machine‑readable OpenAPI, GraphQL, AsyncAPI, gRPC or WSDL contract.
  evidence:
  - status: 200
    url: https://developer.jedlix.com/docs/api-key.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: Jedlix is a fintech company that provides a platform for electric vehicle (EV) owners to manage charging schedules, integrate with energy providers, and optimize costs. The service offers APIs for retrieving vehicle charging status, creating charging plans, and accessing billing information, enabling developers to build applications that help users reduce energy consumption and take advantage of dynamic electricity pricing. Jedlix aims to simplify EV charging through smart automation and data-driven insights, supporting both individual consumers and fleet operators.
layout: provider
modified: '2026-10-14'
name: Jedlix
nav: Providers
network: true
overview: 'Jedlix is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Electric Vehicles, Charging, and Energy.


  The Jedlix catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Jedlix''s developer surface includes sandbox, authentication, getting-started guide, documentation, and 11 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 27.8
  coverage:
    artifact_dirs: 12
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 47.6
    discoverability: 62.5
    operational_transparency: 21.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Jedlix Authentication
  slug: jedlix-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Jedlix Domain Security
  slug: jedlix-domain-security
  summary_line: DNSSEC · DMARC
slug: jedlix
tags:
- Company
- Fintech
- Electric Vehicles
- Charging
- Energy
---
