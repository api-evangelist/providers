---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: unknown
    idempotency: verified
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 62.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 13
  human_in_the_loop: 2
  name: Craterview Ai Agentic Access
  operation_count: 24
  slug: craterview-ai-agentic-access
  summary_line: 24 operations · 13 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.craterview.ai
  baseurl_source: declared
  description: What you have told us about your account.
  name: craterview-ai Account API
  slug: craterview-ai-account-api
- baseURL: https://api.craterview.ai
  baseurl_source: declared
  description: The gallery API from craterview-ai — 3 operation(s) for gallery.
  name: craterview-ai Gallery API
  slug: craterview-ai-gallery-api
- baseURL: https://api.craterview.ai
  baseurl_source: declared
  description: Submit work and read results.
  name: craterview-ai Jobs API
  slug: craterview-ai-jobs-api
- baseURL: https://api.craterview.ai
  baseurl_source: declared
  description: The keys your account authenticates with.
  name: craterview-ai Keys API
  slug: craterview-ai-keys-api
- baseURL: https://api.craterview.ai
  baseurl_source: declared
  description: What is available and what it accepts.
  name: craterview-ai Models API
  slug: craterview-ai-models-api
- baseURL: https://api.craterview.ai
  baseurl_source: declared
  description: What this account has consumed, all time.
  name: craterview-ai Usage API
  slug: craterview-ai-usage-api
artifact_total: 23
asyncapis:
- description: ''
  name: Craterview Ai Webhooks
  slug: craterview-ai-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/craterview-ai/agentic-access/craterview-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/craterview-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/craterview-ai/plans/craterview-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/craterview-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/craterview-ai/rules/craterview-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/craterview-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/craterview-ai/json-ld/craterview-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/craterview-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/craterview-ai/vocabulary/craterview-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/craterview-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/craterview-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/craterview-ai/asyncapi/craterview-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/craterview-ai-webhooks.yml
- group: design
  href: https://artifacts.apis.io/craterview-ai/data-model/craterview-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/craterview-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/craterview-ai/conventions/craterview-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/craterview-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/craterview-ai/conventions/craterview-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/craterview-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/craterview-ai/authentication/craterview-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/craterview-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/craterview-ai/errors/craterview-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/craterview-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/craterview-ai/conformance/craterview-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/craterview-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/craterview-ai/llms/craterview-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/craterview-ai-llms.txt
- group: build
  href: https://artifacts.apis.io/craterview-ai/mcp/craterview-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/craterview-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/craterview-ai/mcp/craterview-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/craterview-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/craterview-ai/well-known/craterview-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/craterview-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/craterview-ai/hosts/craterview-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/craterview-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/craterview-ai/vendors/craterview-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/craterview-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/craterview-ai/packages/craterview-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/craterview-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/craterview-ai/packages/craterview-ai-packages.yml
  title: ''
  type: Packages
  url: packages/craterview-ai-packages.yml
- group: auth
  href: https://artifacts.apis.io/craterview-ai/security/craterview-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/craterview-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://craterview.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://craterview.ai/app
- group: docs
  title: ''
  type: Documentation
  url: https://craterview.ai/guides
- group: docs
  title: ''
  type: APIReference
  url: https://craterview.ai/#how
- group: start
  title: ''
  type: GettingStarted
  url: https://craterview.ai/guides/your-first-api-call
- group: operate
  title: ''
  type: Support
  url: mailto:sales@craterview.ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/craterviewai
- group: commercial
  title: ''
  type: Pricing
  url: https://craterview.ai/#pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://craterview.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://craterview.ai/privacy
created: '2026-10-30'
description: CraterView.ai provides an image restoration and upscaling service accessible via a simple HTTP API and a web interface. Users can denoise, enlarge, and restore photographs directly in the browser or programmatically through API calls. The platform offers a range of models for content checking, denoising, enhancement, face restoration, and more. No signup is required to start, and a free tier is available. Documentation includes guides for first API call, connecting assistants via MCP, and installing agent skills. The service is operated by CraterView Vision Technologies Inc., and the API keys are managed within the web app.
image: https://craterview.ai/static/mark-180.png
json_schemas:
- name: JobResponse
  property_count: 17
  slug: craterview-ai-job-response
- name: JobSubmission
  property_count: 6
  slug: craterview-ai-job-submission
- name: KeyInfo
  property_count: 7
  slug: craterview-ai-key-info
- name: ModelInfo
  property_count: 27
  slug: craterview-ai-model-info
- name: PostResponse
  property_count: 9
  slug: craterview-ai-post-response
- name: UsageResponse
  property_count: 14
  slug: craterview-ai-usage-response
jsonld:
- class_count: 30
  name: Craterview Ai Context
  property_count: 101
  slug: craterview-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.craterview.ai requiring OAuth.
  name: craterview-ai MCP Server
  slug: craterview-ai-mcp-yml
modified: '2026-10-30'
name: craterview-ai
nav: Providers
network: true
overview: 'craterview-ai publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Gallery API, Jobs API, and 3 more. Tagged areas include ImageProcessing, AI, PhotoRestoration, Upscaling, and API.


  The craterview-ai catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  craterview-ai''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, and 26 more developer resources.'
plans:
- name: Craterview Ai Plans Pricing
  plan_count: 4
  slug: craterview-ai-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Craterview Ai Rate Limits
  slug: craterview-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: craterview-ai API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: craterview-ai-rules
scopes:
- name: Craterview Ai Scopes
  scope_count: 0
  slug: craterview-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 62.8
  coverage:
    artifact_dirs: 27
    catalog_earned: 88.5
    catalog_earned_first_party: 0.0
    catalog_gap: 26.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.0
    contract_governance: 79.1
    contract_quality: 67.9
    developer_ergonomics: 68.3
    discoverability: 65.0
    operational_transparency: 13.2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Craterview Ai Authentication
  slug: craterview-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Craterview Ai Domain Security
  slug: craterview-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: crater-view-image-enhancement
  slug: craterview-ai-image-enhancement
slug: craterview-ai
tags:
- ImageProcessing
- AI
- PhotoRestoration
- Upscaling
- API
- Multimedia
website: https://craterview.ai/
---
