---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 56.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 51
  human_in_the_loop: 3
  name: Rendobar Com Agentic Access
  operation_count: 101
  slug: rendobar-com-agentic-access
  summary_line: 101 operations · 51 acting · 3 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.rendobar.com
  baseurl_source: declared
  description: Plan limits and enabled features for the authenticated account
  name: rendobar-com Account API
  slug: rendobar-com-account-api
- baseURL: https://api.rendobar.com
  baseurl_source: declared
  description: Create and manage API keys
  name: rendobar-com API Keys API
  slug: rendobar-com-api-keys-api
- baseURL: https://api.rendobar.com
  baseurl_source: declared
  description: Upload and manage PSD templates and design assets
  name: rendobar-com Assets API
  slug: rendobar-com-assets-api
- baseURL: https://api.rendobar.com
  baseurl_source: declared
  description: Check account balance and usage history
  name: rendobar-com Billing API
  slug: rendobar-com-billing-api
- baseURL: https://api.rendobar.com
  baseurl_source: declared
  description: 'Helpers for the compose job that render nothing: the effects reference, and validating params before submitting'
  name: rendobar-com Compose API
  slug: rendobar-com-compose-api
- baseURL: https://api.rendobar.com
  baseurl_source: declared
  description: Job creation and management (submit, list, get, cancel, download)
  name: rendobar-com Jobs API
  slug: rendobar-com-jobs-api
- baseURL: https://api.rendobar.com
  baseurl_source: declared
  description: Generation model catalog (image.generate / image.edit)
  name: rendobar-com Models API
  slug: rendobar-com-models-api
- baseURL: https://api.rendobar.com
  baseurl_source: declared
  description: Messages for the organization and each member's read state
  name: rendobar-com Notifications API
  slug: rendobar-com-notifications-api
- baseURL: https://api.rendobar.com
  baseurl_source: declared
  description: Manage organizations and their settings
  name: rendobar-com Organizations API
  slug: rendobar-com-organizations-api
- baseURL: https://api.rendobar.com
  baseurl_source: declared
  description: Create and manage public share links for job outputs
  name: rendobar-com Sharing API
  slug: rendobar-com-sharing-api
- baseURL: https://api.rendobar.com
  baseurl_source: declared
  description: Connect your own buckets, then read from them and deliver to them by id
  name: rendobar-com Storage API
  slug: rendobar-com-storage-api
- baseURL: https://api.rendobar.com
  baseurl_source: declared
  description: Invite, promote and remove organization members
  name: rendobar-com Team API
  slug: rendobar-com-team-api
- baseURL: https://api.rendobar.com
  baseurl_source: declared
  description: Tokenized upload sessions for clients without filesystem access
  name: rendobar-com Upload Sessions API
  slug: rendobar-com-upload-sessions-api
- baseURL: https://api.rendobar.com
  baseurl_source: declared
  description: Configure webhook endpoints and view delivery history
  name: rendobar-com Webhooks API
  slug: rendobar-com-webhooks-api
artifact_total: 27
common:
- group: agent
  href: https://artifacts.apis.io/rendobar-com/agentic-access/rendobar-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/rendobar-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/rendobar-com/rate-limits/rendobar-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/rendobar-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/rendobar-com/plans/rendobar-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/rendobar-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/rendobar-com/rules/rendobar-com-rules.yml
  title: ''
  type: Spectral
  url: rules/rendobar-com-rules.yml
- group: design
  href: https://artifacts.apis.io/rendobar-com/json-ld/rendobar-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/rendobar-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/rendobar-com/vocabulary/rendobar-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/rendobar-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/rendobar-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/rendobar-com/data-model/rendobar-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/rendobar-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/rendobar-com/cli/rendobar-com-cli.yml
  title: ''
  type: CLI
  url: cli/rendobar-com-cli.yml
- group: auth
  href: https://artifacts.apis.io/rendobar-com/authentication/rendobar-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rendobar-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/rendobar-com/scopes/rendobar-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/rendobar-com-scopes.yml
- group: design
  href: https://artifacts.apis.io/rendobar-com/errors/rendobar-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/rendobar-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/rendobar-com/conformance/rendobar-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rendobar-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/rendobar-com/llms/rendobar-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rendobar-com-llms.txt
- group: build
  href: https://artifacts.apis.io/rendobar-com/mcp/rendobar-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/rendobar-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/rendobar-com/mcp/rendobar-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/rendobar-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/rendobar-com/well-known/rendobar-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rendobar-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/rendobar-com/hosts/rendobar-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rendobar-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/rendobar-com/vendors/rendobar-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rendobar-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/rendobar-com/packages/rendobar-com-packages.yml
  title: ''
  type: SDKs
  url: packages/rendobar-com-packages.yml
- group: build
  href: https://artifacts.apis.io/rendobar-com/packages/rendobar-com-packages.yml
  title: ''
  type: Packages
  url: packages/rendobar-com-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://rendobar.com/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/rendobar-com/security/rendobar-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rendobar-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rendobar.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.rendobar.com
- group: docs
  title: ''
  type: Documentation
  url: https://rendobar.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.rendobar.com
- group: commercial
  title: ''
  type: Pricing
  url: https://rendobar.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://rendobar.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://rendobar.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rendobar
created: '2026-10-31'
description: Rendobar provides a serverless media processing and AI generation API that lets developers generate images, transcode and compose video, add burned‑in captions, watermark, compress, and apply AI‑driven transformations using a single FFmpeg‑based endpoint. It offers credit‑based billing with a free $5 signup credit, no credit‑card required, and supports MCP‑native integration for tool calling. The platform serves worldwide customers and emphasizes privacy‑friendly video redaction and QR‑code generation.
image: https://rendobar.com/brand/og-default.jpg
json_schemas:
- name: ConnectorField
  property_count: 16
  slug: rendobar-com-connector-field
- name: ConnectorInput
  property_count: 18
  slug: rendobar-com-connector-input
- name: GenModel
  property_count: 10
  slug: rendobar-com-gen-model
jsonld:
- class_count: 2
  name: Rendobar Com Context
  property_count: 27
  slug: rendobar-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.rendobar.com.
  name: rendobar-com MCP Server
  slug: rendobar-com-mcp-yml
modified: '2026-10-31'
name: rendobar-com
nav: Providers
network: true
overview: 'rendobar-com publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, API Keys API, Assets API, and 11 more. Tagged areas include Company, Video Processing, FFmpeg, Artificial Intelligence, and Serverless.


  The rendobar-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  rendobar-com''s developer surface includes CLI, authentication, getting-started guide, documentation, API reference, pricing, engineering blog, and 24 more developer resources.'
plans:
- name: Rendobar Com Plans Pricing
  plan_count: 3
  slug: rendobar-com-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 6
  name: Rendobar Com Rate Limits
  slug: rendobar-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: rendobar-com API Rules
  rule_count: 17
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 4
  slug: rendobar-com-rules
scopes:
- name: Rendobar Com Scopes
  scope_count: 14
  slug: rendobar-com-scopes
  summary_line: 14 scopes
score:
  band: developing
  composite: 50.6
  coverage:
    artifact_dirs: 33
    catalog_earned: 83.8
    catalog_earned_first_party: 24.0
    catalog_gap: 31.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 36.8
    contract_governance: 35.6
    contract_quality: 62.3
    developer_ergonomics: 55.2
    discoverability: 65.0
    operational_transparency: 34.2
  previous_composite: 56.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
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
screenshot: https://apis.io/screenshots/rendobar-com/rendobar-com-2026-11-03T142145.png
security:
- kind: authentication
  name: Rendobar Com Authentication
  slug: rendobar-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Rendobar Com Domain Security
  slug: rendobar-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 1
skills:
- name: rendobar-com-mcp-tools
  slug: rendobar-com-mcp-tools
slug: rendobar-com
tags:
- Company
- Video Processing
- FFmpeg
- Artificial Intelligence
- Serverless
- Media API
website: https://rendobar.com/
---
