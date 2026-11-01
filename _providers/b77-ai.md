---
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 9.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/b77-ai/mcp/b77-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/b77-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/b77-ai/well-known/b77-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/b77-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/b77-ai/hosts/b77-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/b77-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/b77-ai/vendors/b77-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/b77-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://b77.ai/legal/terms
- group: auth
  title: ''
  type: Security
  url: https://b77.ai/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://b77.ai/legal/privacy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://b77.ai/apps/category/developer
- group: auth
  href: https://artifacts.apis.io/b77-ai/security/b77-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/b77-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://b77.ai/
- group: company
  title: ''
  type: Blog
  url: https://b77.ai/blog/
coverage:
  checked: '2026-10-29'
  detail: Probing common OpenAPI spec URLs on api.b77.ai returned 404, and no machine‑readable contract was found in the documentation.
  evidence:
  - status: 404
    url: https://api.b77.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: 'B77 is the app store for your AI assistant: hosted MCP apps for Claude, ChatGPT and Cursor — curated, OAuth-secured, EU-hosted. It helps companies still using paper, phone, and spreadsheets move onto AI rails with a 24/7 AI team. Private access is by request, offering automation, productivity, and enterprise‑grade solutions. The platform provides a digital team that can handle tasks, integrate with existing tools, and accelerate digital transformation for businesses of all sizes.'
image: https://b77.ai/favicon.svg
layout: provider
mcp_servers:
- description: Remote MCP server at api.b77.ai.
  name: b77-ai MCP Server
  slug: b77-ai-mcp-yml
modified: '2026-10-29'
name: b77-ai
nav: Providers
network: true
overview: 'b77-ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Automation, Enterprise, and Productivity.


  b77-ai''s developer surface includes engineering blog and 10 more developer resources.'
plans:
- name: B77 Ai Plans Pricing
  plan_count: 0
  slug: b77-ai-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: B77 Ai Rate Limits
  slug: b77-ai-rate-limits
scopes:
- name: B77 Ai Scopes
  scope_count: 0
  slug: b77-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 13.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.3
    operational_transparency: 10.5
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: B77 Ai Authentication
  slug: b77-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: B77 Ai Domain Security
  slug: b77-ai-domain-security
  summary_line: TLSv1.3 · HSTS
slug: b77-ai
tags:
- Company
- AI
- Automation
- Enterprise
- Productivity
- Private
website: https://b77.ai/
---
