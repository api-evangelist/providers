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
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.3
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Pigment Agentic Access
  operation_count: 19
  slug: pigment-agentic-access
  summary_line: 19 operations · 11 acting
api_count: 8
apis:
- description: The ApplicationApi API from Pigment — 1 operation(s) for applicationapi.
  name: Pigment ApplicationApi API
  slug: pigment-applicationapi-api
- description: The BlocksApi API from Pigment — 1 operation(s) for blocksapi.
  name: Pigment BlocksApi API
  slug: pigment-blocksapi-api
- description: The Export API from Pigment — 4 operation(s) for export.
  name: Pigment Export API
  slug: pigment-export-api
- description: The ExportV1 API from Pigment — 4 operation(s) for exportv1.
  name: Pigment ExportV1 API
  slug: pigment-exportv1-api
- description: The ImportApi API from Pigment — 3 operation(s) for importapi.
  name: Pigment ImportApi API
  slug: pigment-importapi-api
- description: The ImportConfigurationApi API from Pigment — 1 operation(s) for importconfigurationapi.
  name: Pigment ImportConfigurationApi API
  slug: pigment-importconfigurationapi-api
- description: The ImportV1 API from Pigment — 4 operation(s) for importv1.
  name: Pigment ImportV1 API
  slug: pigment-importv1-api
- description: The ViewApi API from Pigment — 1 operation(s) for viewapi.
  name: Pigment ViewApi API
  slug: pigment-viewapi-api
artifact_total: 15
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/pigment-external-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://kb.pigment.com/
- group: docs
  title: ''
  type: Documentation
  url: https://kb.pigment.com/docs/api-management
- group: docs
  title: ''
  type: APIReference
  url: https://pigment.app/api/swagger/
- group: start
  title: ''
  type: GettingStarted
  url: https://kb.pigment.com/docs/export-data-with-apis
- group: operate
  title: ''
  type: Support
  url: https://support.pigment.com/support/home
- group: company
  title: ''
  type: Blog
  url: https://www.pigment.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gopigment
- group: start
  title: ''
  type: Login
  url: https://pigment.app/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pigment.com/msa/online-master-services-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pigment.com/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/pigment-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pigment-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pigment-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pigment-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pigment-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/pigment-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pigment-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.pigment.com/security
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pigment-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pigment-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/pigment-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/pigment-security.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pigment-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/pigment-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pigment-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.pigment.com/vdp
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pigment-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pigment.com/
created: '2026-07-17'
description: Pigment is an enterprise business planning platform (FP&A, workforce, sales, and supply-chain planning, and financial consolidation) that exposes a public REST API. The Pigment External API (OpenAPI 3.0.4, v1-external) covers CSV and Looker imports, CSV exports of Metric/List/Table Views, application/block/view metadata, import triggering and status, plus a SCIM 2.0 user-management API and an Enterprise Audit Logs API. Pigment also operates an official remote Model Context Protocol (MCP) server for AI clients and publishes domain-knowledge Agent Skills. Authentication is via Bearer API keys (typed Import/Export/Metadata/SCIM/Audit) with IP allow lists.
image: https://raw.githubusercontent.com/gopigment/ai-plugins/main/logo.svg
layout: provider
mcp_servers:
- description: ''
  name: pigment-mcp.yml
  slug: pigment-mcpyml
modified: '2026-07-20'
name: Pigment
nav: Providers
network: true
overview: 'Pigment publishes 8 APIs on the [APIs.io](https://apis.io/) network, including ApplicationApi API, BlocksApi API, Export API, and 5 more. Tagged areas include Company, Enterprise Software, Business Planning, Financial Planning, and FP&A.


  Pigment''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 24 more developer resources.'
random_paper: 60
rate_limits:
- limit_count: 1
  name: Pigment Rate Limits
  slug: pigment-rate-limits
score:
  band: developing
  composite: 50.1
  delta: -1.5
  facets:
    commercial_clarity: 50.0
    contract_quality: 44.8
    developer_ergonomics: 67.4
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 36.8
  previous_composite: 51.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Pigment Authentication
  slug: pigment-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Pigment Domain Security
  slug: pigment-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Pigment Vulnerability Disclosure
  slug: pigment-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Pigment Trust Center
  slug: pigment-trust-center
  summary_line: SOC 2, GDPR
slug: pigment
tags:
- Company
- Enterprise Software
- Business Planning
- Financial Planning
- FP&A
- Analytics
- EPM
- Data Integration
- MCP
- SCIM
website: https://www.pigment.com/
---
