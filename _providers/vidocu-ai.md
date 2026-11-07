---
access_model:
  confidence: medium
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
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 49.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 196
  human_in_the_loop: 6
  name: Vidocu Ai Agentic Access
  operation_count: 320
  slug: vidocu-ai-agentic-access
  summary_line: 320 operations · 196 acting · 6 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.vidocu.ai
  baseurl_source: declared
  description: The AI Recorder API from vidocu-ai — 6 operation(s) for ai recorder.
  name: vidocu-ai AI Recorder API
  slug: vidocu-ai-ai-recorder-api
- baseURL: https://api.vidocu.ai
  baseurl_source: declared
  description: Defaults that keep generated output on-brand
  name: vidocu-ai Brand Kit API
  slug: vidocu-ai-brand-kit-api
- baseURL: https://api.vidocu.ai
  baseurl_source: declared
  description: Documents and videos turned into module-based courses
  name: vidocu-ai Courses API
  slug: vidocu-ai-courses-api
- baseURL: https://api.vidocu.ai
  baseurl_source: declared
  description: Locks, approvals and review comments
  name: vidocu-ai Governance API
  slug: vidocu-ai-governance-api
- baseURL: https://api.vidocu.ai
  baseurl_source: declared
  description: Async job status
  name: vidocu-ai Jobs API
  slug: vidocu-ai-jobs-api
- baseURL: https://api.vidocu.ai
  baseurl_source: declared
  description: The Knowledge Center API from vidocu-ai — 16 operation(s) for knowledge center.
  name: vidocu-ai Knowledge Center API
  slug: vidocu-ai-knowledge-center-api
- baseURL: https://api.vidocu.ai
  baseurl_source: declared
  description: Analyze, export, translate, narrate, document
  name: vidocu-ai Operations API
  slug: vidocu-ai-operations-api
- baseURL: https://api.vidocu.ai
  baseurl_source: declared
  description: Project folders
  name: vidocu-ai Projects API
  slug: vidocu-ai-projects-api
- baseURL: https://api.vidocu.ai
  baseurl_source: declared
  description: Static reference data
  name: vidocu-ai Reference API
  slug: vidocu-ai-reference-api
- baseURL: https://api.vidocu.ai
  baseurl_source: declared
  description: The Remix API from vidocu-ai — 9 operation(s) for remix.
  name: vidocu-ai Remix API
  slug: vidocu-ai-remix-api
- baseURL: https://api.vidocu.ai
  baseurl_source: declared
  description: The Studio API from vidocu-ai — 15 operation(s) for studio.
  name: vidocu-ai Studio API
  slug: vidocu-ai-studio-api
- baseURL: https://api.vidocu.ai
  baseurl_source: declared
  description: Standalone processing tools
  name: vidocu-ai Tools API
  slug: vidocu-ai-tools-api
- baseURL: https://api.vidocu.ai
  baseurl_source: declared
  description: The Training Modules API from vidocu-ai — 17 operation(s) for training modules.
  name: vidocu-ai Training Modules API
  slug: vidocu-ai-training-modules-api
- baseURL: https://api.vidocu.ai
  baseurl_source: declared
  description: Balance and limits
  name: vidocu-ai Usage API
  slug: vidocu-ai-usage-api
- baseURL: https://api.vidocu.ai
  baseurl_source: declared
  description: Create, list, update and delete videos
  name: vidocu-ai Videos API
  slug: vidocu-ai-videos-api
- baseURL: https://api.vidocu.ai
  baseurl_source: declared
  description: Event subscriptions
  name: vidocu-ai Webhooks API
  slug: vidocu-ai-webhooks-api
artifact_total: 26
common:
- group: agent
  href: https://artifacts.apis.io/vidocu-ai/agentic-access/vidocu-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/vidocu-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/vidocu-ai/plans/vidocu-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/vidocu-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/vidocu-ai/rules/vidocu-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/vidocu-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/vidocu-ai/json-ld/vidocu-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/vidocu-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/vidocu-ai/vocabulary/vidocu-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/vidocu-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/vidocu-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/vidocu-ai/data-model/vidocu-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/vidocu-ai-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.vidocu.ai/
- group: design
  href: https://artifacts.apis.io/vidocu-ai/errors/vidocu-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/vidocu-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/vidocu-ai/conformance/vidocu-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/vidocu-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/vidocu-ai/llms/vidocu-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vidocu-ai-llms.txt
- group: build
  href: https://artifacts.apis.io/vidocu-ai/mcp/vidocu-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/vidocu-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/vidocu-ai/mcp/vidocu-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/vidocu-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/vidocu-ai/well-known/vidocu-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/vidocu-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/vidocu-ai/hosts/vidocu-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vidocu-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/vidocu-ai/vendors/vidocu-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/vidocu-ai-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.vidocu.ai
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vidocu.ai/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://vidocu.ai/sign-in
- group: start
  title: ''
  type: DeveloperPortal
  url: https://vidocu.ai/developers
- group: auth
  href: https://artifacts.apis.io/vidocu-ai/scopes/vidocu-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/vidocu-ai-scopes.yml
- group: auth
  href: https://artifacts.apis.io/vidocu-ai/authentication/vidocu-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/vidocu-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/vidocu-ai/security/vidocu-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/vidocu-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/vidocu-ai/security/vidocu-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vidocu-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vidocu.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://vidocu.ai/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://vidocu.ai/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://vidocu.ai/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://vidocu.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://vidocu.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vidocu.ai/terms
created: '2026-10-31'
description: Vidocu AI is an AI-powered knowledge platform that transforms videos, PDFs, and slide decks into product videos, step‑by‑step Standard Operating Procedures (SOPs), help articles, and multilingual training material. It supports over 70 languages, offers a free plan with no credit‑card required, and provides tools for teams to create, manage, and share documentation efficiently.
image: https://vidocu.ai/og.png
jsonld:
- class_count: 1
  name: Vidocu Ai Context
  property_count: 1
  slug: vidocu-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.vidocu.ai.
  name: vidocu-ai MCP Server
  slug: vidocu-ai-mcp-yml
modified: '2026-10-31'
name: vidocu-ai
nav: Providers
network: true
overview: 'vidocu-ai publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including AI Recorder API, Brand Kit API, Courses API, and 13 more. Tagged areas include Artificial Intelligence, Video, Documentation, SOP, and Training.


  The vidocu-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  vidocu-ai''s developer surface includes support, authentication, documentation, API reference, getting-started guide, engineering blog, pricing, and 24 more developer resources.'
plans:
- name: Vidocu Ai Plans Pricing
  plan_count: 5
  slug: vidocu-ai-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: vidocu-ai API Rules
  rule_count: 18
  severity_counts:
    error: 16
    hint: 0
    info: 1
    warn: 1
  slug: vidocu-ai-rules
scopes:
- name: Vidocu Ai Scopes
  scope_count: 42
  slug: vidocu-ai-scopes
  summary_line: 42 scopes · authorizationCode
score:
  band: developing
  composite: 46.5
  coverage:
    artifact_dirs: 23
    catalog_earned: 59.8
    catalog_earned_first_party: 12.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.7
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 54.8
    developer_ergonomics: 41.0
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 57.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Vidocu Ai Authentication
  slug: vidocu-ai-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Vidocu Ai Domain Security
  slug: vidocu-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Vidocu Ai Trust Center
  slug: vidocu-ai-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
skill_count: 1
skills:
- name: upload-video
  slug: vidocu-ai-upload-video
slug: vidocu-ai
tags:
- Artificial Intelligence
- Video
- Documentation
- SOP
- Training
- Knowledge Base
website: https://vidocu.ai/
---
