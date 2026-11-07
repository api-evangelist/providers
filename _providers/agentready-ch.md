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
- description: Read company profiles, discover available functions and send contact requests through agentready.ch.
  name: Agent Action API
  slug: agent-action-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/agentready-ch/plans/agentready-ch-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentready-ch-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agentready-ch/conformance/agentready-ch-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentready-ch-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentready-ch/llms/agentready-ch-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentready-ch-llms.txt
- group: build
  href: https://artifacts.apis.io/agentready-ch/mcp/agentready-ch-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/agentready-ch-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/agentready-ch/mcp/agentready-ch-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentready-ch-mcp.yml
- group: other
  href: https://artifacts.apis.io/agentready-ch/hosts/agentready-ch-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentready-ch-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentready-ch/vendors/agentready-ch-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentready-ch-vendors.yml
- group: auth
  href: https://artifacts.apis.io/agentready-ch/security/agentready-ch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentready-ch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentready.ch/
- group: start
  title: ''
  type: Login
  url: https://agentready.ch/login
- group: commercial
  title: ''
  type: Pricing
  url: https://agentready.ch/en/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentready.ch/en/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentready.ch/en/terms
created: '2026-11-01'
description: Agent-ready provides a Swiss directory of companies, making their information readable and contactable by AI agents like ChatGPT, Claude, and Perplexity. The platform structures business profiles so AI agents can understand offerings, sources, and contact details, offering analytics, managed implementation, and visibility audits for a subscription. It aims to improve AI visibility for SMEs in Switzerland, offering free verification calls and tiered pricing.
image: https://agentready.ch/opengraph-image
layout: provider
mcp_servers:
- description: Remote MCP server at agentready.ch.
  name: Agent-ready MCP Server
  slug: agentready-ch-mcp-yml
modified: '2026-11-01'
name: Agent-ready
nav: Providers
network: true
overview: 'Agent-ready is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Directory, Artificial Intelligence, Switzerland, and Software-as-a-Service.


  Agent-ready''s developer surface includes pricing and 12 more developer resources.'
plans:
- name: Agentready Ch Plans Pricing
  plan_count: 4
  slug: agentready-ch-plans-pricing
random_paper: 12
score:
  band: emerging
  composite: 17.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.0
  facets:
    access_clarity: 53.9
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 65.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - switzerland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 22.6
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
  name: Agentready Ch Domain Security
  slug: agentready-ch-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: agentready-ch
tags:
- Company
- Directory
- Artificial Intelligence
- Switzerland
- Software-as-a-Service
website: https://agentready.ch/
---
