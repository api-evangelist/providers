---
access_model:
  confidence: medium
  label: Contact sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://replyr.ai/
  - https://app.replyr.ai/en/login
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.3
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://app.replyr.ai/api
  baseurl_source: declared
  description: The Accounts API from Replyr.ai — 13 operation(s) for accounts.
  name: Replyr.ai Accounts API
  slug: replyrai-accounts-api
- baseURL: https://app.replyr.ai/api
  baseurl_source: declared
  description: The AI Agents API from Replyr.ai — 5 operation(s) for ai agents.
  name: Replyr.ai AI Agents API
  slug: replyrai-ai-agents-api
- baseURL: https://app.replyr.ai/api
  baseurl_source: declared
  description: The Appointment Management API from Replyr.ai — 2 operation(s) for appointment management.
  name: Replyr.ai Appointment Management API
  slug: replyrai-appointment-management-api
- baseURL: https://app.replyr.ai/api
  baseurl_source: declared
  description: The Contacts API from Replyr.ai — 12 operation(s) for contacts.
  name: Replyr.ai Contacts API
  slug: replyrai-contacts-api
- baseURL: https://app.replyr.ai/api
  baseurl_source: declared
  description: The Ecommerce API from Replyr.ai — 6 operation(s) for ecommerce.
  name: Replyr.ai Ecommerce API
  slug: replyrai-ecommerce-api
- baseURL: https://app.replyr.ai/api
  baseurl_source: declared
  description: The Pipelines API from Replyr.ai — 9 operation(s) for pipelines.
  name: Replyr.ai Pipelines API
  slug: replyrai-pipelines-api
- baseURL: https://app.replyr.ai/api
  baseurl_source: declared
  description: The Templates API from Replyr.ai — 1 operation(s) for templates.
  name: Replyr.ai Templates API
  slug: replyrai-templates-api
artifact_total: 11
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/replyrai-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://replyr.ai
- group: docs
  title: ''
  type: APIReference
  url: https://app.replyr.ai/api
- group: docs
  title: ''
  type: Documentation
  url: https://app.replyr.ai/api
- group: start
  title: ''
  type: Login
  url: https://app.replyr.ai/en/login
- group: operate
  title: ''
  type: Support
  url: https://wa.me/60109696912
- group: auth
  title: ''
  type: DomainSecurity
  url: security/replyrai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/replyrai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/replyrai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/replyrai-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/replyrai-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/replyrai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/replyrai-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/replyrai-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/replyrai-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/replyrai-platform-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/replyrai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/replyrai-rate-limits.yml
created: '2026-07-17'
description: Replyr.ai (Replyr Sdn Bhd, Kuala Lumpur, Malaysia) is an AI-powered customer engagement and patient-acquisition platform aimed at Malaysian clinics. It builds GPT-style chat assistants that reply instantly in multiple languages across WhatsApp, Instagram, Facebook Messenger and other chat channels to qualify leads, answer FAQs, recommend products and book appointments 24/7, and packages that with Meta and Google advertising campaigns and a BookAClinic discovery marketplace. The operator console at app.replyr.ai runs a white-labeled deployment of the ChatRace conversational-commerce platform and exposes a REST API of its own at https://app.replyr.ai/api, documented with a live Swagger UI and a Swagger 2.0 specification covering accounts, contacts, tags and custom fields, message sending across channels, sales pipelines and opportunities, AI agents, appointment calendars, templates and an ecommerce cart/order surface. Authentication is a single X-ACCESS-TOKEN API key header. Surfaced
  as a 500 Global portfolio company.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/replyrai.png
layout: provider
modified: '2026-08-13'
name: Replyr.ai
nav: Providers
network: true
overview: 'Replyr.ai publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, AI Agents API, Appointment Management API, and 4 more. Tagged areas include Company, Artificial Intelligence, Chatbots, Conversational AI, and Customer Engagement.


  Replyr.ai''s developer surface includes API reference, documentation, support, authentication, and 15 more developer resources.'
plans:
- name: Replyrai Plans Pricing
  plan_count: 0
  slug: replyrai-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Replyrai Rate Limits
  slug: replyrai-rate-limits
score:
  band: thin
  composite: 27.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 4.5
    contract_quality: 44.8
    developer_ergonomics: 35.1
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 27.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/replyrai/refs/heads/main/screenshots/replyrai-2026-09-02T153511.png
security:
- kind: authentication
  name: Replyrai Authentication
  slug: replyrai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Replyrai Domain Security
  slug: replyrai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: replyrai
tags:
- Company
- Artificial Intelligence
- Chatbots
- Conversational AI
- Customer Engagement
- Lead Generation
- WhatsApp
- Marketing
- Messaging
- CRM
- Appointment Scheduling
- Healthcare
- Malaysia
website: https://replyr.ai
---
