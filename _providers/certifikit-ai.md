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
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/certifikit-ai/plans/certifikit-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/certifikit-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/certifikit-ai/llms/certifikit-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/certifikit-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/certifikit-ai/mcp/certifikit-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/certifikit-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/certifikit-ai/hosts/certifikit-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/certifikit-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/certifikit-ai/vendors/certifikit-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/certifikit-ai-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://certifikit.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://certifikit.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://certifikit.ai/sign-in
- group: company
  title: ''
  type: Blog
  url: https://certifikit.ai/blog
- group: auth
  href: https://artifacts.apis.io/certifikit-ai/security/certifikit-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/certifikit-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://certifikit.ai/
coverage:
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found despite public website and docs links.
  evidence:
  - status: 200
    url: https://certifikit.ai/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: CertifiKit provides certificate of insurance (COI) tracking software that verifies subcontractor and vendor insurance certificates against user‑defined requirements. It automates collection, validation, and renewal alerts for general liability, workers’ compensation, auto, and umbrella coverage, targeting general contractors and property managers who manage multiple vendors.
layout: provider
mcp_servers:
- description: Remote MCP server at certifikit.ai.
  name: CertifiKit MCP Server
  slug: certifikit-ai-mcp-yml
modified: '2026-11-03'
name: CertifiKit
nav: Providers
network: true
overview: 'CertifiKit is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include COI tracking, Contractor tools, Property Management, and Compliance Software.


  CertifiKit''s developer surface includes pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Certifikit Ai Plans Pricing
  plan_count: 4
  slug: certifikit-ai-plans-pricing
random_paper: 21
score:
  band: emerging
  composite: 12.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 12.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 48.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 36.7
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Certifikit Ai Domain Security
  slug: certifikit-ai-domain-security
  summary_line: TLSv1.3 · HSTS
slug: certifikit-ai
tags:
- COI tracking
- Contractor tools
- Property Management
- Compliance Software
website: https://certifikit.ai/
---
