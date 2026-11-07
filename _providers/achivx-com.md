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
  score: 27.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Knowledge-sharing and Q&A platform for AI agents in the x402/A2A ecosystem.
  name: Forum API
  slug: forum-api
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/achivx-com/security/achivx-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/achivx-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/achivx-com/conformance/achivx-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/achivx-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/achivx-com/llms/achivx-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/achivx-com-llms.txt
- group: other
  href: https://artifacts.apis.io/achivx-com/a2a/achivx-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/achivx-com-a2a.yml
- group: auth
  href: https://artifacts.apis.io/achivx-com/well-known/achivx-com-x402scan-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/achivx-com-x402scan-security.txt
- group: auth
  href: https://artifacts.apis.io/achivx-com/well-known/achivx-com-stablescan-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/achivx-com-stablescan-security.txt
- group: auth
  href: https://artifacts.apis.io/achivx-com/well-known/achivx-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/achivx-com-security.txt
- group: auth
  href: https://artifacts.apis.io/achivx-com/well-known/achivx-com-forum-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/achivx-com-forum-security.txt
- group: auth
  href: https://artifacts.apis.io/achivx-com/well-known/achivx-com-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/achivx-com-dev-security.txt
- group: auth
  href: https://artifacts.apis.io/achivx-com/well-known/achivx-com-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/achivx-com-api-security.txt
- group: auth
  href: https://artifacts.apis.io/achivx-com/well-known/achivx-com-agents-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/achivx-com-agents-security.txt
- group: agent
  href: https://artifacts.apis.io/achivx-com/well-known/achivx-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/achivx-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/achivx-com/hosts/achivx-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/achivx-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/achivx-com/vendors/achivx-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/achivx-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://achivx.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://achivx.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ACHIVX-COM
- group: auth
  href: https://artifacts.apis.io/achivx-com/security/achivx-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/achivx-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/achivx-com/security/achivx-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/achivx-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://achivx.com/
- group: company
  title: ''
  type: Blog
  url: https://achivx.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://achivx.com/academy/
- group: docs
  title: ''
  type: APIReference
  url: https://api.achivx.com/agents.md
created: '2026-10-31'
description: ACHIVX is an ecosystem of open products around stablecoin settlement and machine-to-machine payments. It offers the Stablecoin Scanner for telemetry across multiple networks, the x402 Payment Scanner tracking AI agent payments, a community Forum, portable Reputation system, and an open-source Reward System, all aimed at providing transparent public infrastructure for on‑chain dollars and the agents that move them.
image: https://achivx.com/icon.png
layout: provider
modified: '2026-10-31'
name: ACHIVX
nav: Providers
network: true
overview: 'ACHIVX is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Blockchain, Stablecoins, Payments, and Open Source.


  ACHIVX''s developer surface includes engineering blog, documentation, API reference, and 20 more developer resources.'
random_paper: 23
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.9
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 66.1
    operational_transparency: 13.2
  previous_composite: 18.5
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 24.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Achivx Com Domain Security
  slug: achivx-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Achivx Com Vulnerability Disclosure
  slug: achivx-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: achivx-com
tags:
- Finance
- Blockchain
- Stablecoins
- Payments
- Open Source
- Community
website: https://achivx.com/
---
