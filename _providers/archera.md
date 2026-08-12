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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.8
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 9
  human_in_the_loop: 3
  name: Archera Agentic Access
  operation_count: 28
  slug: archera-agentic-access
  summary_line: 28 operations · 9 acting · 3 human-in-the-loop
api_count: 10
apis:
- description: Partner API for onboarding customers, managing their optimization strategies, and creating marketplace offers through AWS CPPO, Microsoft MPO / ISV-to-CSP Private Offer, and Google MCPO programs.
  name: Archera Partner API
  slug: archera-partner-api
- description: API for managing commitment plans
  name: Archera Commitment Plans API
  slug: archera-commitment-plans-api
- description: API for retrieving and analyzing cloud commitment inventory, including Reserved Instances, Savings Plans, and Azure Reserved VM Instances. Provides access to detailed commitment data, utilization metr
  name: Archera Commitments API
  slug: archera-commitments-api
- description: API for commitment exchange recommendations
  name: Archera Exchanges API
  slug: archera-exchanges-api
- description: High level metrics to track commitment performance.
  name: Archera Metrics API
  slug: archera-metrics-api
- description: OAuth 2.0 authorization endpoints for third-party integrations
  name: Archera OAuth API
  slug: archera-oauth-api
- description: Endpoints for organizations accessible to the authenticated user
  name: Archera Orgs API
  slug: archera-orgs-api
- description: API for retrieving and analyzing infrastructure resources
  name: Archera Resources API
  slug: archera-resources-api
- description: API for uploading billing files for savings analysis
  name: Archera Uploads API
  slug: archera-uploads-api
- description: OAuth 2.0 discovery endpoints (JWKS and Authorization Server Metadata)
  name: Archera Well-Known API
  slug: archera-well-known-api
artifact_total: 16
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/archera-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://archera.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.archera.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.archera.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.archera.ai/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.archera.ai/getting-started/how-to-sign-up-with-archera
- group: auth
  title: ''
  type: Authentication
  url: authentication/archera-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/archera-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/archera-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/archera-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/archera-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/archera-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/archera-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/archera-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.archera.ai/trust
- group: auth
  title: ''
  type: TrustCenter
  url: security/archera-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/archera-domain-security.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/archera-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/archera-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/archera-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.archera.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://help.archera.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://www.archera.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.archera.ai/signup
- group: start
  title: ''
  type: Login
  url: https://app.archera.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.archera.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.archera.ai/privacy
created: '2026-07-17'
description: Archera is a cloud financial operations (FinOps) platform that helps organizations reduce cloud spend by 20-30% through intelligent commitment management and insured, short-term cloud commitments across AWS, Azure, and Google Cloud. Its Guaranteed Commitments (Guaranteed Savings Plans, Guaranteed Reserved Instances, and Guaranteed Committed Use Discounts) provide flexible terms as short as 30 days with risk protection for unused capacity. The Archera Public API exposes commitment plans, commitments, exchanges, metrics, resources, orgs, and uploads over a REST v1 interface authenticated with an API key or OAuth 2.0 (Authorization Code + PKCE), and Archera operates a hosted remote MCP server so AI assistants can query cloud cost data and optimization recommendations directly. A Partner API supports onboarding customers and creating marketplace offers via AWS CPPO, Microsoft MPO, and Google MCPO.
image: https://cdn.prod.website-files.com/66df18fcc90988b3a2c38285/677d4bc397e85ea0e180addb_1654705931-website-link-preview.avif
layout: provider
mcp_servers:
- description: ''
  name: archera-mcp.yml
  slug: archera-mcpyml
modified: '2026-07-18'
name: Archera
nav: Providers
network: true
overview: 'Archera publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Commitment Plans API, Commitments API, Exchanges API, and 6 more. Tagged areas include Company, Developer Tools, FinOps, Cloud Cost Management, and Cloud Commitments.


  Archera''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, pricing, and 21 more developer resources.'
random_paper: 30
scopes:
- name: Archera Scopes
  scope_count: 4
  slug: archera-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 47.4
  delta: -0.4
  facets:
    commercial_clarity: 60.5
    contract_quality: 44.2
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 0.0
  previous_composite: 47.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/archera/refs/heads/main/screenshots/archera-2026-07-25T201044.png
security:
- kind: authentication
  name: Archera Authentication
  slug: archera-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Archera Domain Security
  slug: archera-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Archera Trust Center
  slug: archera-trust-center
  summary_line: SOC 2, ISO 27001
slug: archera
tags:
- Company
- Developer Tools
- FinOps
- Cloud Cost Management
- Cloud Commitments
- Cost Optimization
- MCP
- Azure
- Google Cloud
website: https://archera.ai
---
