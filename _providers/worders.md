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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-11-06'
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
  description: The Quotes API from Worders — 2 operation(s) for quotes.
  name: Worders Quotes API
  slug: worders-quotes-api
- baseURL: https://api.worders.net
  baseurl_source: declared
  description: The Templates API from Worders — 1 operation(s) for templates.
  name: Worders Templates API
  slug: worders-templates-api
- baseURL: https://api.worders.net
  baseurl_source: declared
  description: The Purchase Orders API from Worders — 2 operation(s) for purchase orders.
  name: Worders Purchase Orders API
  slug: worders-purchase-orders-api
artifact_total: 21
collections:
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
- group: other
  href: https://artifacts.apis.io/worders/capabilities/worders-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/worders-capability-edges.yml
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
  href: https://artifacts.apis.io/worders/authentication/worders-authentication.yml
  title: ''
  type: Authentication
  url: authentication/worders-authentication.yml
- group: auth
  href: https://artifacts.apis.io/worders/security/worders-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/worders-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/worders/agentic-access/worders-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/worders-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/worders/errors/worders-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/worders-problem-types.yml
- group: design
  href: https://artifacts.apis.io/worders/conventions/worders-conventions.yml
  title: ''
  type: Conventions
  url: conventions/worders-conventions.yml
- group: design
  href: https://artifacts.apis.io/worders/lifecycle/worders-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/worders-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/worders/conformance/worders-conformance.yml
  title: ''
  type: Conformance
  url: conformance/worders-conformance.yml
- group: agent
  href: https://artifacts.apis.io/worders/mcp/worders-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/worders-mcp.yml
- group: agent
  href: https://artifacts.apis.io/worders/llms/worders-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/worders-llms.txt
- group: other
  href: https://artifacts.apis.io/worders/overlays/worders-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/worders-api-overlay.yaml
- group: design
  href: https://artifacts.apis.io/worders/data-model/worders-data-model.yml
  title: ''
  type: DataModel
  url: data-model/worders-data-model.yml
- group: agent
  href: https://artifacts.apis.io/worders/skills/_index.yml
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
overview: 'Worders publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Customers API, Freelancers API, Invoices API, and 4 more. Tagged areas include Company, Applicative Saas, Localization, Translation, and Culturalization.


  The Worders catalog on APIs.io includes 1 Spectral governance ruleset.


  Worders'' developer surface includes documentation, API reference, authentication, and 16 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Worders API Rules
  rule_count: 53
  severity_counts:
    error: 50
    hint: 0
    info: 1
    warn: 2
  slug: worders-rules
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
  delta: 1.3
  facets:
    access_clarity: 6.6
    contract_governance: 18.2
    contract_quality: 51.8
    developer_ergonomics: 30.4
    discoverability: 73.2
    operational_transparency: 0.0
  previous_composite: 34.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 66.7
screenshot: https://apis.io/screenshots/worders/worders-2026-09-02T170926.png
security:
- kind: authentication
  name: Worders Authentication
  slug: worders-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Worders Domain Security
  slug: worders-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Create a Plunet order from a customer template
  slug: worders-create-plunet-order
- name: Create and track a Plunet quote
  slug: worders-create-plunet-quote
- name: Verify a freelancer's invoice against their purchase orders
  slug: worders-verify-freelance-invoice
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
