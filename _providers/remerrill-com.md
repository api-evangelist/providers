---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Agent2Agent protocol surface: a JWS-signed (ES256, JWKS at /.well-known/jwks.json) A2A v1.0 agent card at https://www.remerrill.com/.well-known/agent-card.json declaring four skills — the pump line fi'
  name: RE Merrill Pump Application Agent (A2A)
  slug: pump-application-a2a-agent
- baseURL: https://www.remerrill.com/api
  baseurl_source: declared
  description: The same line finder over the Agent2Agent protocol v1.0 (JSON-RPC 2.0).
  name: R.E. Merrill & Associates A2A API
  slug: remerrill-com-a2a-api
- baseURL: https://www.remerrill.com/api
  baseurl_source: declared
  description: Deterministic pump line selection from curated, manufacturer-published performance data.
  name: R.E. Merrill & Associates Line Finder API
  slug: remerrill-com-line-finder-api
artifact_total: 10
common:
- group: other
  href: https://artifacts.apis.io/remerrill-com/overlays/remerrill-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/remerrill-com-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.remerrill.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.remerrill.com/llms.txt
- group: operate
  title: ''
  type: Support
  url: https://www.remerrill.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.remerrill.com/pump-notes
- group: other
  href: https://artifacts.apis.io/remerrill-com/a2a/remerrill-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/remerrill-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/remerrill-com/well-known/remerrill-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/remerrill-com-well-known.yml
- group: agent
  href: https://artifacts.apis.io/remerrill-com/llms/remerrill-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/remerrill-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/remerrill-com/mcp/remerrill-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/remerrill-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/remerrill-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/remerrill-com/conformance/remerrill-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/remerrill-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/remerrill-com/errors/remerrill-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/remerrill-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/remerrill-com/lifecycle/remerrill-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/remerrill-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/remerrill-com/conventions/remerrill-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/remerrill-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/remerrill-com/authentication/remerrill-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/remerrill-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/remerrill-com/data-model/remerrill-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/remerrill-com-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/remerrill-com/plans/remerrill-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/remerrill-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/remerrill-com/rate-limits/remerrill-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/remerrill-com-rate-limits.yml
- group: other
  href: https://artifacts.apis.io/remerrill-com/regulatory/remerrill-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/remerrill-com-regulatory-posture.yml
- group: auth
  href: https://artifacts.apis.io/remerrill-com/security/remerrill-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/remerrill-com-domain-security.yml
created: '2026-09-19'
description: 'R.E. Merrill & Associates, Inc. is a Texas industrial pump distributor and manufacturers'' representative (founded in Houston in 1987 by Ron Merrill Sr., led since 2020 by Ron Merrill Jr.; based in Wimberley, TX) that applies, quotes and supports 13 pump lines — Vanton thermoplastic pumps (exclusive Texas representative for 30+ years), Grundfos dosing and multistage pumps, Continental progressing cavity pumps, DP Pumps, Pinnacle-Flo, Vertiflo, Simtech, TF Seals, Garbarino, GreenPumps, Pemo, Victor and Walrus — for chemical processing, semiconductor, water/wastewater, boiler and petrochemical service. It publishes one machine-callable capability: a deterministic pump line finder that takes a pumping duty (fluid, flow, pressure or head, service) and returns which represented lines fit, citing the manufacturer catalog page for the smallest covering model, then hands off to a human engineer for quotation. The capability is exposed as an unauthenticated REST endpoint (POST https://www.remerrill.com/api/line-finder)
  and as an Agent2Agent v1.0 agent (JSON-RPC 2.0 at /api/a2a) with a JWS-signed agent card at /.well-known/agent-card.json, a published JWKS, and an llms.txt as its developer documentation. No pricing is returned by the API; quotes come from an engineer.'
image: https://www.remerrill.com/icon.png
layout: provider
mcp_servers:
- description: 'R.E. Merrill ships NO MCP server. Probed 2026-09-19: /mcp and /api/mcp both return the site''s real 404; a JSON-RPC tools/list posted to the A2A endpoint /api/a2a returns -32601 Method not found; no MC'
  name: R.E. Merrill & Associates MCP Server
  slug: remerrill-line-finder
modified: '2026-09-19'
name: R.E. Merrill & Associates
nav: Providers
network: true
overview: 'R.E. Merrill & Associates publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including A2A API, Line Finder API, and 1 more. Tagged areas include Industrial Pumps, Pump Selection, Industrial Equipment, Chemical Processing, and Manufacturing.


  The R.E. Merrill & Associates catalog on APIs.io includes 1 Spectral governance ruleset.


  R.E. Merrill & Associates'' developer surface includes documentation, support, engineering blog, authentication, and 16 more developer resources.'
plans:
- name: Remerrill Com Plans Pricing
  plan_count: 0
  slug: remerrill-com-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Remerrill Com Rate Limits
  slug: remerrill-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: R.E. Merrill & Associates API Rules
  rule_count: 53
  severity_counts:
    error: 51
    hint: 0
    info: 1
    warn: 1
  slug: remerrill-com-rules
score:
  band: emerging
  composite: 20.1
  coverage:
    artifact_dirs: 24
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 31.8
    contract_quality: 13.4
    developer_ergonomics: 30.4
    discoverability: 73.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 20.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/remerrill-com/remerrill-com-2026-10-11T125113.png
security:
- kind: authentication
  name: Remerrill Com Authentication
  slug: remerrill-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Remerrill Com Domain Security
  slug: remerrill-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: remerrill-com-find-pump-line
  slug: remerrill-com-find-pump-line
slug: remerrill-com
tags:
- Industrial Pumps
- Pump Selection
- Industrial Equipment
- Chemical Processing
- Manufacturing
- Distribution
- Agents
- A2A
- Agent-Native
- Texas
- United States
website: https://www.remerrill.com/
---
