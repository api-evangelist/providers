---
access_model:
  confidence: high
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: AgentBuilders API provides endpoints for deploying AI agents, managing apps, storage, authentication, and usage metrics.
  name: AgentBuilders API
  slug: agentbuilders-api
- baseURL: https://api.agentbuilders.app
  baseurl_source: declared
  description: 'AgentBuilders API as documented publicly: 57 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: AgentBuilders API
  slug: agentbuilders-app-api
artifact_total: 16
common:
- group: operate
  href: https://artifacts.apis.io/agentbuilders-app/rate-limits/agentbuilders-app-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agentbuilders-app-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/agentbuilders-app/plans/agentbuilders-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentbuilders-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agentbuilders-app/rules/agentbuilders-app-rules.yml
  title: ''
  type: Spectral
  url: rules/agentbuilders-app-rules.yml
- group: design
  href: https://artifacts.apis.io/agentbuilders-app/json-ld/agentbuilders-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agentbuilders-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/agentbuilders-app/vocabulary/agentbuilders-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentbuilders-app-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agentbuilders-app/data-model/agentbuilders-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentbuilders-app-data-model.yml
- group: build
  href: https://artifacts.apis.io/agentbuilders-app/cli/agentbuilders-app-cli.yml
  title: ''
  type: CLI
  url: cli/agentbuilders-app-cli.yml
- group: auth
  href: https://artifacts.apis.io/agentbuilders-app/authentication/agentbuilders-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentbuilders-app-authentication.yml
- group: design
  href: https://artifacts.apis.io/agentbuilders-app/conformance/agentbuilders-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentbuilders-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentbuilders-app/mcp/agentbuilders-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentbuilders-app-mcp.yml
- group: auth
  href: https://artifacts.apis.io/agentbuilders-app/well-known/agentbuilders-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agentbuilders-app-security.txt
- group: auth
  href: https://artifacts.apis.io/agentbuilders-app/well-known/agentbuilders-app-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agentbuilders-app-docs-security.txt
- group: auth
  href: https://artifacts.apis.io/agentbuilders-app/well-known/agentbuilders-app-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agentbuilders-app-api-security.txt
- group: agent
  href: https://artifacts.apis.io/agentbuilders-app/well-known/agentbuilders-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentbuilders-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentbuilders-app/hosts/agentbuilders-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentbuilders-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentbuilders-app/vendors/agentbuilders-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentbuilders-app-vendors.yml
- group: build
  href: https://artifacts.apis.io/agentbuilders-app/packages/agentbuilders-app-packages.yml
  title: ''
  type: SDKs
  url: packages/agentbuilders-app-packages.yml
- group: build
  href: https://artifacts.apis.io/agentbuilders-app/packages/agentbuilders-app-packages.yml
  title: ''
  type: Packages
  url: packages/agentbuilders-app-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://agentbuilders.app/support
- group: auth
  title: ''
  type: Security
  url: https://agentbuilders.app/security/disclosure
- group: auth
  href: https://artifacts.apis.io/agentbuilders-app/security/agentbuilders-app-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agentbuilders-app-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agentbuilders-app/security/agentbuilders-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentbuilders-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentbuilders.app/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.agentbuilders.app/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.agentbuilders.app/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.agentbuilders.app/docs/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://agentbuilders.app/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentbuilders.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentbuilders.app/privacy
- group: other
  title: ''
  type: AcceptableUse
  url: https://agentbuilders.app/acceptable-use
coverage:
  checked: '2026-11-01'
  detail: Documentation site renders content via JavaScript, preventing automated retrieval of the OpenAPI spec.
  evidence:
  - status: 404
    url: https://docs.agentbuilders.app/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-31'
description: AgentBuilders provides a deployment platform for AI agents, enabling developers to deploy full-stack applications with database, authentication, storage, and access to 25 AI models via a single API call. The service automates infrastructure provisioning, offering features such as vector search, scheduled jobs, custom domains, email, and monitoring, targeting AI coding agents like Claude, Cursor, and Copilot.
image: https://agentbuilders.app/og-image.png
json_schemas:
- name: GetV1AppsMyAppWebsiteImportResponse
  property_count: 8
  slug: agentbuilders-app-get-v1-apps-my-app-website-import-response
- name: GetV1AppsNameWebsiteImportJobidResponse
  property_count: 8
  slug: agentbuilders-app-get-v1-apps-name-website-import-jobid-response
- name: PatchV1AiSettingsRequest
  property_count: 5
  slug: agentbuilders-app-patch-v1-ai-settings-request
- name: PostApiMediaIdTransformRequest
  property_count: 6
  slug: agentbuilders-app-post-api-media-id-transform-request
- name: PostV1DeployResponse
  property_count: 5
  slug: agentbuilders-app-post-v1-deploy-response
- name: PostV1MediaUploadUrlRequest
  property_count: 3
  slug: agentbuilders-app-post-v1-media-upload-url-request
jsonld:
- class_count: 40
  name: Agentbuilders App Context
  property_count: 73
  slug: agentbuilders-app-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.agentbuilders.app.
  name: AgentBuilders MCP Server
  slug: agentbuilders-app-mcp-yml
modified: '2026-10-31'
name: AgentBuilders
nav: Providers
network: true
overview: 'AgentBuilders is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Platform, Deployment, Agents, and Automation.


  The AgentBuilders catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AgentBuilders'' developer surface includes CLI, authentication, support, documentation, API reference, getting-started guide, pricing, and 23 more developer resources.'
plans:
- name: Agentbuilders App Plans Pricing
  plan_count: 7
  slug: agentbuilders-app-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 4
  name: Agentbuilders App Rate Limits
  slug: agentbuilders-app-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: AgentBuilders API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: agentbuilders-app-rules
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 81.8
    catalog_earned_first_party: 24.0
    catalog_gap: 33.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.7
  facets:
    access_clarity: 47.4
    contract_governance: 35.6
    contract_quality: 26.3
    developer_ergonomics: 42.9
    discoverability: 56.7
    operational_transparency: 36.8
  previous_composite: 48.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentbuilders App Authentication
  slug: agentbuilders-app-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Agentbuilders App Domain Security
  slug: agentbuilders-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Agentbuilders App Vulnerability Disclosure
  slug: agentbuilders-app-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: agentbuilders-app
tags:
- Artificial Intelligence
- Platform
- Deployment
- Agents
- Automation
- Company
website: https://agentbuilders.app/
---
