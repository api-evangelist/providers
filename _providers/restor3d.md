---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The machine-readable surface served by restor3d's corporate website. It is a stock WordPress REST API (namespaces wp/v2, wp-abilities/v1, mcp, plus SEO/caching plugin namespaces) covering site content
  name: restor3d Website Content API (WordPress REST + MCP)
  slug: restor3d-website-content-api-wordpress-rest-mcp
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.restor3d.com/
- group: operate
  title: ''
  type: Support
  url: https://www.restor3d.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.restor3d.com/news-press/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.restor3d.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/restor3d
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.restor3d.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.restor3d.com/privacy-policy/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/restor3d-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/restor3d-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/restor3d-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/restor3d-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/restor3d-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/restor3d-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/restor3d-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/restor3d-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/restor3d-llms.txt
created: '2026-08-26'
description: restor3d is a Durham, North Carolina medical device manufacturer, founded in 2017 as a Duke University spinout, that designs and 3D-prints personalized musculoskeletal implants and the single-use instrumentation that goes with them. The company unites additive manufacturing of osseointegrative titanium and cobalt-chrome lattices, biomechanics research, and AI-driven planning and design-automation software to produce patient-matched total ankle, total knee, total hip and shoulder reconstruction systems, plus foot-and-ankle and spine fixation devices. Manufacturing and design are vertically integrated in-house, and the company sponsors device performance research at Duke. restor3d is a regulated device maker rather than a software vendor - it publishes no developer portal, no product or clinical API, no SDKs and no public OpenAPI. The only machine-readable surface it serves is its own corporate WordPress site, which exposes the standard WordPress REST API and an OAuth-protected
  Model Context Protocol endpoint over site content.
image: https://www.restor3d.com/wp-content/uploads/2024/12/Main-Brand-Logo.svg
layout: provider
mcp_servers:
- description: ''
  name: restor3d Website MCP Server
  slug: restor3d-website-mcp-server
modified: '2026-08-26'
name: restor3d
nav: Providers
network: true
overview: 'restor3d publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Medical Devices, Health, Orthopedics, 3D Printing, and Additive Manufacturing.


  restor3d''s developer surface includes support, engineering blog, authentication, and 13 more developer resources.'
plans:
- name: Restor3D Plans Pricing
  plan_count: 0
  slug: restor3d-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Restor3D Rate Limits
  slug: restor3d-rate-limits
scopes:
- name: Restor3D Scopes
  scope_count: 0
  slug: restor3d-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 22.5
  coverage:
    artifact_dirs: 10
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 22.5
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Restor3D Authentication
  slug: restor3d-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Restor3D Domain Security
  slug: restor3d-domain-security
  summary_line: TLSv1.3 · DMARC
slug: restor3d
tags:
- Medical Devices
- Health
- Orthopedics
- 3D Printing
- Additive Manufacturing
- Implants
- Surgery
- Artificial Intelligence
- Manufacturing
- Company
website: https://www.restor3d.com/
---
