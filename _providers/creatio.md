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
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-08-10'
api_count: 2
apis:
- description: OData 4 (recommended) and legacy OData 3 access to Creatio platform entities. The OData 4 service is at /0/odata with EDMX metadata at /0/odata/$metadata; supports $filter/$select/$expand/$orderby/$to
  name: Creatio OData API
  slug: creatio-odata-api
- description: 'RESTful DataService web service for reading and writing platform records via InsertQuery, SelectQuery, UpdateQuery, DeleteQuery, and BatchQuery over HTTP POST. Supports JSON/XML/CSV/JSV serialization '
  name: Creatio DataService API
  slug: creatio-dataservice-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.creatio.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://academy.creatio.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://academy.creatio.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://academy.creatio.com/docs/developer/integrations_and_api/data_services/odata/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://academy.creatio.com/docs/developer/integrations_and_api/integration_options
- group: operate
  title: ''
  type: Support
  url: https://community.creatio.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.creatio.com/services/support/options
- group: company
  title: ''
  type: Blog
  url: https://www.creatio.com/blog
- group: operate
  title: ''
  type: Roadmap
  url: https://www.creatio.com/product/roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://www.creatio.com/products/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.creatio.com/trial
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.creatio.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.creatio.com/legal/privacy-policy
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.creatio.com/
- group: operate
  title: ''
  type: Community
  url: https://community.creatio.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/creatio-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/creatio-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/creatio-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/creatio-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/creatio-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/creatio-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/creatio-llms.txt
created: '2026-07-17'
description: Creatio is a global software vendor of an AI-native no-code platform for customer relationship management (CRM) and workflow / business process automation. Its product line spans Sales Creatio, Marketing Creatio, and Service Creatio, built on Studio Creatio — a no-code toolkit with visual designers, AI agents, and a business process engine. Creatio serves banking, insurance, manufacturing, high tech, retail, CPG, pharmaceuticals, telecom, the public sector, and other industries. For integrations, Creatio exposes platform data and processes over an OData 4 service (recommended), a legacy OData 3 service, and the RESTful DataService web service, secured with forms (cookie) authentication via AuthService.svc or OAuth 2.0 through the Creatio Identity Service. Extensions and connectors are distributed through the Creatio Marketplace. This profile was enriched by the API Evangelist enrichment pipeline from Creatio's public developer documentation.
image: https://www.creatio.com/sites/default/files/creatio-logo.svg
layout: provider
modified: '2026-07-18'
name: Creatio
nav: Providers
network: true
overview: 'Creatio publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Saas, CRM, No-Code, and Low-Code.


  Creatio''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 15 more developer resources.'
random_paper: 47
score:
  band: thin
  composite: 30.3
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 52.2
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 30.3
  provenance:
    conformance: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/creatio/refs/heads/main/screenshots/creatio-2026-07-25T210701.png
security:
- kind: authentication
  name: Creatio Authentication
  slug: creatio-authentication
  summary_line: http/oauth2/cookie · 4 schemes
- kind: domain-security
  name: Creatio Domain Security
  slug: creatio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: creatio
tags:
- Company
- Saas
- CRM
- No-Code
- Low-Code
- Business Process Management
- Workflow Automation
- Sales
- Marketing
- Customer Service
- OData
- AI Agents
website: https://www.creatio.com/
---
