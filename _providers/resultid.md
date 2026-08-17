---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 63.5
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Resultid Agentic Access
  operation_count: 9
  slug: resultid-agentic-access
  summary_line: 9 operations
api_count: 1
apis:
- description: Read API over Resultid's operational intelligence data - campaign data, campaign theme data, campaign trend data, insight last-result payloads, insight grid rows (whole-campaign or by filtered-data EF
  name: Resultid API
  slug: resultid-api
artifact_total: 7
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/resultid-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.resultid.ai/
- group: start
  title: ''
  type: Login
  url: https://app.resultid.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.resultid.ai/
- group: other
  title: ''
  type: X
  url: https://x.com/resultid
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/resultid
- group: auth
  title: ''
  type: DomainSecurity
  url: security/resultid-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Resultid
- group: docs
  title: ''
  type: Documentation
  url: https://docs.resultid.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.resultid.com/22_api_spec_test/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.resultid.com/1_getting_started/
- group: auth
  title: ''
  type: Authentication
  url: authentication/resultid-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/resultid-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/resultid-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/resultid-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/resultid-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/resultid-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/resultid-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/resultid-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/resultid-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/resultid-api-overlay.yaml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/resultid-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/resultid-plans-pricing.yml
created: '2026-07-17'
description: 'Resultid is an enterprise Operational Intelligence platform that connects what customers say, what teams do, and what operational data shows across every product, location, and service to surface hidden revenue opportunities. It ingests data from hundreds of sources - surveys, calls, CRM systems, reviews, and service records - and applies AI to identify the behavioral patterns that separate high-performing locations from underperformers, bridging the gap between well-measured technical operations and largely invisible human operations. The platform serves automotive, airlines, hospitality, financial services, and retail enterprises. Resultid is a Techstars-backed company. It does publish a developer surface, though it is not linked from the marketing site: an MkDocs "Resultid API Docs" site at docs.resultid.com renders a FastAPI-generated OpenAPI schema of nine read operations over campaigns, insights, trackers, themes and highlight data, authenticated with an X-API-Key request
  header. The raw JSON schema is not served and no API base URL is published anywhere, so the contract is readable but not yet callable from the documentation alone.'
image: https://www.resultid.ai/images/logo-white.svg
layout: provider
mcp_servers:
- description: ''
  name: resultid-mcp.yml
  slug: resultid-mcpyml
modified: '2026-08-14'
name: Resultid
nav: Providers
network: true
overview: 'Resultid publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Operational Intelligence, Analytics, Enterprise Software, and Artificial Intelligence.


  Resultid''s developer surface includes documentation, API reference, getting-started guide, authentication, and 20 more developer resources.'
plans:
- name: Resultid Plans Pricing
  plan_count: 0
  slug: resultid-plans-pricing
random_paper: 131
rate_limits:
- limit_count: 0
  name: Resultid Rate Limits
  slug: resultid-rate-limits
score:
  band: thin
  composite: 37.1
  delta: 27.4
  facets:
    commercial_clarity: 13.2
    contract_quality: 44.0
    developer_ergonomics: 52.2
    discoverability: 77.8
    governance: 20.8
    operational_transparency: 21.1
  previous_composite: 9.7
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
security:
- kind: authentication
  name: Resultid Authentication
  slug: resultid-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Resultid Domain Security
  slug: resultid-domain-security
  summary_line: TLSv1.3 · DMARC
slug: resultid
tags:
- Company
- Operational Intelligence
- Analytics
- Enterprise Software
- Artificial Intelligence
- Customer Experience
- Data Integration
- Revenue Intelligence
website: https://www.resultid.ai/
---
