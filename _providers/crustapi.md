---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.5
  scored_at: '2026-09-12'
api_count: 1
apis:
- description: REST API for structured Google and public LinkedIn data, key-authenticated, with a published OpenAPI spec and an x402 agent-payment endpoint. Includes bulk/batch LinkedIn processing with webhook deliv
  name: CrustAPI
  slug: crustapi
artifact_total: 8
asyncapis:
- description: ''
  name: Crustapi Webhooks
  slug: crustapi-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://crustapi.com
- group: auth
  title: ''
  type: TrustCenter
  url: security/crustapi-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crustapi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/crustapi-authentication.yml
- group: build
  title: ''
  type: SDKs
  url: packages/crustapi-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/crustapi-packages.yml
- group: auth
  title: ''
  type: Compliance
  url: security/crustapi-trust-center.yml
created: '2026-09-10'
description: Hosted API delivering structured Google (Search/Maps/etc.) and public LinkedIn data as JSON for developers, data teams, and AI agents. Pay-per-successful-result billing with an OpenAPI spec, an llms.txt, an x402 agent-payment endpoint, and a local MCP server.
image: https://crustapi.com/uploads/crustapi-12-handdrawn-continents-amber-accent.svg
layout: provider
mcp_servers:
- description: First-party MCP server giving MCP clients (Claude Desktop, Cursor, Cline, etc.) live Google (Search/Maps/News/Images/Reviews/webpage) and public LinkedIn data. Distributed as an npm package run locall
  name: CrustAPI MCP Server
  slug: crustapi-mcp-server
modified: '2026-09-10'
name: CrustAPI
nav: Providers
network: true
overview: 'CrustAPI publishes 1 API on the [APIs.io](https://apis.io/) network: CrustAPI. Tagged areas include Search, Google Maps, LinkedIn, SERP / Web Scraping, and Business & Lead Data.


  The CrustAPI catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  CrustAPI''s developer surface includes authentication and 6 more developer resources.'
plans:
- name: Crustapi Plans Pricing
  plan_count: 1
  slug: crustapi-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 3
  name: Crustapi Rate Limits
  slug: crustapi-rate-limits
score:
  band: developing
  composite: 52.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 54.0
    catalog_earned_first_party: 20.0
    catalog_gap: 61.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 81.6
    contract_governance: 18.2
    contract_quality: 48.1
    developer_ergonomics: 44.6
    discoverability: 70.4
    operational_transparency: 50.0
  previous_composite: 52.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Crustapi Authentication
  slug: crustapi-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Crustapi Domain Security
  slug: crustapi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Crustapi Trust Center
  slug: crustapi-trust-center
  summary_line: trust center published
slug: crustapi
tags:
- Search
- Google Maps
- LinkedIn
- SERP / Web Scraping
- Business & Lead Data
- People / Recruiting Data
- Data Enrichment
- AI Agents / MCP
- RAG
- Data
website: https://crustapi.com
---
