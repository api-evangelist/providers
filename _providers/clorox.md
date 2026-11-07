---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the The Clorox Company website at www.thecloroxcompany.com: the route index of the site''s content management system, catalogued as one site surface rather th'
  name: The Clorox Company Website (WordPress REST)
  slug: thecloroxcompany-com-website-wordpress-rest
artifact_total: 6
common:
- group: auth
  href: https://artifacts.apis.io/clorox/security/clorox-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clorox-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-clorox-company
- group: company
  title: ''
  type: Website
  url: https://www.clorox.com
- group: other
  title: ''
  type: CorporateSite
  url: https://www.thecloroxcompany.com/
- group: other
  title: ''
  type: Brands
  url: https://www.thecloroxcompany.com/brands/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.thecloroxcompany.com/
- group: company
  title: ''
  type: Careers
  url: https://www.thecloroxcompany.com/careers/
- group: company
  title: ''
  type: Newsroom
  url: https://www.thecloroxcompany.com/newsroom/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.thecloroxcompany.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.thecloroxcompany.com/privacy/
- group: company
  title: ''
  type: Blog
  url: https://www.thecloroxcompany.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.thecloroxcompany.com/contact-us/
- group: company
  title: ''
  type: Partners
  url: https://www.thecloroxcompany.com/suppliers/
- group: design
  href: https://artifacts.apis.io/clorox/conventions/clorox-conventions.yml
  title: ''
  type: Conventions
  url: conventions/clorox-conventions.yml
- group: design
  href: https://artifacts.apis.io/clorox/conformance/clorox-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clorox-conformance.yml
- group: auth
  href: https://artifacts.apis.io/clorox/authentication/clorox-authentication.yml
  title: ''
  type: Authentication
  url: authentication/clorox-authentication.yml
- group: design
  href: https://artifacts.apis.io/clorox/errors/clorox-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/clorox-problem-types.yml
- group: design
  href: https://artifacts.apis.io/clorox/data-model/clorox-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clorox-data-model.yml
- group: design
  href: https://artifacts.apis.io/clorox/lifecycle/clorox-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/clorox-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/clorox/rate-limits/clorox-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/clorox-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/clorox/plans/clorox-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/clorox-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/clorox/packages/clorox-packages.yml
  title: ''
  type: Packages
  url: packages/clorox-packages.yml
- group: agent
  href: https://artifacts.apis.io/clorox/llms/clorox-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clorox-llms.txt
- group: agent
  href: https://artifacts.apis.io/clorox/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-03-23'
description: The Clorox Company is a multinational consumer-goods manufacturer best known for its bleach, cleaning and disinfecting brands, alongside a portfolio that includes Pine-Sol, Liquid-Plumr, Glad, Kingsford, Brita, Burt's Bees and Hidden Valley. Clorox runs no developer program and publishes no API documentation, OpenAPI, SDK or portal, and its commercial integration with retailers and suppliers runs over EDI and partner agreements rather than a public API. It does nonetheless serve a small, undocumented, anonymous first-party REST surface from its corporate site at /wp-json — Clorox-authored tcc/v1 and clorox-security/v1 namespaces exposing a Safety Data Sheet index, cleaning-product ingredient disclosure records, a CPSC general conformity certificate lookup, a live job feed and consent signalling. A MuleSoft Anypoint gateway at api.clorox.com serves partner traffic behind a 403, and Clorox's Anypoint Exchange public portal is enabled but publishes zero assets.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clorox.png
layout: provider
modified: '2026-09-05'
name: The Clorox Company
nav: Providers
network: true
overview: 'The Clorox Company is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cleaning Products, Consumer Goods, Consumer Packaged Goods, Disinfectants, and Household Products.


  The Clorox Company''s developer surface includes engineering blog, support, authentication, and 21 more developer resources.'
plans:
- name: Clorox Plans Pricing
  plan_count: 0
  slug: clorox-plans-pricing
press:
- date: ''
  title: 'New mindset, new platforms: How Clorox innovates twice ...'
  url: https://www.thecloroxcompany.com/blog/innovating-to-win-with-consumers-and-kantar/
- date: ''
  title: How the Owner of Hidden Valley Ranch Learned to Love AI
  url: https://www.linkedin.com/posts/the-clorox-company_how-the-owner-of-hidden-valley-ranch-learned-activity-7348122895639900160-ySgj
- date: ''
  title: Clorox Reports Q1 Fiscal Year 2026 Results, Updates ...
  url: https://www.prnewswire.com/news-releases/clorox-reports-q1-fiscal-year-2026-results-updates-outlook-302603097.html
- date: ''
  title: 'Innovation Spotlight: How The Clorox Company Uses AI ...'
  url: https://consumerbrandsassociation.org/blog/innovation-spotlight-how-the-clorox-company-uses-ai-to-meet-consumer-demand/
- date: ''
  title: How Clorox Used AI and Chatbots for Customer Service ...
  url: https://www.chiefmarketer.com/how-clorox-used-ai-and-chatbots-for-customer-service-inquiries-during-the-pandemic/
random_paper: 15
rate_limits:
- limit_count: 0
  name: Clorox Rate Limits
  slug: clorox-rate-limits
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 25.6
    discoverability: 58.0
    operational_transparency: 0.0
  previous_composite: 17.5
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/clorox/clorox-2026-06-20T174533.png
security:
- kind: authentication
  name: Clorox Authentication
  slug: clorox-authentication
  summary_line: none/application-password · 2 schemes
- kind: domain-security
  name: Clorox Domain Security
  slug: clorox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: Look up Clorox product safety and ingredient disclosures
  slug: clorox-product-disclosure-lookup
slug: clorox
tags:
- Cleaning Products
- Consumer Goods
- Consumer Packaged Goods
- Disinfectants
- Household Products
- Manufacturer
- Fortune 500
- Safety Data Sheets
- Product Transparency
- MuleSoft
website: https://www.clorox.com
---
