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
    mcp_server: false
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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Provides token counting functionality for OpenAI models via a simple HTTP API.
  name: Prompt Token Counter API
  slug: prompt-token-counter-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/prompttokencounter/hosts/prompttokencounter-hosts.yml
  title: ''
  type: Hosts
  url: hosts/prompttokencounter-hosts.yml
- group: other
  href: https://artifacts.apis.io/prompttokencounter/vendors/prompttokencounter-vendors.yml
  title: ''
  type: Vendors
  url: vendors/prompttokencounter-vendors.yml
- group: auth
  href: https://artifacts.apis.io/prompttokencounter/security/prompttokencounter-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/prompttokencounter-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://prompttokencounter.com/
coverage:
  checked: '2026-10-18'
  detail: The provider's website returns a JavaScript‑rendered Next.js app with no OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL files discoverable.
  evidence:
  - status: 404
    url: https://www.prompttokencounter.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-18'
description: Prompt Token Counter provides an online tool to count tokens for OpenAI models, helping users ensure prompts fit model limits. It offers token counts for various GPT models, professional prompt optimization services, and guidance on token management to control costs and improve prompt efficiency.
layout: provider
modified: '2026-10-18'
name: Prompt Token Counter
nav: Providers
network: true
overview: Prompt Token Counter is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Tokenization, OpenAI, PromptTools, and Artificial Intelligence.
random_paper: 19
score:
  band: minimal
  composite: 4.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  previous_composite: 4.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/prompttokencounter/prompttokencounter-2026-11-03T141624.png
security:
- kind: domain-security
  name: Prompttokencounter Domain Security
  slug: prompttokencounter-domain-security
  summary_line: TLSv1.3 · HSTS
slug: prompttokencounter
tags:
- Company
- Tokenization
- OpenAI
- PromptTools
- Artificial Intelligence
- Utility
website: https://prompttokencounter.com/
---
