---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    mcp_server: documented
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
  score: 21.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for DeckSpace platform, providing endpoints for presentation creation and management.
  name: DeckSpace API
  slug: deckspace-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/deckspace-org/plans/deckspace-org-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/deckspace-org-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/deckspace-org/llms/deckspace-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deckspace-org-llms.txt
- group: agent
  href: https://artifacts.apis.io/deckspace-org/well-known/deckspace-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/deckspace-org-well-known.yml
- group: other
  href: https://artifacts.apis.io/deckspace-org/hosts/deckspace-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deckspace-org-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://deckspace.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://deckspace.org/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://deckspace.org/pricing
- group: auth
  href: https://artifacts.apis.io/deckspace-org/security/deckspace-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deckspace-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://deckspace.org/
created: '2026-11-05'
description: DeckSpace provides an AI‑powered platform for creating presentations, diagrams, and dashboards. Users can start from templates, craft content with AI assistance, refine their work, and share it from a single home. The service offers free starter plans, integrates with ChatGPT and Claude, and supports exporting decks for collaboration. It aims to streamline visual storytelling and data storytelling for individuals and teams.
image: https://deckspace.org/og-image.png
layout: provider
modified: '2026-11-05'
name: DeckSpace
nav: Providers
network: true
overview: 'DeckSpace is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Presentations, Diagramming, Dashboards, and Collaboration.


  DeckSpace''s developer surface includes pricing and 8 more developer resources.'
plans:
- name: Deckspace Org Plans Pricing
  plan_count: 3
  slug: deckspace-org-plans-pricing
random_paper: 8
score:
  band: emerging
  composite: 18.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Deckspace Org Domain Security
  slug: deckspace-org-domain-security
  summary_line: TLSv1.3
slug: deckspace-org
tags:
- Artificial Intelligence
- Presentations
- Diagramming
- Dashboards
- Collaboration
website: https://deckspace.org/
---
