---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: A governed Model Context Protocol gateway that turns GlobalData's business intelligence into tools an AI agent can call directly. One MCP server endpoint per industry vertical, all sharing a single to
  name: GlobalData Intelligence Center MCP
  slug: globaldata-intelligence-center-mcp
artifact_total: 13
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://www.globaldata.com/feed/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mcp.globaldata.com/
- group: docs
  title: ''
  type: Documentation
  url: https://mcp.globaldata.com/
- group: docs
  title: ''
  type: APIReference
  url: https://mcp.globaldata.com/
- group: company
  title: ''
  type: Website
  url: https://www.globaldata.com/
- group: operate
  title: ''
  type: Support
  url: https://www.globaldata.com/contact-us/
- group: start
  title: ''
  type: SignUp
  url: https://login.globaldata.com/login/index
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.globaldata.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.globaldata.com/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://www.globaldata.com/data-insights/
- group: agent
  href: https://artifacts.apis.io/globaldata/well-known/globaldata-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/globaldata-well-known.yml
- group: agent
  href: https://artifacts.apis.io/globaldata/mcp/globaldata-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/globaldata-mcp.yml
- group: auth
  href: https://artifacts.apis.io/globaldata/authentication/globaldata-authentication.yml
  title: ''
  type: Authentication
  url: authentication/globaldata-authentication.yml
- group: auth
  href: https://artifacts.apis.io/globaldata/scopes/globaldata-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/globaldata-scopes.yml
- group: design
  href: https://artifacts.apis.io/globaldata/conformance/globaldata-conformance.yml
  title: ''
  type: Conformance
  url: conformance/globaldata-conformance.yml
- group: design
  href: https://artifacts.apis.io/globaldata/conventions/globaldata-conventions.yml
  title: ''
  type: Conventions
  url: conventions/globaldata-conventions.yml
- group: design
  href: https://artifacts.apis.io/globaldata/lifecycle/globaldata-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/globaldata-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/globaldata/packages/globaldata-packages.yml
  title: ''
  type: Packages
  url: packages/globaldata-packages.yml
- group: commercial
  href: https://artifacts.apis.io/globaldata/plans/globaldata-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/globaldata-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/globaldata/rate-limits/globaldata-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/globaldata-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/globaldata/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/globaldata/llms/globaldata-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/globaldata-llms.txt
- group: auth
  href: https://artifacts.apis.io/globaldata/security/globaldata-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/globaldata-domain-security.yml
created: '2026-09-13'
description: 'GlobalData Plc is a London-listed data, analytics and insights company (LSE: DATA) whose Intelligence Center platform covers companies, deals, news, filings, patents, job postings, research reports, projects and market data across 20+ industry verticals. Its machine-readable surface is agent-native rather than REST-first: GlobalData operates a first-party Model Context Protocol gateway at mcp.globaldata.com that exposes the estate as callable agent tools, one MCP server endpoint per vertical, behind OAuth 2.1 via GlobalData SSO. The gateway publishes a full developer reference at its host root, RFC 8414 and RFC 9728 OAuth metadata, and an Agentic Resource Discovery (AIR) manifest at /.well-known/ai-catalog.json advertising all 23 vertical endpoints. No OpenAPI, GraphQL SDL, AsyncAPI or SOAP contract is published anywhere.'
image: https://www.globaldata.com/wp-content/uploads/2025/12/cropped-cropped-gd_icon-192x192.png
layout: provider
mcp_servers:
- description: 'GlobalData Plc operates a first-party, production Model Context Protocol gateway at mcp.globaldata.com that exposes its business-intelligence estate as callable agent tools. The gateway is documented '
  name: GlobalData Intelligence Center MCP
  slug: globaldata-intelligence-center-mcp
modified: '2026-10-06'
name: GlobalData
nav: Providers
network: true
overview: 'GlobalData is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Market Intelligence, Business Intelligence, Data, and Analytics.


  GlobalData''s developer surface includes documentation, API reference, support, signup flow, engineering blog, authentication, and 17 more developer resources.'
plans:
- name: Globaldata Plans Pricing
  plan_count: 0
  slug: globaldata-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Globaldata Rate Limits
  slug: globaldata-rate-limits
scopes:
- name: Globaldata Scopes
  scope_count: 4
  slug: globaldata-scopes
  summary_line: 4 scopes
score:
  band: thin
  composite: 28.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 47.0
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 28.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 34.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/globaldata/globaldata-2026-10-11T104933.png
security:
- kind: authentication
  name: Globaldata Authentication
  slug: globaldata-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Globaldata Domain Security
  slug: globaldata-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 6
skills:
- name: globaldata-company-profile
  slug: globaldata-company-profile
- name: globaldata-connect-and-orient
  slug: globaldata-connect-and-orient
- name: globaldata-deal-activity
  slug: globaldata-deal-activity
- name: globaldata-filings-evidence
  slug: globaldata-filings-evidence
- name: globaldata-hiring-signal
  slug: globaldata-hiring-signal
- name: globaldata-news-sentiment
  slug: globaldata-news-sentiment
slug: globaldata
tags:
- Company
- Market Intelligence
- Business Intelligence
- Data
- Analytics
- MCP
- Agents
- Company Data
- Deals
- News
- Patents
- Research
- Financial Services
- Energy
- Mining
website: https://www.globaldata.com/
---
