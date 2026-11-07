---
access_model:
  confidence: high
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
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
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Apdf provides a REST API for PDF processing, tracking, analytics, and related operations.
  name: PDF Processing API
  slug: pdf-processing-api
artifact_total: 7
common:
- group: operate
  href: https://artifacts.apis.io/apdf-io/rate-limits/apdf-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/apdf-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/apdf-io/plans/apdf-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apdf-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/apdf-io/conventions/apdf-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/apdf-io-conventions.yml
- group: auth
  href: https://artifacts.apis.io/apdf-io/authentication/apdf-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apdf-io-authentication.yml
- group: agent
  href: https://artifacts.apis.io/apdf-io/llms/apdf-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apdf-io-llms.txt
- group: build
  href: https://artifacts.apis.io/apdf-io/mcp/apdf-io-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/apdf-io-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/apdf-io/mcp/apdf-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/apdf-io-mcp.yml
- group: agent
  href: https://artifacts.apis.io/apdf-io/well-known/apdf-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apdf-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/apdf-io/hosts/apdf-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apdf-io-hosts.yml
- group: auth
  href: https://artifacts.apis.io/apdf-io/security/apdf-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apdf-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apdf.io/
- group: docs
  title: ''
  type: Documentation
  url: https://apdf.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://apdf.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://apdf.io/tutorials
- group: operate
  title: ''
  type: Support
  url: https://apdf.io/support
- group: commercial
  title: ''
  type: Pricing
  url: https://apdf.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://apdf.io/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apdf.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apdf.io/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apdf-io
coverage:
  checked: '2026-10-30'
  detail: The provider's public documentation (https://apdf.io/docs.md) lists a Base URL but no machine‑readable OpenAPI, AsyncAPI, GraphQL, or other spec.
  evidence:
  - status: 200
    url: https://apdf.io/docs.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Apdf provides a PDF generation and analytics API that lets developers create PDFs, embed tracking links, and receive real-time reader interaction events. The service includes a hosted viewer, per-recipient analytics, webhooks, and an MCP for agents. It is EU-hosted, offers a free plan, and targets SaaS applications, AI agents, and business workflows.
image: https://apdf.io/logo_light.png
layout: provider
mcp_servers:
- description: Remote MCP server at apdf.io requiring OAuth.
  name: apdf-io MCP Server
  slug: apdf-io-mcp-yml
modified: '2026-10-30'
name: apdf-io
nav: Providers
network: true
overview: 'apdf-io is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include PDF, Analytics, Software-as-a-Service, and Engagement.


  apdf-io''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, signup flow, and 13 more developer resources.'
plans:
- name: Apdf Io Plans Pricing
  plan_count: 10
  slug: apdf-io-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Apdf Io Rate Limits
  slug: apdf-io-rate-limits
scopes:
- name: Apdf Io Scopes
  scope_count: 0
  slug: apdf-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 26.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 52.0
    catalog_earned_first_party: 20.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.6
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 56.7
    operational_transparency: 23.7
  previous_composite: 36.4
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/apdf-io/apdf-io-2026-11-03T120922.png
security:
- kind: authentication
  name: Apdf Io Authentication
  slug: apdf-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Apdf Io Domain Security
  slug: apdf-io-domain-security
  summary_line: TLSv1.3 · DMARC
slug: apdf-io
tags:
- PDF
- Analytics
- Software-as-a-Service
- Engagement
website: https://apdf.io/
---
