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
api_count: 1
apis:
- description: Flett provides an AI‑powered whiteboard platform with an MCP server for integration; the API is documented in HTML pages without a machine‑readable contract.
  name: Flett API
  slug: flett-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/flett-app/plans/flett-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/flett-app-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/flett-app/llms/flett-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/flett-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/flett-app/well-known/flett-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/flett-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/flett-app/hosts/flett-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/flett-app-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://flett.app/privacy
- group: auth
  href: https://artifacts.apis.io/flett-app/security/flett-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/flett-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://flett.app/
- group: docs
  title: ''
  type: Documentation
  url: https://flett.app/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://flett.app/docs/plans
- group: start
  title: ''
  type: GettingStarted
  url: https://flett.app/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://flett.app/signin
coverage:
  checked: '2026-10-30'
  detail: Documentation is provided as HTML pages without a machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contract.
  evidence:
  - status: 200
    url: https://flett.app/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Flett is an AI‑powered whiteboard platform that lets teams collaboratively create slides, documents, diagrams and other visual content. Users can clip web pages, screenshots or AI‑generated artifacts onto a shared board, edit and comment in real time, and export the results to PowerPoint, PDF or other formats. The service includes an MCP server for integration with Claude, ChatGPT, Gemini and other models, and offers a Chrome extension for easy clipping. Flett provides a range of templates, brand kits and collaborative tools to streamline brainstorming and presentation creation.
image: https://flett.app/opengraph-image?35a046c3cdee8278
layout: provider
modified: '2026-10-30'
name: flett-app
nav: Providers
network: true
overview: 'flett-app is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Collaboration, Whiteboard, Presentation, and Productivity.


  flett-app''s developer surface includes documentation, pricing, getting-started guide, support, and 7 more developer resources.'
plans:
- name: Flett App Plans Pricing
  plan_count: 3
  slug: flett-app-plans-pricing
random_paper: 21
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.0
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 21.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/flett-app/flett-app-2026-11-03T132133.png
security:
- kind: domain-security
  name: Flett App Domain Security
  slug: flett-app-domain-security
  summary_line: TLSv1.3 · DMARC
slug: flett-app
tags:
- Artificial Intelligence
- Collaboration
- Whiteboard
- Presentation
- Productivity
- Company
website: https://flett.app/
---
