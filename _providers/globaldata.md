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
    mcp_server: templated
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.0
  scored_at: '2026-09-14'
api_count: 1
apis:
- description: A governed Model Context Protocol gateway that turns GlobalData's business intelligence into tools an AI agent can call directly. One MCP server endpoint per industry vertical, all sharing a single to
  name: GlobalData Intelligence Center MCP
  slug: globaldata-intelligence-center-mcp
artifact_total: 7
common:
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
  href: https://raw.githubusercontent.com/api-evangelist/globaldata/refs/heads/main/well-known/globaldata-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/globaldata-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/globaldata/refs/heads/main/mcp/globaldata-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/globaldata-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/globaldata/refs/heads/main/authentication/globaldata-authentication.yml
  title: ''
  type: Authentication
  url: authentication/globaldata-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/globaldata/refs/heads/main/scopes/globaldata-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/globaldata-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/globaldata/refs/heads/main/conformance/globaldata-conformance.yml
  title: ''
  type: Conformance
  url: conformance/globaldata-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/globaldata/refs/heads/main/conventions/globaldata-conventions.yml
  title: ''
  type: Conventions
  url: conventions/globaldata-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/globaldata/refs/heads/main/lifecycle/globaldata-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/globaldata-lifecycle.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/globaldata/refs/heads/main/packages/globaldata-packages.yml
  title: ''
  type: Packages
  url: packages/globaldata-packages.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/globaldata/refs/heads/main/plans/globaldata-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/globaldata-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/globaldata/refs/heads/main/rate-limits/globaldata-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/globaldata-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/globaldata/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/globaldata/refs/heads/main/llms/globaldata-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/globaldata-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/globaldata/refs/heads/main/security/globaldata-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/globaldata-domain-security.yml
created: '2026-09-13'
description: 'GlobalData Plc is a London-listed data, analytics and insights company (LSE: DATA) whose Intelligence Center platform covers companies, deals, news, filings, patents, job postings, research reports, projects and market data across 20+ industry verticals. Its machine-readable surface is agent-native rather than REST-first: GlobalData operates a first-party Model Context Protocol gateway at mcp.globaldata.com that exposes the estate as callable agent tools, one MCP server endpoint per vertical, behind OAuth 2.1 via GlobalData SSO. The gateway publishes a full developer reference at its host root, RFC 8414 and RFC 9728 OAuth metadata, and an Agentic Resource Discovery (AIR) manifest at /.well-known/ai-catalog.json advertising all 23 vertical endpoints. No OpenAPI, GraphQL SDL, AsyncAPI or SOAP contract is published anywhere.'
image: https://www.globaldata.com/wp-content/uploads/2025/12/cropped-cropped-gd_icon-192x192.png
layout: provider
mcp_servers:
- description: ''
  name: GlobalData Intelligence Center MCP
  slug: globaldata-intelligence-center-mcp
modified: '2026-09-13'
name: GlobalData
nav: Providers
network: true
overview: 'GlobalData publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Market Intelligence, Business Intelligence, Data, and Analytics.


  GlobalData''s developer surface includes documentation, API reference, support, signup flow, engineering blog, authentication, and 16 more developer resources.'
plans:
- name: Globaldata Plans Pricing
  plan_count: 0
  slug: globaldata-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Globaldata Rate Limits
  slug: globaldata-rate-limits
scopes:
- name: Globaldata Scopes
  scope_count: 0
  slug: globaldata-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 25.6
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 20.8
    discoverability: 68.5
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 56.8
  schema_version: 0.22.0
  scored_at: '2026-09-14'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Globaldata Authentication
  slug: globaldata-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Globaldata Domain Security
  slug: globaldata-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
- Financial-Services
- Energy
- Mining
website: https://www.globaldata.com/
---
