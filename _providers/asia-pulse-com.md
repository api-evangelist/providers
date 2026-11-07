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
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Asia Pulse Com Agentic Access
  operation_count: 9
  slug: asia-pulse-com-agentic-access
  summary_line: 9 operations
api_count: 1
apis:
- description: Market intelligence API providing paid data endpoints for crypto, treasury, and Asian sector analytics.
  name: Asia Pulse API
  slug: asia-pulse-api
- baseURL: https://asia-pulse.com
  baseurl_source: declared
  description: Paid market data and analysis endpoints.
  name: Asia Pulse Market Intelligence API
  slug: asia-pulse-com-market-intelligence-api
- baseURL: https://asia-pulse.com
  baseurl_source: declared
  description: Free service metadata.
  name: Asia Pulse Meta API
  slug: asia-pulse-com-meta-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/asia-pulse-com/agentic-access/asia-pulse-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/asia-pulse-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/asia-pulse-com/rules/asia-pulse-com-rules.yml
  title: ''
  type: Spectral
  url: rules/asia-pulse-com-rules.yml
- group: design
  href: https://artifacts.apis.io/asia-pulse-com/vocabulary/asia-pulse-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/asia-pulse-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/asia-pulse-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/asia-pulse-com/security/asia-pulse-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/asia-pulse-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/asia-pulse-com/errors/asia-pulse-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/asia-pulse-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/asia-pulse-com/conformance/asia-pulse-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/asia-pulse-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/asia-pulse-com/llms/asia-pulse-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/asia-pulse-com-llms.txt
- group: other
  href: https://artifacts.apis.io/asia-pulse-com/a2a/asia-pulse-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/asia-pulse-com-a2a.yml
- group: auth
  href: https://artifacts.apis.io/asia-pulse-com/well-known/asia-pulse-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/asia-pulse-com-security.txt
- group: agent
  href: https://artifacts.apis.io/asia-pulse-com/well-known/asia-pulse-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/asia-pulse-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/asia-pulse-com/hosts/asia-pulse-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asia-pulse-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/asia-pulse-com/security/asia-pulse-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/asia-pulse-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/asia-pulse-com/security/asia-pulse-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asia-pulse-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://asia-pulse.com/
created: '2026-11-01'
description: Asia Pulse provides Asia-session market intelligence for AI agents, delivering structured JSON data on crypto price gaps, funding rates, and sector analyses across Korean and Japanese markets. Their service offers transparent, timestamped analytics with testable claims anchored on X Layer, ensuring honesty and verifiability for AI-driven decision making.
image: https://asia-pulse.com/og-image.png
layout: provider
modified: '2026-11-01'
name: Asia Pulse
nav: Providers
network: true
overview: 'Asia Pulse publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including Market Intelligence API, Meta API, and 1 more. Tagged areas include Company, Artificial Intelligence, Market Intelligence, Cryptocurrency, and Asia.


  The Asia Pulse catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: Asia Pulse API Rules
  rule_count: 37
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 1
  slug: asia-pulse-com-rules
score:
  band: emerging
  composite: 23.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 45.9
    developer_ergonomics: 6.4
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 23.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Asia Pulse Com Domain Security
  slug: asia-pulse-com-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Asia Pulse Com Vulnerability Disclosure
  slug: asia-pulse-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: asia-pulse-com-main
  slug: asia-pulse-com-main
slug: asia-pulse-com
tags:
- Company
- Artificial Intelligence
- Market Intelligence
- Cryptocurrency
- Asia
website: https://asia-pulse.com/
---
