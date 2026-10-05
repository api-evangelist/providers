---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.4
  scored_at: '2026-10-04'
api_count: 1
apis:
- baseURL: https://api.onbolder.com/v2
  baseurl_source: declared
  description: The Catalog API from Bootic — 3 operation(s) for catalog.
  name: Bootic Catalog API
  slug: bootic-catalog-api
- baseURL: https://api.onbolder.com/v2
  baseurl_source: declared
  description: Curated product collections (manually or rule-based). Products can belong to multiple collections.
  name: Bootic Collections API
  slug: bootic-collections-api
- baseURL: https://api.onbolder.com/v2
  baseurl_source: declared
  description: CMS-style content for a shop's storefront — blog posts, static pages, and contact/lead-capture forms.
  name: Bootic Content API
  slug: bootic-content-api
- baseURL: https://api.onbolder.com/v2
  baseurl_source: declared
  description: Shop customers. Includes customer authentication and password-reset flows.
  name: Bootic Customers API
  slug: bootic-customers-api
- baseURL: https://api.onbolder.com/v2
  baseurl_source: declared
  description: Shop orders. Supports batch status updates and per-order document management.
  name: Bootic Orders API
  slug: bootic-orders-api
- baseURL: https://api.onbolder.com/v2
  baseurl_source: declared
  description: Named price lists for B2B / wholesale pricing. Products can have per-variant price overrides within a price list.
  name: Bootic Price Lists API
  slug: bootic-price-lists-api
- baseURL: https://api.onbolder.com/v2
  baseurl_source: declared
  description: Product type definitions used to group and filter catalog products.
  name: Bootic Product Types API
  slug: bootic-product-types-api
- baseURL: https://api.onbolder.com/v2
  baseurl_source: declared
  description: Catalog products, automatically scoped to the authenticated account's sellers. Account-scoped tokens need no extra parameters; tokens without an account/seller scope must supply `shop_subdomains`.
  name: Bootic Products API
  slug: bootic-products-api
- baseURL: https://api.onbolder.com/v2
  baseurl_source: declared
  description: Promotional discount codes and automatic discounts applied at checkout.
  name: Bootic Promotions API
  slug: bootic-promotions-api
- baseURL: https://api.onbolder.com/v2
  baseurl_source: declared
  description: API entry point — embeds sellers, shops, and navigation links to every resource
  name: Bootic Root API
  slug: bootic-root-api
- baseURL: https://api.onbolder.com/v2
  baseurl_source: declared
  description: Seller entities — the business layer between an account and its shops. An account can have multiple sellers, each owning one or more shops and their product catalog.
  name: Bootic Sellers API
  slug: bootic-sellers-api
- baseURL: https://api.onbolder.com/v2
  baseurl_source: declared
  description: Shops owned by the authenticated account. A shop is the customer-facing storefront that belongs to a seller. Settings, admins, shipping tables, payment methods, exchange rates, and other shop-level co
  name: Bootic Shops API
  slug: bootic-shops-api
- baseURL: https://api.onbolder.com/v2
  baseurl_source: declared
  description: The Store API from Bootic — 1 operation(s) for store.
  name: Bootic Store API
  slug: bootic-store-api
- baseURL: https://api.onbolder.com/v2
  baseurl_source: declared
  description: Recurring product subscriptions. `SubscriptionFee` defines the recurring payment terms attached to a product/variant; `SubscriptionPurchase` is a customer's active subscription created from a recurrin
  name: Bootic Subscriptions API
  slug: bootic-subscriptions-api
- baseURL: https://api.onbolder.com/v2
  baseurl_source: declared
  description: Hosted-storefront themes, templates, and assets. Applies only to shops with a hosted storefront (`store:` namespace); absent for headless shops.
  name: Bootic Themes API
  slug: bootic-themes-api
- baseURL: https://api.onbolder.com/v2
  baseurl_source: declared
  description: Product variants (size, colour, etc.). Nested under `/products/{product_id}/variants`. Each variant holds its own SKU, price, stock level, and images.
  name: Bootic Variants API
  slug: bootic-variants-api
- baseURL: https://api.onbolder.com/v2
  baseurl_source: declared
  description: Quantity-based discount rules (tiered pricing by units purchased).
  name: Bootic Volume Discounts API
  slug: bootic-volume-discounts-api
- baseURL: https://api.onbolder.com/v2
  baseurl_source: declared
  description: Points and store-credit wallets, one per contact per program. A seller runs at most one active `PointsProgram` and one active `CreditProgram`, each covering every shop under the seller. Use `register_
  name: Bootic Wallets API
  slug: bootic-wallets-api
- baseURL: https://api.onbolder.com/v2
  baseurl_source: declared
  description: Event webhooks. Subscribe to events such as `orders.created`, `products.updated`, etc. Inactive subscriptions can be reactivated and their delivery history inspected.
  name: Bootic Webhooks API
  slug: bootic-webhooks-api
artifact_total: 22
asyncapis:
- description: ''
  name: Bootic Webhooks
  slug: bootic-webhooks
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bootic/refs/heads/main/asyncapi/bootic-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/bootic-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bootic/refs/heads/main/data-model/bootic-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bootic-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bootic/refs/heads/main/conventions/bootic-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bootic-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bootic/refs/heads/main/authentication/bootic-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bootic-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bootic/refs/heads/main/errors/bootic-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bootic-problem-types.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bootic/refs/heads/main/llms/bootic-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bootic-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bootic/refs/heads/main/hosts/bootic-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bootic-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bootic/refs/heads/main/vendors/bootic-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bootic-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bootic/refs/heads/main/packages/bootic-packages.yml
  title: ''
  type: SDKs
  url: packages/bootic-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bootic/refs/heads/main/packages/bootic-packages.yml
  title: ''
  type: Packages
  url: packages/bootic-packages.yml
- group: company
  title: ''
  type: Blog
  url: https://www.bootic.io/blog/2009/12/13/hola-mundo
- group: start
  title: ''
  type: GettingStarted
  url: https://api.onbolder.com/docs/v2#getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://dev.bootic.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.bootic.net
- group: docs
  title: ''
  type: APIReference
  url: https://api.onbolder.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bootic
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bootic/refs/heads/main/security/bootic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bootic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bootic.io
created: '2026-10-02'
description: Bootic is an e‑commerce platform based in Chile, offering a marketplace where multiple vendors sell products through a unified shopping experience. The site provides a modern storefront, advanced search, and integration options for businesses to reach customers online.
image: https://static.bolder.run/2594/logo/original/logo-logo_bootic_negro.png
layout: provider
modified: '2026-10-02'
name: Bootic
nav: Providers
network: true
overview: 'Bootic publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Collections API, Content API, and 16 more. Tagged areas include E-Commerce, Marketplace, Chile, Platform, and Retail.


  The Bootic catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Bootic''s developer surface includes authentication, engineering blog, getting-started guide, documentation, API reference, and 13 more developer resources.'
random_paper: 2
score:
  band: developing
  composite: 41.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 60.9
    developer_ergonomics: 59.5
    discoverability: 73.2
    operational_transparency: 13.2
  provenance:
    conformance: unknown
    contracts:
      callable: 95.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: true
    score: 61.1
security:
- kind: authentication
  name: Bootic Authentication
  slug: bootic-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Bootic Domain Security
  slug: bootic-domain-security
  summary_line: TLSv1.3 · HSTS
slug: bootic
tags:
- E-Commerce
- Marketplace
- Chile
- Platform
- Retail
website: https://www.bootic.io
---
