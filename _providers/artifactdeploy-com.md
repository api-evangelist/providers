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
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Remote MCP server for ArtifactDeploy, enabling Claude AI to deploy artifacts via the MCP endpoint.
  name: ArtifactDeploy MCP
  slug: artifactdeploy-mcp
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/artifactdeploy-com/mcp/artifactdeploy-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/artifactdeploy-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/artifactdeploy-com/well-known/artifactdeploy-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/artifactdeploy-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/artifactdeploy-com/hosts/artifactdeploy-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/artifactdeploy-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/artifactdeploy-com/vendors/artifactdeploy-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/artifactdeploy-com-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://artifactdeploy.com/press
- group: start
  title: ''
  type: Login
  url: https://artifactdeploy.com/auth/signin
- group: auth
  href: https://artifacts.apis.io/artifactdeploy-com/security/artifactdeploy-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/artifactdeploy-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://artifactdeploy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://artifactdeploy.com/docs
- group: company
  title: ''
  type: Blog
  url: https://artifactdeploy.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://artifactdeploy.com/pricing
- group: company
  title: ''
  type: About
  url: https://artifactdeploy.com/about
- group: commercial
  title: ''
  type: TermsOfService
  url: https://artifactdeploy.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://artifactdeploy.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://artifactdeploy.com/contact
coverage:
  checked: '2026-11-02'
  detail: Documentation is publicly readable but no OpenAPI/GraphQL/AsyncAPI spec is published.
  evidence:
  - status: 200
    url: https://artifactdeploy.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: ArtifactDeploy is a platform that enables Claude AI users to instantly publish generated artifacts—such as web pages, dashboards, slide decks, markdown docs, and full‑site prototypes—to permanent, shareable URLs. It provides rich link previews on WhatsApp, LinkedIn, and other social channels, personal link analytics showing who opened each link and when, and a suite of templates and tools for freelancers, creators, small businesses, and teams. The service offers a free tier with no credit‑card required and paid plans with higher limits, custom domain support, and team collaboration features.
image: https://artifactdeploy.com/icon.svg
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.artifactdeploy.com.
  name: ArtifactDeploy MCP Server
  slug: artifactdeploy-com-mcp-yml
modified: '2026-11-01'
name: ArtifactDeploy
nav: Providers
network: true
overview: 'ArtifactDeploy is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, No-Code, Deployment, Templates, and Collaboration.


  ArtifactDeploy''s developer surface includes documentation, engineering blog, pricing, support, and 11 more developer resources.'
plans:
- name: Artifactdeploy Com Plans Pricing
  plan_count: 0
  slug: artifactdeploy-com-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Artifactdeploy Com Rate Limits
  slug: artifactdeploy-com-rate-limits
scopes:
- name: Artifactdeploy Com Scopes
  scope_count: 0
  slug: artifactdeploy-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.8
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 65.8
    operational_transparency: 0.0
  previous_composite: 20.8
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Artifactdeploy Com Authentication
  slug: artifactdeploy-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Artifactdeploy Com Domain Security
  slug: artifactdeploy-com-domain-security
  summary_line: TLSv1.3
slug: artifactdeploy-com
tags:
- Artificial Intelligence
- No-Code
- Deployment
- Templates
- Collaboration
website: https://artifactdeploy.com/
---
