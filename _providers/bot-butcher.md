---
access_model:
  confidence: high
  label: Usage-based · Self-serve signup · First 10 requests each month free
  onboarding: self-serve
  pricing: unknown
  public: true
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Bot Butcher Agentic Access
  operation_count: 2
  slug: bot-butcher-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.botbutcher.com
  baseurl_source: declared
  description: Submit contact form data to Bot Butcher and receive a JSON classification result indicating whether the message is spam or legitimate. The AI model classifies each message within the context of your s
  name: Bot Butcher Classification API
  slug: bot-butcher-classification-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bot Butcher Classification API
  slug: open-bot-butcher-classification-api
- collection_type: open
  name: Bot Butcher Classification API
  slug: open-bot-butcher
common:
- group: company
  title: ''
  type: Website
  url: https://botbutcher.com/
- group: docs
  title: ''
  type: Documentation
  url: https://botbutcher.com/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://botbutcher.com/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://botbutcher.com/get-started
- group: start
  title: ''
  type: SignUp
  url: https://botbutcher.com/get-started
- group: start
  title: ''
  type: Login
  url: https://botbutcher.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://botbutcher.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://botbutcher.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://botbutcher.com/privacy
- group: build
  title: ''
  type: Postman
  url: https://god.postman.co/run-collection/24192121-47f4e172-5026-4788-b752-cbbc5488a03e
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bot-butcher-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bot-butcher-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bot-butcher-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bot-butcher-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bot-butcher-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bot-butcher-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bot-butcher-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bot-butcher-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/bot-butcher-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bot-butcher-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bot-butcher-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2025-01-07'
description: Bot Butcher is an AI-powered spam detection API that uses a fine-tuned large language model to classify contact form submissions as spam or legitimate messages. The service analyzes messages within the context of what each website is about, providing context-aware classification with 99% reported accuracy against the provider's own human-graded benchmark. It supports multi-tenant architectures and is designed for enterprise scalability across vertical SaaS and website builder platforms. The API has two operations — classify a message, retrieve a message by id — authenticated with a per-form x-api-key header, and is sold on a single usage-based plan whose first ten requests each month are free. Bot Butcher is operated by Hillside Lab Inc, a Delaware corporation based in Pasadena, California.
finops:
- name: Bot Butcher Finops
  service_category: API
  slug: bot-butcher-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bot-butcher.png
layout: provider
modified: '2026-09-04'
name: Bot Butcher
nav: Providers
network: true
overview: 'Bot Butcher publishes 1 API on the [APIs.io](https://apis.io/) network: Classification API. Tagged areas include Bots, Spam Detection, Contact Forms, AI Classification, and Security.


  Bot Butcher''s developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, authentication, and 16 more developer resources.'
plans:
- name: Bot Butcher Plans Pricing
  plan_count: 1
  slug: bot-butcher-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Bot Butcher Rate Limits
  slug: bot-butcher-rate-limits
score:
  band: thin
  composite: 36.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 18.2
    contract_quality: 15.0
    developer_ergonomics: 47.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 36.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bot-butcher/refs/heads/main/screenshots/bot-butcher-2026-06-20T173615.png
security:
- kind: authentication
  name: Bot Butcher Authentication
  slug: bot-butcher-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bot Butcher Domain Security
  slug: bot-butcher-domain-security
  summary_line: TLSv1.3
slug: bot-butcher
tags:
- Bots
- Spam Detection
- Contact Forms
- AI Classification
- Security
website: https://botbutcher.com/
---
