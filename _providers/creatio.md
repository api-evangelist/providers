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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-08-26'
api_count: 4
apis:
- description: OData 4 (recommended) and legacy OData 3 access to Creatio platform entities. The OData 4 service is at /0/odata with EDMX metadata at /0/odata/$metadata; supports $filter/$select/$expand/$orderby/$to
  name: Creatio OData API
  slug: creatio-odata-api
- description: 'RESTful DataService web service for reading and writing platform records via InsertQuery, SelectQuery, UpdateQuery, DeleteQuery, and BatchQuery over HTTP POST. Supports JSON/XML/CSV/JSV serialization '
  name: Creatio DataService API
  slug: creatio-dataservice-api
- description: ProcessEngineService.svc runs Creatio business processes from an external application over HTTP. Execute() runs a process by schema name, passing incoming parameters and returning the execution result
  name: Creatio Business Process Service
  slug: creatio-business-process-service
- description: Inbound webhook receiver. Lets an external app push data into Creatio in real time over an authenticated POST, writing a record into a target object named by the EntityName parameter. Contact, Lead, O
  name: Creatio Webhook Service
  slug: creatio-webhook-service
artifact_total: 10
asyncapis:
- description: ''
  name: Creatio Webhooks
  slug: creatio-webhooks
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
  url: https://www.creatio.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.creatio.com/privacy-policy
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
- group: auth
  title: ''
  type: Compliance
  url: security/creatio-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/creatio-trust-center.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/creatio-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/creatio-changelog.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/creatio-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/creatio-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/creatio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/creatio-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/creatio-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/creatio-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/creatio-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/creatio-error-codes.yml
created: '2026-07-17'
description: Creatio is a global software vendor of an AI-native no-code platform for customer relationship management (CRM) and workflow / business process automation. Its product line spans Sales Creatio, Marketing Creatio, and Service Creatio, built on Studio Creatio — a no-code toolkit with visual designers, AI agents, and a business process engine. Creatio serves banking, insurance, manufacturing, high tech, retail, CPG, pharmaceuticals, telecom, the public sector, and other industries. For integrations, Creatio exposes platform data and processes over an OData 4 service (recommended), a legacy OData 3 service, and the RESTful DataService web service, secured with forms (cookie) authentication via AuthService.svc or OAuth 2.0 through the Creatio Identity Service. Extensions and connectors are distributed through the Creatio Marketplace. This profile was enriched by the API Evangelist enrichment pipeline from Creatio's public developer documentation.
image: https://www.creatio.com/sites/default/files/creatio-logo.svg
layout: provider
modified: '2026-08-13'
name: Creatio
nav: Providers
network: true
overview: 'Creatio publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software-as-a-Service, CRM, No-Code, and Low-Code.


  The Creatio catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Creatio''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 22 more developer resources.'
plans:
- name: Creatio Plans Pricing
  plan_count: 3
  slug: creatio-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Creatio Rate Limits
  slug: creatio-rate-limits
score:
  band: strong
  composite: 59.5
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 64.3
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 55.3
  previous_composite: 59.5
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
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
- kind: trust-center
  name: Creatio Trust Center
  slug: creatio-trust-center
  summary_line: ISO/IEC 27001:2013, SOC 1, SOC 2, GDPR, HIPAA, FedRAMP
slug: creatio
tags:
- Company
- Software-as-a-Service
- CRM
- No-Code
- Low-Code
- Business Process Management
- Workflow-Automation
- Sales
- Marketing
- Customer Service
- OData
- AI Agents
website: https://www.creatio.com/
---
