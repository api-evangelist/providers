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
  - sandbox
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.2
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 10
  human_in_the_loop: 10
  name: Denim Agentic Access
  operation_count: 19
  slug: denim-agentic-access
  summary_line: 19 operations · 10 acting · 10 human-in-the-loop
api_count: 1
apis:
- baseURL: https://app.denim.com/api
  baseurl_source: declared
  description: A company in our system includes Payees, Debtors, and Factoring companies. Companies records are available globally in our ecosystem and shared by other clients.
  name: Denim Companies API
  slug: denim-companies-api
- baseURL: https://app.denim.com/api
  baseurl_source: declared
  description: A debtor is your customer or shipper. They are the entity that will be paying the invoices. Debtors are a type of Company in our ecosystem and are associated to our shared client through Client-Debtor
  name: Denim Debtors API
  slug: denim-debtors-api
- baseURL: https://app.denim.com/api
  baseurl_source: declared
  description: A job is a collection of obligations (payables, receivables, and fees) associated with an invoice or purchase order.
  name: Denim Jobs API
  slug: denim-jobs-api
- baseURL: https://app.denim.com/api
  baseurl_source: declared
  description: Version 2. A job is a collection of obligations (payables, receivables, and fees) associated with an invoice or purchase order.
  name: Denim Jobs V2 API
  slug: denim-jobs-v2-api
- baseURL: https://app.denim.com/api
  baseurl_source: declared
  description: A payee is your contractor or carrier. They are the entity that needs to be paid for services. Payees are a type of Company in our ecosystem and are associated to our shared client through Client-Paye
  name: Denim Payees API
  slug: denim-payees-api
- baseURL: https://app.denim.com/api
  baseurl_source: declared
  description: Transactions are payments incoming, outgoing, netting, and adjustments. Transactions are are generally applied towards obligations.
  name: Denim Transactions API
  slug: denim-transactions-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Denim Public API Reference Documentation Companies API
  slug: open-denim-companies-api
- collection_type: open
  name: Denim Public API Reference Documentation Companies Debtors API
  slug: open-denim-debtors-api
- collection_type: open
  name: Denim Public API Reference Documentation Companies Jobs API
  slug: open-denim-jobs-api
- collection_type: open
  name: Denim Public API Reference Documentation Companies Jobs V2 API
  slug: open-denim-jobs-v2-api
- collection_type: open
  name: Denim Public API Reference Documentation Companies Payees API
  slug: open-denim-payees-api
- collection_type: open
  name: Denim Public API Reference Documentation Companies Transactions API
  slug: open-denim-transactions-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/denim-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://denim.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.denim.com/api/v1/documentation
- group: docs
  title: ''
  type: Documentation
  url: https://app.denim.com/api/v1/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://app.denim.com/api/v1/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://www.denim.com/denim-api-documents
- group: operate
  title: ''
  type: Support
  url: https://help.denim.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.denim.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.denim.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://info.denim.com/freightfactoring
- group: start
  title: ''
  type: Login
  url: https://app.denim.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.denim.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.denim.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.denim.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/denim-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/denim-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/denim-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/denim-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/denim-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/denim-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/denim-openapi-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/denim-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/denim-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/denim-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/denim-well-known.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/denim-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Denim (denim.com, formerly Axle Payments) is an all-in-one financial and back-office platform for freight brokers, trucking companies, and 3PLs. It provides freight factoring, invoicing, collections, carrier payments, and a fuel card, automating the broker back office and syncing two ways with transportation management systems. The Denim Public API (OpenAPI 3.0) exposes freight loads (jobs), debtors, payees, companies, factoring companies, and transactions, secured with an x-api-key header, so partners can create and quote jobs, onboard debtor/payee relationships, and reconcile transactions programmatically. Added to the API Evangelist network as a portfolio-company lead and enriched from the provider's public developer surface.
image: https://app.denim.com/apple-touch-icon.png
layout: provider
modified: '2026-07-18'
name: Denim
nav: Providers
network: true
overview: 'Denim publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Companies API, Debtors API, Jobs API, and 3 more. Tagged areas include Company, Freight, Factoring, Payments, and Logistics.


  Denim''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 20 more developer resources.'
random_paper: 0
score:
  band: developing
  composite: 46.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 58.8
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 46.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/denim/refs/heads/main/screenshots/denim-2026-07-25T211718.png
security:
- kind: authentication
  name: Denim Authentication
  slug: denim-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Denim Domain Security
  slug: denim-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: denim
tags:
- Company
- Freight
- Factoring
- Payments
- Logistics
- Trucking
- Fintech
- Back Office
website: https://denim.com/
---
