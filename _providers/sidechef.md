---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: The live REST surface behind SideChef's embeddable partner widgets. Observed endpoints include /v3/widget/recipes/ (shoppable recipe lookup and cart hand-off) and /v3/widget/events/ (widget telemetry)
  name: SideChef Widget API (v3)
  slug: widget-api
- description: 'A partner-embeddable JavaScript component that turns a recipe ingredient list on a partner site into a multi-retailer add-to-cart experience (Walmart, Target, Amazon Fresh, Instacart). Integration is '
  name: SideChef Shoppable Button
  slug: shoppable-button
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.sidechef.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.sidechef.com/business/
- group: docs
  title: ''
  type: Documentation
  url: https://business.sidechef.com/sb-documentation
- group: docs
  title: ''
  type: APIReference
  url: https://business.sidechef.com/sb-documentation
- group: operate
  title: ''
  type: Support
  url: https://www.sidechef.com/business/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.sidechef.com/business/insights
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sidechef.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sidechef.com/privacy-policy/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/sidechef-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sidechef-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sidechef-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/sidechef-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sidechef-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sidechef-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sidechef-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sidechef-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sidechef-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sidechef-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/sidechef-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sidechef-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sidechef-domain-security.yml
created: '2026-08-27'
description: 'SideChef is a food-technology company that licenses recipe content, shoppable-commerce and recipe-AI infrastructure to food brands, grocery retailers, food media publishers and kitchen-appliance makers. Its consumer cooking platform doubles as a B2B platform whose partner-facing surface is delivered three ways: embeddable JavaScript components (the Shoppable Recipe Button, Recipe Recommendation Row, RecipeAdapt personalization widget and an on-site recipe chat), a hosted Recipe Management System, and partner APIs such as the Recipe Recommendation API and RecipeAdapt. The underlying v3 REST surface is live at www.sidechef.com and the widget-delivery host www.scgrocery.net, but it is authenticated per partner and SideChef publishes no OpenAPI, developer portal or public API reference; the only public technical documentation is the Shoppable Button integration guide, and API access runs through a contact-sales motion.'
image: https://cdn.prod.website-files.com/63b6aab1b5182398d5ad85ad/67bd6fdbf07c15c096431062_Bannerimg-1.png
layout: provider
modified: '2026-08-27'
name: SideChef
nav: Providers
network: true
overview: 'SideChef publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food, Recipes, Retail, and Grocery.


  SideChef''s developer surface includes documentation, API reference, support, engineering blog, changelog, authentication, and 15 more developer resources.'
plans:
- name: Sidechef Plans Pricing
  plan_count: 0
  slug: sidechef-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Sidechef Rate Limits
  slug: sidechef-rate-limits
score:
  band: emerging
  composite: 26.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 26.1
  provenance:
    conformance: first-party
    mcp: unknown
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sidechef/refs/heads/main/screenshots/sidechef-2026-09-02T155353.png
security:
- kind: authentication
  name: Sidechef Authentication
  slug: sidechef-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Sidechef Domain Security
  slug: sidechef-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sidechef
tags:
- Company
- Food
- Recipes
- Retail
- Grocery
- Commerce
- Advertising
- Content
- Widgets
- Artificial Intelligence
- Nutrition
- Media
website: https://www.sidechef.com/
---
