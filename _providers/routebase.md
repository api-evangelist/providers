---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.1
  scored_at: '2026-09-12'
api_count: 1
apis:
- description: ''
  name: Routebase API
  slug: routebase-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/routebase-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/routebase-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/routebase-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://routebase.dev
created: '2026-09-11'
description: API lifecycle platform covering Design (visual OpenAPI editor), Mock (spec-driven mock servers), Test (suites, assertions, OWASP security scanning), Document (published docs portals), and Agents (MCP server), built around a single living OpenAPI spec.
layout: provider
mcp_servers:
- description: ''
  name: Routebase MCP Server
  slug: routebase-mcp-server
modified: '2026-09-11'
name: Routebase
nav: Providers
network: true
overview: 'Routebase publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API lifecycle management, API design, OpenAPI, API documentation, and API testing.


  Routebase''s developer surface includes authentication and 3 more developer resources.'
plans:
- name: Routebase Plans Pricing
  plan_count: 4
  slug: routebase-plans-pricing
random_paper: 4
scopes:
- name: Routebase Scopes
  scope_count: 0
  slug: routebase-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.2
  coverage:
    artifact_dirs: 13
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 33.3
    developer_ergonomics: 21.4
    discoverability: 66.7
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  upsert:
    applies: true
    score: 27.8
security:
- kind: authentication
  name: Routebase Authentication
  slug: routebase-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Routebase Domain Security
  slug: routebase-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Routebase Vulnerability Disclosure
  slug: routebase-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: routebase
tags:
- API lifecycle management
- API design
- OpenAPI
- API documentation
- API testing
- API mocking
- API monitoring
- API security
- MCP
- AI agents
- developer tools
- CI/CD
- REST
- OAuth 2.1
- SCIM
- Streamable HTTP
website: https://routebase.dev
---
