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
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 41.3
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Magento 2 Agentic Access
  operation_count: 17
  slug: magento-2-agentic-access
  summary_line: 17 operations · 8 acting
api_count: 8
apis:
- description: REST API for managing products, customers, orders, inventory, cart, and checkout in Magento 2 / Adobe Commerce. The base URL pattern is https://{host}/rest/{storeCode}/V1/. Authentication supports OAu
  name: Adobe Commerce REST API
  slug: rest-api
- description: GraphQL API for headless storefront use cases in Magento 2 / Adobe Commerce, providing single-request access to catalog, cart, checkout, and customer data. Mutations require customer token authenticat
  name: Adobe Commerce GraphQL API
  slug: graphql-api
- description: The Auth API from Magento 2 (Adobe Commerce) — 2 operation(s) for auth.
  name: Magento 2 (Adobe Commerce) Auth API
  slug: magento-2-auth-api
- description: The Carts API from Magento 2 (Adobe Commerce) — 2 operation(s) for carts.
  name: Magento 2 (Adobe Commerce) Carts API
  slug: magento-2-carts-api
- description: The Categories API from Magento 2 (Adobe Commerce) — 2 operation(s) for categories.
  name: Magento 2 (Adobe Commerce) Categories API
  slug: magento-2-categories-api
- description: The Customers API from Magento 2 (Adobe Commerce) — 3 operation(s) for customers.
  name: Magento 2 (Adobe Commerce) Customers API
  slug: magento-2-customers-api
- description: The Orders API from Magento 2 (Adobe Commerce) — 2 operation(s) for orders.
  name: Magento 2 (Adobe Commerce) Orders API
  slug: magento-2-orders-api
- description: The Products API from Magento 2 (Adobe Commerce) — 2 operation(s) for products.
  name: Magento 2 (Adobe Commerce) Products API
  slug: magento-2-products-api
artifact_total: 14
collections:
- collection_type: open
  name: Adobe Commerce (Magento 2) REST API
  slug: open-magento-2
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/magento-2-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/magento-2-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/magento-2-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/magento-2-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/adobe-commerce
- group: company
  title: ''
  type: Website
  url: https://business.adobe.com/products/magento/magento-commerce.html
- group: docs
  title: ''
  type: Documentation
  url: https://developer.adobe.com/commerce/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/magento/magento2
- group: commercial
  title: ''
  type: Pricing
  url: https://business.adobe.com/products/magento/magento-commerce.html
- group: start
  title: ''
  type: Signup
  url: https://account.magento.com/customer/account/create
created: '2026-05-11'
description: Magento 2, now branded as Adobe Commerce (with the open source Magento Open Source edition), is a flexible PHP-based ecommerce platform for building storefronts, managing catalogs, processing orders, and orchestrating omnichannel customer experiences. It exposes REST, GraphQL, and SOAP web APIs that allow developers and integrators to programmatically manage products, orders, customers, inventory, and store configuration. Authentication supports OAuth 1.0a, token-based authentication (admin and customer tokens), and Adobe IMS for the cloud service.
graphqls:
- description: GraphQL API for headless storefront use cases in Magento 2 / Adobe Commerce, providing single-request access to catalog, cart, checkout, and customer data. Mutations require customer token authenticat
  name: Magento 2 (Adobe Commerce) GraphQL API
  slug: magento-2-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/magento-2.png
layout: provider
modified: '2026-05-11'
name: Magento 2 (Adobe Commerce)
nav: Providers
network: true
overview: 'Magento 2 (Adobe Commerce) publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Carts API, Categories API, and 3 more. Tagged areas include Ecommerce, Commerce, Online Store, Catalog Management, and Order Management.


  Magento 2 (Adobe Commerce)''s developer surface includes authentication, documentation, GitHub presence, pricing, signup flow, and 5 more developer resources.'
random_paper: 26
score:
  band: emerging
  composite: 26.3
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 51.3
    developer_ergonomics: 19.6
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 26.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/magento-2/refs/heads/main/screenshots/magento-2-2026-06-20T184840.png
security:
- kind: authentication
  name: Magento 2 Authentication
  slug: magento-2-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Magento 2 Domain Security
  slug: magento-2-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Magento 2 Vulnerability Disclosure
  slug: magento-2-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: magento-2
tags:
- Ecommerce
- Commerce
- Online Store
- Catalog Management
- Order Management
- GraphQL
- REST
- SOAP
website: https://business.adobe.com/products/magento/magento-commerce.html
---
