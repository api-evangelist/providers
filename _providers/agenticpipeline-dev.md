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
  band: human-only
  dimensions:
    agent_card: false
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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Agentic Pipeline provides an agent‑native CI/CD platform with live logs and MCP control.
  name: Agentic Pipeline API
  slug: agentic-pipeline-api
artifact_total: 5
common:
- group: auth
  href: https://artifacts.apis.io/agenticpipeline-dev/security/agenticpipeline-dev-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/agenticpipeline-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agenticpipeline-dev/well-known/agenticpipeline-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agenticpipeline-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/agenticpipeline-dev/well-known/agenticpipeline-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agenticpipeline-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/agenticpipeline-dev/hosts/agenticpipeline-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agenticpipeline-dev-hosts.yml
- group: auth
  href: https://artifacts.apis.io/agenticpipeline-dev/security/agenticpipeline-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agenticpipeline-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agenticpipeline-dev/security/agenticpipeline-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agenticpipeline-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agenticpipeline.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://agenticpipeline.dev/docs/
- group: company
  title: ''
  type: Blog
  url: https://agenticpipeline.dev/resources/
- group: start
  title: ''
  type: GettingStarted
  url: https://agenticpipeline.dev/#how-it-works
coverage:
  checked: '2026-11-01'
  detail: Documentation is public HTML but provides no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec.
  evidence:
  - status: 200
    url: https://agenticpipeline.dev/docs/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Agentic Pipeline is an agent-native CI/CD platform that serves as a GitHub Actions alternative. It streams agent‑readable logs while a run is live, allowing coding agents to diagnose failures and rerun failed work over the MCP (Machine Control Protocol). The platform provides live control, automatic profiling, required GitHub checks, and the ability to turn off pipelines at any time. It offers a dashboard for replacing GitHub Actions, integrates with GitHub checks, and emphasizes security and transparency.
image: https://agenticpipeline.dev/icon.svg?icon.3a_aq278mhxiu.svg
layout: provider
modified: '2026-11-01'
name: Agentic Pipeline
nav: Providers
network: true
overview: 'Agentic Pipeline is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include CI/CD, DevOps, Automation, AI Agents, and GitHub Actions Alternative.


  Agentic Pipeline''s developer surface includes documentation, engineering blog, getting-started guide, and 7 more developer resources.'
random_paper: 5
scopes:
- name: Agenticpipeline Dev Scopes
  scope_count: 0
  slug: agenticpipeline-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.4
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 10.5
  previous_composite: 12.8
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agenticpipeline Dev Authentication
  slug: agenticpipeline-dev-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Agenticpipeline Dev Domain Security
  slug: agenticpipeline-dev-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Agenticpipeline Dev Vulnerability Disclosure
  slug: agenticpipeline-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: agenticpipeline-dev
tags:
- CI/CD
- DevOps
- Automation
- AI Agents
- GitHub Actions Alternative
- MCP
website: https://agenticpipeline.dev/
---
