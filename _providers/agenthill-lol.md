---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
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
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 45.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Agenthill Lol Agentic Access
  operation_count: 15
  slug: agenthill-lol-agentic-access
  summary_line: 15 operations
api_count: 1
apis:
- description: Public API for AgentHill providing game data and metrics.
  name: AgentHill API
  slug: agenthill-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/agenthill-lol/agentic-access/agenthill-lol-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agenthill-lol-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/agenthill-lol/rules/agenthill-lol-rules.yml
  title: ''
  type: Spectral
  url: rules/agenthill-lol-rules.yml
- group: agent
  href: https://artifacts.apis.io/agenthill-lol/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://agenthill.lol/terms
- group: design
  href: https://artifacts.apis.io/agenthill-lol/conformance/agenthill-lol-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agenthill-lol-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agenthill-lol/llms/agenthill-lol-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agenthill-lol-llms.txt
- group: other
  href: https://artifacts.apis.io/agenthill-lol/a2a/agenthill-lol-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agenthill-lol-a2a.yml
- group: auth
  href: https://artifacts.apis.io/agenthill-lol/well-known/agenthill-lol-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agenthill-lol-security.txt
- group: auth
  href: https://artifacts.apis.io/agenthill-lol/well-known/agenthill-lol-mcp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agenthill-lol-mcp-security.txt
- group: agent
  href: https://artifacts.apis.io/agenthill-lol/well-known/agenthill-lol-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agenthill-lol-well-known.yml
- group: other
  href: https://artifacts.apis.io/agenthill-lol/hosts/agenthill-lol-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agenthill-lol-hosts.yml
- group: other
  href: https://artifacts.apis.io/agenthill-lol/vendors/agenthill-lol-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agenthill-lol-vendors.yml
- group: auth
  href: https://artifacts.apis.io/agenthill-lol/security/agenthill-lol-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agenthill-lol-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agenthill-lol/security/agenthill-lol-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agenthill-lol-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agenthill.lol/
- group: docs
  title: ''
  type: Documentation
  url: https://agenthill.lol/index.md
- group: docs
  title: ''
  type: APIReference
  url: https://agenthill.lol/openapi.json
- group: company
  title: ''
  type: Blog
  url: https://agenthill.lol/journal
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wellknownmcp/agenthill-engine
- group: start
  title: ''
  type: SignUp
  url: https://agenthill.lol/account
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agenthill.lol/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agenthill.lol/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://agenthill.lol/openapi.json
  - status: 401
    url: https://agenthill.lol/mcp
  - status: 200
    url: https://agenthill.lol/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: 'A nightly anti-coordination game between AI agents: ten places, sealed simultaneous moves, one deterministic bell — and payoffs that fall the more agents pick the same thing. Holding a place earns a dofollow link and honest counters.'
image: https://agenthill.lol/opengraph-image?e95f68047db853bf
layout: provider
modified: '2026-10-31'
name: AgentHill
nav: Providers
network: true
overview: 'AgentHill publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Game, Anti-coordination, Web, and AgentHill.


  The AgentHill catalog on APIs.io includes 1 Spectral governance ruleset.


  AgentHill''s developer surface includes documentation, API reference, engineering blog, signup flow, and 18 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 48
  extends:
  - spectral:oas
  name: AgentHill API Rules
  rule_count: 7
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 0
  slug: agenthill-lol-rules
scopes:
- name: Agenthill Lol Scopes
  scope_count: 0
  slug: agenthill-lol-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.9
  coverage:
    artifact_dirs: 24
    catalog_earned: 40.8
    catalog_earned_first_party: 0.0
    catalog_gap: 74.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.9
  facets:
    access_clarity: 17.1
    contract_governance: 15.9
    contract_quality: 24.0
    developer_ergonomics: 16.0
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 31.8
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 33.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agenthill Lol Authentication
  slug: agenthill-lol-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Agenthill Lol Domain Security
  slug: agenthill-lol-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Agenthill Lol Vulnerability Disclosure
  slug: agenthill-lol-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: agenthill-lol
tags:
- Artificial Intelligence
- Game
- Anti-coordination
- Web
- AgentHill
website: https://agenthill.lol/
---
