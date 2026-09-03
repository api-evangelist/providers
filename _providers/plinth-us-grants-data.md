---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 49.7
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://data.useplinth.com/api
  baseurl_source: declared
  description: Plain-English questions answered with SQL the service writes itself.
  name: Plinth US Grants Data Analyze API
  slug: plinth-us-grants-data-analyze-api
- baseURL: https://data.useplinth.com/api
  baseurl_source: declared
  description: 'The funder-grantee graph: grants, funders, recipients and aggregates.'
  name: Plinth US Grants Data Grants API
  slug: plinth-us-grants-data-grants-api
- baseURL: https://data.useplinth.com/api
  baseurl_source: declared
  description: Per-organization profiles, financials and IRS compliance facets.
  name: Plinth US Grants Data Organizations API
  slug: plinth-us-grants-data-organizations-api
- baseURL: https://data.useplinth.com/api
  baseurl_source: declared
  description: Turn an organization name into an EIN and a canonical URL. No key required.
  name: Plinth US Grants Data Resolve API
  slug: plinth-us-grants-data-resolve-api
- baseURL: https://data.useplinth.com/api
  baseurl_source: declared
  description: Ad-hoc read-only SQL over the warehouse. Paid keys only.
  name: Plinth US Grants Data SQL API
  slug: plinth-us-grants-data-sql-api
artifact_total: 14
common:
- group: agent
  title: ''
  type: MCPServer
  url: https://data.useplinth.com/api/connector/mcp
- group: agent
  title: ''
  type: MCPServer
  url: mcp/plinth-us-grants-data-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/plinth-us-grants-data-grants-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://data.useplinth.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://data.useplinth.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://data.useplinth.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://data.useplinth.com/developers#auth
- group: operate
  title: ''
  type: Support
  url: https://data.useplinth.com/developers#governance
- group: operate
  title: ''
  type: Contact
  url: mailto:data@useplinth.com
- group: commercial
  title: ''
  type: Pricing
  url: https://data.useplinth.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://data.useplinth.com/account
- group: start
  title: ''
  type: Login
  url: https://data.useplinth.com/account
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.useplinth.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.useplinth.com/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/plinth-us-grants-data-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/plinth-us-grants-data-scopes.yml
- group: auth
  title: ''
  type: Security
  url: security/plinth-us-grants-data-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/plinth-us-grants-data-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/plinth-us-grants-data-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/plinth-us-grants-data-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/plinth-us-grants-data-security.txt
- group: other
  title: ''
  type: APICatalog
  url: well-known/plinth-us-grants-data-api-catalog.json
- group: design
  title: ''
  type: Conformance
  url: conformance/plinth-us-grants-data-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/plinth-us-grants-data-lifecycle.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/plinth-us-grants-data-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/plinth-us-grants-data-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/plinth-us-grants-data-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-13'
description: 'A JSON API over the entire US grantmaking universe — about 205,000 grantmaking foundations and 17.9 million grants, read from public IRS Form 990, 990-EZ and 990-PF e-file filings and the IRS Business Master File. The funder-grantee graph traverses in both directions: filter by funder_id for everything a foundation funded, or by recip_id for every funder behind a nonprofit. Offers REST endpoints for grants, organization profiles, an IRS compliance and OFAC screen, an ad-hoc read-only SQL endpoint over a 31-table warehouse, and a hosted OAuth 2.1 MCP connector for AI agents. Entity resolution is free and unmetered. Published by Plinth, trading name of Time to Spare Ltd (UK Companies House 11530023), which also operates plinth.org.uk in the UK.'
image: https://data.useplinth.com/plinth-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: Plinth US Grants Data MCP Server
  slug: plinth-us-grants-data-mcp-server
- description: ''
  name: Plinth
  slug: plinth
modified: '2026-08-14'
name: Plinth US Grants Data
nav: Providers
network: true
overview: 'Plinth US Grants Data publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Analyze API, Grants API, Organizations API, and 2 more. Tagged areas include Philanthropy, Grants, Non-Profit, Foundations, and IRS 990.


  The Plinth US Grants Data catalog on APIs.io includes 1 Spectral governance ruleset.


  Plinth US Grants Data''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, authentication, and 21 more developer resources.'
plans:
- name: Plinth Us Grants Data Plans Pricing
  plan_count: 4
  slug: plinth-us-grants-data-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Plinth Us Grants Data Rate Limits
  slug: plinth-us-grants-data-rate-limits
rules:
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Plinth US Grants Data API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 0
    warn: 1
  slug: plinth-us-grants-data-spectral
scopes:
- name: Plinth Us Grants Data Scopes
  scope_count: 0
  slug: plinth-us-grants-data-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 67.4
  coverage:
    artifact_dirs: 20
    catalog_gap: 46.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 78.8
    contract_quality: 57.1
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 78.8
    operational_transparency: 10.5
  previous_composite: 67.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 75.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/plinth-us-grants-data/refs/heads/main/screenshots/plinth-us-grants-data-2026-08-17T081307.png
security:
- kind: authentication
  name: Plinth Us Grants Data Authentication
  slug: plinth-us-grants-data-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Plinth Us Grants Data Domain Security
  slug: plinth-us-grants-data-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Plinth Us Grants Data Vulnerability Disclosure
  slug: plinth-us-grants-data-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: plinth-us-grants-data
tags:
- Philanthropy
- Grants
- Non-Profit
- Foundations
- IRS 990
- Open Data
- Government Spending
- Research
- Agents
- REST
- JSON
- MCP
- SQL
website: https://data.useplinth.com/developers
---
