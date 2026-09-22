---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.6
  scored_at: '2026-09-21'
api_count: 0
artifact_total: 5
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ingredion/refs/heads/main/security/ingredion-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ingredion-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ingredion/refs/heads/main/authentication/ingredion-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ingredion-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ingredion/refs/heads/main/scopes/ingredion-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/ingredion-scopes.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ingredion/refs/heads/main/well-known/ingredion-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ingredion-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ingredion/refs/heads/main/conformance/ingredion-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ingredion-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ingredion/refs/heads/main/llms/ingredion-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ingredion-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/ingredion/refs/heads/main/plans/ingredion-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ingredion-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ingredion/refs/heads/main/rate-limits/ingredion-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ingredion-rate-limits.yml
- group: company
  title: ''
  type: Blog
  url: https://www.ingredion.com/na/en-us/news-events/news
- group: operate
  title: ''
  type: Support
  url: https://www.ingredion.com/na/en-us/company/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ingredion.com/na/en-us/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ingredion.com/na/en-us/legal/sales-terms-and-conditions
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Ingredion
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ingredion-incorporated
- group: company
  title: ''
  type: Website
  url: https://www.ingredion.com
coverage:
  checked: '2026-09-13'
  detail: Ingredion sells food ingredients, not software — its 2,898-URL corporate sitemap contains no developer, API or integration page at all, and the only customer-facing system, the MyIngredion portal, is a login-only Salesforce Experience Cloud site whose one anonymously readable document is a stock OpenID Connect discovery file.
  evidence:
  - status: 404
    url: https://www.ingredion.com/openapi.json
  - status: 404
    url: https://www.ingredion.com/.well-known/api-catalog
  - status: 200
    url: https://www.ingredion.com/sitemap.xml
  - status: 200
    url: https://myingredion.com/s/login/
  - status: 200
    url: https://myingredion.com/.well-known/openid-configuration
  reason: not-a-software-company
  state: none
created: '2026-05-01'
description: Ingredion Incorporated is a Fortune 500 global ingredient solutions provider headquartered in Westchester, Illinois, that turns grains, fruits, vegetables and other plant materials into starches, sweeteners, plant-based proteins, texturizers, and clean-label and sugar-reduction systems for food, beverage, brewing, animal nutrition, pharmaceutical and industrial manufacturers across more than 120 countries. Ingredion publishes no developer program and no machine-readable API contract; its customer-facing ordering, document and support surface is the login-only MyIngredion portal, which runs on Salesforce Experience Cloud under Ingredion's own domain and is the only host serving an anonymously readable discovery document.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ingredion.png
layout: provider
modified: '2026-09-13'
name: Ingredion
nav: Providers
network: true
overview: 'Ingredion is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 500, Food and Beverage, Ingredients, Food Manufacturing, and Agriculture.


  Ingredion''s developer surface includes authentication, engineering blog, support, and 12 more developer resources.'
plans:
- name: Ingredion Plans Pricing
  plan_count: 0
  slug: ingredion-plans-pricing
press:
- date: ''
  title: Ingredion, Shiru Partnership Signals Faster Push Toward ...
  url: https://www.nutritionaloutlook.com/view/ingredion-shiru-partnership-ai-driven-functional-protein-discovery
- date: ''
  title: Ingredion at IFT FIRST 2025 — Connecting texture, health ...
  url: https://www.ingredion.com/na/en-us/be-whats-next/ift-first-2025-recap
- date: ''
  title: Ingredion using AI to accelerate innovation
  url: https://www.foodbusinessnews.net/articles/29055-ingredion-using-ai-to-accelerate-innovation
- date: ''
  title: How food giants are embracing AI to forecast recipes ...
  url: https://www.fooddive.com/news/food-giants-AI-artificial-intelligence-kellanova-ingredion-ingredients-tastewise-tech-investments/745642/
- date: ''
  title: Amyris And Ingredion Partner To Manufacture And Market ...
  url: https://www.prnewswire.com/news-releases/amyris-and-ingredion-partner-to-manufacture-and-market-sugar-reduction-and-fermentation-based-food-ingredients-301282441.html
random_paper: 13
rate_limits:
- limit_count: 0
  name: Ingredion Rate Limits
  slug: ingredion-rate-limits
scopes:
- name: Ingredion Scopes
  scope_count: 0
  slug: ingredion-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 16.3
  coverage:
    artifact_dirs: 14
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.4
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 16.3
  provenance:
    conformance: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/ingredion/refs/heads/main/screenshots/ingredion-2026-06-20T183350.png
security:
- kind: authentication
  name: Ingredion Authentication
  slug: ingredion-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Ingredion Domain Security
  slug: ingredion-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ingredion
tags:
- Fortune 500
- Food and Beverage
- Ingredients
- Food Manufacturing
- Agriculture
- Plant-Based Proteins
- Specialty Chemicals
- Consumer Packaged Goods
website: https://www.ingredion.com
---
