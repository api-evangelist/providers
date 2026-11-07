---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: derived
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Detect AI-generated speech detection and speaker verification API.
  name: DetectifAI Developer API
  slug: detectifai-developer-api
- baseURL: https://platform.detectif.ai
  baseurl_source: declared
  description: The DetectifAI developer API detects synthetic (AI-generated) speech and verifies speakers by voice.
  name: DetectifAI Developer API API
  slug: detectifai-developer-api-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/detectif-ai/rules/detectif-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/detectif-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/detectif-ai/json-ld/detectif-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/detectif-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/detectif-ai/vocabulary/detectif-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/detectif-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/detectif-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/detectif-ai/data-model/detectif-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/detectif-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/detectif-ai/conventions/detectif-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/detectif-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/detectif-ai/conventions/detectif-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/detectif-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/detectif-ai/authentication/detectif-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/detectif-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/detectif-ai/errors/detectif-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/detectif-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/detectif-ai/conformance/detectif-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/detectif-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/detectif-ai/llms/detectif-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/detectif-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/detectif-ai/well-known/detectif-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/detectif-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/detectif-ai/hosts/detectif-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/detectif-ai-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://platform.detectif.ai/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://platform.detectif.ai/privacy/
- group: start
  title: ''
  type: Login
  url: https://platform.detectif.ai/login/
- group: company
  title: ''
  type: Blog
  url: https://detectif.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://platform.detectif.ai/docs/noesis/quickstart
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.noesis.detectif.ai`
- group: auth
  href: https://artifacts.apis.io/detectif-ai/security/detectif-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/detectif-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://detectif.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://detectif.ai/deepfake-detection
- group: docs
  title: ''
  type: APIReference
  url: https://detectif.ai/deepfake-detection
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://platform.detectif.ai/openapi.json
  - status: null
    url: https://api.noesis.detectif.ai/v1/openapi.json
  - status: 401
    url: https://platform.detectif.ai/mcp
  - status: 200
    url: https://detectif.ai/
  reason: partner-login
  state: gated
created: '2026-11-05'
description: Detectif.ai provides audio deepfake detection and speaker verification models for calls, recordings, and voice agents. Their solutions can be deployed in the cloud, a private VPC, on‑premises, or on‑device, targeting contact‑center fraud prevention, banking voice security, and synthetic voice detection use‑cases.
image: https://detectif.ai/social/detectif-ai-share.jpg
json_schemas:
- name: CreditsObject
  property_count: 7
  slug: detectif-ai-credits-object
- name: DeepfakeResponse
  property_count: 8
  slug: detectif-ai-deepfake-response
- name: EnrollResponse
  property_count: 9
  slug: detectif-ai-enroll-response
- name: OperationObject
  property_count: 13
  slug: detectif-ai-operation-object
- name: SpeakerObject
  property_count: 7
  slug: detectif-ai-speaker-object
- name: VerifyResponse
  property_count: 10
  slug: detectif-ai-verify-response
jsonld:
- class_count: 26
  name: Detectif Ai Context
  property_count: 64
  slug: detectif-ai-context
layout: provider
modified: '2026-11-05'
name: Detectif.ai
nav: Providers
network: true
overview: 'Detectif.ai publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including DetectifAI Developer API API, and 1 more. Tagged areas include Company, Artificial Intelligence, Voice, Deepfake, and Security.


  The Detectif.ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Detectif.ai''s developer surface includes authentication, engineering blog, getting-started guide, documentation, API reference, and 18 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 112
  extends:
  - spectral:oas
  name: Detectif.ai API Rules
  rule_count: 71
  severity_counts:
    error: 65
    hint: 0
    info: 2
    warn: 4
  slug: detectif-ai-rules
score:
  band: developing
  composite: 41.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 50.7
    developer_ergonomics: 58.8
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 21.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Detectif Ai Authentication
  slug: detectif-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Detectif Ai Domain Security
  slug: detectif-ai-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: detectif-ai
tags:
- Company
- Artificial Intelligence
- Voice
- Deepfake
- Security
- Audio
website: https://detectif.ai/
---
