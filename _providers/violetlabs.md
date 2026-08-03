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
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: REST API for programmatic access to your Violet data. The Explore endpoint (POST /api/explore) accepts a rich query payload (keyword, filterModel, sort, grouping, pagination) and returns a paginated P
  name: Violet Explore API
  slug: violet-explore-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/violetlabs-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/violetlabs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://violetlabs.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.violetlabs.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.violetlabs.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.violetlabs.com/features/api/endpoints
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.violetlabs.com/features/api/generate-an-api-key
- group: start
  title: ''
  type: SignUp
  url: https://app.violetlabs.com/login
- group: start
  title: ''
  type: Login
  url: https://app.violetlabs.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.violetlabs.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.violetlabs.com/resources/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.violetlabs.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.violetlabs.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.violetlabs.com/contact-us
- group: operate
  title: ''
  type: StatusPage
  url: https://violetlabs.statuspage.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://changelog.violetlabs.com/changelog
- group: auth
  title: ''
  type: Compliance
  url: https://trust.violetlabs.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/violetlabsinc/
- group: company
  title: ''
  type: Careers
  url: https://jobs.violetlabs.com/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/violetlabs-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/violetlabs-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/violetlabs-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/violetlabs-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/violetlabs-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/violetlabs-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/violetlabs-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/violetlabs-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/violetlabs-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/violetlabs-llms.txt
created: '2026-07-17'
description: Violet Labs is the connective tissue for hardware engineering data. Its cloud platform gives hardware, systems, and manufacturing teams a single workspace that harmonizes the software stack — PLM, ERP, CAD, PDM, MES, requirements, and procurement tools — through no-code integrations, data-sync workflows, parameters, native Python/Julia/MATLAB scripts, requirements management, reporting, and dashboards. Violet exposes a REST API (the Explore endpoint) authenticated with an x-api-key header, an OAuth 2.0 authorization server with dynamic client registration for its hosted Model Context Protocol (MCP) server, and an AI chat/agent surface. The platform is ITAR/EAR-aware, SOC 2 certified, and NIST/CMMC/FedRAMP-aligned, with on-premises and VioletGov deployment options for defense and regulated hardware programs.
image: https://cdn.prod.website-files.com/681bdb35ddf11baf679e267f/689288c5b6e253d5a804b2cf_Share%20Image.webp
layout: provider
mcp_servers:
- description: ''
  name: violetlabs-mcp.yml
  slug: violetlabs-mcpyml
modified: '2026-07-21'
name: Violetlabs
nav: Providers
network: true
overview: 'Violetlabs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hardware, Engineering, Manufacturing, and PLM.


  Violetlabs'' developer surface includes documentation, API reference, getting-started guide, signup flow, engineering blog, pricing, support, and 22 more developer resources.'
random_paper: 32
scopes:
- name: Violetlabs Scopes
  scope_count: 1
  slug: violetlabs-scopes
  summary_line: 1 scope · authorizationCode/clientCredentials
score:
  band: thin
  composite: 39.9
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 67.4
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 31.6
  previous_composite: 39.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Violetlabs Authentication
  slug: violetlabs-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Violetlabs Domain Security
  slug: violetlabs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Violetlabs Trust Center
  slug: violetlabs-trust-center
  summary_line: SOC 2, HIPAA, FIPS 140
slug: violetlabs
tags:
- Company
- Hardware
- Engineering
- Manufacturing
- PLM
- ERP
- Data Integration
- Requirements Management
- Aerospace
- Defense
- MCP
- Systems Engineering
website: https://violetlabs.com
---
