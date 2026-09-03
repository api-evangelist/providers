---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
  score: 12.3
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: REST API for retrieving public company org charts, prospecting positions/people, and monitoring credit usage. Metered in credits; authenticated with an X-Api-Key header.
  name: The Org API
  slug: the-org-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/theorg-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://theorg.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.theorg.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.theorg.com/api
- group: docs
  title: ''
  type: APIReference
  url: https://developers.theorg.com/api/endpoints/company-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.theorg.com/api/get-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.theorg.com/api/change-log
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/theorg-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/theorg-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/theorg-tool-crosswalk.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/theorg-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/theorg-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/theorg-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/theorg-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/theorg-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/theorg-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/theorg-components.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/theorg-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/theorg-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/theorg-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/theorg-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/theorg-well-known.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/theorg-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://theorg.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://support.theorg.com/en/
- group: company
  title: ''
  type: Blog
  url: https://blog.theorg.com/
- group: start
  title: ''
  type: SignUp
  url: https://theorg.com/signup
- group: start
  title: ''
  type: Login
  url: https://theorg.com/subscription
- group: commercial
  title: ''
  type: TermsOfService
  url: https://theorg.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://theorg.com/privacy
created: '2026-07-17'
description: 'The Org operates the world''s largest network of public organizational charts, mapping companies, their teams, and reporting hierarchies. Its developer platform exposes a metered REST API and an official MCP server for retrieving a company''s public org chart by domain or LinkedIn URL, prospecting positions and people with rich filters, resolving a person''s manager, and monitoring credit usage. Authentication is via an account-scoped X-Api-Key header over HTTPS, usage is metered in monthly credits, and the same key powers a remote Model Context Protocol endpoint exposing thirteen tools for agent-native access — company and person lookup, job search, reporting-line traversal, work-email resolution, and lead-list management. The MCP surface is materially wider than the REST API: eight of the thirteen tools have no REST equivalent, and list creation is the only write operation The Org exposes anywhere. Originally added to the API Evangelist network as a portfolio company of Balderton
  Capital.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/theorg.png
layout: provider
mcp_servers:
- description: ''
  name: The Org MCP Server
  slug: the-org-mcp-server
modified: '2026-08-14'
name: The Org
nav: Providers
network: true
overview: 'The Org publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Organizational Charts, People Data, Sales Intelligence, and Prospecting.


  The Org''s developer surface includes documentation, API reference, getting-started guide, changelog, authentication, pricing, support, and 24 more developer resources.'
plans:
- name: Theorg Plans Pricing
  plan_count: 4
  slug: theorg-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Theorg Rate Limits
  slug: theorg-rate-limits
scopes:
- name: Theorg Scopes
  scope_count: 1
  slug: theorg-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 42.4
  coverage:
    artifact_dirs: 19
    catalog_gap: 58.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 58.9
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 36.8
  previous_composite: 42.4
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/theorg/refs/heads/main/screenshots/theorg-2026-08-17T082341.png
security:
- kind: authentication
  name: Theorg Authentication
  slug: theorg-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Theorg Domain Security
  slug: theorg-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Theorg Trust Center
  slug: theorg-trust-center
  summary_line: trust center published
slug: theorg
tags:
- Company
- Organizational Charts
- People Data
- Sales Intelligence
- Prospecting
- Org Chart
- B2B Data
- MCP
- Contact Data
- Lead Generation
- Job
- Agents
website: https://theorg.com/
---
