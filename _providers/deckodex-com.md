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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Deckodex provides a deck management service but does not expose a public developer API.
  name: Deckodex API
  slug: deckodex-api
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/deckodex-com/security/deckodex-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/deckodex-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/deckodex-com/llms/deckodex-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deckodex-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/deckodex-com/well-known/deckodex-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/deckodex-com-security.txt
- group: agent
  href: https://artifacts.apis.io/deckodex-com/well-known/deckodex-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/deckodex-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/deckodex-com/hosts/deckodex-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deckodex-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/deckodex-com/vendors/deckodex-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deckodex-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://deckodex.com/terms
- group: operate
  title: ''
  type: Support
  url: https://deckodex.com/gundam/glossary/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://deckodex.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://deckodex.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/markomatic507
- group: auth
  href: https://artifacts.apis.io/deckodex-com/security/deckodex-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/deckodex-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/deckodex-com/security/deckodex-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deckodex-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://deckodex.com/
coverage:
  checked: '2026-11-05'
  detail: No public OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found despite documentation pages.
  evidence:
  - status: 200
    url: https://deckodex.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: Deckodex offers a deckbuilder, card database, price tracking, and collection management tools for trading card games. It supports the Gundam Card Game and the Naruto Card Game, allowing users to search cards by effect text, build and share decks, and view tournament tier lists and daily price data. The service is free to use, with an optional paid Pro tier for unlimited decks and value history.
image: https://deckodex.com/og/default.png?r=5
layout: provider
modified: '2026-11-05'
name: Deckodex
nav: Providers
network: true
overview: 'Deckodex is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include deckbuilder, Card Database, collection tracking, Trading Card Games, and Price-Tracking.


  Deckodex''s developer surface includes support, pricing, and 12 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 23.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Deckodex Com Domain Security
  slug: deckodex-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Deckodex Com Vulnerability Disclosure
  slug: deckodex-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: deckodex-com
tags:
- deckbuilder
- Card Database
- collection tracking
- Trading Card Games
- Price-Tracking
- tournament meta
website: https://deckodex.com/
---
