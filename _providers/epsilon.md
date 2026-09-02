---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.7
  scored_at: '2026-09-01'
api_count: 3
apis:
- description: Serves brand-page content modules for retailer-hosted brand landing pages. A retailer routes /brands/{slug} on its own domain, calls POST /ads/v3/brand-pages on its assigned regional Epsilon RMN ads h
  name: Epsilon Retail Media Brand Pages API
  slug: epsilon-retail-media-brand-pages-api
- description: The Ads API from Epsilon — 2 operation(s) for ads.
  name: Epsilon Ads API
  slug: epsilon-ads-api
- description: The Catalog Products API from Epsilon — 2 operation(s) for catalog products.
  name: Epsilon Catalog Products API
  slug: epsilon-catalog-products-api
- description: The Catalogs API from Epsilon — 1 operation(s) for catalogs.
  name: Epsilon Catalogs API
  slug: epsilon-catalogs-api
- description: The crossSellCategory API from Epsilon — 2 operation(s) for crosssellcategory.
  name: Epsilon Cross Sell Category API
  slug: epsilon-crosssellcategory-api
- description: The Customers API from Epsilon — 3 operation(s) for customers.
  name: Epsilon Customers API
  slug: epsilon-customers-api
- description: The filterMapping API from Epsilon — 2 operation(s) for filtermapping.
  name: Epsilon Filter Mapping API
  slug: epsilon-filtermapping-api
- description: The Orders API from Epsilon — 2 operation(s) for orders.
  name: Epsilon Orders API
  slug: epsilon-orders-api
artifact_total: 15
collections:
- collection_type: open
  name: CrossSellCategory API
  slug: open-epsilon-retail-media-cross-sell-category
- collection_type: open
  name: Citrus filter-mapping API
  slug: open-epsilon-retail-media-filter-mapping
- collection_type: open
  name: Epsilon Retail Media Integration API
  slug: open-epsilon-retail-media-integration
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/epsilon-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/epsilon-retail-media-integration-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/epsilon-retail-media-filter-mapping-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/epsilon-retail-media-cross-sell-category-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/epsilon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://epsilon.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.citrusad.com/integration/reference/overview
- group: docs
  title: ''
  type: Documentation
  url: https://developers.citrusad.com/integration/reference/api-overview
- group: docs
  title: ''
  type: APIReference
  url: https://developers.citrusad.com/integration/reference/generate
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.citrusad.com/integration/reference/before-you-start
- group: operate
  title: ''
  type: Support
  url: https://help-center.peoplecloud.epsilon.com/
- group: company
  title: ''
  type: Blog
  url: https://www.epsilon.com/us/insights/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.epsilon.com/us/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.epsilon.com/global-privacy-policies
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/epsilon-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/epsilon-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://developers.citrusad.com/.well-known/api-catalog
- group: auth
  title: ''
  type: Authentication
  url: authentication/epsilon-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/epsilon-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/epsilon-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/epsilon-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/epsilon-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/epsilon-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/epsilon-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/epsilon-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/epsilon-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/epsilon-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-12'
description: Epsilon is a Publicis Groupe marketing and advertising technology company that operates identity-led, data-driven marketing across paid, owned and earned channels. Its public, machine-readable API surface sits almost entirely inside Epsilon Retail Media (the platform built on CitrusAd, which Publicis acquired in 2021 and folded into Epsilon), whose developer hub at developers.citrusad.com publishes an Integration API for syncing catalogs, products, customers and orders and for generating product, banner and Banner X ads; a Filter Mapping API; a Cross-Sell Category API; and a Brand Pages API served from regional *.rmn.dotomi.com hosts. Epsilon also runs Epsilon PeopleCloud (loyalty, CRM, digital media) and CORE Private Exchange for publishers, but neither publishes a public machine-readable contract. API access is provisioned by a Technical Account Manager rather than self-service signup.
image: https://www.epsilon.com/images/logos/epsilon-og-image.png
layout: provider
modified: '2026-08-12'
name: Epsilon
nav: Providers
network: true
overview: 'Epsilon publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Ads API, Catalog Products API, Catalogs API, and 4 more. Tagged areas include Company, Marketing, Advertising, Retail Media, and Advertising Technology.


  Epsilon''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, sandbox, and 21 more developer resources.'
plans:
- name: Epsilon Plans Pricing
  plan_count: 0
  slug: epsilon-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Epsilon Rate Limits
  slug: epsilon-rate-limits
score:
  band: thin
  composite: 34.4
  coverage:
    artifact_dirs: 21
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 52.7
    developer_ergonomics: 28.0
    discoverability: 92.6
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 34.4
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Epsilon Authentication
  slug: epsilon-authentication
  summary_line: apiKey/http-basic/oauth2/jwt-bearer · 4 schemes
- kind: domain-security
  name: Epsilon Domain Security
  slug: epsilon-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: epsilon
tags:
- Company
- Marketing
- Advertising
- Retail Media
- Advertising Technology
- Identity Resolution
- Customer Data
- Loyalty
- Retail
- Publicis Groupe
website: https://epsilon.com/
---
