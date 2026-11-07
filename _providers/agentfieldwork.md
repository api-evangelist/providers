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
    agentic_access: derived
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
  score: 1.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Agentfieldwork Agentic Access
  operation_count: 1
  slug: agentfieldwork-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: Submit task briefs for review by a single human provider based in Sweden.
  name: Task Intake API
  slug: task-intake-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/agentfieldwork/agentic-access/agentfieldwork-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agentfieldwork-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/agentfieldwork/rules/agentfieldwork-rules.yml
  title: ''
  type: Spectral
  url: rules/agentfieldwork-rules.yml
- group: design
  href: https://artifacts.apis.io/agentfieldwork/conformance/agentfieldwork-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentfieldwork-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentfieldwork/llms/agentfieldwork-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentfieldwork-llms.txt
- group: other
  href: https://artifacts.apis.io/agentfieldwork/hosts/agentfieldwork-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentfieldwork-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentfieldwork/vendors/agentfieldwork-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentfieldwork-vendors.yml
- group: auth
  href: https://artifacts.apis.io/agentfieldwork/security/agentfieldwork-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentfieldwork-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentfieldwork.com
- group: docs
  title: ''
  type: Documentation
  url: https://agentfieldwork.com/llms.txt
created: '2026-10-20'
description: AgentFieldwork provides a human‑assistance service where AI agents can submit task proposals for individual review by a single real person based in Sweden. The provider evaluates each request, may decline it, or issues a quote for the work. Payment and fulfilment are not yet active. The service supports remote worldwide tasks and local Stockholm‑area activities, offering real‑world verification, observation, and testing for AI‑driven workflows.
image: https://pub-bb2e103a32db4e198524a2e9ed8f35b4.r2.dev/lovp_6dhjearbmk98caf1hf7ez72ejf/b23a5a341d7a13ced5ca0bcc698d673e_1792219081192.png
layout: provider
modified: '2026-10-20'
name: AgentFieldwork
nav: Providers
network: true
overview: 'AgentFieldwork is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Human Assistance, Task Verification, Remote Observation, and Sweden Provider.


  The AgentFieldwork catalog on APIs.io includes 1 Spectral governance ruleset.


  AgentFieldwork''s developer surface includes documentation and 8 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: AgentFieldwork API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: agentfieldwork-rules
score:
  band: minimal
  composite: 8.9
  coverage:
    artifact_dirs: 12
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 64.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - sweden
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 9.9
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/agentfieldwork/agentfieldwork-2026-11-03T120356.png
security:
- kind: domain-security
  name: Agentfieldwork Domain Security
  slug: agentfieldwork-domain-security
  summary_line: TLSv1.3 · HSTS
slug: agentfieldwork
tags:
- Human Assistance
- Task Verification
- Remote Observation
- Sweden Provider
website: https://agentfieldwork.com
---
