---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - finops
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 2.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 'Internal API platform built on MuleSoft Anypoint that exposes reusable experience, process, and system APIs across The Coca-Cola Company''s bottling, marketing, ecommerce, and supply-chain operations. '
  name: Coca-Cola Internal API Platform
  slug: coca-cola-internal-api-platform
- description: Partner-facing Azure API Management hub through which The Coca-Cola Company's bottlers register and operate AI agents. Documented publicly in TCCC's own GitHub organization as part of the "Soft Bottle
  name: TCCC Soft Bottler Agent Hub
  slug: tccc-soft-bottler-agent-hub
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/coca-cola/plans/coca-cola-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/coca-cola-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/coca-cola/rate-limits/coca-cola-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/coca-cola-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/coca-cola/finops/coca-cola-finops.yml
  title: ''
  type: FinOps
  url: finops/coca-cola-finops.yml
- group: auth
  href: https://artifacts.apis.io/coca-cola/security/coca-cola-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coca-cola-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/The-Coca-Cola-Company
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-coca-cola-company
- group: company
  title: ''
  type: Website
  url: https://www.coca-colacompany.com/
- group: other
  title: ''
  type: Brands
  url: https://www.coca-colacompany.com/brands
- group: company
  title: ''
  type: Investors
  url: https://investors.coca-colacompany.com/
- group: company
  title: ''
  type: Press
  url: https://www.coca-colacompany.com/media-center
- group: other
  title: ''
  type: Sustainability
  url: https://www.coca-colacompany.com/sustainability
- group: company
  title: ''
  type: Careers
  url: https://www.coca-colacompany.com/careers
- group: operate
  title: ''
  type: Support
  url: https://www.coca-colacompany.com/about-us/contact-us
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/C0k3
- group: agent
  href: https://artifacts.apis.io/coca-cola/llms/coca-cola-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coca-cola-llms.txt
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://datatrust.coca-cola.com/us/en/notices/global-consumer-privacy-notice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coca-cola.com/us/en/legal/terms-of-service
coverage:
  checked: '2026-09-05'
  detail: The only public developer program Coca-Cola ever ran, developer.cokecce.com, is a dead Mashery tenant that now answers "Unrecognized domain" while its gateway api.cokecce.com returns 596 "Service Not Found"; the company's two live API surfaces — an internal MuleSoft platform and a partner-gated Azure APIM hub for bottler agents documented in its own GitHub org — publish no contract, no reference and no key request path for anyone outside the bottling system.
  evidence:
  - status: 404
    url: https://developer.cokecce.com/docs/Product_API
  - status: 596
    url: https://api.cokecce.com/
  - status: 404
    url: https://www.coca-colacompany.com/.well-known/api-catalog
  - status: 200
    url: https://www.coca-colacompany.com/
  reason: no-developer-program
  state: none
created: '2026-03-21'
description: The Coca-Cola Company is the world's largest non-alcoholic beverage company, owning and marketing more than 200 brands across sparkling soft drinks, water, hydration, sports, coffee, tea, juice, dairy, and plant-based drinks. The company sells its products in more than 200 countries through a bottling and distribution partner network. While Coca-Cola does not currently publish a broadly available public REST API, it is a heavy enterprise API consumer running an internal API program on MuleSoft that connects ERP, manufacturing, distribution, retail, marketing, and consumer engagement systems through a Center for Enablement (C4E) model. Historical Coca-Cola Enterprises (CCE) Product and Location APIs at developer.cokecce.com are no longer maintained as a public-facing developer program.
finops:
- has_sources: true
  method: generated
  name: Coca Cola Finops
  primary_unit: ''
  service_category: Consumer Goods Manufacturing
  slug: coca-cola-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/coca-cola.png
layout: provider
modified: '2026-09-05'
name: The Coca-Cola Company
nav: Providers
network: true
overview: 'The Coca-Cola Company is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Beverages, Beverage Manufacturer, Consumer Goods, Distribution, and Retail.


  The Coca-Cola Company''s developer surface includes support and 16 more developer resources.'
plans:
- name: Coca Cola Plans Pricing
  plan_count: 0
  slug: coca-cola-plans-pricing
press:
- date: ''
  title: Coca-Cola causes controversy with AI-made ad
  url: https://www.nbcnews.com/tech/innovation/coca-cola-causes-controversy-ai-made-ad-rcna180665
- date: ''
  title: AI Images, Class Fourteen Have a Coke and a Smile
  url: https://www.cyberneticforests.com/ai-images-14
- date: ''
  title: How Coca-Cola, Hershey and United are using AI and data ...
  url: https://www.instagram.com/p/DXz8IZBmWsO/
- date: ''
  title: 'Social Data to Consumer Insights: Artificial Intelligence and ...'
  url: https://jg056.medium.com/social-data-to-consumer-insights-artificial-intelligence-and-coca-cola-dd2db325cbb9
- date: ''
  title: Coca-Cola® Creations Imagines Year 3000 With New ...
  url: https://www.coca-colacompany.com/media-center/coca-cola-creations-imagines-year-3000-futuristic-flavor-ai-powered-experience
- date: ''
  title: 02/20/2026 - The Coca-Cola Company
  url: https://investors.coca-colacompany.com/filings-reports/all-sec-filings/content/0001628280-26-010047/0001628280-26-010047.pdf
- date: ''
  title: IRS Properly Reallocated Income to Coca-Cola From ...
  url: https://www.taxnotes.com/research/federal/court-documents/court-opinions-and-orders/irs-properly-reallocated-income-to-coca-cola-from-foreign-affiliates/2d73h
- date: ''
  title: Coca-Cola Refreshes Givers of the Season, Embraces AI- ...
  url: https://www.coca-colacompany.com/media-center/coca-cola-refreshes-givers-of-the-season-embraces-ai-powered-storytelling-in-global-holiday-campaign
random_paper: 2
rate_limits:
- limit_count: 0
  name: Coca Cola Rate Limits
  slug: coca-cola-rate-limits
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 58.0
    operational_transparency: 2.6
  previous_composite: 13.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/coca-cola/coca-cola-2026-06-20T174646.png
security:
- kind: domain-security
  name: Coca Cola Domain Security
  slug: coca-cola-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: coca-cola
tags:
- Beverages
- Beverage Manufacturer
- Consumer Goods
- Distribution
- Retail
- Supply Chain
- Food and Beverage
- Consumer Packaged Goods
website: https://www.coca-colacompany.com/
---
