---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API for Charisma.ai conversational platform
  name: Charisma AI API
  slug: charisma-ai-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/charismaai/refs/heads/main/hosts/charismaai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/charismaai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/charismaai/refs/heads/main/vendors/charismaai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/charismaai-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/charismaai/refs/heads/main/security/charismaai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/charismaai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://charisma.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.charisma.ai
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.charisma.ai/quick-start
- group: operate
  title: ''
  type: Support
  url: https://charisma.ai/contact
- group: company
  title: ''
  type: Blog
  url: https://charisma.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://charisma.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://charisma.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://charisma.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://charisma.ai/privacy
coverage:
  checked: '2026-10-08'
  detail: Docs at https://docs.charisma.ai are JavaScript‑rendered and provide no machine‑readable OpenAPI spec.
  evidence:
  - status: 404
    url: https://docs.charisma.ai/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-08'
description: Charisma.ai provides immersive conversational AI platforms for training, brand experiences, and interactive simulations. Their technology enables realistic dialogue scenarios, real‑time analytics, and cross‑platform integration for enterprises seeking high‑impact conversational outcomes. Based in Oxford, UK, Charisma.ai serves clients worldwide with award‑winning responsible AI systems and customizable SDKs for Unity, Unreal, and other environments.
image: https://charisma.ai/static/images/open-graph-promo.png
layout: provider
modified: '2026-10-08'
name: Charisma.ai
nav: Providers
network: true
overview: 'Charisma.ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, ConversationalAI, Training, BrandExperience, and ImmersiveTech.


  Charisma.ai''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, signup flow, and 6 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 20.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Charismaai Domain Security
  slug: charismaai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: charismaai
tags:
- Artificial Intelligence
- ConversationalAI
- Training
- BrandExperience
- ImmersiveTech
- Company
website: https://charisma.ai
---
