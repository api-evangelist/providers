---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Platform hosting 469 MCP servers that expose APIs of popular SaaS tools across payments, CRM, messaging, healthcare, and DevOps.
  name: UsefulAPI MCP
  slug: usefulapi-mcp
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/usefulapi-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/usefulapi-io/llms/usefulapi-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/usefulapi-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/usefulapi-io/mcp/usefulapi-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/usefulapi-io-mcp.yml
- group: other
  href: https://artifacts.apis.io/usefulapi-io/hosts/usefulapi-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/usefulapi-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/usefulapi-io/vendors/usefulapi-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/usefulapi-io-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://usefulapi.io/category/media/
- group: auth
  href: https://artifacts.apis.io/usefulapi-io/security/usefulapi-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/usefulapi-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://usefulapi.io/
- group: company
  title: ''
  type: Blog
  url: https://usefulapi.io/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://usefulapi.io/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://usefulapi.io/terms/
- group: operate
  title: ''
  type: Support
  url: https://usefulapi.io/services/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usefulapi
coverage:
  checked: '2026-10-29'
  detail: MCP endpoint https://api.usefulapi.io/api/mcp returns 403, indicating the API contract is behind authentication.
  evidence:
  - status: 403
    url: https://api.usefulapi.io/api/mcp
  reason: partner-login
  state: gated
created: '2026-10-29'
description: UsefulAPI provides a platform hosting 469 remote MCP servers that expose APIs of popular SaaS tools across payments, CRM, messaging, healthcare, and DevOps. Users can access these services via standardized endpoints with a free tier and paid plans, enabling rapid integration without managing individual vendor credentials.
image: https://usefulapi.io/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.usefulapi.io.
  name: usefulapi-io MCP Server
  slug: usefulapi-io-mcp-yml
modified: '2026-10-29'
name: usefulapi-io
nav: Providers
network: true
overview: 'usefulapi-io is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, MCP, SaaS, API Hosting, and Developer Tools.


  usefulapi-io''s developer surface includes engineering blog, support, and 11 more developer resources.'
random_paper: 11
rate_limits:
- limit_count: 0
  name: Usefulapi Io Rate Limits
  slug: usefulapi-io-rate-limits
scopes:
- name: Usefulapi Io Scopes
  scope_count: 0
  slug: usefulapi-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.6
    discoverability: 58.3
    operational_transparency: 5.3
  provenance:
    conformance: unknown
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Usefulapi Io Authentication
  slug: usefulapi-io-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Usefulapi Io Domain Security
  slug: usefulapi-io-domain-security
  summary_line: TLSv1.3 · DMARC
slug: usefulapi-io
tags:
- Company
- MCP
- SaaS
- API Hosting
- Developer Tools
website: https://usefulapi.io/
---
