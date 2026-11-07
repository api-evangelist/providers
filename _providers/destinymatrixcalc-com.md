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
    agent_skills: unknown
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
  score: 6.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public read-only JSON API for the Destiny Matrix (numerology) calculator.
  name: Destiny Matrix API
  slug: destiny-matrix-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/destinymatrixcalc-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/destinymatrixcalc-com/conformance/destinymatrixcalc-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/destinymatrixcalc-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/destinymatrixcalc-com/llms/destinymatrixcalc-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/destinymatrixcalc-com-llms.txt
- group: other
  href: https://artifacts.apis.io/destinymatrixcalc-com/hosts/destinymatrixcalc-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/destinymatrixcalc-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://destinymatrixcalc.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://destinymatrixcalc.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://destinymatrixcalc.com/blog
- group: auth
  href: https://artifacts.apis.io/destinymatrixcalc-com/security/destinymatrixcalc-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/destinymatrixcalc-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://destinymatrixcalc.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://destinymatrixcalc.com/openapi.json
  - status: 401
    url: https://destinymatrixcalc.com/api/mcp
  - status: 200
    url: https://destinymatrixcalc.com/
  reason: partner-login
  state: gated
created: '2026-11-05'
description: ArcFlow provides a free online Destiny Matrix service that calculates a personal matrix, couple compatibility, and child profiles from a user's date of birth. The tool offers self‑analysis based on a numerological‑psychological system using the 22 Major Arcana, delivering insights into talents, finances, relationships, and ancestral patterns for individuals seeking personal development.
image: https://destinymatrixcalc.com/api/og?c=eyJ0IjoiRGVzdGlueSBNYXRyaXg6IGFyY2FuYSwgcHJvZ3JhbXMgYW5kIGthcm1pYyB0YWlscyBleHBsYWluZWQiLCJrIjoiRGVzdGlueSBtYXRyaXgiLCJpIjoiaHR0cHM6Ly9zMy50d2NzdG9yYWdlLnJ1L2Q1OTBjNWVhLWE4YWYtNDkzYS04MDA2LTg2ZDJjOWI4NzUxZS9hcmNmbG93L29nLWhvbWUtb2cud2VicCJ9
layout: provider
modified: '2026-11-05'
name: ArcFlow
nav: Providers
network: true
overview: 'ArcFlow is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Astrology, Tarot, Numerology, and Self-Discovery.


  ArcFlow''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 13.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 8.8
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Destinymatrixcalc Com Domain Security
  slug: destinymatrixcalc-com-domain-security
  summary_line: TLSv1.3
slug: destinymatrixcalc-com
tags:
- Company
- Astrology
- Tarot
- Numerology
- Self-Discovery
- Personal Development
website: https://destinymatrixcalc.com/
---
