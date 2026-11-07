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
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 50.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Audiomap Ai Agentic Access
  operation_count: 18
  slug: audiomap-ai-agentic-access
  summary_line: 18 operations · 9 acting
api_count: 1
apis:
- baseURL: https://api.audiomap.ai
  baseurl_source: declared
  description: Ask questions over one note or the whole library
  name: AudioMap Ask API
  slug: audiomap-ai-ask-api
- baseURL: https://api.audiomap.ai
  baseurl_source: declared
  description: Transcript, analysis and outline of a note
  name: AudioMap Content API
  slug: audiomap-ai-content-api
- baseURL: https://api.audiomap.ai
  baseurl_source: declared
  description: Generate emails, documents and slide decks from a note
  name: AudioMap Deliverables API
  slug: audiomap-ai-deliverables-api
- baseURL: https://api.audiomap.ai
  baseurl_source: declared
  description: Create and browse notes
  name: AudioMap Notes API
  slug: audiomap-ai-notes-api
artifact_total: 20
common:
- group: operate
  title: ''
  type: StatusPage
  url: https://audiomap.ai/es/status
- group: agent
  href: https://artifacts.apis.io/audiomap-ai/agentic-access/audiomap-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/audiomap-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/audiomap-ai/plans/audiomap-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/audiomap-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/audiomap-ai/rules/audiomap-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/audiomap-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/audiomap-ai/json-ld/audiomap-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/audiomap-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/audiomap-ai/vocabulary/audiomap-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/audiomap-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/audiomap-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/audiomap-ai/data-model/audiomap-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/audiomap-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/audiomap-ai/conventions/audiomap-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/audiomap-ai-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://audiomap.ai/es/trust
- group: auth
  href: https://artifacts.apis.io/audiomap-ai/authentication/audiomap-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/audiomap-ai-authentication.yml
- group: operate
  href: https://artifacts.apis.io/audiomap-ai/lifecycle/audiomap-ai-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/audiomap-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/audiomap-ai/lifecycle/audiomap-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/audiomap-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/audiomap-ai/errors/audiomap-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/audiomap-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/audiomap-ai/conformance/audiomap-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/audiomap-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/audiomap-ai/llms/audiomap-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/audiomap-ai-llms.txt
- group: build
  href: https://artifacts.apis.io/audiomap-ai/mcp/audiomap-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/audiomap-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/audiomap-ai/mcp/audiomap-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/audiomap-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/audiomap-ai/well-known/audiomap-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/audiomap-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/audiomap-ai/hosts/audiomap-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/audiomap-ai-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://audiomap.ai/es/security
- group: company
  title: ''
  type: Newsroom
  url: https://audiomap.ai/es/press
- group: start
  title: ''
  type: GettingStarted
  url: https://audiomap.ai/es/docs/mcp-setup
- group: auth
  href: https://artifacts.apis.io/audiomap-ai/security/audiomap-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/audiomap-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/audiomap-ai/security/audiomap-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/audiomap-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://audiomap.ai/
- group: company
  title: ''
  type: Blog
  url: https://audiomap.ai/es/blog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://audiomap.ai/es/developers
- group: docs
  title: ''
  type: Documentation
  url: https://api.audiomap.ai/docs
- group: operate
  title: ''
  type: Support
  url: https://audiomap.ai/es/support
- group: commercial
  title: ''
  type: Pricing
  url: https://audiomap.ai/es/pricing
- group: start
  title: ''
  type: SignUp
  url: https://audiomap.ai/es/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://audiomap.ai/es/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://audiomap.ai/es/privacy
- group: operate
  title: ''
  type: Roadmap
  url: https://audiomap.ai/es/roadmap
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/audiomap
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.audiomap.ai/v1/openapi.json
  - status: 401
    url: https://api.audiomap.ai/mcp
  - status: 401
    url: https://mcp.audiomap.ai/mcp
  - status: 200
    url: https://audiomap.ai/
  reason: partner-login
  state: gated
created: '2026-11-02'
description: AudioMap provides AI-powered transcription and note-taking services for meetings, webinars and audio/video content, focusing on Spanish and English. Hosted on European servers, it ensures data residency within the EU and complies with privacy regulations. Users can generate summaries, action items, and structured deliverables such as minutes, emails and slide decks. Free tier offers 300 minutes per month; paid plans scale for higher usage.
image: https://audiomap.ai/es/opengraph-image-1ptsfv?d3c7f1c2dd6673ca
json_schemas:
- name: CreateNoteRequest
  property_count: 7
  slug: audiomap-ai-create-note-request
- name: CreateNoteResponse
  property_count: 5
  slug: audiomap-ai-create-note-response
- name: GlobalAnswer
  property_count: 5
  slug: audiomap-ai-global-answer
- name: NoteDetail
  property_count: 18
  slug: audiomap-ai-note-detail
- name: SpeakerList
  property_count: 2
  slug: audiomap-ai-speaker-list
- name: Transcript
  property_count: 9
  slug: audiomap-ai-transcript
jsonld:
- class_count: 16
  name: Audiomap Ai Context
  property_count: 72
  slug: audiomap-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.audiomap.ai requiring OAuth.
  name: AudioMap MCP Server
  slug: audiomap-ai-mcp-yml
modified: '2026-11-02'
name: AudioMap
nav: Providers
network: true
overview: 'AudioMap publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Ask API, Content API, Deliverables API, and 1 more. Tagged areas include Company, Artificial Intelligence, Transcription, Audio, and Meeting Notes.


  The AudioMap catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AudioMap''s developer surface includes authentication, getting-started guide, engineering blog, documentation, support, pricing, signup flow, and 29 more developer resources.'
plans:
- name: Audiomap Ai Plans Pricing
  plan_count: 5
  slug: audiomap-ai-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: AudioMap API Rules
  rule_count: 60
  severity_counts:
    error: 53
    hint: 0
    info: 4
    warn: 3
  slug: audiomap-ai-rules
scopes:
- name: Audiomap Ai Scopes
  scope_count: 0
  slug: audiomap-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 51.3
  coverage:
    artifact_dirs: 27
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.4
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 62.9
    developer_ergonomics: 37.4
    discoverability: 65.8
    operational_transparency: 26.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 63.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
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
  name: Audiomap Ai Authentication
  slug: audiomap-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Audiomap Ai Domain Security
  slug: audiomap-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Audiomap Ai Trust Center
  slug: audiomap-ai-trust-center
  summary_line: SOC 2, HIPAA, GDPR
skill_count: 1
skills:
- name: transcribe-audio
  slug: audiomap-ai-transcribe
slug: audiomap-ai
tags:
- Company
- Artificial Intelligence
- Transcription
- Audio
- Meeting Notes
- Europe
website: https://audiomap.ai/
---
