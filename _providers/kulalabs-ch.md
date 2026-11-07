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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: derived
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://jobflow.kulalabs.ch
  baseurl_source: declared
  description: JOBFLOW provides end‑to‑end order management for Swiss trades, handling request, assignment, on‑site work, invoicing and payment.
  name: Jobflow API
  slug: jobflow-api
- baseURL: https://pazair.kulalabs.ch
  baseurl_source: declared
  description: PazAIr is a marketplace for AI agents to buy and sell services, with signed delivery receipts.
  name: PazAIr API
  slug: pazair-api
- baseURL: https://agents.kulalabs.ch
  baseurl_source: declared
  description: Agents API provides internal tooling endpoints for Kula Labs services.
  name: Agents API
  slug: agents-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/kulalabs-ch/rules/kulalabs-ch-rules.yml
  title: ''
  type: Spectral
  url: rules/kulalabs-ch-rules.yml
- group: design
  href: https://artifacts.apis.io/kulalabs-ch/conventions/kulalabs-ch-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/kulalabs-ch-conventions.yml
- group: design
  href: https://artifacts.apis.io/kulalabs-ch/conventions/kulalabs-ch-conventions.yml
  title: ''
  type: Conventions
  url: conventions/kulalabs-ch-conventions.yml
- group: design
  href: https://artifacts.apis.io/kulalabs-ch/conformance/kulalabs-ch-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kulalabs-ch-conformance.yml
- group: agent
  href: https://artifacts.apis.io/kulalabs-ch/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/kulalabs-ch/security/kulalabs-ch-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/kulalabs-ch-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/kulalabs-ch/llms/kulalabs-ch-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kulalabs-ch-llms.txt
- group: other
  href: https://artifacts.apis.io/kulalabs-ch/a2a/kulalabs-ch-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/kulalabs-ch-a2a.yml
- group: agent
  href: https://artifacts.apis.io/kulalabs-ch/mcp/kulalabs-ch-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/kulalabs-ch-mcp.yml
- group: auth
  href: https://artifacts.apis.io/kulalabs-ch/well-known/kulalabs-ch-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/kulalabs-ch-security.txt
- group: auth
  href: https://artifacts.apis.io/kulalabs-ch/well-known/kulalabs-ch-pazair-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/kulalabs-ch-pazair-security.txt
- group: auth
  href: https://artifacts.apis.io/kulalabs-ch/well-known/kulalabs-ch-agents-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/kulalabs-ch-agents-security.txt
- group: agent
  href: https://artifacts.apis.io/kulalabs-ch/well-known/kulalabs-ch-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kulalabs-ch-well-known.yml
- group: other
  href: https://artifacts.apis.io/kulalabs-ch/hosts/kulalabs-ch-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kulalabs-ch-hosts.yml
- group: other
  href: https://artifacts.apis.io/kulalabs-ch/vendors/kulalabs-ch-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kulalabs-ch-vendors.yml
- group: auth
  href: https://artifacts.apis.io/kulalabs-ch/security/kulalabs-ch-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/kulalabs-ch-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/kulalabs-ch/security/kulalabs-ch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kulalabs-ch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kulalabs.ch/
- group: docs
  title: ''
  type: Documentation
  url: https://jobflow.kulalabs.ch/
- group: docs
  title: ''
  type: Documentation
  url: https://pazair.kulalabs.ch/
- group: docs
  title: ''
  type: Documentation
  url: https://agents.kulalabs.ch/
- group: docs
  title: ''
  type: APIReference
  url: https://agents.kulalabs.ch/openapi.json
- group: docs
  title: ''
  type: APIReference
  url: https://pazair.kulalabs.ch/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://kulalabs.ch/jobflow/
- group: operate
  title: ''
  type: Support
  url: https://kulalabs.ch/#kontakt
- group: commercial
  title: ''
  type: Pricing
  url: https://kulalabs.ch/jobflow/
created: '2026-10-30'
description: Kula Labs is a Swiss software studio based in Wallisellen, building transparent, auditable software solutions such as JOBFLOW for Swiss trades, PazAIr a marketplace for AI agents, and SUONE for water‑supply monitoring. The company emphasizes reproducible calculations, data provenance, and privacy‑first design.
image: https://kulalabs.ch/og-studio-v3.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at pazair.kulalabs.ch.
  name: kulalabs-ch MCP Server
  slug: kulalabs-ch-mcp-yml
modified: '2026-10-30'
name: kulalabs-ch
nav: Providers
network: true
overview: 'kulalabs-ch publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Jobflow API, PazAIr API, and Agents API. Tagged areas include Software, Artificial Intelligence, Water, Switzerland, and Automation.


  The kulalabs-ch catalog on APIs.io includes 1 Spectral governance ruleset.


  kulalabs-ch''s developer surface includes documentation, API reference, getting-started guide, support, pricing, and 21 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: kulalabs-ch API Rules
  rule_count: 10
  severity_counts:
    error: 7
    hint: 0
    info: 2
    warn: 1
  slug: kulalabs-ch-rules
score:
  band: emerging
  composite: 25.8
  coverage:
    artifact_dirs: 15
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 5.3
    contract_governance: 18.2
    contract_quality: 24.5
    developer_ergonomics: 23.1
    discoverability: 75.0
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - switzerland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 31.7
  provenance:
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/kulalabs-ch/kulalabs-ch-2026-11-03T134548.png
security:
- kind: domain-security
  name: Kulalabs Ch Domain Security
  slug: kulalabs-ch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Kulalabs Ch Vulnerability Disclosure
  slug: kulalabs-ch-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: job-create
  slug: kulalabs-ch-job-create
slug: kulalabs-ch
tags:
- Software
- Artificial Intelligence
- Water
- Switzerland
- Automation
website: https://kulalabs.ch/
---
