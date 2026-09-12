---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: true
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-09-12'
api_count: 2
apis:
- description: 'The private production API behind the Acelab Material Hub web application and Revit add-in. It is not a published developer product: no OpenAPI, no API reference and no key-issuance flow is published '
  name: Acelab Material Hub Platform API
  slug: acelab-material-hub-platform-api
- description: A remote, anonymously reachable Model Context Protocol server serving search and retrieval over Acelab's public documentation and webinar library. It is provided by the Mintlify documentation platform
  name: Acelab Documentation MCP Server
  slug: acelab-documentation-mcp-server
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.acelabusa.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.acelabusa.com/help-center
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.acelabusa.com/partner-help-center/getting-started/index
- group: operate
  title: ''
  type: Support
  url: https://www.acelabusa.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.acelabusa.com/resources
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.acelabusa.com/resources?type_equal=New+Features
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/acelab-usa
- group: commercial
  title: ''
  type: Pricing
  url: https://www.acelabusa.com/pricing/architect-designers
- group: start
  title: ''
  type: SignUp
  url: https://app.acelabusa.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.acelabusa.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.acelabusa.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acelabusa.com/privacy-policy
- group: other
  title: ''
  type: ContentSignal
  url: https://docs.acelabusa.com/robots.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/acelab-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/acelab-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/acelab-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/acelab-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/acelab-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/acelab-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/acelab-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/acelab-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/acelab-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/acelab-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acelab-domain-security.yml
created: '2026-09-06'
description: 'Acelab is a Brooklyn, New York software company building Material Hub, an AI-assisted material intelligence platform for the architecture, engineering, construction and owner (AECO) market. Founded in 2019 by architecture graduates from Harvard and MIT, the platform lets architects, designers, owners and manufacturer partners research, compare, specify, document and track building products across a database of more than 200,000 items, with SpecPlanner, Smart Docs, schedules, sustainability conformance and vendor management on top. Its marquee integration is a bi-directional Autodesk Revit add-in that syncs materials, families, keynotes and schedules between the model and the Material Hub library; ACC360, Procore, SharePoint and "custom API" integrations are sold only on the Enterprise tier. Acelab does not publish a public developer program: the production platform API answers Bearer-token challenges and its Swagger surface is protected by HTTP Basic auth, while the only anonymously
  reachable machine surface is a documentation-search MCP server on the docs host.'
image: https://cdn.prod.website-files.com/69975a27432ddb9dcf949f22/69a700a421be3d2a922e2752_acelab%20logo%20black.svg
layout: provider
mcp_servers:
- description: ''
  name: Acelab MCP Server
  slug: acelab-mcp-server
modified: '2026-09-06'
name: Acelab
nav: Providers
network: true
overview: 'Acelab publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Construction, Architecture, Building Materials, and Design.


  Acelab''s developer surface includes documentation, getting-started guide, support, engineering blog, changelog, pricing, signup flow, and 17 more developer resources.'
plans:
- name: Acelab Plans Pricing
  plan_count: 3
  slug: acelab-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Acelab Rate Limits
  slug: acelab-rate-limits
scopes:
- name: Acelab Scopes
  scope_count: 0
  slug: acelab-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 35.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 75.9
    operational_transparency: 18.4
  previous_composite: 35.5
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Acelab Authentication
  slug: acelab-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Acelab Domain Security
  slug: acelab-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: acelab
tags:
- Company
- Construction
- Architecture
- Building Materials
- Design
- Sustainability
- Product Data
- AECO
- Revit
- Specification
website: https://www.acelabusa.com/
---
