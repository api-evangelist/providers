---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'agenthost API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: agenthost API
  slug: agenthost-eu-api
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/agenthost-eu/plans/agenthost-eu-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agenthost-eu-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agenthost-eu/rules/agenthost-eu-rules.yml
  title: ''
  type: Spectral
  url: rules/agenthost-eu-rules.yml
- group: design
  href: https://artifacts.apis.io/agenthost-eu/vocabulary/agenthost-eu-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agenthost-eu-vocabulary.yml
- group: auth
  title: ''
  type: Compliance
  url: https://agenthost.eu/security
- group: auth
  href: https://artifacts.apis.io/agenthost-eu/authentication/agenthost-eu-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agenthost-eu-authentication.yml
- group: design
  href: https://artifacts.apis.io/agenthost-eu/conformance/agenthost-eu-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agenthost-eu-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agenthost-eu/llms/agenthost-eu-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agenthost-eu-llms.txt
- group: agent
  href: https://artifacts.apis.io/agenthost-eu/well-known/agenthost-eu-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agenthost-eu-well-known.yml
- group: other
  href: https://artifacts.apis.io/agenthost-eu/hosts/agenthost-eu-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agenthost-eu-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://agenthost.eu/security
- group: auth
  href: https://artifacts.apis.io/agenthost-eu/security/agenthost-eu-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/agenthost-eu-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/agenthost-eu/security/agenthost-eu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agenthost-eu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agenthost.eu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://agenthost.eu/developers
- group: docs
  title: ''
  type: Documentation
  url: https://agenthost.eu/docs
- group: docs
  title: ''
  type: APIReference
  url: https://agenthost.eu/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://agenthost.eu/getting-started
- group: operate
  title: ''
  type: Support
  url: https://agenthost.eu/support
- group: commercial
  title: ''
  type: Pricing
  url: https://agenthost.eu/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agenthost.eu/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agenthost.eu/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://agenthost.eu/mcp
  - status: 200
    url: https://agenthost.eu/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: Web hosting you can just ask for. Connect agenthost to Claude, Cursor or any MCP client, then tell your agent to put your app online. Websites, Node, Python and PHP — no dashboard, no settings, no setup.
image: https://agenthost.eu/og.png
layout: provider
modified: '2026-10-31'
name: agenthost
nav: Providers
network: true
overview: 'agenthost is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Web Hosting, Artificial Intelligence, MCP, Cloud, and EU.


  The agenthost catalog on APIs.io includes 1 Spectral governance ruleset.


  agenthost''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, and 15 more developer resources.'
plans:
- name: Agenthost Eu Plans Pricing
  plan_count: 2
  slug: agenthost-eu-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Agenthost Eu Rate Limits
  slug: agenthost-eu-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: agenthost API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: agenthost-eu-rules
scopes:
- name: Agenthost Eu Scopes
  scope_count: 0
  slug: agenthost-eu-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.7
  coverage:
    artifact_dirs: 22
    catalog_earned: 45.8
    catalog_earned_first_party: 8.0
    catalog_gap: 69.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.8
  facets:
    access_clarity: 48.7
    contract_governance: 35.6
    contract_quality: 9.4
    developer_ergonomics: 33.3
    discoverability: 57.1
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 41.5
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agenthost Eu Authentication
  slug: agenthost-eu-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Agenthost Eu Domain Security
  slug: agenthost-eu-domain-security
  summary_line: TLSv1.3
- kind: trust-center
  name: Agenthost Eu Trust Center
  slug: agenthost-eu-trust-center
  summary_line: SOC 2, ISO 27001
slug: agenthost-eu
tags:
- Web Hosting
- Artificial Intelligence
- MCP
- Cloud
- EU
website: https://agenthost.eu/
---
