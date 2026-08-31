---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.9
  scored_at: '2026-08-30'
api_count: 3
apis:
- description: An OAuth-protected Model Context Protocol server RunBuggy operates on its application host. Discovered by probe — it is not referenced from the public developer documentation. tools/list returns 401 i
  name: RunBuggy Data Science MCP Server
  slug: mcp-datascience
- description: Companies operations.
  name: RunBuggy Companies API
  slug: runbuggy-companies-api
- description: The Order operations.
  name: RunBuggy Orders API
  slug: runbuggy-orders-api
- description: The Token API from RunBuggy — 1 operation(s) for token.
  name: RunBuggy Token API
  slug: runbuggy-token-api
- description: The Vehicle Transfer Order operations.
  name: RunBuggy Vehicle Transfer Orders API
  slug: runbuggy-vehicle-transfer-orders-api
- description: Webhook operations.
  name: RunBuggy Webhooks API
  slug: runbuggy-webhooks-api
artifact_total: 19
asyncapis:
- description: ''
  name: Runbuggy Webhooks
  slug: runbuggy-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Companies API
  slug: open-runbuggy-companies-api
- collection_type: open
  name: Orders API
  slug: open-runbuggy-orders-api
- collection_type: open
  name: Authentication Token API
  slug: open-runbuggy-token-api
- collection_type: open
  name: Orders Vehicle Transfer Orders API
  slug: open-runbuggy-vehicle-transfer-orders-api
- collection_type: open
  name: Orders Webhooks API
  slug: open-runbuggy-webhooks-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/runbuggy-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/runbuggy-authentication-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://runbuggy.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.runbuggy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.runbuggy.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.runbuggy.com/docs/shipping/1b7acf7f4d493-orders
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.runbuggy.com/docs/shipping/e66c4d2e84e08-ship-vehicles
- group: auth
  title: ''
  type: Authentication
  url: authentication/runbuggy-authentication.yml
- group: operate
  title: ''
  type: Support
  url: https://support.runbuggy.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://runbuggy.com/runbuggy-blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://runbuggy.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/runbuggyinc
- group: start
  title: ''
  type: SignUp
  url: https://apps.runbuggy.com/runbuggy/spa-v2/#/workflows/onboarding/SignupProcess/
- group: start
  title: ''
  type: Login
  url: https://apps.runbuggy.com/runbuggy/spa-v2/#/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://runbuggy.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://runbuggy.com/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.runbuggy.com/
- group: auth
  title: ''
  type: Security
  url: security/runbuggy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/runbuggy-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/runbuggy-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/runbuggy-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/runbuggy-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/runbuggy-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/runbuggy-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/runbuggy-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/runbuggy-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/runbuggy-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/runbuggy-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/runbuggy-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/runbuggy-data-model.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/runbuggy-scopes.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/runbuggy-llms.txt
created: '2026-08-05'
description: RunBuggy is a Phoenix, Arizona based technology company operating an open, automotive-focused vehicle transportation marketplace and TMS that connects car shippers — dealers, auctions, OEMs, rental and fleet operators — with car haulers and transporters. Its products are the RunBuggy Marketplace (transportation-as-a-service for finding, moving and tracking a vehicle), RunBuggy HITCH (a cloud transportation management system that connects to an existing dealer or auction management system and transporter network), RunBuggy One (personal vehicle shipping) and RunBot (a generative-AI assistant applied to order resolution and delivery-exception prediction). RunBuggy publishes a public Shippers API — Swagger 2.0 definitions for Orders, Vehicle Transfer Orders, Gate Passes, Webhooks, Companies and Authentication — at docs.runbuggy.com, and operates an OAuth-protected Model Context Protocol server for its data-science surface.
image: https://runbuggy.com/wp-content/uploads/2019/05/logo.png
layout: provider
mcp_servers:
- description: ''
  name: RunBuggy MCP Server
  slug: runbuggy-mcp-server
modified: '2026-08-05'
name: RunBuggy
nav: Providers
network: true
overview: 'RunBuggy publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Companies API, Orders API, Token API, and 2 more. Tagged areas include Company, Automotive, Logistics, Transportation, and Vehicle Shipping.


  The RunBuggy catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  RunBuggy''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, signup flow, and 26 more developer resources.'
random_paper: 1
scopes:
- name: Runbuggy Scopes
  scope_count: 0
  slug: runbuggy-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 46.6
  coverage:
    artifact_dirs: 23
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 14.5
    commercial_clarity: 14.5
    contract_governance: 4.5
    contract_quality: 61.7
    developer_ergonomics: 63.7
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 52.6
  previous_composite: 46.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/runbuggy/refs/heads/main/screenshots/runbuggy-2026-08-17T081656.png
security:
- kind: authentication
  name: Runbuggy Authentication
  slug: runbuggy-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Runbuggy Domain Security
  slug: runbuggy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Runbuggy Vulnerability Disclosure
  slug: runbuggy-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Runbuggy Trust Center
  slug: runbuggy-trust-center
  summary_line: trust center published
slug: runbuggy
tags:
- Company
- Automotive
- Logistics
- Transportation
- Vehicle Shipping
- Marketplace
- Supply Chain
- Fleet
- TMS
- Freight
website: https://runbuggy.com/
---
