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
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Safeship provides API monitoring via its MCP server; the documentation is public but no machine‑readable spec is available.
  name: Safeship API
  slug: safeship-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/safeship-app/mcp/safeship-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/safeship-app-mcp.yml
- group: other
  href: https://artifacts.apis.io/safeship-app/hosts/safeship-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/safeship-app-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://safeship.app/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://safeship.app/legal/privacy
- group: start
  title: ''
  type: Login
  url: https://safeship.app/login
- group: company
  title: ''
  type: Blog
  url: https://safeship.app/blog
- group: auth
  href: https://artifacts.apis.io/safeship-app/security/safeship-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/safeship-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://safeship.app/
- group: docs
  title: ''
  type: Documentation
  url: https://safeship.app/features
- group: commercial
  title: ''
  type: Pricing
  url: https://safeship.app/pricing
coverage:
  checked: '2026-10-31'
  detail: The public documentation is readable but no OpenAPI, GraphQL, AsyncAPI, or other machine‑readable contract is published.
  evidence:
  - status: 200
    url: https://safeship.app/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Safeship provides real‑time API monitoring that validates response bodies, not just status codes. Users configure checks via natural‑language prompts to an AI‑powered MCP, receiving alerts via email, webhook, SMS or WhatsApp. The SaaS platform offers a 15‑day free trial, tiered pricing from €3/month, and supports multi‑region checks. Features include HTTPS endpoint monitoring, JSON response validation, and AI‑driven fix suggestions.
image: https://safeship.app/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.safeship.app requiring an API key.
  name: safeship-app MCP Server
  slug: safeship-app-mcp-yml
modified: '2026-10-31'
name: safeship-app
nav: Providers
network: true
overview: 'safeship-app is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Monitoring, AI Integration, Software-as-a-Service, Alerts, and Developer Tools.


  safeship-app''s developer surface includes engineering blog, documentation, pricing, and 7 more developer resources.'
random_paper: 17
rate_limits:
- limit_count: 0
  name: Safeship App Rate Limits
  slug: safeship-app-rate-limits
scopes:
- name: Safeship App Scopes
  scope_count: 0
  slug: safeship-app-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.3
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 18.3
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/safeship-app/safeship-app-2026-11-03T142630.png
security:
- kind: authentication
  name: Safeship App Authentication
  slug: safeship-app-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Safeship App Domain Security
  slug: safeship-app-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: safeship-app
tags:
- API Monitoring
- AI Integration
- Software-as-a-Service
- Alerts
- Developer Tools
website: https://safeship.app/
---
