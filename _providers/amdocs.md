---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.7
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Amdocs Agentic Access
  operation_count: 8
  slug: amdocs-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 1
apis:
- description: The Amdocs MarketONE API provides digital BSS capabilities for telecoms, supporting catalog management, order management, customer management, and digital service delivery. REST APIs enable integratio
  name: Amdocs MarketONE API
  slug: amdocs-marketone-api
- description: The Amdocs NetCracker OSS API provides network inventory management, network provisioning, and service assurance capabilities for telecom operators. REST and SOAP APIs support integration with network
  name: Amdocs NetCracker OSS API
  slug: amdocs-netcracker-oss-api
- baseURL: https://api.amdocs-dbs.com
  baseurl_source: declared
  description: Billing and invoice operations
  name: Amdocs Billing API
  slug: amdocs-billing-api
- baseURL: https://api.amdocs-dbs.com
  baseurl_source: declared
  description: Customer account management
  name: Amdocs Customers API
  slug: amdocs-customers-api
- baseURL: https://api.amdocs-dbs.com
  baseurl_source: declared
  description: Product catalog management
  name: Amdocs Products API
  slug: amdocs-products-api
- baseURL: https://api.amdocs-dbs.com
  baseurl_source: declared
  description: Subscription lifecycle management
  name: Amdocs Subscriptions API
  slug: amdocs-subscriptions-api
artifact_total: 93
asyncapis:
- description: The Amdocs connectX BSS Event API delivers real-time event notifications for telecom BSS operations including customer lifecycle events, subscription changes, billing events, and provisioning status u
  name: Amdocs connectX BSS Event API
  slug: amdocs-events-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amdocs connectX BSS Billing API
  slug: open-amdocs-billing-api
- collection_type: open
  name: Amdocs connectX BSS API
  slug: open-amdocs-connectx
- collection_type: open
  name: Amdocs connectX BSS Billing Customers API
  slug: open-amdocs-customers-api
- collection_type: open
  name: Amdocs connectX BSS Billing Products API
  slug: open-amdocs-products-api
- collection_type: open
  name: Amdocs connectX BSS Billing Subscriptions API
  slug: open-amdocs-subscriptions-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/amdocs-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amdocs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amdocs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amdocs-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/amdocs-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/amdocs
- group: company
  title: ''
  type: Website
  url: https://www.amdocs.com/
- group: start
  title: ''
  type: Portal
  url: https://devportal.amdocs-dbs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://knowledge.amdocs-dbs.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.amdocs-dbs.com/reference/getting-started-with-your-api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/open-amdocs
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/amdocs/refs/heads/main/json-schema/amdocs-customer-schema.json
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/amdocs/refs/heads/main/json-ld/amdocs-context.jsonld
created: '2026-03-18'
description: Amdocs is a global technology company providing software and services to communications and media companies worldwide. Its connectX platform is a cloud-native SaaS BSS solution for telecom operators covering customer management, billing, provisioning, and subscription lifecycle. Amdocs also provides MarketONE for digital BSS, NetCracker for OSS network management, and an expanding suite of AI-powered telco solutions built on TM Forum Open APIs.
examples:
- key_count: 14
  name: Amdocs Customer Example
  slug: amdocs-customer-example
- key_count: 5
  name: Connectx Address Example
  slug: connectx-address-example
- key_count: 13
  name: Connectx Customer Example
  slug: connectx-customer-example
- key_count: 2
  name: Connectx Customer List Example
  slug: connectx-customer-list-example
- key_count: 7
  name: Connectx Customer Request Example
  slug: connectx-customer-request-example
- key_count: 4
  name: Connectx Customer Update Example
  slug: connectx-customer-update-example
- key_count: 10
  name: Connectx Invoice Example
  slug: connectx-invoice-example
- key_count: 4
  name: Connectx Invoice Line Item Example
  slug: connectx-invoice-line-item-example
- key_count: 2
  name: Connectx Invoice List Example
  slug: connectx-invoice-list-example
- key_count: 4
  name: Connectx Pagination Example
  slug: connectx-pagination-example
- key_count: 8
  name: Connectx Product Example
  slug: connectx-product-example
- key_count: 1
  name: Connectx Product List Example
  slug: connectx-product-list-example
- key_count: 10
  name: Connectx Subscription Example
  slug: connectx-subscription-example
- key_count: 1
  name: Connectx Subscription List Example
  slug: connectx-subscription-list-example
- key_count: 3
  name: Connectx Subscription Request Example
  slug: connectx-subscription-request-example
features:
- description: All connectX APIs comply with TM Forum Open API standards, enabling fast integration with third-party systems and reducing customization requirements.
  name: TM Forum Open API Compliance
- description: GenAI-powered platform capabilities including AI-driven customer journeys, predictive analytics, and automated decision making for telco operations.
  name: AI-Native Capabilities
- description: Serverless microservices architecture deployed on AWS providing elastic scalability, local data residency compliance, and rapid deployment for MVNOs and telcos.
  name: Cloud-Native SaaS Architecture
- description: Built-in eSIM lifecycle management enabling telcos and MVNOs to support digital SIM provisioning without physical SIM cards.
  name: eSIM Management
- description: Pre-built customer journeys spanning mobile apps, web self-service, and multi-channel support for consumer and business segments.
  name: Omnichannel Customer Experience
- description: End-to-end MVNO and MVNE capabilities including wireless prepaid, postpaid, and B2C solutions with rapid market launch support.
  name: MVNO and MVNE Support
- description: Flexible product catalog management for bundling connectivity with digital services, plus end-to-end order management across consumer, business, and enterprise segments.
  name: Catalog and Order Management
- description: Converged billing, revenue assurance, and monetization capabilities supporting current and emerging revenue models including subscription and usage-based billing.
  name: Revenue Management
finops:
- name: Amdocs Finops
  service_category: Telecom Software
  slug: amdocs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amdocs.png
integrations:
- description: connectX is powered by Amazon Web Services providing cloud infrastructure, elastic scalability, and global reach.
  name: AWS
- description: Full compliance with TM Forum Open API standards enabling plug-and-play integration with ecosystem partners and third-party systems.
  name: TM Forum Open APIs
- description: Customer Engagement Platform partnership with Microsoft for AI-driven customer interactions and analytics.
  name: Microsoft
- description: Integration with multi-vendor network management systems and OSS platforms via NetCracker APIs.
  name: Network Management Systems
json_schemas:
- name: Amdocs Customer
  property_count: 14
  slug: amdocs-customer
- name: Address
  property_count: 5
  slug: connectx-address
- name: CustomerList
  property_count: 2
  slug: connectx-customer-list
- name: CustomerRequest
  property_count: 7
  slug: connectx-customer-request
- name: Customer
  property_count: 13
  slug: connectx-customer
- name: CustomerUpdate
  property_count: 4
  slug: connectx-customer-update
- name: InvoiceLineItem
  property_count: 4
  slug: connectx-invoice-line-item
- name: InvoiceList
  property_count: 2
  slug: connectx-invoice-list
- name: Invoice
  property_count: 10
  slug: connectx-invoice
- name: Pagination
  property_count: 4
  slug: connectx-pagination
- name: ProductList
  property_count: 1
  slug: connectx-product-list
- name: Product
  property_count: 8
  slug: connectx-product
- name: SubscriptionList
  property_count: 1
  slug: connectx-subscription-list
- name: SubscriptionRequest
  property_count: 3
  slug: connectx-subscription-request
- name: Subscription
  property_count: 10
  slug: connectx-subscription
json_structures:
- name: Amdocs Customer Structure
  property_count: 14
  slug: amdocs-customer-structure
- name: Connectx Address Structure
  property_count: 5
  slug: connectx-address-structure
- name: Connectx Customer List Structure
  property_count: 2
  slug: connectx-customer-list-structure
- name: Connectx Customer Request Structure
  property_count: 7
  slug: connectx-customer-request-structure
- name: Connectx Customer Structure
  property_count: 13
  slug: connectx-customer-structure
- name: Connectx Customer Update Structure
  property_count: 4
  slug: connectx-customer-update-structure
- name: Connectx Invoice Line Item Structure
  property_count: 4
  slug: connectx-invoice-line-item-structure
- name: Connectx Invoice List Structure
  property_count: 2
  slug: connectx-invoice-list-structure
- name: Connectx Invoice Structure
  property_count: 10
  slug: connectx-invoice-structure
- name: Connectx Pagination Structure
  property_count: 4
  slug: connectx-pagination-structure
- name: Connectx Product List Structure
  property_count: 1
  slug: connectx-product-list-structure
- name: Connectx Product Structure
  property_count: 8
  slug: connectx-product-structure
- name: Connectx Subscription List Structure
  property_count: 1
  slug: connectx-subscription-list-structure
- name: Connectx Subscription Request Structure
  property_count: 3
  slug: connectx-subscription-request-structure
- name: Connectx Subscription Structure
  property_count: 10
  slug: connectx-subscription-structure
jsonld:
- class_count: 4
  name: Amdocs Amdocs Context
  property_count: 11
  slug: amdocs-amdocs-context
- class_count: 18
  name: Amdocs Connectx Context
  property_count: 42
  slug: amdocs-connectx-context
- class_count: 0
  name: Amdocs Context
  property_count: 5
  slug: amdocs-context
layout: provider
modified: '2026-05-19'
name: Amdocs
nav: Providers
network: true
overview: 'Amdocs publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Billing API, Customers API, Products API, and 1 more. Tagged areas include Telecom, BSS, OSS, Billing, and Customer Management.


  The Amdocs catalog on APIs.io includes 1 event-driven AsyncAPI specification, 3 JSON-LD contexts, and 3 Spectral governance rulesets.


  Amdocs'' developer surface includes authentication, developer portal, documentation, getting-started guide, and 9 more developer resources.'
plans:
- name: Amdocs Plans Pricing
  plan_count: 1
  slug: amdocs-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Amdocs Rate Limits
  slug: amdocs-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Amdocs API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: amdocs-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Amdocs API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amdocs-jsonschema-spectral-rules
- effective_rule_count: 68
  extends:
  - spectral:oas
  name: Amdocs API Rules
  rule_count: 27
  severity_counts:
    error: 12
    hint: 0
    info: 4
    warn: 11
  slug: amdocs-spectral-rules
scopes:
- name: Amdocs Scopes
  scope_count: 4
  slug: amdocs-scopes
  summary_line: 4 scopes · clientCredentials
score:
  band: developing
  composite: 39.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 59.5
    catalog_earned_first_party: 0.0
    catalog_gap: 55.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 13.6
    contract_quality: 66.9
    developer_ergonomics: 39.3
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 7.9
  previous_composite: 39.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 47.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amdocs/refs/heads/main/screenshots/amdocs-2026-06-20T171859.png
security:
- kind: authentication
  name: Amdocs Authentication
  slug: amdocs-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Amdocs Domain Security
  slug: amdocs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: amdocs
solutions:
- description: All-in-one SaaS BSS platform for telcos and MVNOs with AI-powered customer management, billing, and monetization capabilities.
  name: connectX
- description: Digital BSS platform for managing and monetizing subscriptions with integrated digital partners and omnichannel delivery.
  name: MarketONE
- description: Telco cloud transformation solutions for 5G, fiber, and IoT network deployment and optimization.
  name: Amdocs Networks
- description: Mobile wallet and financial services enablement for telco operators entering digital banking and fintech markets.
  name: Digital Financial Services Platform
tags:
- Telecom
- BSS
- OSS
- Billing
- Customer Management
- MVNO
- 5G
- Software-as-a-Service
use_cases:
- description: Rapidly launch new MVNO brands with pre-integrated telco-in-a-box capabilities including customer management, billing, and digital channels.
  name: MVNO Launch
- description: Migrate from legacy BSS to cloud-native SaaS BSS with TM Forum Open API compliance and pre-built integrations for telco digital transformation.
  name: BSS Digital Transformation
- description: Launch and monetize 5G services with flexible catalog management, usage-based billing, and analytics for network slicing and IoT.
  name: 5G Monetization
- description: Deploy omnichannel self-service portals and mobile apps with pre-built customer journeys for account management, plan changes, and billing.
  name: Customer Self-Service
- description: Launch fully customizable mobile plans enabling subscribers to configure data, calls, texts, and plan length via AI-powered apps.
  name: Gen Z Mobile Services
- description: Manage IoT connectivity, device onboarding, and usage-based billing for enterprise IoT deployments across telecom networks.
  name: IoT Service Management
website: https://www.amdocs.com/
---
