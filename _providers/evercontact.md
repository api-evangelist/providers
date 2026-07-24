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
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: true
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 35.6
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: REST API that extracts structured contact data from email signature text (parse), completes a known contact with verified details (enrich), retrieves canonical deduplicated person records, registers w
  name: Evercontact API
  slug: evercontact-api
artifact_total: 5
asyncapis:
- description: ''
  name: Evercontact Webhooks
  slug: evercontact-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.evercontact.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.evercontact.com/api.html
- group: docs
  title: ''
  type: Documentation
  url: https://www.evercontact.com/api.html
- group: docs
  title: ''
  type: APIReference
  url: https://www.evercontact.com/api.html
- group: other
  title: ''
  type: HowItWorks
  url: https://www.evercontact.com/how-it-works.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.evercontact.com/pricing.html
- group: start
  title: ''
  type: SignUp
  url: https://www.evercontact.com/pricing.html
- group: company
  title: ''
  type: Blog
  url: https://blog.evercontact.com
- group: operate
  title: ''
  type: Support
  url: https://www.evercontact.com/contact.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.evercontact.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.evercontact.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.evercontact.com/privacy.html
- group: auth
  title: ''
  type: Security
  url: https://www.evercontact.com/security.html
- group: auth
  title: ''
  type: Compliance
  url: https://www.evercontact.com/dpa-compliance.html
- group: auth
  title: ''
  type: Authentication
  url: authentication/evercontact-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/evercontact-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/evercontact-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/evercontact-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/evercontact-mcp.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/evercontact-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/evercontact-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/evercontact-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/evercontact-llms.txt
- group: start
  title: ''
  type: Sandbox
  url: sandbox/evercontact-sandbox.yml
created: '2026-07-17'
description: Evercontact is an AI-powered contact intelligence platform that automatically extracts, enriches, and syncs contact data from email signatures across Google Workspace and Microsoft 365. A multilingual model parses names, titles, phone numbers, and postal addresses from the signature block of every email in 30+ languages, deduplicates and enriches the resulting person records, and continuously syndicates clean contacts to CRMs (Salesforce, HubSpot, Pipedrive, Zoho, Microsoft Dynamics, Attio) and address books. Evercontact also exposes a REST API (parse, enrich, contacts, webhooks, events) and a webhook event stream for custom integrations, with SOC 2 Type II, Google CASA Tier 2, and GDPR compliance.
image: https://www.evercontact.com/assets/favicon-32x32.png
layout: provider
mcp_servers:
- description: ''
  name: evercontact-mcp.yml
  slug: evercontact-mcpyml
modified: '2026-07-19'
name: Evercontact
nav: Providers
network: true
overview: 'Evercontact publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Contact Management, Contact Data, Data Enrichment, and Email.


  The Evercontact catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Evercontact''s developer surface includes documentation, API reference, pricing, signup flow, engineering blog, support, authentication, and 17 more developer resources.'
random_paper: 9
score:
  band: thin
  composite: 41.2
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 22.6
    developer_ergonomics: 56.5
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 41.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Evercontact Authentication
  slug: evercontact-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Evercontact Domain Security
  slug: evercontact-domain-security
  summary_line: TLSv1.3 · DMARC
slug: evercontact
tags:
- Company
- Contact Management
- Contact Data
- Data Enrichment
- Email
- Signature Parsing
- Data Extraction
- CRM
website: https://www.evercontact.com
---
