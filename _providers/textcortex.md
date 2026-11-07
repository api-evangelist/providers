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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Textcortex Agentic Access
  operation_count: 5
  slug: textcortex-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.textcortex.com/v1
  baseurl_source: declared
  description: Read API credit balance for the current API key.
  name: Textcortex Balance API
  slug: textcortex-balance-api
- baseURL: https://api.textcortex.com/v1
  baseurl_source: declared
  description: Generate chat completions with TextCortex models.
  name: Textcortex Chat Completions API
  slug: textcortex-chat-completions-api
- baseURL: https://api.textcortex.com/v1
  baseurl_source: declared
  description: Discover OpenAI-compatible TextCortex models.
  name: Textcortex Models API
  slug: textcortex-models-api
- baseURL: https://api.textcortex.com/v1
  baseurl_source: declared
  description: Generate responses with TextCortex models.
  name: Textcortex Responses API
  slug: textcortex-responses-api
artifact_total: 17
collections:
- collection_type: open
  name: TextCortex Balance API
  slug: open-textcortex-balance-api
- collection_type: open
  name: TextCortex Balance Chat Completions API
  slug: open-textcortex-chat-completions-api
- collection_type: open
  name: TextCortex Balance Models API
  slug: open-textcortex-models-api
- collection_type: open
  name: TextCortex Balance Responses API
  slug: open-textcortex-responses-api
common:
- group: commercial
  href: https://artifacts.apis.io/textcortex/plans/textcortex-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/textcortex-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://textcortex.com/blog
- group: other
  href: https://artifacts.apis.io/textcortex/capabilities/textcortex-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/textcortex-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.textcortex.com/
- group: auth
  href: https://artifacts.apis.io/textcortex/security/textcortex-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/textcortex-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/textcortex/agentic-access/textcortex-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/textcortex-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/textcortex/authentication/textcortex-authentication.yml
  title: ''
  type: Authentication
  url: authentication/textcortex-authentication.yml
- group: build
  href: https://artifacts.apis.io/textcortex/packages/textcortex-packages.yml
  title: ''
  type: Packages
  url: packages/textcortex-packages.yml
- group: build
  href: https://artifacts.apis.io/textcortex/packages/textcortex-packages.yml
  title: ''
  type: SDKs
  url: packages/textcortex-packages.yml
- group: agent
  href: https://artifacts.apis.io/textcortex/well-known/textcortex-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/textcortex-well-known.yml
- group: agent
  href: https://artifacts.apis.io/textcortex/mcp/textcortex-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/textcortex-mcp.yml
- group: agent
  href: https://artifacts.apis.io/textcortex/llms/textcortex-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/textcortex-llms.txt
- group: other
  href: https://artifacts.apis.io/textcortex/overlays/textcortex-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/textcortex-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/textcortex/conformance/textcortex-conformance.yml
  title: ''
  type: Conformance
  url: conformance/textcortex-conformance.yml
- group: design
  href: https://artifacts.apis.io/textcortex/errors/textcortex-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/textcortex-problem-types.yml
- group: design
  href: https://artifacts.apis.io/textcortex/lifecycle/textcortex-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/textcortex-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.textcortex.com/
- group: design
  href: https://artifacts.apis.io/textcortex/conventions/textcortex-conventions.yml
  title: ''
  type: Conventions
  url: conventions/textcortex-conventions.yml
- group: design
  href: https://artifacts.apis.io/textcortex/data-model/textcortex-data-model.yml
  title: ''
  type: DataModel
  url: data-model/textcortex-data-model.yml
- group: agent
  href: https://artifacts.apis.io/textcortex/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.textcortex.com/
- group: operate
  title: ''
  type: Support
  url: https://help.textcortex.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/textcortex
- group: commercial
  title: ''
  type: Pricing
  url: https://textcortex.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://textcortex.com/terms-of-services
- group: start
  title: ''
  type: SignUp
  url: https://app.textcortex.com/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/textcortex/textcortex-text-generation-api/overview
created: '2026-07-17'
description: TextCortex is a Berlin-based AI writing and content-generation platform (ZenoChat assistant, knowledge bases, and a suite of writing tools) that also ships a public, OpenAI-compatible REST API. The API, served from https://api.textcortex.com/v1 with Bearer API-key authentication, exposes model discovery, chat completions, and an OpenAI Responses-compatible generation endpoint, plus an API-credit balance check. Streaming is supported over server-sent events and infrastructure is EU-hosted and GDPR-compliant. TextCortex is backed by Speedinvest and maintains first-party Python and JavaScript client libraries.
finops:
- has_sources: true
  method: derived
  name: Textcortex Finops
  primary_unit: user
  service_category: ''
  slug: textcortex-finops
  template: false
image: https://docs.textcortex.com/logo192.png
layout: provider
modified: '2026-10-06'
name: Textcortex
nav: Providers
network: true
overview: 'Textcortex publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Balance API, Chat Completions API, Models API, and 1 more. Tagged areas include Company, Artificial Intelligence, Text Generation, LLM, and Chat Completions.


  The Textcortex catalog on APIs.io includes 1 Spectral governance ruleset.


  Textcortex''s developer surface includes engineering blog, authentication, support, pricing, signup flow, and 22 more developer resources.'
plans:
- name: Textcortex Plans Pricing
  plan_count: 3
  slug: textcortex-plans-pricing
- name: Textcortex Price Estimates
  plan_count: 0
  slug: textcortex-price-estimates
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Textcortex API Rules
  rule_count: 56
  severity_counts:
    error: 54
    hint: 0
    info: 1
    warn: 1
  slug: textcortex-rules
score:
  band: developing
  composite: 43.7
  coverage:
    artifact_dirs: 27
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 51.1
    developer_ergonomics: 42.3
    discoverability: 73.2
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 43.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/textcortex/textcortex-2026-08-17T082329.png
security:
- kind: authentication
  name: Textcortex Authentication
  slug: textcortex-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Textcortex Domain Security
  slug: textcortex-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 2
skills:
- name: Generate a chat completion with TextCortex
  slug: textcortex-generate-chat-completion
- name: Generate text with the TextCortex Responses API
  slug: textcortex-generate-response
slug: textcortex
tags:
- Company
- Artificial Intelligence
- Text Generation
- LLM
- Chat Completions
- OpenAI-Compatible
- Content Generation
- Developer Tools
- Foundation Models
website: https://www.textcortex.com/
---
