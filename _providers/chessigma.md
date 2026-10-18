---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.3
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Chessigma Agentic Access
  operation_count: 4
  slug: chessigma-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 1
apis:
- baseURL: https://www.chessigma.com/public-api/v1
  baseurl_source: declared
  description: The Daily Puzzle API from Chessigma — 1 operation(s) for daily puzzle.
  name: Chessigma Daily Puzzle API
  slug: chessigma-daily-puzzle-api
- baseURL: https://www.chessigma.com/public-api/v1
  baseurl_source: declared
  description: The Elo Calculator API from Chessigma — 1 operation(s) for elo calculator.
  name: Chessigma Elo Calculator API
  slug: chessigma-elo-calculator-api
- baseURL: https://www.chessigma.com/public-api/v1
  baseurl_source: declared
  description: The Game API from Chessigma — 2 operation(s) for game.
  name: Chessigma Game API
  slug: chessigma-game-api
artifact_total: 13
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chessigma/refs/heads/main/agentic-access/chessigma-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/chessigma-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/chessigma/refs/heads/main/plans/chessigma-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chessigma-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chessigma/refs/heads/main/rules/chessigma-rules.yml
  title: ''
  type: Spectral
  url: rules/chessigma-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chessigma/refs/heads/main/json-ld/chessigma-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/chessigma-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chessigma/refs/heads/main/vocabulary/chessigma-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/chessigma-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chessigma/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chessigma/refs/heads/main/data-model/chessigma-data-model.yml
  title: ''
  type: DataModel
  url: data-model/chessigma-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chessigma/refs/heads/main/errors/chessigma-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/chessigma-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/chessigma/refs/heads/main/conformance/chessigma-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chessigma-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chessigma/refs/heads/main/llms/chessigma-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chessigma-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chessigma/refs/heads/main/well-known/chessigma-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chessigma-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chessigma/refs/heads/main/hosts/chessigma-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chessigma-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chessigma/refs/heads/main/vendors/chessigma-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chessigma-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/chessigma/refs/heads/main/packages/chessigma-packages.yml
  title: ''
  type: SDKs
  url: packages/chessigma-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/chessigma/refs/heads/main/packages/chessigma-packages.yml
  title: ''
  type: Packages
  url: packages/chessigma-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chessigma/refs/heads/main/security/chessigma-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chessigma-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.chessigma.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.chessigma.com/developers
- group: company
  title: ''
  type: Blog
  url: https://www.chessigma.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.chessigma.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.chessigma.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chessigma.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.chessigma.com/contact
created: '2026-10-05'
description: Chessigma provides a free, no‑auth API for chess game analysis and daily puzzles. Users can submit PGN games, retrieve engine analysis, calculate rating changes, and access training puzzles without signup or rate‑limited keys. The platform runs Stockfish in the browser, offering compute‑free, unlimited analysis for Chess.com, Lichess and uploaded PGN files.
image: https://www.chessigma.com/opengraph-image.png
json_schemas:
- name: DailyPuzzle
  property_count: 8
  slug: chessigma-daily-puzzle
- name: EloResponse
  property_count: 8
  slug: chessigma-elo-response
- name: GameAnalysisResponse
  property_count: 4
  slug: chessigma-game-analysis-response
- name: GameSubmissionResponse
  property_count: 4
  slug: chessigma-game-submission-response
- name: GameSubmission
  property_count: 1
  slug: chessigma-game-submission
jsonld:
- class_count: 7
  name: Chessigma Context
  property_count: 35
  slug: chessigma-context
layout: provider
modified: '2026-10-05'
name: Chessigma
nav: Providers
network: true
overview: 'Chessigma publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Daily Puzzle API, Elo Calculator API, and Game API. Tagged areas include Company, Chess, Free, and NoAuth.


  The Chessigma catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Chessigma''s developer surface includes documentation, engineering blog, pricing, support, and 19 more developer resources.'
plans:
- name: Chessigma Plans Pricing
  plan_count: 5
  slug: chessigma-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Chessigma API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: chessigma-rules
score:
  band: developing
  composite: 44.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 35.6
    contract_quality: 63.4
    developer_ergonomics: 25.6
    discoverability: 64.3
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Chessigma Domain Security
  slug: chessigma-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chessigma
tags:
- Company
- Chess
- Free
- NoAuth
website: https://www.chessigma.com
---
