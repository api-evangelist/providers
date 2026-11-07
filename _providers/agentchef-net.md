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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/agentchef-net/security/agentchef-net-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/agentchef-net-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/agentchef-net/llms/agentchef-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentchef-net-llms.txt
- group: auth
  href: https://artifacts.apis.io/agentchef-net/well-known/agentchef-net-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agentchef-net-security.txt
- group: agent
  href: https://artifacts.apis.io/agentchef-net/well-known/agentchef-net-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentchef-net-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentchef-net/hosts/agentchef-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentchef-net-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentchef-net/vendors/agentchef-net-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentchef-net-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentchef.net/terms
- group: operate
  title: ''
  type: Support
  url: https://agentchef.net/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentchef.net/privacy
- group: start
  title: ''
  type: Login
  url: https://agentchef.net/login
- group: auth
  href: https://artifacts.apis.io/agentchef-net/security/agentchef-net-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agentchef-net-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agentchef-net/security/agentchef-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentchef-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentchef.net/
coverage:
  checked: '2026-11-01'
  detail: The site provides a consumer AI dinner‑planning service with no public API documentation or machine‑readable contracts.
  evidence:
  - status: 200
    url: https://agentchef.net/
  reason: not-a-software-company
  state: none
created: '2026-10-31'
description: Agent Chef is an AI‑powered dinner planning service that helps families decide what to eat each week. Users receive ten recipe suggestions from an AI agent, vote on their favorites, and the top choices are turned into a grocery list. The platform integrates with popular large‑language models like Claude, ChatGPT, and Cursor, and operates without requiring accounts—just share a link to vote. It also offers comparisons with other meal‑kit services and supports feedback loops to improve future suggestions. The service aims to simplify meal planning, reduce decision fatigue, and streamline grocery shopping for households.
image: https://agentchef.net/static/og.png
layout: provider
modified: '2026-10-31'
name: Agent Chef
nav: Providers
network: true
overview: 'Agent Chef is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Dinner Planning, Family, and Meal Service.


  Agent Chef''s developer surface includes support and 12 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.5
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 10.5
  previous_composite: 15.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentchef Net Domain Security
  slug: agentchef-net-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Agentchef Net Vulnerability Disclosure
  slug: agentchef-net-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: agentchef-net
tags:
- Company
- Artificial Intelligence
- Dinner Planning
- Family
- Meal Service
website: https://agentchef.net/
---
