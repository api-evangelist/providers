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
    well_known_catalog: true
  schema_version: '0.2'
  score: 8.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Proxykey API provides endpoints for managing API keys, generating passes, and viewing usage.
  name: Proxykey API
  slug: proxykey-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/proxykey-org/mcp/proxykey-org-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/proxykey-org-mcp.yml
- group: other
  href: https://artifacts.apis.io/proxykey-org/hosts/proxykey-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/proxykey-org-hosts.yml
- group: auth
  href: https://artifacts.apis.io/proxykey-org/security/proxykey-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/proxykey-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://proxykey.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.proxykey.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://proxykey.org/#start
coverage:
  checked: '2026-10-31'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on any discovered host.
  evidence:
  - status: 404
    url: https://api.proxykey.org/openapi.json
  - status: 404
    url: https://api.proxykey.org/swagger.json
  - status: 404
    url: https://api.proxykey.org/graphql
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Proxykey provides a secure vault for API keys, encrypting them with AES-256-GCM and allowing controlled, IP‑bound access tokens. The service works with major AI providers such as OpenAI, Anthropic, Google, Mistral, and Together, offering a single pass‑through key that can be revoked instantly. Users can generate a “pass” that limits usage, protects keys from leakage, and integrates into existing applications without exposing raw credentials. The platform includes a web portal (app.proxykey.org) for managing keys, viewing usage, and configuring limits.
image: https://proxykey.org/favicon.ico
layout: provider
mcp_servers:
- description: Remote MCP server at app.proxykey.org.
  name: proxykey-org MCP Server
  slug: proxykey-org-mcp-yml
modified: '2026-10-31'
name: proxykey-org
nav: Providers
network: true
overview: 'proxykey-org is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Security, API Management, Encryption, Key Vault, and Developer Tools.


  proxykey-org''s developer surface includes getting-started guide and 5 more developer resources.'
plans:
- name: Proxykey Org Plans Pricing
  plan_count: 0
  slug: proxykey-org-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Proxykey Org Rate Limits
  slug: proxykey-org-rate-limits
scopes:
- name: Proxykey Org Scopes
  scope_count: 0
  slug: proxykey-org-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.1
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 10.0
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/proxykey-org/proxykey-org-2026-11-03T141656.png
security:
- kind: authentication
  name: Proxykey Org Authentication
  slug: proxykey-org-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Proxykey Org Domain Security
  slug: proxykey-org-domain-security
  summary_line: TLSv1.3 · DMARC
slug: proxykey-org
tags:
- Security
- API Management
- Encryption
- Key Vault
- Developer Tools
website: https://proxykey.org/
---
