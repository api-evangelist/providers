---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    mcp_server: documented
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
  score: 3.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: ALPNAI Agent API for analyzing AI-agent measurements.
  name: ALPNAI Agent API
  slug: alpnai-agent-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/alpnai-com/plans/alpnai-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/alpnai-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/alpnai-com/conformance/alpnai-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/alpnai-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/alpnai-com/llms/alpnai-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alpnai-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/alpnai-com/mcp/alpnai-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/alpnai-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/alpnai-com/well-known/alpnai-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alpnai-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/alpnai-com/hosts/alpnai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alpnai-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/alpnai-com/vendors/alpnai-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alpnai-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alpnai.com/fr/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alpnai.com/fr/legal/privacy
- group: auth
  href: https://artifacts.apis.io/alpnai-com/security/alpnai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alpnai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alpnai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://alpnai.com/fr/docs
- group: docs
  title: ''
  type: APIReference
  url: https://alpnai.com/fr/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://alpnai.com/fr/docs/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://alpnai.com/fr/plans
- group: company
  title: ''
  type: About
  url: https://alpnai.com/fr/about
created: '2026-11-01'
description: ALPNAI is a Swiss‑based SaaS platform that provides economic and performance analysis for AI agents. It offers tools such as Spend Proof, Latency Lab, and Quality Gate to measure cost per successful task, latency, and quality thresholds. Users can compare configurations, generate audit reports, and integrate the service via its API. The product is developed in Geneva by Frederic Pure and targets developers and teams deploying AI agents.
layout: provider
mcp_servers:
- description: Remote MCP server at alpnai.com.
  name: ALPNAI MCP Server
  slug: alpnai-com-mcp-yml
modified: '2026-11-01'
name: ALPNAI
nav: Providers
network: true
overview: 'ALPNAI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Software-as-a-Service, Performance, Analytics, and Swiss.


  ALPNAI''s developer surface includes documentation, API reference, getting-started guide, pricing, and 12 more developer resources.'
plans:
- name: Alpnai Com Plans Pricing
  plan_count: 2
  slug: alpnai-com-plans-pricing
random_paper: 9
score:
  band: emerging
  composite: 16.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 43.0
    catalog_earned_first_party: 8.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.6
  facets:
    access_clarity: 36.8
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 61.7
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - switzerland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 23.3
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Alpnai Com Domain Security
  slug: alpnai-com-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: alpnai-com
tags:
- Artificial Intelligence
- Software-as-a-Service
- Performance
- Analytics
- Swiss
website: https://alpnai.com/
---
