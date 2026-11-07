---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
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
  score: 15.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: JSON-RPC MCP server for Studio Pro customers to integrate AI agents.
  name: 2nd Brick MCP
  slug: 2nd-brick-mcp
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/2ndbrick-com/plans/2ndbrick-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/2ndbrick-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/2ndbrick-com/llms/2ndbrick-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/2ndbrick-com-llms.txt
- group: build
  href: https://artifacts.apis.io/2ndbrick-com/mcp/2ndbrick-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/2ndbrick-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/2ndbrick-com/mcp/2ndbrick-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/2ndbrick-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/2ndbrick-com/well-known/2ndbrick-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/2ndbrick-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/2ndbrick-com/hosts/2ndbrick-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/2ndbrick-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/2ndbrick-com/vendors/2ndbrick-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/2ndbrick-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://2ndbrick.com/terms
- group: operate
  title: ''
  type: Support
  url: https://2ndbrick.com/support
- group: start
  title: ''
  type: SignUp
  url: https://2ndbrick.com/sign-up?redirect_url=%2Fpricing
- group: docs
  title: ''
  type: Documentation
  url: https://2ndbrick.com/guides/company-brick-set-brief
- group: auth
  href: https://artifacts.apis.io/2ndbrick-com/security/2ndbrick-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/2ndbrick-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://2ndbrick.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://2ndbrick.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://2ndbrick.com/privacy
coverage:
  checked: '2026-10-31'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract found on any discovered host.
  evidence:
  - status: 404
    url: https://2ndbrick.com/openapi.json
  - status: 0
    url: https://api.2ndbrick.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: 2nd Brick designs custom LEGO brick sets for businesses, from logos and mascots to client gifts. Send a brief for a design by email in 12–24 hours, or design your own with AI. The service offers quick turnaround, AI‑assisted design tools, and a studio for ordering finished kits, targeting corporate branding, promotional gifts, and personal projects.
image: https://2ndbrick.com/og-image-v10.png
layout: provider
mcp_servers:
- description: Remote MCP server at 2ndbrick.com.
  name: 2nd Brick MCP Server
  slug: 2ndbrick-com-mcp-yml
modified: '2026-10-31'
name: 2nd Brick
nav: Providers
network: true
overview: '2nd Brick is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Custom, LEGO, Design, E-Commerce, and Artificial Intelligence.


  2nd Brick''s developer surface includes support, signup flow, documentation, pricing, and 11 more developer resources.'
plans:
- name: 2Ndbrick Com Plans Pricing
  plan_count: 1
  slug: 2ndbrick-com-plans-pricing
random_paper: 19
score:
  band: emerging
  composite: 16.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.5
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 23.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: 2Ndbrick Com Domain Security
  slug: 2ndbrick-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 2ndbrick-com
tags:
- Custom
- LEGO
- Design
- E-Commerce
- Artificial Intelligence
website: https://2ndbrick.com/
---
