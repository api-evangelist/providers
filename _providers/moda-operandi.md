---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.8
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The first-party GraphQL API that powers search, browse and merchandising on modaoperandi.com. It is referenced by the storefront's own client bundle as SEARCH_API_GRAPHQL_ENDPOINT, answers anonymous i
  name: Moda Operandi Search API
  slug: search-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.modaoperandi.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.modaoperandi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.modaoperandi.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://www.modaoperandi.com/register
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ModaOperandi
- group: operate
  title: ''
  type: Support
  url: https://help.modaoperandi.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.modaoperandi.com/editorial/the-edits
- group: docs
  title: ''
  type: GraphQL
  url: graphql/moda-operandi-search-schema.graphql
- group: auth
  title: ''
  type: Authentication
  url: authentication/moda-operandi-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/moda-operandi-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/moda-operandi-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/moda-operandi-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/moda-operandi-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/moda-operandi-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/moda-operandi-packages.yml
- group: design
  title: ''
  type: Components
  url: components/moda-operandi-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/moda-operandi-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/moda-operandi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/moda-operandi-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moda-operandi-domain-security.yml
created: '2026-08-25'
description: Moda Operandi is a New York-based luxury fashion e-commerce marketplace founded in 2010 by Lauren Santo Domingo and Aslaug Magnusdottir, built around the "trunkshow" model — customers pre-order directly from designers' full runway collections weeks before the clothes reach stores — alongside a conventional in-season boutique carrying more than 1,000 brands across ready-to-wear, fine jewelry, home and beauty. The company publishes no developer program, no partner API documentation and no OpenAPI definition. It does, however, operate a first-party GraphQL search and merchandising API at search.modaoperandi.com/graphql that powers modaoperandi.com itself, which answers anonymous introspection and exposes a read-only, 37-field catalog graph (trunkshows, designers, looks, product variants, recommendations and faceted search). Moda Operandi also publishes its design system and design tokens as first-party npm packages under the @moda scope.
graphqls:
- description: 'generated: ''2026-08-25'''
  name: Moda Operandi Search API — GraphQL
  slug: moda-operandi-graphql
image: https://www.modaoperandi.com/dist/public/favicon.png
layout: provider
modified: '2026-08-25'
name: Moda Operandi
nav: Providers
network: true
overview: 'Moda Operandi publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, E-Commerce, Fashion, and Luxury.


  Moda Operandi''s developer surface includes signup flow, support, engineering blog, authentication, and 17 more developer resources.'
plans:
- name: Moda Operandi Plans Pricing
  plan_count: 0
  slug: moda-operandi-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Moda Operandi Rate Limits
  slug: moda-operandi-rate-limits
score:
  band: thin
  composite: 28.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 37.2
    developer_ergonomics: 20.8
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 28.0
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/moda-operandi/refs/heads/main/screenshots/moda-operandi-2026-09-02T150616.png
security:
- kind: authentication
  name: Moda Operandi Authentication
  slug: moda-operandi-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Moda Operandi Domain Security
  slug: moda-operandi-domain-security
  summary_line: TLSv1.3 · DMARC
slug: moda-operandi
tags:
- Company
- Retail
- E-Commerce
- Fashion
- Luxury
- Marketplace
- Apparel
- Search
- GraphQL
- Product Catalog
website: https://www.modaoperandi.com/
---
