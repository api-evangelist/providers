---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
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
  score: 37.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Viewmax Studio Agentic Access
  operation_count: 11
  slug: viewmax-studio-agentic-access
  summary_line: 11 operations · 6 acting
api_count: 1
apis:
- baseURL: https://viewmax.studio
  baseurl_source: declared
  description: Credit balance for the authenticated key.
  name: ViewMax Studio Account API
  slug: viewmax-studio-account-api
- baseURL: https://viewmax.studio
  baseurl_source: declared
  description: Workflows whose inputs are created in the ViewMax web app.
  name: ViewMax Studio Advanced API
  slug: viewmax-studio-advanced-api
- baseURL: https://viewmax.studio
  baseurl_source: declared
  description: Public model and voice discovery.
  name: ViewMax Studio Catalog API
  slug: viewmax-studio-catalog-api
- baseURL: https://viewmax.studio
  baseurl_source: declared
  description: Create credit-consuming generation tasks.
  name: ViewMax Studio Generation API
  slug: viewmax-studio-generation-api
- baseURL: https://viewmax.studio
  baseurl_source: declared
  description: Poll generation tasks.
  name: ViewMax Studio Tasks API
  slug: viewmax-studio-tasks-api
artifact_total: 20
common:
- group: agent
  href: https://artifacts.apis.io/viewmax-studio/agentic-access/viewmax-studio-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/viewmax-studio-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/viewmax-studio/plans/viewmax-studio-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/viewmax-studio-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/viewmax-studio/rules/viewmax-studio-rules.yml
  title: ''
  type: Spectral
  url: rules/viewmax-studio-rules.yml
- group: design
  href: https://artifacts.apis.io/viewmax-studio/json-ld/viewmax-studio-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/viewmax-studio-context.jsonld
- group: design
  href: https://artifacts.apis.io/viewmax-studio/vocabulary/viewmax-studio-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/viewmax-studio-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/viewmax-studio/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/viewmax-studio/data-model/viewmax-studio-data-model.yml
  title: ''
  type: DataModel
  url: data-model/viewmax-studio-data-model.yml
- group: design
  href: https://artifacts.apis.io/viewmax-studio/conventions/viewmax-studio-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/viewmax-studio-conventions.yml
- group: design
  href: https://artifacts.apis.io/viewmax-studio/conventions/viewmax-studio-conventions.yml
  title: ''
  type: Conventions
  url: conventions/viewmax-studio-conventions.yml
- group: auth
  href: https://artifacts.apis.io/viewmax-studio/security/viewmax-studio-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/viewmax-studio-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/viewmax-studio/authentication/viewmax-studio-authentication.yml
  title: ''
  type: Authentication
  url: authentication/viewmax-studio-authentication.yml
- group: design
  href: https://artifacts.apis.io/viewmax-studio/errors/viewmax-studio-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/viewmax-studio-problem-types.yml
- group: design
  href: https://artifacts.apis.io/viewmax-studio/conformance/viewmax-studio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/viewmax-studio-conformance.yml
- group: agent
  href: https://artifacts.apis.io/viewmax-studio/llms/viewmax-studio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/viewmax-studio-llms.txt
- group: auth
  href: https://artifacts.apis.io/viewmax-studio/well-known/viewmax-studio-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/viewmax-studio-security.txt
- group: agent
  href: https://artifacts.apis.io/viewmax-studio/well-known/viewmax-studio-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/viewmax-studio-well-known.yml
- group: other
  href: https://artifacts.apis.io/viewmax-studio/hosts/viewmax-studio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/viewmax-studio-hosts.yml
- group: other
  href: https://artifacts.apis.io/viewmax-studio/vendors/viewmax-studio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/viewmax-studio-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://viewmax.studio/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://viewmax.studio/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://viewmax.studio/pricing
- group: start
  title: ''
  type: DeveloperPortal
  url: https://viewmax.studio/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://viewmax.studio/en/docs/mcp
- group: docs
  title: ''
  type: APIReference
  url: https://viewmax.studio/docs/api
- group: auth
  href: https://artifacts.apis.io/viewmax-studio/scopes/viewmax-studio-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/viewmax-studio-scopes.yml
- group: auth
  href: https://artifacts.apis.io/viewmax-studio/security/viewmax-studio-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/viewmax-studio-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/viewmax-studio/security/viewmax-studio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/viewmax-studio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://viewmax.studio/
- group: docs
  title: ''
  type: Documentation
  url: https://viewmax.studio/mcp
created: '2026-11-03'
description: ViewMax Studio offers a free AI-powered video generation platform that creates scripts, voiceovers, captions, and viral video templates. Users can start without a credit card, receiving free credits on signup. The service aims to simplify video content creation for marketing, social media, and personal projects, leveraging artificial intelligence to streamline production and boost engagement.
image: https://viewmax.studio/preview.png
json_schemas:
- name: CreateImageRequest
  property_count: 5
  slug: viewmax-studio-create-image-request
- name: CreateMusicRequest
  property_count: 2
  slug: viewmax-studio-create-music-request
- name: CreateSpeechRequest
  property_count: 3
  slug: viewmax-studio-create-speech-request
- name: CreateVideoRequest
  property_count: 6
  slug: viewmax-studio-create-video-request
- name: ShortsStudioRequest
  property_count: 10
  slug: viewmax-studio-shorts-studio-request
- name: ShortsStudioTask
  property_count: 9
  slug: viewmax-studio-shorts-studio-task
jsonld:
- class_count: 18
  name: Viewmax Studio Context
  property_count: 78
  slug: viewmax-studio-context
layout: provider
modified: '2026-11-03'
name: ViewMax Studio
nav: Providers
network: true
overview: 'ViewMax Studio publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Advanced API, Catalog API, and 2 more. Tagged areas include Company, Artificial Intelligence, Video, Generation, and Marketing.


  The ViewMax Studio catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ViewMax Studio''s developer surface includes authentication, pricing, getting-started guide, API reference, documentation, and 24 more developer resources.'
plans:
- name: Viewmax Studio Plans Pricing
  plan_count: 5
  slug: viewmax-studio-plans-pricing
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 114
  extends:
  - spectral:oas
  name: ViewMax Studio API Rules
  rule_count: 73
  severity_counts:
    error: 70
    hint: 0
    info: 2
    warn: 1
  slug: viewmax-studio-rules
scopes:
- name: Viewmax Studio Scopes
  scope_count: 4
  slug: viewmax-studio-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 45.7
  coverage:
    artifact_dirs: 23
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 65.3
    developer_ergonomics: 32.7
    discoverability: 66.1
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 33.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Viewmax Studio Authentication
  slug: viewmax-studio-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Viewmax Studio Domain Security
  slug: viewmax-studio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Viewmax Studio Vulnerability Disclosure
  slug: viewmax-studio-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: viewmax-studio-create-and-poll-shorts-studio
  slug: viewmax-studio-create-and-poll-shorts-studio
slug: viewmax-studio
tags:
- Company
- Artificial Intelligence
- Video
- Generation
- Marketing
website: https://viewmax.studio/
---
