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
- description: Public API endpoints for Docteur Bet, providing betting odds and user data.
  name: Docteur Bet API
  slug: docteur-bet-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Security
  url: https://docteurbet.fr/fr/mcp#signaler-une-faille
- group: agent
  href: https://artifacts.apis.io/docteurbet-fr/llms/docteurbet-fr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/docteurbet-fr-llms.txt
- group: auth
  href: https://artifacts.apis.io/docteurbet-fr/well-known/docteurbet-fr-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/docteurbet-fr-security.txt
- group: agent
  href: https://artifacts.apis.io/docteurbet-fr/well-known/docteurbet-fr-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/docteurbet-fr-well-known.yml
- group: other
  href: https://artifacts.apis.io/docteurbet-fr/hosts/docteurbet-fr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/docteurbet-fr-hosts.yml
- group: auth
  href: https://artifacts.apis.io/docteurbet-fr/security/docteurbet-fr-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/docteurbet-fr-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/docteurbet-fr/security/docteurbet-fr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/docteurbet-fr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docteurbet.fr/
coverage:
  checked: '2026-11-05'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found after probing known hosts.
  evidence:
  - status: 404
    url: https://api.docteurbet.fr/openapi.json
  - status: 404
    url: https://api.docteurbet.fr/openapi.yaml
  - status: 404
    url: https://api.docteurbet.fr/swagger.json
  - status: 404
    url: https://api.docteurbet.fr/v1/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: Docteur Bet provides a value‑betting platform for football, offering a model that calculates the probability of each outcome and compares it to bookmakers' odds. The service publishes public records of gains and losses, a free 7‑day trial, and premium subscriptions. It targets French‑speaking users and presents data via a web app and API endpoints. The company also shares its methodology, training resources, and analyses on its site.
image: https://docteurbet.fr/opengraph-image
layout: provider
modified: '2026-11-05'
name: Docteur Bet
nav: Providers
network: true
overview: Docteur Bet is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Value betting, Sports Betting, Subscription Service, and Odds Comparison.
random_paper: 14
score:
  band: minimal
  composite: 5.7
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
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Docteurbet Fr Domain Security
  slug: docteurbet-fr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Docteurbet Fr Vulnerability Disclosure
  slug: docteurbet-fr-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: docteurbet-fr
tags:
- Value betting
- Sports Betting
- Subscription Service
- Odds Comparison
website: https://docteurbet.fr/
---
