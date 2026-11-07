---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 50.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Autoshort Org Agentic Access
  operation_count: 22
  slug: autoshort-org-agentic-access
  summary_line: 22 operations · 10 acting
api_count: 1
apis:
- baseURL: https://autoshort.org
  baseurl_source: declared
  description: Credits, usage and plan.
  name: AutoShort Account API
  slug: autoshort-org-account-api
- baseURL: https://autoshort.org
  baseurl_source: declared
  description: Valid option values.
  name: AutoShort Catalog API
  slug: autoshort-org-catalog-api
- baseURL: https://autoshort.org
  baseurl_source: declared
  description: 'Director mode: agree the script before paying for a render.'
  name: AutoShort Drafts API
  slug: autoshort-org-drafts-api
- baseURL: https://autoshort.org
  baseurl_source: declared
  description: AI motion clips (only when enabled on the server).
  name: AutoShort Motion API
  slug: autoshort-org-motion-api
- baseURL: https://autoshort.org
  baseurl_source: declared
  description: 'No account: pay one video per call in USDC with x402 (only when enabled on the server).'
  name: AutoShort Pay per call (x402) API
  slug: autoshort-org-pay-per-call-x402-api
- baseURL: https://autoshort.org
  baseurl_source: declared
  description: How your own posted Shorts performed.
  name: AutoShort Series API
  slug: autoshort-org-series-api
- baseURL: https://autoshort.org
  baseurl_source: declared
  description: Create, read and delete videos.
  name: AutoShort Videos API
  slug: autoshort-org-videos-api
- baseURL: https://autoshort.org
  baseurl_source: declared
  description: Signed callbacks for video.completed / video.failed.
  name: AutoShort Webhooks API
  slug: autoshort-org-webhooks-api
artifact_total: 22
common:
- group: agent
  href: https://artifacts.apis.io/autoshort-org/agentic-access/autoshort-org-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/autoshort-org-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/autoshort-org/plans/autoshort-org-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/autoshort-org-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/autoshort-org/rules/autoshort-org-rules.yml
  title: ''
  type: Spectral
  url: rules/autoshort-org-rules.yml
- group: design
  href: https://artifacts.apis.io/autoshort-org/json-ld/autoshort-org-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/autoshort-org-context.jsonld
- group: design
  href: https://artifacts.apis.io/autoshort-org/vocabulary/autoshort-org-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/autoshort-org-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/autoshort-org/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/autoshort-org/data-model/autoshort-org-data-model.yml
  title: ''
  type: DataModel
  url: data-model/autoshort-org-data-model.yml
- group: design
  href: https://artifacts.apis.io/autoshort-org/conventions/autoshort-org-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/autoshort-org-conventions.yml
- group: design
  href: https://artifacts.apis.io/autoshort-org/conventions/autoshort-org-conventions.yml
  title: ''
  type: Conventions
  url: conventions/autoshort-org-conventions.yml
- group: auth
  href: https://artifacts.apis.io/autoshort-org/authentication/autoshort-org-authentication.yml
  title: ''
  type: Authentication
  url: authentication/autoshort-org-authentication.yml
- group: design
  href: https://artifacts.apis.io/autoshort-org/errors/autoshort-org-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/autoshort-org-problem-types.yml
- group: design
  href: https://artifacts.apis.io/autoshort-org/conformance/autoshort-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/autoshort-org-conformance.yml
- group: agent
  href: https://artifacts.apis.io/autoshort-org/llms/autoshort-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/autoshort-org-llms.txt
- group: build
  href: https://artifacts.apis.io/autoshort-org/mcp/autoshort-org-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/autoshort-org-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/autoshort-org/mcp/autoshort-org-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/autoshort-org-mcp.yml
- group: agent
  href: https://artifacts.apis.io/autoshort-org/well-known/autoshort-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/autoshort-org-well-known.yml
- group: other
  href: https://artifacts.apis.io/autoshort-org/hosts/autoshort-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/autoshort-org-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://autoshort.org/en/login
- group: start
  title: ''
  type: GettingStarted
  url: https://autoshort.org/en/dashboard/connect-ai
- group: docs
  title: ''
  type: APIReference
  url: https://autoshort.org/en/developers
- group: auth
  href: https://artifacts.apis.io/autoshort-org/security/autoshort-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autoshort-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://autoshort.org/
- group: commercial
  title: ''
  type: Pricing
  url: https://autoshort.org/en/pricing
- group: company
  title: ''
  type: Blog
  url: https://autoshort.org/en/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://autoshort.org/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://autoshort.org/en/privacy
- group: operate
  title: ''
  type: Support
  url: https://autoshort.org/en/support
created: '2026-11-02'
description: AutoShort enables creators to generate faceless AI Shorts for YouTube and TikTok without filming. It offers AI‑written scripts, voice‑over, captions and scene generation, posting automatically to YouTube. Users can start with a 3‑day trial for $5, then choose plans from $19/month, with the ability to cancel anytime.
image: https://autoshort.org/api/og?title=AutoShort%20%E2%80%94%20Make%20Faceless%20AI%20Shorts%20Without%20Filming&subtitle=Turn%20a%20niche%20into%20faceless%20Shorts%20that%20grow%20your%20channel%3A%20AI%20script%2C%20voiceover%2C%20captions%20and%20scenes%20in%20minutes.%20Posts%20to%20YouTube%20automatically.
json_schemas:
- name: CreateMotionClipRequest
  property_count: 7
  slug: autoshort-org-create-motion-clip-request
- name: CreateVideoRequest
  property_count: 9
  slug: autoshort-org-create-video-request
- name: DraftView
  property_count: 13
  slug: autoshort-org-draft-view
- name: UpdateDraftRequest
  property_count: 9
  slug: autoshort-org-update-draft-request
- name: VideoDetail
  property_count: 22
  slug: autoshort-org-video-detail
- name: X402VideoRequest
  property_count: 5
  slug: autoshort-org-x402-video-request
jsonld:
- class_count: 26
  name: Autoshort Org Context
  property_count: 115
  slug: autoshort-org-context
layout: provider
mcp_servers:
- description: Remote MCP server at autoshort.org.
  name: AutoShort MCP Server
  slug: autoshort-org-mcp-yml
modified: '2026-11-02'
name: AutoShort
nav: Providers
network: true
overview: 'AutoShort publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Catalog API, Drafts API, and 5 more. Tagged areas include Artificial Intelligence, Video Generation, YouTube Shorts, Automation, and Faceless Content.


  The AutoShort catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AutoShort''s developer surface includes authentication, getting-started guide, API reference, pricing, engineering blog, support, and 21 more developer resources.'
plans:
- name: Autoshort Org Plans Pricing
  plan_count: 8
  slug: autoshort-org-plans-pricing
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 109
  extends:
  - spectral:oas
  name: AutoShort API Rules
  rule_count: 68
  severity_counts:
    error: 58
    hint: 0
    info: 1
    warn: 9
  slug: autoshort-org-rules
score:
  band: developing
  composite: 42.8
  coverage:
    artifact_dirs: 25
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 65.5
    developer_ergonomics: 31.4
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 50.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Autoshort Org Authentication
  slug: autoshort-org-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Autoshort Org Domain Security
  slug: autoshort-org-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: generate-video
  slug: autoshort-org-generate-video
slug: autoshort-org
tags:
- Artificial Intelligence
- Video Generation
- YouTube Shorts
- Automation
- Faceless Content
website: https://autoshort.org/
---
