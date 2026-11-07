---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
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
    agent_skills: derived
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 53.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Azurade Com Agentic Access
  operation_count: 11
  slug: azurade-com-agentic-access
  summary_line: 11 operations · 6 acting
api_count: 1
apis:
- baseURL: https://azurade.com
  baseurl_source: declared
  description: Who the credentials belong to, what the balance is, and a checkout link to buy more credits.
  name: Azurade AI Account API
  slug: azurade-com-account-api
- baseURL: https://azurade.com
  baseurl_source: declared
  description: Submit image and video jobs, price them before submitting, and poll them to completion.
  name: Azurade AI Generations API
  slug: azurade-com-generations-api
- baseURL: https://azurade.com
  baseurl_source: declared
  description: What can be generated, with the parameters and price of each model. Public.
  name: Azurade AI Models API
  slug: azurade-com-models-api
- baseURL: https://azurade.com
  baseurl_source: declared
  description: Rewrite a prompt for a model, or screen one against the content policy, without generating.
  name: Azurade AI Prompts API
  slug: azurade-com-prompts-api
- baseURL: https://azurade.com
  baseurl_source: declared
  description: Put an image, video or audio file on our storage so a generation can take it as input.
  name: Azurade AI Uploads API
  slug: azurade-com-uploads-api
artifact_total: 20
common:
- group: agent
  href: https://artifacts.apis.io/azurade-com/agentic-access/azurade-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/azurade-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/azurade-com/plans/azurade-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/azurade-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/azurade-com/rules/azurade-com-rules.yml
  title: ''
  type: Spectral
  url: rules/azurade-com-rules.yml
- group: design
  href: https://artifacts.apis.io/azurade-com/json-ld/azurade-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/azurade-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/azurade-com/vocabulary/azurade-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/azurade-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/azurade-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/azurade-com/data-model/azurade-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/azurade-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/azurade-com/changelog/azurade-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/azurade-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/azurade-com/errors/azurade-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/azurade-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/azurade-com/conformance/azurade-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/azurade-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/azurade-com/llms/azurade-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/azurade-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/azurade-com/mcp/azurade-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/azurade-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/azurade-com/well-known/azurade-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/azurade-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/azurade-com/hosts/azurade-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/azurade-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/azurade-com/vendors/azurade-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/azurade-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://azurade.com/security/
- group: docs
  title: ''
  type: APIReference
  url: https://azurade.com/swagger/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azurade
- group: auth
  href: https://artifacts.apis.io/azurade-com/security/azurade-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/azurade-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://azurade.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://azurade.com/mcp
- group: commercial
  title: ''
  type: Pricing
  url: https://azurade.com/prices/
- group: company
  title: ''
  type: Blog
  url: https://azurade.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://azurade.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://azurade.com/privacy-policy/
- group: start
  title: ''
  type: SignUp
  url: https://azurade.com/login/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://azurade.com/openapi.json
  - status: 401
    url: https://azurade.com/mcp
  - status: 200
    url: https://azurade.com/
  reason: partner-login
  state: gated
created: '2026-11-02'
description: Azurade AI is an online AI image and video generation platform that unifies 45 AI models into a single studio. Users can create images and videos from text prompts, purchase credits at per‑generation pricing, and manage their balance without subscription lock‑in. The service offers low‑cost models such as Nano Banana at $0.04 per image and premium video models at $0.80 per five‑second clip. Credits never expire, and the platform provides tools for social media content, product photography, virtual staging, and AI influencer creation. Support is available via email at support@azurade.com. Operated by Dubir Group LTD.
image: https://azurade.com/logo-mark.webp
json_schemas:
- name: CheckoutRequest
  property_count: 3
  slug: azurade-com-checkout-request
- name: Checkout
  property_count: 8
  slug: azurade-com-checkout
- name: EnhanceRequest
  property_count: 3
  slug: azurade-com-enhance-request
- name: GenerationRequest
  property_count: 64
  slug: azurade-com-generation-request
- name: Generation
  property_count: 11
  slug: azurade-com-generation
- name: Model
  property_count: 10
  slug: azurade-com-model
jsonld:
- class_count: 19
  name: Azurade Com Context
  property_count: 112
  slug: azurade-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at azurade.com.
  name: Azurade AI MCP Server
  slug: azurade-com-mcp-yml
modified: '2026-11-02'
name: Azurade AI
nav: Providers
network: true
overview: 'Azurade AI publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Generations API, Models API, and 2 more. Tagged areas include Artificial Intelligence, Image Generation, Video Generation, Platform, and Creative.


  The Azurade AI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Azurade AI''s developer surface includes changelog, API reference, pricing, engineering blog, signup flow, and 21 more developer resources.'
plans:
- name: Azurade Com Plans Pricing
  plan_count: 5
  slug: azurade-com-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: Azurade AI API Rules
  rule_count: 59
  severity_counts:
    error: 57
    hint: 0
    info: 1
    warn: 1
  slug: azurade-com-rules
scopes:
- name: Azurade Com Scopes
  scope_count: 0
  slug: azurade-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.2
  coverage:
    artifact_dirs: 31
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.9
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 65.4
    developer_ergonomics: 11.3
    discoverability: 65.0
    operational_transparency: 23.7
  previous_composite: 51.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
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
security:
- kind: authentication
  name: Azurade Com Authentication
  slug: azurade-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Azurade Com Domain Security
  slug: azurade-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 1
skills:
- name: azurade-com-generation
  slug: azurade-com-generation
slug: azurade-com
tags:
- Artificial Intelligence
- Image Generation
- Video Generation
- Platform
- Creative
website: https://azurade.com/
---
