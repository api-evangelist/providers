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
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 51.0
  scored_at: '2026-07-27'
api_count: 11
apis:
- description: The canplug API from Farmers Edge — 1 operation(s) for canplug.
  name: Farmers Edge canplug API
  slug: farmers-edge-canplug-api
- description: The carbon API from Farmers Edge — 1 operation(s) for carbon.
  name: Farmers Edge carbon API
  slug: farmers-edge-carbon-api
- description: The client API from Farmers Edge — 7 operation(s) for client.
  name: Farmers Edge client API
  slug: farmers-edge-client-api
- description: The contact API from Farmers Edge — 2 operation(s) for contact.
  name: Farmers Edge contact API
  slug: farmers-edge-contact-api
- description: The gridcalc API from Farmers Edge — 1 operation(s) for gridcalc.
  name: Farmers Edge gridcalc API
  slug: farmers-edge-gridcalc-api
- description: The hefty API from Farmers Edge — 4 operation(s) for hefty.
  name: Farmers Edge hefty API
  slug: farmers-edge-hefty-api
- description: The integrations API from Farmers Edge — 1 operation(s) for integrations.
  name: Farmers Edge integrations API
  slug: farmers-edge-integrations-api
- description: The labcommand API from Farmers Edge — 3 operation(s) for labcommand.
  name: Farmers Edge labcommand API
  slug: farmers-edge-labcommand-api
- description: The payments API from Farmers Edge — 3 operation(s) for payments.
  name: Farmers Edge payments API
  slug: farmers-edge-payments-api
- description: The recengine API from Farmers Edge — 1 operation(s) for recengine.
  name: Farmers Edge recengine API
  slug: farmers-edge-recengine-api
- description: The token-login API from Farmers Edge — 1 operation(s) for token-login.
  name: Farmers Edge token-login API
  slug: farmers-edge-token-login-api
artifact_total: 14
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/farmers-edge-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/farmers-edge-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.farmcommand.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.farmcommand.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.farmcommand.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api.farmcommand.com/docs/
- group: design
  title: ''
  type: Conventions
  url: conventions/farmers-edge-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/farmers-edge-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/farmers-edge-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/farmers-edge-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/farmers-edge-lifecycle.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/farmers-edge-farmcommand-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/farmers-edge-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/farmers-edge-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Farmers Edge is a precision-agriculture and digital-farming company whose FarmCommand platform combines satellite imagery, connected weather stations, in-field telematics (the CanPlug IoT device), agronomic modeling, carbon-program tooling, and soil/lab products such as LabCommand and Hefty/FESoils. The public FarmCommand API is a Django REST (drf-yasg) service on admin.farmcommand.com that handles self-serve client onboarding and verification, token-based login for FarmCommand, LabCommand, GridCalc, RecEngine and Hefty users, password resets, CanPlug device lookup, and inbound integration webhooks (Stripe billing, DocuSign envelopes, LEAF field alerts). Authentication is a FarmCommand API token passed as a query parameter.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/farmers-edge.png
layout: provider
mcp_servers:
- description: ''
  name: farmers-edge-mcp.yml
  slug: farmers-edge-mcpyml
modified: '2026-07-19'
name: Farmers Edge
nav: Providers
network: true
overview: 'Farmers Edge publishes 11 APIs on the [APIs.io](https://apis.io/) network, including canplug API, carbon API, client API, and 8 more. Tagged areas include Company, Enterprise, Agriculture, Precision Agriculture, and AgTech.


  Farmers Edge''s developer surface includes authentication, documentation, API reference, and 12 more developer resources.'
random_paper: 46
score:
  band: emerging
  composite: 29.4
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 37.7
    developer_ergonomics: 50.0
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 29.4
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/farmers-edge/refs/heads/main/screenshots/farmers-edge-2026-07-25T214231.png
security:
- kind: authentication
  name: Farmers Edge Authentication
  slug: farmers-edge-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Farmers Edge Domain Security
  slug: farmers-edge-domain-security
  summary_line: TLSv1.3 · HSTS
slug: farmers-edge
tags:
- Company
- Enterprise
- Agriculture
- Precision Agriculture
- AgTech
- Farm Management
- Digital Agriculture
- IoT
- Weather
- Carbon
- API
website: https://www.farmcommand.com/
---
