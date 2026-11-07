---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: MCP server provides AI connector tools for journaling entries.
  name: Dabble Me MCP
  slug: dabble-me-mcp
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/dabble-me/conventions/dabble-me-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dabble-me-conventions.yml
- group: auth
  href: https://artifacts.apis.io/dabble-me/authentication/dabble-me-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dabble-me-authentication.yml
- group: agent
  href: https://artifacts.apis.io/dabble-me/llms/dabble-me-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dabble-me-llms.txt
- group: agent
  href: https://artifacts.apis.io/dabble-me/well-known/dabble-me-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dabble-me-well-known.yml
- group: other
  href: https://artifacts.apis.io/dabble-me/hosts/dabble-me-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dabble-me-hosts.yml
- group: other
  href: https://artifacts.apis.io/dabble-me/vendors/dabble-me-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dabble-me-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dabble.me/terms
- group: operate
  title: ''
  type: Support
  url: https://dabble.me/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dabble.me/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://dabble.me/mcp-server#agent-instructions
- group: auth
  href: https://artifacts.apis.io/dabble-me/security/dabble-me-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dabble-me-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dabble.me/
coverage:
  checked: '2026-11-04'
  detail: The provider's docs are public but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found despite probing known endpoints.
  evidence:
  - status: 0
    url: https://api.dabble.me/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Dabble Me is a private, email‑first personal journaling service that helps users reflect daily. Users receive prompts by email and can reply to create entries, which are stored privately. The platform offers a free core product and a PRO tier ($4 / month or $40 / year) unlocking daily prompts, photo uploads, search, web writing, and remote MCP server access. It integrates with AI via MCP tools for searching, listing, analyzing entries, and more, while emphasizing privacy and no data training for AI.
image: https://dabble.me/dabble_logo_ogimage.jpg
layout: provider
modified: '2026-11-04'
name: Dabble Me
nav: Providers
network: true
overview: 'Dabble Me is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Journaling, Private, email-first, AI Integration, and Productivity.


  Dabble Me''s developer surface includes authentication, support, getting-started guide, and 9 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 16.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
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
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dabble Me Authentication
  slug: dabble-me-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Dabble Me Domain Security
  slug: dabble-me-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: dabble-me
tags:
- Journaling
- Private
- email-first
- AI Integration
- Productivity
website: https://dabble.me/
---
