---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 61.3
  scored_at: '2026-08-24'
api_count: 11
apis:
- description: Retrieve quotes and quote documents from DealHub, list quotes for a CRM opportunity, create renewal opportunities and read DealRoom signer status. The read side of the CPQ platform used to feed BI sys
  name: DealHub Quote API
  slug: dealhub-quote-api
- description: Generate, simulate, submit, publish and externally sign quotes entirely from a backend system with no user interaction in the DealHub UI, including the Actions API and the quote-template generator for
  name: DealHub Headless Quote API
  slug: dealhub-headless-api
- description: Authenticate a user from an external CRM into DealHub with a short-lived one-time access token, then create or open a quote and view quotes and opportunities through returned redirect URLs.
  name: DealHub CRM API
  slug: dealhub-crm-api
- description: Start, track, inspect and retry asynchronous imports of buyer accounts and contacts from a tenant's connected CRM into DealHub, with per-id lookup and aggregate success/failure counts.
  name: DealHub CRM Import API
  slug: dealhub-crm-import-api
- description: Retrieve DealHub users by login or by DealHub user id, list users, and create or update users in bulk through the v1 and v2 user provisioning endpoints.
  name: DealHub User API
  slug: dealhub-user-api
- description: Two-step PRM integration that authenticates a partner user from a partner relationship management system and returns redirect URLs to create a quote, open an existing quote, or view an opportunity's q
  name: DealHub Partner API
  slug: dealhub-partner-api
- description: Return the list of parameters required to price each SKU and return a calculated price per SKU, used to expose DealHub pricing logic to external systems.
  name: DealHub Pricing API
  slug: dealhub-pricing-api
- description: 'Manage DealHub configuration Versions and their product catalog — retrieve, duplicate and activate versions, export playbook data, read and upload the product catalog, patch catalog items, manage the '
  name: DealHub Version API
  slug: dealhub-version-api
- description: The subscription management, usage-based billing and revenue recognition API DealHub acquired with Subskribe — accounts, orders, subscriptions, plans and rate plans, charge types, usage records and ag
  name: DealHub Subskribe API
  slug: dealhub-subskribe-api
- description: The endpoint contract a DealHub customer implements on their own infrastructure so DealHub can send the current quote's playbook and product list to an external system and populate the returned data b
  name: DealHub External Query (inbound callback contract)
  slug: dealhub-external-query
- description: 'The endpoint contract a DealHub customer implements so DealHub can retrieve real-time product prices and attributes from an external system such as an ERP while a quote is being generated. The server '
  name: DealHub Callout API (inbound callback contract)
  slug: dealhub-callout-api
artifact_total: 30
asyncapis:
- description: ''
  name: Dealhub Webhooks
  slug: dealhub-webhooks
collections:
- collection_type: open
  name: Callout API
  slug: open-dealhub-callout-api
- collection_type: open
  name: CRM API
  slug: open-dealhub-crm-api
- collection_type: open
  name: CRM Import API
  slug: open-dealhub-crm-import-api
- collection_type: open
  name: External Query
  slug: open-dealhub-external-query
- collection_type: open
  name: Headless API
  slug: open-dealhub-headless-api
- collection_type: open
  name: Partner API
  slug: open-dealhub-partner-api
- collection_type: open
  name: Pricing API
  slug: open-dealhub-pricing-api
- collection_type: open
  name: Quote API
  slug: open-dealhub-quote-api
- collection_type: open
  name: Subskribe API
  slug: open-dealhub-subskribe-api
- collection_type: open
  name: User API
  slug: open-dealhub-user-api
- collection_type: open
  name: Version API
  slug: open-dealhub-version-api
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/dealhub-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://dealhub.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.dealhub.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.dealhub.io/docs/introduction-to-dealhub-apis
- group: docs
  title: ''
  type: APIReference
  url: https://developers.dealhub.io/reference/getquotebyid
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.dealhub.io/docs/introduction-to-dealhub-apis
- group: auth
  title: ''
  type: Authentication
  url: authentication/dealhub-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://dealhub.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://dealhub.io/pricing/
- group: commercial
  title: ''
  type: Plans
  url: plans/dealhub-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dealhub-rate-limits.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dealhub.io/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dealhub.io/enterprise-subscription-agreement-msa/
- group: auth
  title: ''
  type: Trust
  url: https://trust.dealhub.io/
- group: auth
  title: ''
  type: Compliance
  url: https://dealhub.io/security/
- group: auth
  title: ''
  type: Security
  url: https://dealhub.io/security/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dealhub-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dealhub-domain-security.yml
- group: operate
  title: ''
  type: Support
  url: https://support.dealhub.io/support/home/
- group: start
  title: ''
  type: Login
  url: https://login.dealhub.io/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/dealhub-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dealhub-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dealhub-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dealhub-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dealhub-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dealhub-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/dealhub-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dealhub-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/dealhub-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dealhub-llms.txt
created: '2026-08-12'
description: 'DealHub is an agentic quote-to-revenue platform that unifies CPQ (Configure, Price, Quote), CLM (contract lifecycle management), DealRoom digital sales rooms, subscription management, usage-based billing and revenue recognition. The platform is governed by the customer''s CRM — with native connectors for Salesforce, HubSpot and Microsoft Dynamics — and centers the quoting experience on a guided-selling Playbook that generates products, calculates pricing and applies discount and approval workflows automatically. DealHub publishes a public developer portal at developers.dealhub.io covering eleven OpenAPI 3.0.3 contracts: Quote, Headless Quote, Actions, CRM, CRM Import, User, Partner, Pricing and Version APIs on api.dealhub.io, the Subskribe billing and revenue API acquired with Subskribe on api.app.subskribe.com, plus two inbound callback contracts (External Query and Callouts) that customers implement so DealHub can pull real-time data and pricing from an external system during
  quote generation.'
image: https://cms.dealhub.io/wp-content/uploads/2026/02/HP-Thumbnail-1.png
layout: provider
mcp_servers:
- description: ''
  name: DealHub MCP Server
  slug: dealhub-mcp-server
modified: '2026-08-12'
name: DealHub
nav: Providers
network: true
overview: 'DealHub publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Quote API, Headless Quote API, CRM API, and 8 more. Tagged areas include Company, CPQ, Quote-to-Cash, Contract Lifecycle Management, and Subscription Management.


  The DealHub catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  DealHub''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, pricing, support, and 24 more developer resources.'
plans:
- name: Dealhub Plans Pricing
  plan_count: 0
  slug: dealhub-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Dealhub Rate Limits
  slug: dealhub-rate-limits
score:
  band: developing
  composite: 50.2
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 16.7
    contract_quality: 67.8
    developer_ergonomics: 54.2
    discoverability: 72.2
    governance: 16.7
    operational_transparency: 18.4
  previous_composite: 50.2
  provenance:
    conformance: derived
    contracts:
      callable: 90.9
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dealhub/refs/heads/main/screenshots/dealhub-2026-08-17T080848.png
security:
- kind: authentication
  name: Dealhub Authentication
  slug: dealhub-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Dealhub Domain Security
  slug: dealhub-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dealhub Vulnerability Disclosure
  slug: dealhub-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Dealhub Trust Center
  slug: dealhub-trust-center
  summary_line: ISO 42001, ISO 27701, ISO 27001, ISO 22301, SOC 1 Type II, SOC 2 Type II, CSA STAR Level 1, CSA STAR for AI Level 1
slug: dealhub
tags:
- Company
- CPQ
- Quote-to-Cash
- Contract Lifecycle Management
- Subscription Management
- Billing
- Revenue Operations
- Sales
- Pricing
- Usage-Based Billing
- Revenue Recognition
- Sales Enablement
website: https://dealhub.io/
---
