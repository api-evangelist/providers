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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 7
  human_in_the_loop: 1
  name: Hitchpin Agentic Access
  operation_count: 11
  slug: hitchpin-agentic-access
  summary_line: 11 operations · 7 acting · 1 human-in-the-loop
api_count: 3
apis:
- description: Invoices shared with a buyer.
  name: HitchPin instant-invoice-share API
  slug: hitchpin-instant-invoice-share-api
- description: Invoices created by a seller.
  name: HitchPin instant-invoices API
  slug: hitchpin-instant-invoices-api
- description: The rendering API from HitchPin — 3 operation(s) for rendering.
  name: HitchPin rendering API
  slug: hitchpin-rendering-api
artifact_total: 9
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/hitchpin-django-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.hitchpin.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HitchPin
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/HitchPin/public-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.hitchpin.com/how-it-works
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hitchpin.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.hitchpin.com/accounts/register
- group: start
  title: ''
  type: Login
  url: https://www.hitchpin.com/accounts/login
- group: operate
  title: ''
  type: Support
  url: https://www.hitchpin.com/company/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hitchpin.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hitchpin.com/legal
- group: auth
  title: ''
  type: Authentication
  url: authentication/hitchpin-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hitchpin-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hitchpin-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hitchpin-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hitchpin-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hitchpin-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hitchpin-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hitchpin-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/hitchpin-instant-invoicing.md
- group: start
  title: ''
  type: Sandbox
  url: sandbox/hitchpin-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hitchpin-llms.txt
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/hitchpin-problem-details.schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/hitchpin-cloudevents.schema.json
created: '2026-07-17'
description: HitchPin is an online marketplace for the agriculture and rural economy, connecting farmers, ranchers, and rural businesses to buy and sell hay and forage, grain, cattle and livestock, farm and ranch equipment, trailers, land, and custom agricultural services. Sellers operate branded storefronts, send instant invoices, and collect payment, while buyers browse and purchase listings across the United States. HitchPin publishes public OpenAPI 3.1 definitions for its marketplace and instant-invoicing service, a receipt-rendering service, and a URL-shortcode service on GitHub. The company is backed by Foundry Group.
image: https://avatars.githubusercontent.com/u/38983146?v=4
json_schemas:
- name: Hitchpin Cloudevents.Schema
  property_count: 10
  slug: hitchpin-cloudevents.schema
- name: Hitchpin Problem Details.Schema
  property_count: 7
  slug: hitchpin-problem-details.schema
layout: provider
mcp_servers:
- description: ''
  name: hitchpin-mcp.yml
  slug: hitchpin-mcpyml
modified: '2026-07-19'
name: HitchPin
nav: Providers
network: true
overview: 'HitchPin publishes 3 APIs on the [APIs.io](https://apis.io/) network: instant-invoice-share API, instant-invoices API, and rendering API. Tagged areas include Company, Marketplace, Agriculture, Livestock, and Hay and Forage.


  HitchPin''s developer surface includes documentation, getting-started guide, pricing, signup flow, support, authentication, sandbox, and 17 more developer resources.'
random_paper: 43
score:
  band: thin
  composite: 41.0
  delta: -1.4
  facets:
    commercial_clarity: 44.7
    contract_quality: 52.8
    developer_ergonomics: 45.1
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 42.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hitchpin/refs/heads/main/screenshots/hitchpin-2026-07-25T221300.png
security:
- kind: authentication
  name: Hitchpin Authentication
  slug: hitchpin-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Hitchpin Domain Security
  slug: hitchpin-domain-security
  summary_line: TLSv1.3 · DMARC
slug: hitchpin
tags:
- Company
- Marketplace
- Agriculture
- Livestock
- Hay and Forage
- Farm Equipment
- Invoicing
- Payments
- Rural
website: https://www.hitchpin.com
---
