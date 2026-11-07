---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: false
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Aqueduct Agentic Access
  operation_count: 32
  slug: aqueduct-agentic-access
  summary_line: 32 operations · 19 acting
api_count: 1
apis:
- baseURL: https://api.tryaqueduct.com/v1
  baseurl_source: declared
  description: The AccountOwner API from Aqueduct — 3 operation(s) for accountowner.
  name: Aqueduct AccountOwner API
  slug: aqueduct-accountowner-api
- baseURL: https://api.tryaqueduct.com/v1
  baseurl_source: declared
  description: The Bill API from Aqueduct — 2 operation(s) for bill.
  name: Aqueduct Bill API
  slug: aqueduct-bill-api
- baseURL: https://api.tryaqueduct.com/v1
  baseurl_source: declared
  description: The Invoice API from Aqueduct — 6 operation(s) for invoice.
  name: Aqueduct Invoice API
  slug: aqueduct-invoice-api
- baseURL: https://api.tryaqueduct.com/v1
  baseurl_source: declared
  description: The PriceModel API from Aqueduct — 3 operation(s) for pricemodel.
  name: Aqueduct PriceModel API
  slug: aqueduct-pricemodel-api
- baseURL: https://api.tryaqueduct.com/v1
  baseurl_source: declared
  description: The ProductPurchases API from Aqueduct — 1 operation(s) for productpurchases.
  name: Aqueduct ProductPurchases API
  slug: aqueduct-productpurchases-api
- baseURL: https://api.tryaqueduct.com/v1
  baseurl_source: declared
  description: The Products API from Aqueduct — 2 operation(s) for products.
  name: Aqueduct Products API
  slug: aqueduct-products-api
- baseURL: https://api.tryaqueduct.com/v1
  baseurl_source: declared
  description: The Provisioning API from Aqueduct — 1 operation(s) for provisioning.
  name: Aqueduct Provisioning API
  slug: aqueduct-provisioning-api
- baseURL: https://api.tryaqueduct.com/v1
  baseurl_source: declared
  description: The Subscriptions API from Aqueduct — 2 operation(s) for subscriptions.
  name: Aqueduct Subscriptions API
  slug: aqueduct-subscriptions-api
- baseURL: https://api.tryaqueduct.com/v1
  baseurl_source: declared
  description: The Webhooks API from Aqueduct — 1 operation(s) for webhooks.
  name: Aqueduct Webhooks API
  slug: aqueduct-webhooks-api
- baseURL: https://api.tryaqueduct.com/v1
  baseurl_source: declared
  description: The Invoice Line Item API from Aqueduct — 1 operation(s) for invoice line item.
  name: Aqueduct Invoice Line Item API
  slug: aqueduct-invoice-line-item-api
artifact_total: 28
asyncapis:
- description: Event notifications delivered by Aqueduct to registered webhook endpoints. Each event is an HTTP POST carrying the shared envelope. Subscribe by creating a webhook endpoint (POST /webhookendpoints) wi
  name: Aqueduct Webhooks
  slug: aqueduct-webhooks-asyncapi
collections:
- collection_type: open
  name: Aqueduct API Reference AccountOwner API
  slug: open-aqueduct-accountowner-api
- collection_type: open
  name: Aqueduct API Reference AccountOwner Bill API
  slug: open-aqueduct-bill-api
- collection_type: open
  name: Aqueduct API Reference AccountOwner Invoice API
  slug: open-aqueduct-invoice-api
- collection_type: open
  name: Aqueduct API Reference AccountOwner InvoiceLineItem API
  slug: open-aqueduct-invoicelineitem-api
- collection_type: open
  name: Aqueduct API Reference AccountOwner PriceModel API
  slug: open-aqueduct-pricemodel-api
- collection_type: open
  name: Aqueduct API Reference AccountOwner ProductPurchases API
  slug: open-aqueduct-productpurchases-api
- collection_type: open
  name: Aqueduct API Reference AccountOwner Products API
  slug: open-aqueduct-products-api
- collection_type: open
  name: Aqueduct API Reference AccountOwner Provisioning API
  slug: open-aqueduct-provisioning-api
- collection_type: open
  name: Aqueduct API Reference AccountOwner Subscriptions API
  slug: open-aqueduct-subscriptions-api
- collection_type: open
  name: Aqueduct API Reference AccountOwner Webhooks API
  slug: open-aqueduct-webhooks-api
common:
- group: other
  href: https://artifacts.apis.io/aqueduct/capabilities/aqueduct-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/aqueduct-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/aqueduct/overlays/aqueduct-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aqueduct-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tryaqueduct.com/reference
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tryaqueduct.com/reference
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tryaqueduct.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tryaqueduct.com/reference/getting-started-with-your-api
- group: auth
  href: https://artifacts.apis.io/aqueduct/authentication/aqueduct-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aqueduct-authentication.yml
- group: design
  href: https://artifacts.apis.io/aqueduct/conventions/aqueduct-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aqueduct-conventions.yml
- group: design
  href: https://artifacts.apis.io/aqueduct/conventions/aqueduct-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/aqueduct-conventions.yml
- group: design
  href: https://artifacts.apis.io/aqueduct/asyncapi/aqueduct-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/aqueduct-webhooks-asyncapi.yml
- group: docs
  href: https://artifacts.apis.io/aqueduct/asyncapi/aqueduct-webhooks-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/aqueduct-webhooks-asyncapi.yml
- group: agent
  href: https://artifacts.apis.io/aqueduct/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/aqueduct/mcp/aqueduct-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/aqueduct-mcp.yml
- group: agent
  href: https://artifacts.apis.io/aqueduct/llms/aqueduct-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aqueduct-llms.txt
- group: design
  href: https://artifacts.apis.io/aqueduct/conformance/aqueduct-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aqueduct-conformance.yml
- group: design
  href: https://artifacts.apis.io/aqueduct/lifecycle/aqueduct-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aqueduct-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/aqueduct/security/aqueduct-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aqueduct-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/aqueduct/agentic-access/aqueduct-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aqueduct-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.tryaqueduct.com/
created: '2026-07-17'
description: Aqueduct is a fintech billing platform that equips B2B businesses with billing, invoicing, quoting, and accounting for usage-based and metered business models. Developers configure how they collect money as a PriceModel (composed of price functions such as per-unit meters), send billable usage events, and let Aqueduct create invoices and subscriptions, send invoices by email, issue refunds, and auto-provision access via signed webhooks. The REST API lives at api.tryaqueduct.com/v1 with API-key authentication and a documented Idempotency-Key contract. Founded 2020 in Bellevue, WA and backed by Bain Capital Ventures and Conversion Capital, Aqueduct was acquired by Stripe in August 2024; its ReadMe developer portal at docs.tryaqueduct.com remains live.
image: https://files.readme.io/9e3d7fe-small-Logo_4.png
layout: provider
modified: '2026-07-18'
name: Aqueduct
nav: Providers
network: true
overview: 'Aqueduct publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including AccountOwner API, Bill API, Invoice API, and 7 more. Tagged areas include Company, Fintech, Billing, Invoicing, and Metering.


  The Aqueduct catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Aqueduct''s developer surface includes documentation, API reference, getting-started guide, authentication, and 15 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: Aqueduct API Rules
  rule_count: 50
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 7
  slug: aqueduct-rules
score:
  band: thin
  composite: 36.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 5.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 55.2
    developer_ergonomics: 51.8
    discoverability: 73.2
    operational_transparency: 7.9
  previous_composite: 31.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 15.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/aqueduct/aqueduct-2026-07-25T200954.png
security:
- kind: authentication
  name: Aqueduct Authentication
  slug: aqueduct-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Aqueduct Domain Security
  slug: aqueduct-domain-security
  summary_line: DNSSEC · DMARC
skill_count: 3
skills:
- name: Issue and collect an invoice on Aqueduct
  slug: aqueduct-invoice-and-collect
- name: Set up usage-based billing on Aqueduct
  slug: aqueduct-metered-billing-setup
- name: Auto-provision on Aqueduct webhooks
  slug: aqueduct-provisioning-webhooks
slug: aqueduct
tags:
- Company
- Fintech
- Billing
- Invoicing
- Metering
- Usage-Based
- Subscription
- Payments
website: https://www.tryaqueduct.com/
---
