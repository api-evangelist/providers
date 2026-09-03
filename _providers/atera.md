---
access_model:
  confidence: low
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Atera's REST API. Twelve data domains — Agents, Alerts, Billing, Contacts, Contracts, Customers, CustomValues, Departments, Devices, KnowledgeBase, Rates and Tickets — reachable over HTTPS only at htt
  name: Atera API v3
  slug: atera-api-v3
artifact_total: 5
asyncapis:
- description: ''
  name: Atera Webhooks
  slug: atera-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/atera-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.atera.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.atera.com/apidocs
- group: docs
  title: ''
  type: Documentation
  url: https://support.atera.com/hc/en-us/articles/219083397-Using-the-Atera-API
- group: docs
  title: ''
  type: APIReference
  url: https://app.atera.com/apidocs
- group: start
  title: ''
  type: GettingStarted
  url: https://support.atera.com/hc/en-us/articles/360019612194-Getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.atera.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.atera.com/hc/en-us
- group: operate
  title: ''
  type: Community
  url: https://community.atera.com/
- group: company
  title: ''
  type: Blog
  url: https://www.atera.com/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.atera.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.atera.com/hc/en-us/sections/201896227-Release-Notes
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.atera.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/atera-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.atera.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.atera.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.atera.com/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/atera-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/atera-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/atera-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/atera-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/atera-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/atera-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/atera-llms.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.atera.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atera.com/privacy/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/atera-changelog.yml
created: '2026-08-06'
description: Atera Networks Ltd. operates an all-in-one IT management platform that combines remote monitoring and management (RMM), professional services automation (PSA), helpdesk and ticketing, patch management, network discovery, remote access (Splashtop, AnyDesk, TeamViewer, ScreenConnect), reporting, and billing/invoicing in a single per-technician subscription used by managed service providers and internal IT departments. Its AI layer adds Action AI, AI Copilot, and Robin (IT Autopilot), and an AI Center that lets administrators install Model Context Protocol (MCP) integrations from a catalog or register custom MCP servers so Atera's own agents can reach outside systems. Atera is programmable through a versioned REST API at https://app.atera.com/api/v3 covering twelve data domains (agents, alerts, billing, contacts, contracts, customers, custom values, departments, devices, knowledge base, rates, tickets) authenticated with an X-API-KEY token, plus outbound webhooks bound to ticket
  automation rules. Atera states its API is driven by OpenAPI 3.0, but the interactive reference at https://app.atera.com/apidocs requires an account token before it will render and no specification is published at a public URL.
image: https://us.v-cdn.net/6037292/uploads/23NA1N62IAVU/atera-200x200.png
layout: provider
modified: '2026-08-06'
name: Atera
nav: Providers
network: true
overview: 'Atera publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include IT Management, RMM, PSA, Help Desk, and Ticketing.


  The Atera catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Atera''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, pricing, and 20 more developer resources.'
random_paper: 0
score:
  band: developing
  composite: 44.0
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 48.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 39.5
  previous_composite: 44.0
  provenance:
    conformance: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/atera/refs/heads/main/screenshots/atera-2026-08-07T161850.png
security:
- kind: authentication
  name: Atera Authentication
  slug: atera-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Atera Domain Security
  slug: atera-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Atera Trust Center
  slug: atera-trust-center
  summary_line: trust center published
slug: atera
tags:
- IT Management
- RMM
- PSA
- Help Desk
- Ticketing
- Patch Management
- Remote Monitoring
- Endpoint Management
- MSP
- Network Discovery
- Alerts
- Devices
- Billing
- Webhook
- Artificial Intelligence
website: https://www.atera.com/
---
