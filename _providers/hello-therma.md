---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
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
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.4
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: First-party remote Model Context Protocol server exposing read-only GlacierGrid facility monitoring data — HVAC, refrigeration, energy and savings, sensor readings, issues, notifications, device conne
  name: GlacierGrid MCP Server
  slug: glaciergrid-mcp-server
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hello-therma-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.glaciergrid.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.glaciergrid.com/connector
- group: operate
  title: ''
  type: Support
  url: https://www.glaciergrid.com/helpcenter
- group: company
  title: ''
  type: Blog
  url: https://www.glaciergrid.com/resources/research-and-impact
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.glaciergrid.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.glaciergrid.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.glaciergrid.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/glaciergrid
- group: operate
  title: ''
  type: StatusPage
  url: https://www.glaciergrid.com/status-page
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.glaciergrid.com/resources/product-features
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hello-therma-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hello-therma-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hello-therma-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hello-therma-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hello-therma-scopes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hello-therma-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hello-therma-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hello-therma-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hello-therma-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/hello-therma-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hello-therma-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hello-therma-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/hello-therma-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/hello-therma-packages.yml
created: '2026-08-22'
description: Hello Therma is the original brand of Therma, Inc., the San Francisco cold-chain and cooling intelligence company founded in 2014 by Manik Suri, which rebranded as GlacierGrid in February 2024 and now operates as GlacierGrid, Inc. out of Richmond, Virginia. The platform pairs LoRaWAN temperature and humidity sensors, cellular monitoring hubs and BAS integrations with a cloud dashboard that gives multi-unit retail, restaurant, convenience-store, education and fitness operators remote refrigeration and HVAC monitoring, automated temperature logging for HACCP-style food-safety reporting, equipment-failure prediction and energy optimization across 50 to 500 locations. GlacierGrid publishes no REST, GraphQL or SOAP API and no developer portal; its single machine-callable surface is a first-party remote Model Context Protocol server at mcp.glaciergrid.com, marketed as the GlacierGrid Connector for Claude, which exposes read-only facility, sensor, alert and energy data to an agent
  under OAuth with account-scoped permissions.
image: https://www.glaciergrid.com/hubfs/Glacier%20Grid%20Primary%20Teal-2.png
layout: provider
mcp_servers:
- description: ''
  name: GlacierGrid MCP Server
  slug: glaciergrid-mcp-server
modified: '2026-08-22'
name: Hello Therma
nav: Providers
network: true
overview: 'Hello Therma publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Internet of Things, Energy, Sustainability, and Cold Chain.


  Hello Therma''s developer surface includes documentation, support, engineering blog, signup flow, changelog, authentication, and 19 more developer resources.'
plans:
- name: Hello Therma Plans Pricing
  plan_count: 0
  slug: hello-therma-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Hello Therma Rate Limits
  slug: hello-therma-rate-limits
scopes:
- name: Hello Therma Scopes
  scope_count: 0
  slug: hello-therma-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 35.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 55.3
  previous_composite: 35.1
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 63.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hello-therma/refs/heads/main/screenshots/hello-therma-2026-09-02T145719.png
security:
- kind: authentication
  name: Hello Therma Authentication
  slug: hello-therma-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Hello Therma Domain Security
  slug: hello-therma-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hello-therma
tags:
- Company
- Internet of Things
- Energy
- Sustainability
- Cold Chain
- Temperature Monitoring
- Refrigeration
- HVAC
- Building Automation
- Food Safety
- Facilities Management
- Restaurant
- Retail
- MCP
- Agents
website: https://www.glaciergrid.com/
---
