---
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-19'
api_count: 4
apis:
- description: The core Epsilon Retail Media (CitrusAd) REST API. Retailers use it to sync product catalogs, catalog products, customers and order data into the platform, and to request product ads, static banner ad
  name: Epsilon Retail Media Integration API
  slug: epsilon-retail-media-integration-api
- description: Serves brand-page content modules for retailer-hosted brand landing pages. A retailer routes /brands/{slug} on its own domain, calls POST /ads/v3/brand-pages on its assigned regional Epsilon RMN ads h
  name: Epsilon Retail Media Brand Pages API
  slug: epsilon-retail-media-brand-pages-api
- description: Manages filter mappings that translate a retailer's own product filter vocabulary into the filters Epsilon Retail Media applies when selecting ads. Five operations — create, list, get, update and dele
  name: Epsilon Retail Media Filter Mapping API
  slug: epsilon-retail-media-filter-mapping-api
- description: Manages cross-sell category definitions used by the category cross-sell ad placement, where ads for one category are shown against products in a different, related category. Four operations — list, cr
  name: Epsilon Retail Media Cross-Sell Category API
  slug: epsilon-retail-media-cross-sell-category-api
artifact_total: 11
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
overview: 'Epsilon publishes 3 APIs on the [APIs.io](https://apis.io/) network: Retail Media Integration API, Retail Media Filter Mapping API, and Retail Media Cross-Sell Category API. Tagged areas include Company, Marketing, Advertising, Retail Media, and Advertising Technology.


  Epsilon''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, sandbox, and 17 more developer resources.'
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
  composite: 35.0
  delta: -5.5
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 30.3
    contract_quality: 53.4
    developer_ergonomics: 28.0
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 0.0
  previous_composite: 40.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
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
