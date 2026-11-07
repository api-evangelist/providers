---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: templated
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Pigment Agentic Access
  operation_count: 19
  slug: pigment-agentic-access
  summary_line: 19 operations · 11 acting
api_count: 1
apis:
- baseURL: https://pigment.app/api
  baseurl_source: declared
  description: The BlocksApi API from Pigment — 1 operation(s) for blocksapi.
  name: Pigment BlocksApi API
  slug: pigment-blocksapi-api
- baseURL: https://pigment.app/api
  baseurl_source: declared
  description: The Export API from Pigment — 4 operation(s) for export.
  name: Pigment Export API
  slug: pigment-export-api
- baseURL: https://pigment.app/api
  baseurl_source: declared
  description: The ExportV1 API from Pigment — 4 operation(s) for exportv1.
  name: Pigment ExportV1 API
  slug: pigment-exportv1-api
- baseURL: https://pigment.app/api
  baseurl_source: declared
  description: The ImportConfigurationApi API from Pigment — 1 operation(s) for importconfigurationapi.
  name: Pigment ImportConfigurationApi API
  slug: pigment-importconfigurationapi-api
- baseURL: https://pigment.app/api
  baseurl_source: declared
  description: The ImportV1 API from Pigment — 4 operation(s) for importv1.
  name: Pigment ImportV1 API
  slug: pigment-importv1-api
- baseURL: https://pigment.app/api
  baseurl_source: declared
  description: The ViewApi API from Pigment — 1 operation(s) for viewapi.
  name: Pigment ViewApi API
  slug: pigment-viewapi-api
- baseURL: https://pigment.app/api
  baseurl_source: declared
  description: The Application API API from Pigment — 1 operation(s) for application api.
  name: Pigment Application API
  slug: pigment-application-api-api
- baseURL: https://pigment.app/api
  baseurl_source: declared
  description: The Import API API from Pigment — 3 operation(s) for import api.
  name: Pigment Import API
  slug: pigment-import-api-api
artifact_total: 34
collections:
- collection_type: open
  name: Pigment External ApplicationApi API
  slug: open-pigment-applicationapi-api
- collection_type: open
  name: Pigment External ApplicationApi BlocksApi API
  slug: open-pigment-blocksapi-api
- collection_type: open
  name: Pigment External ApplicationApi Export API
  slug: open-pigment-export-api
- collection_type: open
  name: Pigment External ApplicationApi ExportV1 API
  slug: open-pigment-exportv1-api
- collection_type: open
  name: Pigment External ApplicationApi ImportApi API
  slug: open-pigment-importapi-api
- collection_type: open
  name: Pigment External ApplicationApi ImportConfigurationApi API
  slug: open-pigment-importconfigurationapi-api
- collection_type: open
  name: Pigment External ApplicationApi ImportV1 API
  slug: open-pigment-importv1-api
- collection_type: open
  name: Pigment External ApplicationApi ViewApi API
  slug: open-pigment-viewapi-api
common:
- group: other
  href: https://artifacts.apis.io/pigment/overlays/pigment-external-api-overlay.yaml
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
  href: https://artifacts.apis.io/pigment/authentication/pigment-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pigment-authentication.yml
- group: operate
  href: https://artifacts.apis.io/pigment/rate-limits/pigment-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/pigment-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/pigment/errors/pigment-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/pigment-problem-types.yml
- group: design
  href: https://artifacts.apis.io/pigment/conventions/pigment-conventions.yml
  title: ''
  type: Conventions
  url: conventions/pigment-conventions.yml
- group: design
  href: https://artifacts.apis.io/pigment/lifecycle/pigment-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/pigment-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/pigment/data-model/pigment-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pigment-data-model.yml
- group: design
  href: https://artifacts.apis.io/pigment/conformance/pigment-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pigment-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.pigment.com/security
- group: agent
  href: https://artifacts.apis.io/pigment/mcp/pigment-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/pigment-mcp.yml
- group: agent
  href: https://artifacts.apis.io/pigment/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/pigment/llms/pigment-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pigment-llms.txt
- group: agent
  href: https://artifacts.apis.io/pigment/well-known/pigment-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pigment-well-known.yml
- group: auth
  href: https://artifacts.apis.io/pigment/well-known/pigment-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pigment-security.txt
- group: agent
  href: https://artifacts.apis.io/pigment/agentic-access/pigment-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/pigment-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/pigment/security/pigment-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/pigment-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/pigment/security/pigment-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/pigment-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.pigment.com/vdp
- group: auth
  href: https://artifacts.apis.io/pigment/security/pigment-domain-security.yml
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
- description: Remote MCP server at pigment.app over HTTP.
  name: Pigment MCP Server
  slug: pigment
modified: '2026-07-20'
name: Pigment
nav: Providers
network: true
overview: 'Pigment publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including BlocksApi API, Export API, ExportV1 API, and 5 more. Tagged areas include Company, Enterprise Software, Business Planning, Financial Planning, and FP&A.


  The Pigment catalog on APIs.io includes 1 Spectral governance ruleset.


  Pigment''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 24 more developer resources.'
random_paper: 12
rate_limits:
- limit_count: 1
  name: Pigment Rate Limits
  slug: pigment-rate-limits
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: Pigment API Rules
  rule_count: 49
  severity_counts:
    error: 46
    hint: 0
    info: 1
    warn: 2
  slug: pigment-rules
score:
  band: developing
  composite: 50.4
  coverage:
    artifact_dirs: 23
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    contract_governance: 31.8
    contract_quality: 43.8
    developer_ergonomics: 66.7
    discoverability: 68.3
    operational_transparency: 34.2
  previous_composite: 50.4
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
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/pigment/pigment-2026-08-17T081227.png
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
skill_count: 10
skills:
- name: analyzing-pigment-data
  slug: pigment-analyzing-pigment-data
- name: designing-boards
  slug: pigment-designing-boards
- name: designing-views
  slug: pigment-designing-views
- name: formatting-and-highlighting
  slug: pigment-formatting-and-highlighting
- name: integrating-external-data
  slug: pigment-integrating-external-data
- name: modeling-pigment-applications
  slug: pigment-modeling-pigment-applications
- name: optimizing-pigment-performance
  slug: pigment-optimizing-pigment-performance
- name: planning-cycles-pigment-applications
  slug: pigment-planning-cycles-pigment-applications
- name: securing-pigment-applications
  slug: pigment-securing-pigment-applications
- name: solving-specific-use-cases
  slug: pigment-solving-specific-use-cases
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
- Data Platform
- Visualization
- Collaboration
website: https://www.pigment.com/
---
