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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.8
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'Undocumented first-party REST surface served from The Clorox Company''s corporate WordPress site. Two Clorox-authored namespaces sit alongside WordPress core: tcc/v1 exposes a Safety Data Sheet index a'
  name: The Clorox Company Product Disclosure & Content API
  slug: the-clorox-company-product-disclosure-content-api
artifact_total: 5
common:
- group: auth
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
  title: ''
  type: Conventions
  url: conventions/clorox-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/clorox-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clorox-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/clorox-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/clorox-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/clorox-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/clorox-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/clorox-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/clorox-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/clorox-llms.txt
- group: agent
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
overview: 'The Clorox Company publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cleaning Products, Consumer Goods, CPG, Disinfectants, and Household Products.


  The Clorox Company''s developer surface includes engineering blog, support, authentication, and 21 more developer resources.'
plans:
- name: Clorox Plans Pricing
  plan_count: 0
  slug: clorox-plans-pricing
press:
- date: '2026-05-25'
  title: 'New mindset, new platforms: How Clorox innovates twice ...'
  url: https://www.thecloroxcompany.com/blog/innovating-to-win-with-consumers-and-kantar/
- date: '2026-05-25'
  title: How the Owner of Hidden Valley Ranch Learned to Love AI
  url: https://www.linkedin.com/posts/the-clorox-company_how-the-owner-of-hidden-valley-ranch-learned-activity-7348122895639900160-ySgj
- date: '2026-05-25'
  title: Clorox Reports Q1 Fiscal Year 2026 Results, Updates ...
  url: https://www.prnewswire.com/news-releases/clorox-reports-q1-fiscal-year-2026-results-updates-outlook-302603097.html
- date: '2026-05-25'
  title: 'Innovation Spotlight: How The Clorox Company Uses AI ...'
  url: https://consumerbrandsassociation.org/blog/innovation-spotlight-how-the-clorox-company-uses-ai-to-meet-consumer-demand/
- date: '2026-05-25'
  title: How Clorox Used AI and Chatbots for Customer Service ...
  url: https://www.chiefmarketer.com/how-clorox-used-ai-and-chatbots-for-customer-service-inquiries-during-the-pandemic/
random_paper: 12
rate_limits:
- limit_count: 0
  name: Clorox Rate Limits
  slug: clorox-rate-limits
score:
  band: emerging
  composite: 15.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 9.7
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 20.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.5
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/clorox/refs/heads/main/screenshots/clorox-2026-06-20T174533.png
security:
- kind: authentication
  name: Clorox Authentication
  slug: clorox-authentication
  summary_line: none/application-password · 2 schemes
- kind: domain-security
  name: Clorox Domain Security
  slug: clorox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clorox
tags:
- Cleaning Products
- Consumer Goods
- CPG
- Disinfectants
- Household Products
- Manufacturer
- Fortune 500
- Safety Data Sheets
- Product Transparency
- MuleSoft
website: https://www.clorox.com
---
