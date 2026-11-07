---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Scrappa API provides web scraping endpoints across various data sources.
  name: Scrappa API
  slug: scrappa-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/scrappa-co/plans/scrappa-co-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/scrappa-co-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/scrappa-co/authentication/scrappa-co-authentication.yml
  title: ''
  type: Authentication
  url: authentication/scrappa-co-authentication.yml
- group: design
  href: https://artifacts.apis.io/scrappa-co/errors/scrappa-co-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/scrappa-co-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/scrappa-co/llms/scrappa-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/scrappa-co-llms.txt
- group: agent
  href: https://artifacts.apis.io/scrappa-co/mcp/scrappa-co-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/scrappa-co-mcp.yml
- group: agent
  href: https://artifacts.apis.io/scrappa-co/well-known/scrappa-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/scrappa-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/scrappa-co/hosts/scrappa-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/scrappa-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/scrappa-co/vendors/scrappa-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/scrappa-co-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://scrappa.co/legal/terms-of-service
- group: start
  title: ''
  type: Sandbox
  url: https://scrappa.co/dashboard/playground
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://scrappa.co/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/userlip
- group: auth
  href: https://artifacts.apis.io/scrappa-co/security/scrappa-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scrappa-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://scrappa.co/
- group: docs
  title: ''
  type: Documentation
  url: https://scrappa.co/docs
- group: docs
  title: ''
  type: APIReference
  url: https://scrappa.co/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://scrappa.co/docs#getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://scrappa.co/pricing
- group: start
  title: ''
  type: Login
  url: https://scrappa.co/login
created: '2026-10-31'
description: Scrappa is a web scraping API platform offering over 80 JSON endpoints that provide structured data from sources such as Google Search, Google Maps, YouTube, LinkedIn, job listings, reviews, travel, and commerce. Developers can retrieve data in a consistent JSON format with a simple API key, benefiting from a free tier of 500 monthly credits and pay‑as‑you‑go pricing. The service aims to simplify data extraction, reduce the need for custom scrapers, and accelerate integration of web‑derived information into applications.
image: https://scrappa.co/logo.png
layout: provider
mcp_servers:
- description: Remote MCP server at scrappa.co requiring an API key.
  name: scrappa-co MCP Server
  slug: scrappa-co-mcp-yml
modified: '2026-10-31'
name: scrappa-co
nav: Providers
network: true
overview: 'scrappa-co is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Web Scraping, Data API, Search, Automation, and JSON.


  scrappa-co''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, pricing, and 13 more developer resources.'
plans:
- name: Scrappa Co Plans Pricing
  plan_count: 3
  slug: scrappa-co-plans-pricing
random_paper: 17
scopes:
- name: Scrappa Co Scopes
  scope_count: 0
  slug: scrappa-co-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 25.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.0
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 29.8
    discoverability: 65.0
    operational_transparency: 2.6
  previous_composite: 34.1
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/scrappa-co/scrappa-co-2026-11-03T142838.png
security:
- kind: authentication
  name: Scrappa Co Authentication
  slug: scrappa-co-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Scrappa Co Domain Security
  slug: scrappa-co-domain-security
  summary_line: TLSv1.3 · DMARC
slug: scrappa-co
tags:
- Web Scraping
- Data API
- Search
- Automation
- JSON
website: https://scrappa.co/
---
