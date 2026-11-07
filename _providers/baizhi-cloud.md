---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 19.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Financial data platform providing market and fundamental data via API.
  name: Financial Data API
  slug: financial-data-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/baizhi-cloud/mcp/baizhi-cloud-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/baizhi-cloud-mcp.yml
- group: agent
  href: https://artifacts.apis.io/baizhi-cloud/well-known/baizhi-cloud-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/baizhi-cloud-well-known.yml
- group: other
  href: https://artifacts.apis.io/baizhi-cloud/hosts/baizhi-cloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/baizhi-cloud-hosts.yml
- group: start
  title: ''
  type: Sandbox
  url: https://baizhi.cloud/console/apps
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chaitin
- group: auth
  href: https://artifacts.apis.io/baizhi-cloud/security/baizhi-cloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/baizhi-cloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://baizhi.cloud/
coverage:
  checked: '2026-11-02'
  detail: Landing page https://baizhi.cloud/landing/financial-api lists API usage but no published OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://baizhi.cloud/landing/financial-api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: 长亭百智云 (Changting Baizhi Cloud) provides an AI infrastructure platform that integrates online services, applications, and on‑premise solutions, enabling enterprises to rapidly build and deploy AI capabilities. The platform offers a suite of APIs, large‑model gateways, knowledge‑base services, document and web parsing, and AI skill hubs, supporting various AI models and enabling secure, scalable AI integration for business workflows.
image: https://baizhi.cloud/images/platform-logo.png
layout: provider
mcp_servers:
- description: Remote MCP server at model-evaluation.app.baizhi.cloud.
  name: 长亭百智云 MCP Server
  slug: baizhi-cloud-mcp-yml
modified: '2026-11-02'
name: 长亭百智云
nav: Providers
network: true
overview: '长亭百智云 is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Cloud, Platform, Enterprise, and Chinese.


  长亭百智云''s developer surface includes sandbox and 6 more developer resources.'
plans:
- name: Baizhi Cloud Plans Pricing
  plan_count: 0
  slug: baizhi-cloud-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Baizhi Cloud Rate Limits
  slug: baizhi-cloud-rate-limits
scopes:
- name: Baizhi Cloud Scopes
  scope_count: 0
  slug: baizhi-cloud-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 7.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 56.7
    operational_transparency: 2.6
  previous_composite: 8.5
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Baizhi Cloud Authentication
  slug: baizhi-cloud-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Baizhi Cloud Domain Security
  slug: baizhi-cloud-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: baizhi-cloud
tags:
- Artificial Intelligence
- Cloud
- Platform
- Enterprise
- Chinese
website: https://baizhi.cloud/
---
