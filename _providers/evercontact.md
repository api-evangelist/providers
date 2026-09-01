---
access_model:
  confidence: high
  label: Self-serve signup with 14-day free trial; API access is sales-gated
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - https://www.evercontact.com/pricing.html
  - https://www.evercontact.com/api.html
  - authentication
  trial: true
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
    error_semantics: false
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: REST API that extracts structured contact data from email signature text (parse), completes a known contact with verified details (enrich), retrieves canonical deduplicated person records, registers w
  name: Evercontact API
  slug: evercontact-api
artifact_total: 7
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
- group: commercial
  title: ''
  type: Plans
  url: plans/evercontact-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/evercontact-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/evercontact-packages.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/evercontact-data-model.yml
created: '2026-07-17'
description: Evercontact is an AI-powered contact intelligence platform that automatically extracts, enriches, and syncs contact data from email signatures across Google Workspace and Microsoft 365. A multilingual model parses names, titles, phone numbers, and postal addresses from the signature block of every email in 30+ languages, deduplicates and enriches the resulting person records, and continuously syndicates clean contacts to CRMs (Salesforce, HubSpot, Pipedrive, Zoho, Microsoft Dynamics, Attio) and address books. Evercontact also exposes a REST API (parse, enrich, contacts, webhooks, events) and a webhook event stream for custom integrations, with SOC 2 Type II, Google CASA Tier 2, and GDPR compliance.
image: https://www.evercontact.com/assets/favicon-32x32.png
layout: provider
mcp_servers:
- description: ''
  name: Evercontact MCP Server
  slug: evercontact-mcp-server
modified: '2026-08-14'
name: Evercontact
nav: Providers
network: true
overview: 'Evercontact publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Contact Management, Contact Data, Data Enrichment, and Email.


  The Evercontact catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Evercontact''s developer surface includes documentation, API reference, pricing, signup flow, engineering blog, support, authentication, and 21 more developer resources.'
plans:
- name: Evercontact Plans Pricing
  plan_count: 5
  slug: evercontact-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 3
  name: Evercontact Rate Limits
  slug: evercontact-rate-limits
score:
  band: strong
  composite: 56.3
  coverage:
    artifact_dirs: 16
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 52.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 65.8
  previous_composite: 56.3
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/evercontact/refs/heads/main/screenshots/evercontact-2026-07-25T213720.png
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
