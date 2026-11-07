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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/doomscore-vc/hosts/doomscore-vc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/doomscore-vc-hosts.yml
- group: other
  href: https://artifacts.apis.io/doomscore-vc/vendors/doomscore-vc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/doomscore-vc-vendors.yml
- group: auth
  href: https://artifacts.apis.io/doomscore-vc/security/doomscore-vc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/doomscore-vc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://doomscore.vc/
coverage:
  checked: '2026-11-05'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found on discovered hosts.
  evidence:
  - status: 404
    url: https://api.doomscore.vc/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: Doom scores any product, deck, or URL for sherlock risk — the odds Claude, ChatGPT, Gemini, or Grok ships its whole company as a checkbox. Four models, one number, the receipts behind it. The service provides rapid risk assessment for startups and products based on AI model predictions, helping investors and founders evaluate potential AI-driven market impacts.
image: https://doomscore.vc/og/home
layout: provider
modified: '2026-11-05'
name: Doom
nav: Providers
network: true
overview: Doom is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Risk Management, Startups, Analytics, and Scoring.
random_paper: 9
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Doomscore Vc Domain Security
  slug: doomscore-vc-domain-security
  summary_line: TLSv1.3
slug: doomscore-vc
tags:
- Artificial Intelligence
- Risk Management
- Startups
- Analytics
- Scoring
- Company
website: https://doomscore.vc/
---
