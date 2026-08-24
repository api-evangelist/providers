---
access_model:
  confidence: medium
  label: Public storefront commerce API, no developer program
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - authentication
  - openapi
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.2
  scored_at: '2026-08-24'
api_count: 4
apis:
- description: The public REST surface of the MODIVO storefront, served by its Adobe Commerce / Magento 2.4 deployment at https://modivo.pl/rest/all and self-described by a Swagger 2.0 document the platform generate
  name: MODIVO Commerce REST API
  slug: modivo-commerce-rest-api
- description: The GraphQL endpoint that powers the MODIVO storefront and mobile applications, exposed at https://modivo.pl/graphql with introspection left open to anonymous callers. The schema carries 770 types, 11
  name: MODIVO Storefront GraphQL API
  slug: modivo-storefront-graphql-api
- description: The public REST surface of eobuwie.com.pl, the MODIVO Group's footwear storefront, served by its own Adobe Commerce / Magento 2.4 deployment and self-described at https://eobuwie.com.pl/rest/all/schem
  name: eobuwie Commerce REST API
  slug: eobuwie-commerce-rest-api
- description: MODIVO's third-party marketplace runs on a Mirakl tenant at modivo.mirakl.net. Sellers automate offers, stock, prices, orders and tracking numbers through the standard Mirakl Marketplace Seller API on
  name: MODIVO Marketplace Seller API (Mirakl)
  slug: modivo-marketplace-seller-api-mirakl
artifact_total: 11
asyncapis:
- description: ''
  name: Modivo Webhooks
  slug: modivo-webhooks
collections:
- collection_type: open
  name: MODIVO Commerce REST API
  slug: open-modivo-commerce-rest-api
- collection_type: open
  name: eobuwie Commerce REST API
  slug: open-modivo-eobuwie-commerce-rest-api
common:
- group: company
  title: ''
  type: Website
  url: https://modivo.pl/
- group: other
  title: ''
  type: Company
  url: https://modivoplatform.com/en
- group: operate
  title: ''
  type: Support
  url: https://modivo.pl/b/centrum-pomocy
- group: operate
  title: ''
  type: HelpCenter
  url: https://modivo.pl/b/centrum-pomocy
- group: start
  title: ''
  type: SignUp
  url: https://modivo.pl/login
- group: start
  title: ''
  type: Login
  url: https://modivo.pl/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://modivo.pl/b/regulamin-sklepu
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://modivo.pl/b/regulamin_prywatnosci
- group: company
  title: ''
  type: Blog
  url: https://advertising.modivo.com/news
- group: other
  title: ''
  type: Advertising
  url: https://advertising.modivo.com/
- group: company
  title: ''
  type: Careers
  url: https://praca.modivo.pl/technologia-i-produkt
- group: company
  title: ''
  type: InvestorRelations
  url: https://modivoplatform.com/en/investors
- group: auth
  title: ''
  type: Authentication
  url: authentication/modivo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/modivo-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/modivo-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/modivo-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/modivo-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/modivo-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/modivo-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/modivo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/modivo-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/modivo-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/modivo-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/modivo-domain-security.yml
created: '2026-07-17'
description: 'MODIVO is a Polish multibrand fashion and lifestyle retailer that operates one of the largest fashion e-commerce platforms in Central and Eastern Europe, selling clothing, footwear, accessories, beauty and home products from more than a thousand brands across Poland, the Czech Republic, Slovakia, Romania, Hungary, Ukraine, the Baltics and Western Europe. MODIVO S.A. is the listed parent of the former CCC Group (renamed MODIVO S.A. in February 2026) and the group behind the eobuwie.pl, CCC, HalfPrice, worldbox and DeeZee retail brands; the MODIVO storefront company itself is the former eobuwie.pl S.A., a consumer-technology investment of SoftBank Vision Fund. MODIVO does not run a developer portal, but its storefront is an Adobe Commerce (Magento 2.4) deployment that serves two live, publicly readable machine contracts from its own domain: a self-describing Swagger 2.0 REST schema at https://modivo.pl/rest/all/schema?services=all and an openly introspectable GraphQL endpoint
  at https://modivo.pl/graphql. Third-party sellers integrate through a Mirakl-hosted marketplace tenant, and brands buy sponsored placements through MODIVO Ads, the group''s retail-media platform spanning MODIVO and eobuwie.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/modivo.png
layout: provider
modified: '2026-08-12'
name: MODIVO
nav: Providers
network: true
overview: 'MODIVO publishes 2 APIs on the [APIs.io](https://apis.io/) network: Commerce REST API and eobuwie Commerce REST API. Tagged areas include Company, Consumer, Fashion, E-Commerce, and Retail.


  The MODIVO catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  MODIVO''s developer surface includes support, signup flow, engineering blog, authentication, and 21 more developer resources.'
plans:
- name: Modivo Plans Pricing
  plan_count: 0
  slug: modivo-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Modivo Rate Limits
  slug: modivo-rate-limits
score:
  band: thin
  composite: 37.6
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 16.7
    contract_quality: 57.7
    developer_ergonomics: 20.8
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 7.9
  previous_composite: 37.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/modivo/refs/heads/main/screenshots/modivo-2026-08-07T184029.png
security:
- kind: authentication
  name: Modivo Authentication
  slug: modivo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Modivo Domain Security
  slug: modivo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: modivo
tags:
- Company
- Consumer
- Fashion
- E-Commerce
- Retail
- Marketplace
- Retail Media
- Commerce
- Checkout
- Catalog
- GraphQL
- Adobe Commerce
- Magento
- Poland
- Central Europe
website: https://modivo.pl/
---
