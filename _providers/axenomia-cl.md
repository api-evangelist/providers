---
access_model:
  confidence: medium
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/axenomia-cl/vendors/axenomia-cl-vendors.yml
  title: ''
  type: Vendors
  url: vendors/axenomia-cl-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/axenomia-cl/plans/axenomia-cl-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/axenomia-cl-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/axenomia-cl/mcp/axenomia-cl-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/axenomia-cl-mcp.yml
- group: other
  href: https://artifacts.apis.io/axenomia-cl/hosts/axenomia-cl-hosts.yml
  title: ''
  type: Hosts
  url: hosts/axenomia-cl-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://axenomia.cl/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://axenomia.cl/privacy
- group: company
  title: ''
  type: Website
  url: https://axenomia.cl/
- group: auth
  href: https://artifacts.apis.io/axenomia-cl/security/axenomia-cl-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/axenomia-cl-domain-security.yml
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found despite probing known hosts.
  evidence:
  - status: 404
    url: https://axenomia.cl/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: 'axenomia-cl is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://axenomia.cl/assets/axenomia-share-es.png
layout: provider
mcp_servers:
- description: Remote MCP server at axenomia.cl.
  name: axenomia-cl MCP Server
  slug: axenomia-cl-mcp-yml
modified: '2026-11-02'
name: axenomia-cl
nav: Providers
network: true
overview: axenomia-cl is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
plans:
- name: Axenomia Cl Plans Pricing
  plan_count: 3
  slug: axenomia-cl-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Axenomia Cl Rate Limits
  slug: axenomia-cl-rate-limits
scopes:
- name: Axenomia Cl Scopes
  scope_count: 0
  slug: axenomia-cl-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 29.0
    catalog_earned_first_party: 12.0
    catalog_gap: 86.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 31.7
    operational_transparency: 0.0
  previous_composite: 15.0
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Axenomia Cl Authentication
  slug: axenomia-cl-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Axenomia Cl Domain Security
  slug: axenomia-cl-domain-security
  summary_line: TLSv1.3
slug: axenomia-cl
tags:
- Company
website: https://axenomia.cl/
---
