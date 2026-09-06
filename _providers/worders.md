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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.9
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Worders Agentic Access
  operation_count: 13
  slug: worders-agentic-access
  summary_line: 13 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.worders.net
  baseurl_source: declared
  description: The Customers API from Worders — 1 operation(s) for customers.
  name: Worders Customers API
  slug: worders-customers-api
- baseURL: https://api.worders.net
  baseurl_source: declared
  description: The Freelancers API from Worders — 1 operation(s) for freelancers.
  name: Worders Freelancers API
  slug: worders-freelancers-api
- baseURL: https://api.worders.net
  baseurl_source: declared
  description: The Invoices API from Worders — 2 operation(s) for invoices.
  name: Worders Invoices API
  slug: worders-invoices-api
- baseURL: https://api.worders.net
  baseurl_source: declared
  description: The Orders API from Worders — 2 operation(s) for orders.
  name: Worders Orders API
  slug: worders-orders-api
- baseURL: https://api.worders.net
  baseurl_source: declared
  description: The PurchaseOrders API from Worders — 2 operation(s) for purchaseorders.
  name: Worders PurchaseOrders API
  slug: worders-purchaseorders-api
- baseURL: https://api.worders.net
  baseurl_source: declared
  description: The Quotes API from Worders — 2 operation(s) for quotes.
  name: Worders Quotes API
  slug: worders-quotes-api
- baseURL: https://api.worders.net
  baseurl_source: declared
  description: The Templates API from Worders — 1 operation(s) for templates.
  name: Worders Templates API
  slug: worders-templates-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Worders API V1 Customers API
  slug: open-worders-customers-api
- collection_type: open
  name: Worders API V1 Customers Freelancers API
  slug: open-worders-freelancers-api
- collection_type: open
  name: Worders API V1 Customers Invoices API
  slug: open-worders-invoices-api
- collection_type: open
  name: Worders API V1 Customers Orders API
  slug: open-worders-orders-api
- collection_type: open
  name: Worders API V1 Customers PurchaseOrders API
  slug: open-worders-purchaseorders-api
- collection_type: open
  name: Worders API V1 Customers Quotes API
  slug: open-worders-quotes-api
- collection_type: open
  name: Worders API V1 Customers Templates API
  slug: open-worders-templates-api
common:
- group: company
  title: ''
  type: Website
  url: https://worders.net/
- group: docs
  title: ''
  type: Documentation
  url: https://api.worders.net/api-docs/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://api.worders.net/api-docs/index.html
- group: start
  title: ''
  type: Login
  url: https://admin.worders.net/users/sign_in
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/worders/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/WordersNET
- group: auth
  title: ''
  type: Authentication
  url: authentication/worders-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/worders-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/worders-agentic-access.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/worders-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/worders-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/worders-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/worders-conformance.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/worders-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/worders-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/worders-api-overlay.yaml
- group: design
  title: ''
  type: DataModel
  url: data-model/worders-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Worders is a culturalization and localization company (a Partech portfolio company) that crafts translated, culturally-adapted content for global brands with in-country linguists. Alongside the services business it runs a Ruby on Rails translation-management platform (admin.worders.net) and publishes the Worders API V1 at api.worders.net — an OpenAPI 3.0.1-documented surface for freelance invoice verification and Plunet TMS automation covering customers, freelancers, invoices, orders, purchase orders, quotes, and order templates.
image: https://cdn.prod.website-files.com/67befd57da776c510ff3b66b/6830866136954deeba98bba4_worders_webclip.png
layout: provider
modified: '2026-07-21'
name: Worders
nav: Providers
network: true
overview: 'Worders publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Customers API, Freelancers API, Invoices API, and 4 more. Tagged areas include Company, Applicative Saas, Localization, Translation, and Culturalization.


  Worders'' developer surface includes documentation, API reference, authentication, and 15 more developer resources.'
random_paper: 18
score:
  band: thin
  composite: 27.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 4.5
    contract_quality: 49.1
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 27.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/worders/refs/heads/main/screenshots/worders-2026-09-02T170926.png
security:
- kind: authentication
  name: Worders Authentication
  slug: worders-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Worders Domain Security
  slug: worders-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: worders
tags:
- Company
- Applicative Saas
- Localization
- Translation
- Culturalization
- Language Services
- Invoicing
website: https://worders.net/
---
