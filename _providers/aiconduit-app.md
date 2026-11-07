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
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
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
  score: 27.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://mcp.aiconduit.app
  baseurl_source: declared
  description: 'Conduit API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Conduit API
  slug: aiconduit-app-api
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/aiconduit-app/well-known/aiconduit-app-calendly-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aiconduit-app-calendly-security.txt
- group: design
  href: https://artifacts.apis.io/aiconduit-app/rules/aiconduit-app-rules.yml
  title: ''
  type: Spectral
  url: rules/aiconduit-app-rules.yml
- group: design
  href: https://artifacts.apis.io/aiconduit-app/vocabulary/aiconduit-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aiconduit-app-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/aiconduit-app/conformance/aiconduit-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aiconduit-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aiconduit-app/llms/aiconduit-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aiconduit-app-llms.txt
- group: other
  href: https://artifacts.apis.io/aiconduit-app/a2a/aiconduit-app-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/aiconduit-app-a2a.yml
- group: agent
  href: https://artifacts.apis.io/aiconduit-app/well-known/aiconduit-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aiconduit-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/aiconduit-app/hosts/aiconduit-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aiconduit-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/aiconduit-app/vendors/aiconduit-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aiconduit-app-vendors.yml
- group: auth
  href: https://artifacts.apis.io/aiconduit-app/security/aiconduit-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiconduit-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aiconduit.app/
- group: docs
  title: ''
  type: Documentation
  url: https://aiconduit.app/agents.md
- group: docs
  title: ''
  type: APIReference
  url: https://aiconduit.app/agent.txt
- group: start
  title: ''
  type: GettingStarted
  url: https://aiconduit.app/research
- group: operate
  title: ''
  type: Support
  url: https://calendly.com/yuri-goncharenko/new-meeting
- group: company
  title: ''
  type: Blog
  url: https://aiconduit.app/research/2026-q3
coverage:
  checked: '2026-11-01'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found despite accessible markdown documentation.
  evidence:
  - status: 404
    url: https://aiconduit.app/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Conduit provides an agentic procurement hub connecting businesses with over 13,000 merchants without fees. The platform monitors supply lines, ranks alternate suppliers, and enables agents to place orders within set limits, automating restocking and procurement workflows. It offers tools like MCP connectors, pipes, and a yard for managing vendor relationships, aiming to reduce risk and streamline B2B purchasing.
image: https://aiconduit.app/opengraph-image.png
layout: provider
modified: '2026-11-01'
name: Conduit
nav: Providers
network: true
overview: 'Conduit is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Procurement, B2B, Automation, Marketplace, and Artificial Intelligence.


  The Conduit catalog on APIs.io includes 1 Spectral governance ruleset.


  Conduit''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, and 11 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 64
  extends:
  - spectral:oas
  name: Conduit API Rules
  rule_count: 23
  severity_counts:
    error: 21
    hint: 0
    info: 1
    warn: 1
  slug: aiconduit-app-rules
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 14
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.5
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 11.7
    developer_ergonomics: 17.9
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 20.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
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
  name: Aiconduit App Domain Security
  slug: aiconduit-app-domain-security
  summary_line: TLSv1.3 · HSTS
slug: aiconduit-app
tags:
- Procurement
- B2B
- Automation
- Marketplace
- Artificial Intelligence
website: https://aiconduit.app/
---
