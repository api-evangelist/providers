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
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 55.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 36
  human_in_the_loop: 0
  name: Deapi Ai Agentic Access
  operation_count: 39
  slug: deapi-ai-agentic-access
  summary_line: 39 operations · 36 acting
api_count: 2
apis:
- baseURL: https://api.deapi.ai
  baseurl_source: declared
  description: Endpoints for client operations
  name: deapi-ai Client API
  slug: deapi-ai-client-api-api
- baseURL: https://api.deapi.ai
  baseurl_source: declared
  description: Current client endpoints (OpenAI-aligned noun-based paths)
  name: deapi-ai Client API v2 API
  slug: deapi-ai-client-api-v2-api
artifact_total: 19
asyncapis:
- description: ''
  name: Deapi Ai Webhooks
  slug: deapi-ai-webhooks
common:
- group: auth
  href: https://artifacts.apis.io/deapi-ai/well-known/deapi-ai-n8n-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/deapi-ai-n8n-security.txt
- group: agent
  href: https://artifacts.apis.io/deapi-ai/agentic-access/deapi-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/deapi-ai-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/deapi-ai/rate-limits/deapi-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/deapi-ai-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/deapi-ai/rules/deapi-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/deapi-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/deapi-ai/json-ld/deapi-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/deapi-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/deapi-ai/vocabulary/deapi-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/deapi-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/deapi-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/deapi-ai/asyncapi/deapi-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/deapi-ai-webhooks.yml
- group: design
  href: https://artifacts.apis.io/deapi-ai/data-model/deapi-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/deapi-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/deapi-ai/authentication/deapi-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/deapi-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/deapi-ai/errors/deapi-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/deapi-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/deapi-ai/conformance/deapi-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/deapi-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/deapi-ai/llms/deapi-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deapi-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/deapi-ai/a2a/deapi-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/deapi-ai-a2a.yml
- group: build
  href: https://artifacts.apis.io/deapi-ai/mcp/deapi-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/deapi-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/deapi-ai/mcp/deapi-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/deapi-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/deapi-ai/well-known/deapi-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/deapi-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/deapi-ai/hosts/deapi-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deapi-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/deapi-ai/vendors/deapi-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deapi-ai-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.deapi.ai
- group: start
  title: ''
  type: Sandbox
  url: https://deapi.ai/playground
- group: operate
  title: ''
  type: ChangeLog
  url: https://deapi.ai/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.deapi.ai/quickstart
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.deapi.ai</code
- group: auth
  href: https://artifacts.apis.io/deapi-ai/security/deapi-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deapi-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://deapi.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.deapi.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.deapi.ai/
- group: operate
  title: ''
  type: Support
  url: https://status.deapi.ai/
- group: company
  title: ''
  type: Blog
  url: https://deapi.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://deapi.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://deapi.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://deapi.ai/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://app.deapi.ai/register
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/deapi-ai
created: '2026-10-30'
description: deAPI provides a unified RESTful API that gives developers access to open-source generative AI models for image generation, text-to-speech, video transcription, and more. By routing requests through a decentralized GPU cloud, it offers fast, scalable inference at a fraction of typical costs. New users receive free credits, and pricing is usage‑based with transparent rates. The platform includes comprehensive documentation, SDKs, and a playground for quick experimentation.
image: https://deapi.ai/images/og/og-deapi.jpg
json_schemas:
- name: ClientDiffusionModelCollection
  property_count: 1
  slug: deapi-ai-client-diffusion-model-collection
- name: ClientInfoResource
  property_count: 1
  slug: deapi-ai-client-info-resource
- name: JobRequestResponseResource
  property_count: 1
  slug: deapi-ai-job-request-response-resource
- name: JobRequestStatusResource
  property_count: 1
  slug: deapi-ai-job-request-status-resource
jsonld:
- class_count: 26
  name: Deapi Ai Context
  property_count: 21
  slug: deapi-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.deapi.ai.
  name: deapi-ai MCP Server
  slug: deapi-ai-mcp-yml
modified: '2026-10-30'
name: deapi-ai
nav: Providers
network: true
overview: 'deapi-ai publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Client API and Client API v2 API. Tagged areas include Artificial Intelligence, Generative AI, Open Source, Image Generation, and Text-to-Speech.


  The deapi-ai catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  deapi-ai''s developer surface includes authentication, sandbox, changelog, getting-started guide, documentation, API reference, support, and 28 more developer resources.'
plans:
- name: Deapi Ai Plans Pricing
  plan_count: 0
  slug: deapi-ai-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 7
  name: Deapi Ai Rate Limits
  slug: deapi-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 109
  extends:
  - spectral:oas
  name: deapi-ai API Rules
  rule_count: 68
  severity_counts:
    error: 55
    hint: 0
    info: 4
    warn: 9
  slug: deapi-ai-rules
scopes:
- name: Deapi Ai Scopes
  scope_count: 0
  slug: deapi-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 52.5
  coverage:
    artifact_dirs: 37
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.6
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 78.1
    developer_ergonomics: 44.5
    discoverability: 65.0
    operational_transparency: 68.4
  previous_composite: 65.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/deapi-ai/deapi-ai-2026-11-03T130356.png
security:
- kind: authentication
  name: Deapi Ai Authentication
  slug: deapi-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Deapi Ai Domain Security
  slug: deapi-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: audio-to-video
  slug: audio-to-video
- name: audio-transcription
  slug: audio-transcription
- name: image-to-video
  slug: image-to-video
slug: deapi-ai
tags:
- Artificial Intelligence
- Generative AI
- Open Source
- Image Generation
- Text-to-Speech
- Video Transcription
website: https://deapi.ai/
---
