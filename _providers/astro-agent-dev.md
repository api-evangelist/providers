---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Astro Agent Dev Agentic Access
  operation_count: 25
  slug: astro-agent-dev-agentic-access
  summary_line: 25 operations · 23 acting
api_count: 1
apis:
- baseURL: https://astro-agent.dev
  baseurl_source: declared
  description: 'Verifiable, reproducible astro-financial data for backtesting: geocentric and heliocentric positions, declination, Gann planetary lines and a celestial event calendar.'
  name: astro-agent-dev Finance API
  slug: astro-agent-dev-finance-api
- baseURL: https://astro-agent.dev
  baseurl_source: declared
  description: The free API from astro-agent-dev — 3 operation(s) for free.
  name: astro-agent-dev Free API
  slug: astro-agent-dev-free-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/astro-agent-dev/agentic-access/astro-agent-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/astro-agent-dev-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/astro-agent-dev/rules/astro-agent-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/astro-agent-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/astro-agent-dev/vocabulary/astro-agent-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/astro-agent-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/astro-agent-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://astro-agent.dev/support
- group: design
  href: https://artifacts.apis.io/astro-agent-dev/errors/astro-agent-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/astro-agent-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/astro-agent-dev/conformance/astro-agent-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/astro-agent-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/astro-agent-dev/llms/astro-agent-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/astro-agent-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/astro-agent-dev/a2a/astro-agent-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/astro-agent-dev-a2a.yml
- group: auth
  href: https://artifacts.apis.io/astro-agent-dev/well-known/astro-agent-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/astro-agent-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/astro-agent-dev/well-known/astro-agent-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/astro-agent-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/astro-agent-dev/hosts/astro-agent-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/astro-agent-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/astro-agent-dev/vendors/astro-agent-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/astro-agent-dev-vendors.yml
- group: auth
  href: https://artifacts.apis.io/astro-agent-dev/security/astro-agent-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/astro-agent-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/astro-agent-dev/security/astro-agent-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/astro-agent-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://astro-agent.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://astro-agent.dev/openapi.json
- group: docs
  title: ''
  type: APIReference
  url: https://astro-agent.dev/openapi.json
- group: operate
  title: ''
  type: Support
  url: https://astro-agent.dev/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aidatatools-dev
- group: commercial
  title: ''
  type: TermsOfService
  url: https://astro-agent.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://astro-agent.dev/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/astro-agent-dev/workspace
created: '2026-10-30'
description: Astro Agents provides verifiable planetary timing data for market analysis, backtesting, and astrology. Leveraging NASA/JPL DE440 ephemeris, the API delivers precise geocentric and heliocentric positions, declination, Gann planetary lines, and a comprehensive celestial event calendar. Data is reproducible, SHA‑256 hashed, and offered via pay‑per‑call or prepaid credit packs, with no account or API key required. Ideal for traders, quants, and AI agents seeking reliable astro‑financial signals without speculative forecasts.
image: https://astro-agent.dev/icon.png
layout: provider
modified: '2026-10-30'
name: astro-agent-dev
nav: Providers
network: true
overview: 'astro-agent-dev publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Finance API and Free API. Tagged areas include Company, AstroFinance, Astrology, MarketData, and API.


  The astro-agent-dev catalog on APIs.io includes 1 Spectral governance ruleset.


  astro-agent-dev''s developer surface includes documentation, API reference, support, and 20 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: astro-agent-dev API Rules
  rule_count: 15
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 2
  slug: astro-agent-dev-rules
score:
  band: developing
  composite: 40.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 57.7
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 79.1
    contract_quality: 42.2
    developer_ergonomics: 32.6
    discoverability: 66.1
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Astro Agent Dev Domain Security
  slug: astro-agent-dev-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Astro Agent Dev Vulnerability Disclosure
  slug: astro-agent-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: finance
  slug: astro-agent-dev-finance
slug: astro-agent-dev
tags:
- Company
- AstroFinance
- Astrology
- MarketData
- API
website: https://astro-agent.dev/
---
