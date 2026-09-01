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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-01'
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
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Django instant-invoice-share API
  slug: open-hitchpin-instant-invoice-share-api
- collection_type: open
  name: Django instant-invoice-share instant-invoices API
  slug: open-hitchpin-instant-invoices-api
- collection_type: open
  name: Django instant-invoice-share rendering API
  slug: open-hitchpin-rendering-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/hitchpin-capability-edges.yml
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
  name: HitchPin MCP Server
  slug: hitchpin-mcp-server
modified: '2026-07-19'
name: HitchPin
nav: Providers
network: true
overview: 'HitchPin publishes 3 APIs on the [APIs.io](https://apis.io/) network: instant-invoice-share API, instant-invoices API, and rendering API. Tagged areas include Company, Marketplace, Agriculture, Livestock, and Hay and Forage.


  HitchPin''s developer surface includes documentation, getting-started guide, pricing, signup flow, support, authentication, sandbox, and 18 more developer resources.'
random_paper: 15
score:
  band: thin
  composite: 28.1
  coverage:
    artifact_dirs: 18
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 4.5
    contract_quality: 50.2
    developer_ergonomics: 30.4
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 28.1
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
    score: 26.6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
