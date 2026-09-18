---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
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
  schema_version: '0.2'
  score: 42.5
  scored_at: '2026-09-17'
api_count: 1
apis:
- baseURL: https://api.car-cutter.com
  baseurl_source: declared
  description: Asynchronous API
  name: Meero Asynchronous API
  slug: meero-asynchronous-api
- baseURL: https://api.car-cutter.com
  baseurl_source: declared
  description: Feature API
  name: Meero Feature API
  slug: meero-feature-api
- baseURL: https://api.car-cutter.com
  baseurl_source: declared
  description: Synchronous API
  name: Meero Synchronous API
  slug: meero-synchronous-api
- baseURL: https://api.car-cutter.com
  baseurl_source: declared
  description: Vehicle API
  name: Meero Vehicle API
  slug: meero-vehicle-api
artifact_total: 10
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/meero/refs/heads/main/overlays/meero-carcutter-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/meero-carcutter-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/meero/refs/heads/main/security/meero-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/meero-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/meero/refs/heads/main/authentication/meero-authentication.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/meero/refs/heads/main/llms/meero-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/meero-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/meero/refs/heads/main/well-known/meero-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/meero-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/meero/refs/heads/main/mcp/meero-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/meero-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/meero/refs/heads/main/mcp/meero-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/meero-tool-crosswalk.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/meero/refs/heads/main/scopes/meero-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/meero-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/meero/refs/heads/main/conformance/meero-conformance.yml
  title: ''
  type: Conformance
  url: conformance/meero-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/meero/refs/heads/main/errors/meero-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/meero-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/meero/refs/heads/main/lifecycle/meero-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/meero-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/meero/refs/heads/main/conventions/meero-conventions.yml
  title: ''
  type: Conventions
  url: conventions/meero-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/meero/refs/heads/main/data-model/meero-data-model.yml
  title: ''
  type: DataModel
  url: data-model/meero-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/meero/refs/heads/main/packages/meero-packages.yml
  title: ''
  type: Packages
  url: packages/meero-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/meero/refs/heads/main/components/meero-components.yml
  title: ''
  type: Components
  url: components/meero-components.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/meero/refs/heads/main/sandbox/meero-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/meero-sandbox.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/meero/refs/heads/main/changelog/meero-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/meero-changelog.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/meero/refs/heads/main/plans/meero-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/meero-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/meero/refs/heads/main/rate-limits/meero-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/meero-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/meero/refs/heads/main/skills/_index.yml
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
overview: 'Meero publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Asynchronous API, Feature API, Synchronous API, and 1 more. Tagged areas include Automotive, Image, Artificial Intelligence, Computer-Vision, and Photography.


  Meero''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 26 more developer resources.'
plans:
- name: Meero Plans Pricing
  plan_count: 0
  slug: meero-plans-pricing
random_paper: 8
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
  composite: 42.5
  coverage:
    artifact_dirs: 23
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 6.6
    contract_governance: 4.5
    contract_quality: 56.9
    developer_ergonomics: 58.9
    discoverability: 75.9
    operational_transparency: 34.2
  previous_composite: 42.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://raw.githubusercontent.com/api-evangelist/meero/refs/heads/main/screenshots/meero-2026-09-02T150502.png
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
- Image
- Artificial Intelligence
- Computer-Vision
- Photography
- Media Processing
- E-Commerce
- Vehicle Merchandising
- Company
website: https://www.carcutter.com/
---
