---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.5
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The Car-Cutter API is the public REST contract for CarCutter vehicle image processing. It covers vehicle inventory records and shot lists, synchronous single-image composition, asynchronous batch imag
  name: Car-Cutter API
  slug: carcutter-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/meero-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/meero-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.carcutter.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cloud.car-cutter.com/doc/api.html
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.car-cutter.com/doc/api.html
- group: docs
  title: ''
  type: APIReference
  url: https://cloud.car-cutter.com/doc/api.html
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/carcutter/carcutter-api-samples
- group: operate
  title: ''
  type: Support
  url: https://www.carcutter.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.carcutter.com/resources/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/carcutter
- group: start
  title: ''
  type: SignUp
  url: https://www.carcutter.com/book-a-demo/
- group: start
  title: ''
  type: Login
  url: https://hub.car-cutter.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.carcutter.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.carcutter.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://carcutter.statuspage.io/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/meero-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/meero-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/meero-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/meero-tool-crosswalk.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/meero-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/meero-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/meero-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/meero-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/meero-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/meero-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/meero-packages.yml
- group: design
  title: ''
  type: Components
  url: components/meero-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/meero-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/meero-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/meero-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/meero-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-25'
description: 'Meero is the Paris-founded AI visual-content company that rebranded to Diffusely in December 2024 after pivoting away from on-demand photography marketplaces toward vertical AI imaging software. Its surviving operating brand is CarCutter (DIFFUSELY Austria GmbH, whose API host still returns the copyright line "(c) 2026 Meero Austria GmbH"), a B2B vehicle merchandising platform used by dealership groups, OEMs and used-vehicle marketplaces for guided capture, AI backgrounding, 360 spins, feature hotspots and automated publishing. The public developer surface is the Car-Cutter API (OpenAPI 3.1, bearer token, api.car-cutter.com), a keyless public demo endpoint, an OAuth-gated remote MCP server, a WebPlayer web-component family on npm, and a Statuspage. Two former Diffusely verticals have since left the group: autoRetouch merged into Grand Shooting (February 2026) and ProperShot joined Nodalview, so neither of their APIs is attributed here.'
image: https://www.carcutter.com/wp-content/themes/carcutter/img/car-cutter-logo-25.svg
layout: provider
mcp_servers:
- description: ''
  name: CarCutter MCP Server
  slug: carcutter-mcp-server
modified: '2026-08-25'
name: Meero
nav: Providers
network: true
overview: 'Meero publishes 1 API on the [APIs.io](https://apis.io/) network: Car-Cutter API. Tagged areas include Automotive, Images, Artificial Intelligence, Computer Vision, and Photography.


  Meero''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 25 more developer resources.'
plans:
- name: Meero Plans Pricing
  plan_count: 0
  slug: meero-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Meero Rate Limits
  slug: meero-rate-limits
scopes:
- name: Meero Scopes
  scope_count: 0
  slug: meero-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 41.7
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 16.7
    contract_quality: 53.7
    developer_ergonomics: 58.9
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 34.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Meero Authentication
  slug: meero-authentication
  summary_line: http/oauth2/openIdConnect · 4 schemes
- kind: domain-security
  name: Meero Domain Security
  slug: meero-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: meero
tags:
- Automotive
- Images
- Artificial Intelligence
- Computer Vision
- Photography
- Media Processing
- E-Commerce
- Vehicle Merchandising
- Company
website: https://www.carcutter.com/
---
