---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
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
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 'Programmatic access to Tracxn''s private-market database. Version 3.0 is current and version 2.2 is formally announced for deprecation. A uniform JSON-over-HTTPS contract: every data endpoint is a POST'
  name: Tracxn API
  slug: tracxn-api
- description: 'Tracxn''s official first-party remote Model Context Protocol server, exposing the private-market database to any MCP-compatible AI client — Claude, ChatGPT, Cursor, Gemini CLI, Perplexity, or anything '
  name: Tracxn MCP Server
  slug: tracxn-mcp-server
artifact_total: 12
common:
- group: auth
  href: https://artifacts.apis.io/tracxn/security/tracxn-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tracxn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tracxn.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://w.tracxn.com/api-developers-page
- group: docs
  title: ''
  type: Documentation
  url: https://platform.tracxn.com/a/api/gettingstarted/apibasics
- group: start
  title: ''
  type: GettingStarted
  url: https://platform.tracxn.com/a/api/gettingstarted/apibasics
- group: commercial
  title: ''
  type: Pricing
  url: https://tracxn.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://tracxn.com/signup
- group: start
  title: ''
  type: Login
  url: https://tracxn.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tracxn.com/termsofuse
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tracxn.com/privacypolicy
- group: operate
  title: ''
  type: Support
  url: https://help.tracxn.com/en/
- group: operate
  title: ''
  type: ContactUs
  url: https://tracxn.com/contactus
- group: operate
  title: ''
  type: FAQ
  url: https://w.tracxn.com/faqs
- group: company
  title: ''
  type: Blog
  url: https://tracxn.com/p/media
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tracxn
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/tracxnapi/tracxn-api/overview
- group: agent
  href: https://artifacts.apis.io/tracxn/mcp/tracxn-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/tracxn-mcp.yml
- group: agent
  href: https://artifacts.apis.io/tracxn/llms/tracxn-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tracxn-llms.txt
- group: auth
  href: https://artifacts.apis.io/tracxn/authentication/tracxn-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tracxn-authentication.yml
- group: start
  href: https://artifacts.apis.io/tracxn/sandbox/tracxn-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/tracxn-sandbox.yml
- group: design
  href: https://artifacts.apis.io/tracxn/conventions/tracxn-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tracxn-conventions.yml
- group: design
  href: https://artifacts.apis.io/tracxn/errors/tracxn-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tracxn-problem-types.yml
- group: design
  href: https://artifacts.apis.io/tracxn/lifecycle/tracxn-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tracxn-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/tracxn/conformance/tracxn-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tracxn-conformance.yml
- group: design
  href: https://artifacts.apis.io/tracxn/data-model/tracxn-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tracxn-data-model.yml
- group: build
  href: https://artifacts.apis.io/tracxn/mcp/tracxn-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/tracxn-tool-crosswalk.yml
- group: auth
  href: https://artifacts.apis.io/tracxn/scopes/tracxn-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/tracxn-scopes.yml
- group: agent
  href: https://artifacts.apis.io/tracxn/well-known/tracxn-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tracxn-well-known.yml
- group: operate
  href: https://artifacts.apis.io/tracxn/rate-limits/tracxn-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tracxn-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/tracxn/plans/tracxn-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tracxn-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/tracxn/packages/tracxn-packages.yml
  title: ''
  type: Packages
  url: packages/tracxn-packages.yml
- group: agent
  href: https://artifacts.apis.io/tracxn/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/tracxn/lifecycle/tracxn-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/tracxn-lifecycle.yml
- group: docs
  title: ''
  type: APIReference
  url: https://www.postman.com/tracxnapi/tracxn-api/folder/gg9mglv/companies-search-3-0
created: '2026-07-17'
description: 'Tracxn is a market intelligence platform for private company data, tracking 7.7M+ companies worldwide across 2,000+ sectors, 3K+ feeds and 55K+ taxonomies for venture capital funds, private equity, investment banks, corporate M&A and innovation teams. Alongside the platform it sells Data Solutions for programmatic access: the Tracxn API (JSON over HTTPS at platform.tracxn.com/api/2.2 with companies, investors, funding transactions and acquisition endpoints, plus a rate-limited Playground sandbox), an official Tracxn MCP server for AI assistants such as Claude, ChatGPT and Cursor, scheduled SFTP dumps, and Snowflake and BigQuery data-share integrations. Founded in Bengaluru by Neha Singh and Abhishek Goyal and backed by Accel, Tracxn is listed on the Indian stock exchanges (NSE: TRACXN).'
finops:
- has_sources: true
  method: derived
  name: Tracxn Finops
  primary_unit: ''
  service_category: ''
  slug: tracxn-finops
  template: true
image: https://avatars.githubusercontent.com/u/12694738?v=4
layout: provider
mcp_servers:
- description: 'Tracxn operates an official, first-party, REMOTE MCP server that exposes the private-market database — companies, legal entities, funding rounds, acquisitions, investors, IPOs, time series, locations '
  name: Tracxn MCP
  slug: tracxn-mcp
modified: '2026-08-14'
name: Tracxn
nav: Providers
network: true
overview: 'Tracxn is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud Saas, Market Intelligence, Private Markets, and Venture Capital.


  Tracxn''s developer surface includes documentation, getting-started guide, pricing, signup flow, support, FAQ, engineering blog, and 27 more developer resources.'
plans:
- name: Tracxn Plans Pricing
  plan_count: 3
  slug: tracxn-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 9
  name: Tracxn Rate Limits
  slug: tracxn-rate-limits
scopes:
- name: Tracxn Scopes
  scope_count: 1
  slug: tracxn-scopes
  summary_line: 1 scope
score:
  band: developing
  composite: 46.3
  coverage:
    artifact_dirs: 23
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 64.9
    discoverability: 75.0
    operational_transparency: 42.1
  previous_composite: 46.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tracxn/tracxn-2026-09-02T164035.png
security:
- kind: authentication
  name: Tracxn Authentication
  slug: tracxn-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Tracxn Domain Security
  slug: tracxn-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Research a private company on Tracxn
  slug: tracxn-company-research
- name: Connect an AI client to the Tracxn MCP server
  slug: tracxn-mcp-connect
- name: Map a sector landscape and its funding activity on Tracxn
  slug: tracxn-sector-landscape
slug: tracxn
tags:
- Company
- Cloud Saas
- Market Intelligence
- Private Markets
- Venture Capital
- Startups
- Company Data
- Investor
- Funding
website: https://tracxn.com
---
