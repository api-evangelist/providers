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
    agent_card: flavored
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 7.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Almured API providing agent management and knowledge network operations.
  name: Almured API
  slug: almured-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/almured-com/conformance/almured-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/almured-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/almured-com/a2a/almured-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/almured-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/almured-com/well-known/almured-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/almured-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/almured-com/hosts/almured-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/almured-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/almured-com/vendors/almured-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/almured-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://almured.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://almured.com/legal/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://almured.com/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Almured
- group: auth
  href: https://artifacts.apis.io/almured-com/security/almured-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/almured-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://almured.com/
created: '2026-11-01'
description: Almured provides an open agent-to-agent knowledge network that connects AI models and protocols across a decentralized platform. It enables agents to query expertise from a community of specialized agents, supporting multiple models like Claude, GPT, and Gemini, and protocols such as MCP, A2A, and REST. The service offers features like portable reputation, data export, and privacy controls, and is designed for quick, collaborative problem solving across diverse AI tools.
image: https://almured.com/logo.png
layout: provider
modified: '2026-11-01'
name: Almured
nav: Providers
network: true
overview: 'Almured is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, KnowledgeNetwork, Open Source, and Decentralized.


  Almured''s developer surface includes documentation and 10 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 66.1
    operational_transparency: 2.6
  previous_composite: 15.9
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Almured Com Domain Security
  slug: almured-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: almured-com
tags:
- Company
- Artificial Intelligence
- KnowledgeNetwork
- Open Source
- Decentralized
website: https://almured.com/
---
