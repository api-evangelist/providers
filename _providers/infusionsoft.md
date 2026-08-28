---
access_model:
  confidence: high
  label: Free developer sandbox with a paid production platform plan
  onboarding: unknown
  pricing: paid
  public: true
  source:
  - https://keap.com/pricing
  - https://developer.keap.com/resources/sandbox-application/
  - https://developer.keap.com/faqs/cost-become-developer-partner/
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.4
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 336
  human_in_the_loop: 3
  name: Infusionsoft Agentic Access
  operation_count: 585
  slug: infusionsoft-agentic-access
  summary_line: 585 operations · 336 acting · 3 human-in-the-loop
api_count: 4
apis:
- description: 'The default Keap REST API: 237 paths and 399 operations covering contacts, companies, tags, opportunities and stages, orders and order items, products, subscriptions and plans, notes, tasks, emails, a'
  name: Keap REST API v2
  slug: rest-v2
- description: 'The original Keap REST API, still labelled Current: 92 paths and 141 operations covering contacts, companies, orders, products, subscriptions, campaigns, appointments, files, tags, notes, tasks, affil'
  name: Keap REST API v1
  slug: rest-v1
- description: The Keap Pipelines (deals) API - 28 paths and 45 operations for deals, deal notes, deal custom fields, date expressions and bulk deal operations. Keap's own developer portal loads this as the Pipeline
  name: Keap Pipelines API
  slug: pipelines
- description: The legacy Infusionsoft XML-RPC API, explicitly labelled Deprecated in the Keap developer guide. It remains documented, with a published table schema reference, but Keap publishes no sunset date for i
  name: Infusionsoft XML-RPC API
  slug: xml-rpc
artifact_total: 12
asyncapis:
- description: ''
  name: Infusionsoft Rest Hooks Webhooks
  slug: infusionsoft-rest-hooks-webhooks
collections:
- collection_type: open
  name: SLAAPI
  slug: open-infusionsoft-pipelines
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/infusionsoft-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/infusionsoft-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/infusionsoft-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/infusionsoft-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/infusionsoft-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/infusionsoft-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/infusionsoft-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/infusionsoft-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/infusionsoft-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/infusionsoft-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/infusionsoft-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.keap.com/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/infusionsoft-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/infusionsoft-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/infusionsoft-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/infusionsoft-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/infusionsoft-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/infusionsoft-plans-pricing.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/infusionsoft-rest-hooks-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/2915979/UVByKWEZ
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.keap.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.keap.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.keap.com/docs/restv2/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.keap.com/developer-guide/
- group: learn
  title: ''
  type: Tutorials
  url: https://developer.keap.com/tutorials/
- group: operate
  title: ''
  type: FAQ
  url: https://developer.keap.com/faqs/
- group: operate
  title: ''
  type: Support
  url: https://developer.keap.com/get-support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://community.keap.com/c/api/5
- group: operate
  title: ''
  type: Developer Community
  url: https://integration.keap.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/infusionsoft
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/keap-growing
- group: company
  title: ''
  type: Website
  url: https://keap.com
- group: company
  title: ''
  type: Blog
  url: https://keap.com/small-business-automation-blog
- group: commercial
  title: ''
  type: Pricing
  url: https://keap.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://keap.com/free-trial
- group: start
  title: ''
  type: Login
  url: https://keys.developer.keap.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.thryv.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.thryv.com/privacy/
created: '2026-05-11'
description: 'Infusionsoft, now branded as Keap and owned by Thryv Holdings, is a sales and marketing automation CRM built for small businesses that combines contact management, tagging, email marketing, campaign and automation sequences, e-commerce orders and subscriptions, sales pipelines, appointments and invoicing in a single platform. Keap publishes three machine-readable REST contracts: a 399-operation OpenAPI 3.1 for REST v2, a 141-operation OpenAPI 3.1 for REST v1, and a separate 45-operation Pipelines (deals) API, alongside a deprecated XML-RPC surface. Everything authenticates as a bearer token, either an OAuth 2.0 authorization-code token or a Personal Access Token or Service Account Key. Keap''s event surface is REST Hooks and lives only on v1. There are no granular OAuth scopes and no idempotency keys anywhere in the API.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/infusionsoft.png
layout: provider
modified: '2026-08-13'
name: Infusionsoft (Keap)
nav: Providers
network: true
overview: 'Infusionsoft (Keap) publishes 3 APIs on the [APIs.io](https://apis.io/) network: Keap REST API v2, Keap REST API v1, and Keap Pipelines API. Tagged areas include CRM, Marketing Automation, Sales Automation, Email Marketing, and E-Commerce.


  The Infusionsoft (Keap) catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Infusionsoft (Keap)''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, FAQ, support, and 32 more developer resources.'
plans:
- name: Infusionsoft Plans Pricing
  plan_count: 1
  slug: infusionsoft-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 8
  name: Infusionsoft Rate Limits
  slug: infusionsoft-rate-limits
scopes:
- name: Infusionsoft Scopes
  scope_count: 0
  slug: infusionsoft-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 63.4
  delta: 0.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 16.7
    contract_quality: 68.4
    developer_ergonomics: 78.0
    discoverability: 74.1
    governance: 16.7
    operational_transparency: 50.0
  previous_composite: 63.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/infusionsoft/refs/heads/main/screenshots/infusionsoft-2026-06-20T183345.png
security:
- kind: authentication
  name: Infusionsoft Authentication
  slug: infusionsoft-authentication
  summary_line: oauth2/bearer · 3 schemes
- kind: domain-security
  name: Infusionsoft Domain Security
  slug: infusionsoft-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: infusionsoft
tags:
- CRM
- Marketing Automation
- Sales Automation
- Email Marketing
- E-Commerce
- Small Business
- Contacts
- Subscription
- Webhook
- Authentication
website: https://keap.com
---
