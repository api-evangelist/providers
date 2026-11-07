---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/atendio-co/llms/atendio-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/atendio-co-llms.txt
- group: agent
  href: https://artifacts.apis.io/atendio-co/well-known/atendio-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/atendio-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/atendio-co/hosts/atendio-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atendio-co-hosts.yml
- group: auth
  href: https://artifacts.apis.io/atendio-co/security/atendio-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atendio-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://atendio.co/
- group: company
  title: ''
  type: Blog
  url: https://atendio.co/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://atendio.co/precios
- group: commercial
  title: ''
  type: TermsOfService
  url: https://atendio.co/terminos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://atendio.co/privacidad
- group: operate
  title: ''
  type: Support
  url: https://atendio.co/ayuda
- group: start
  title: ''
  type: SignUp
  url: https://atendio.co/registro
- group: start
  title: ''
  type: Login
  url: https://atendio.co/login
coverage:
  checked: '2026-11-02'
  detail: No machine-readable API specification (OpenAPI, AsyncAPI, GraphQL, etc.) was found despite probing typical locations.
  evidence:
  - status: 0
    url: https://api.atendio.co/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Atendio provides AI-powered WhatsApp chatbot solutions for businesses across Latin America. The platform, a product of btodigital based in Medellín, Colombia, enables companies to automate customer interactions, schedule appointments, and sell 24/7 using the same phone number. Plans start at US$49 per month and include AI features. The service integrates with the WhatsApp Business API and offers multi‑channel support via web, iOS, and Android apps.
image: https://atendio.co/icon-512.png
layout: provider
modified: '2026-11-01'
name: Atendio
nav: Providers
network: true
overview: 'Atendio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include WhatsApp, Artificial Intelligence, Chatbots, Business, and Latin America.


  Atendio''s developer surface includes engineering blog, pricing, support, signup flow, and 8 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.7
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - colombia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 15.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Atendio Co Domain Security
  slug: atendio-co-domain-security
  summary_line: TLSv1.3 · HSTS
slug: atendio-co
tags:
- WhatsApp
- Artificial Intelligence
- Chatbots
- Business
- Latin America
- Colombia
website: https://atendio.co/
---
