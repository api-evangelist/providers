---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://public.api.serval.com
  baseurl_source: declared
  description: The Auth API API from Serval — 1 operation(s) for auth api.
  name: Serval Auth API
  slug: serval-auth-api-api
artifact_total: 10
asyncapis:
- description: ''
  name: Serval Webhooks
  slug: serval-webhooks
collections:
- collection_type: open
  name: API Spec Auth API API
  slug: open-serval-auth-api-api
common:
- group: commercial
  href: https://artifacts.apis.io/serval/plans/serval-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/serval-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://www.serval.com/feed.xml
- group: auth
  href: https://artifacts.apis.io/serval/security/serval-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/serval-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.serval.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.serval.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.serval.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.serval.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.serval.com/sections/documentation/overview/welcome
- group: operate
  title: ''
  type: Support
  url: https://docs.serval.com/sections/documentation/platform/support
- group: company
  title: ''
  type: Blog
  url: https://www.serval.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.serval.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.serval.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.serval.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.serval.com/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ServalHQ
- group: operate
  href: https://artifacts.apis.io/serval/changelog/serval-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/serval-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.serval.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.serval.com/
- group: agent
  href: https://artifacts.apis.io/serval/mcp/serval-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/serval-mcp.yml
- group: build
  href: https://artifacts.apis.io/serval/cli/serval-cli.yml
  title: ''
  type: CLI
  url: cli/serval-cli.yml
- group: agent
  href: https://artifacts.apis.io/serval/llms/serval-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/serval-llms.txt
- group: agent
  href: https://artifacts.apis.io/serval/well-known/serval-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/serval-well-known.yml
- group: design
  href: https://artifacts.apis.io/serval/lifecycle/serval-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/serval-lifecycle.yml
created: '2026-07-17'
description: Serval is an AI-native IT service management (ITSM) platform for modern teams. It pairs an AI help-desk agent that resolves employee requests in Slack, Microsoft Teams, email, and a web portal with a separate admin-facing automation agent (Catalyst) that turns intent into deterministic, version-controlled TypeScript workflows. Serval covers ticketing, knowledge base, journeys (onboarding/offboarding), just-in-time access management with approval flows, campaigns, SLAs, and 130+ integrations. Its public REST API (v2), hosted MCP server, CLI, and webhooks let teams manage tickets, workflows, access, users, and audit logs programmatically, with US and EU data-residency regions.
finops:
- has_sources: true
  method: derived
  name: Serval Finops
  primary_unit: ''
  service_category: ''
  slug: serval-finops
  template: true
image: https://framerusercontent.com/images/V6k6fFCAJ2d3ZHM9P4chDQnDbY.png
layout: provider
mcp_servers:
- description: Remote MCP server at public.api.serval.com over HTTP; 4 tools listed.
  name: Serval MCP Server
  slug: serval
modified: '2026-10-06'
name: Serval
nav: Providers
network: true
overview: 'Serval publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Auth API. Tagged areas include Company, ITSM, Help Desk, Workflow Automation, and AI Agents.


  The Serval catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Serval''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, changelog, and 16 more developer resources.'
plans:
- name: Serval Plans Pricing
  plan_count: 0
  slug: serval-plans-pricing
random_paper: 5
scopes:
- name: Serval Scopes
  scope_count: 1
  slug: serval-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 53.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    contract_governance: 4.5
    contract_quality: 54.0
    developer_ergonomics: 64.3
    discoverability: 65.0
    operational_transparency: 44.7
  previous_composite: 53.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/serval/serval-2026-08-17T081819.png
security:
- kind: authentication
  name: Serval Authentication
  slug: serval-authentication
  summary_line: http-basic/http-bearer/oauth2 · 0 schemes
- kind: domain-security
  name: Serval Domain Security
  slug: serval-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Serval Trust Center
  slug: serval-trust-center
  summary_line: trust center published
slug: serval
tags:
- Company
- ITSM
- Help Desk
- Workflow Automation
- AI Agents
- Identity and Access Management
- Employee Support
- Ticketing
website: https://www.serval.com/
---
