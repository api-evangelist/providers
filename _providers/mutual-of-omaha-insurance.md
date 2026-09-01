---
access_model:
  confidence: medium
  label: Partner Only
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://view.mutualofomaha.com/mutual-of-omaha-api-connections
  - https://www.mutualofomaha.com/about/newsroom/article/mutual-of-omaha-continues-expansion-of-api-offerings-to-streamline-benefits-administration-for-brokers-and-employers
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Mutual of Omaha's Workplace Solutions API program for group and voluntary benefits, delivered to brokers and employers through benefits administration platforms rather than a first-party developer por
  name: Mutual of Omaha Benefits Administration APIs
  slug: mutual-of-omaha-insurance-benefits-administration-apis
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mutual-of-omaha-insurance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mutualofomaha.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mutualofomaha
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mutual-of-omaha
- group: operate
  title: ''
  type: Support
  url: https://www.mutualofomaha.com/support/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.mutualofomaha.com/careers/life-at-mutual/careers-blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mutualofomaha.com/legal-services/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mutualofomaha.com/legal-services/privacy-notices-and-forms
- group: company
  title: ''
  type: Newsroom
  url: https://www.mutualofomaha.com/about/newsroom/news-releases
- group: commercial
  title: ''
  type: Plans
  url: plans/mutual-of-omaha-insurance-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mutual-of-omaha-insurance-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mutual-of-omaha-insurance-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mutual-of-omaha-insurance-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/mutual-of-omaha-insurance-packages.yml
- group: design
  title: ''
  type: Components
  url: components/mutual-of-omaha-insurance-components.yml
coverage:
  checked: '2026-08-28'
  detail: 'Mutual of Omaha markets three production APIs (Plan Setup, Evidence of Insurability, Enrollment) but ships them only as pre-built connections inside partner benefits-administration platforms — ADP Workforce Now, bswift, Employee Navigator and PlanSource — with no first-party developer site of any kind: developer.mutualofomaha.com and apis.mutualofomaha.com have no DNS record, and the only public API page is a marketing overview at view.mutualofomaha.com with a "find out here" contact form and no reference, base URL or spec.'
  evidence:
  - status: 200
    url: https://view.mutualofomaha.com/mutual-of-omaha-api-connections
  - status: 0
    url: https://developer.mutualofomaha.com/
  - status: 403
    url: https://api.mutualofomaha.com/
  - status: 404
    url: https://api.mutualofomaha.com/openapi.json
  - status: 404
    url: https://www.mutualofomaha.com/.well-known/api-catalog
  reason: marketplace-only
  state: gated
created: '2026-03-21'
description: Mutual of Omaha is a Fortune 500 mutual insurance and financial services company headquartered in Omaha, Nebraska, providing life, disability, dental, vision, critical illness, accident and long-term care insurance, Medicare supplement and Medicare Advantage plans, annuities, retirement services, mortgage lending and investment products to individuals, employers and groups across the United States. Its Workplace Solutions unit runs an API integration program for group and voluntary benefits — Plan Setup, Evidence of Insurability and Enrollment — but those APIs are delivered through benefits administration platform partners such as ADP Workforce Now, bswift, Employee Navigator and PlanSource rather than through a public developer portal, and no machine-readable contract is published.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mutual-of-omaha-insurance.png
layout: provider
modified: '2026-08-28'
name: Mutual of Omaha
nav: Providers
network: true
overview: 'Mutual of Omaha publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Life Insurance, Medicare, Employee Benefits, and Benefits Administration.


  Mutual of Omaha''s developer surface includes support, engineering blog, and 13 more developer resources.'
plans:
- name: Mutual Of Omaha Insurance Plans Pricing
  plan_count: 0
  slug: mutual-of-omaha-insurance-plans-pricing
press:
- date: '2026-05-25'
  title: Mutual of Omaha and bswift Streamline EOI for Employers
  url: https://www.businesswire.com/news/home/20250708122444/en/Mutual-of-Omaha-and-bswift-Streamline-EOI-for-Employers
- date: '2026-05-25'
  title: Mutual of Omaha Board Approves Reorganization as ...
  url: https://news.ambest.com/newscontent.aspx?refnum=265274&altsrc=23
- date: '2026-05-25'
  title: Homebot Partners with Fortune 500 Lender Mutual of ...
  url: https://www.prnewswire.com/news-releases/homebot-partners-with-fortune-500-lender-mutual-of-omaha-mortgage-to-transform-client-engagement-beyond-the-closing-table-302575614.html
- date: '2026-05-25'
  title: Mutual of Omaha Elevates Customer Engagement with ...
  url: https://www.mutualofomaha.com/about/newsroom/article/mutual-of-omaha-elevates-customer-engagement-with-acxiom-designed-intelligence-solution
- date: '2026-05-25'
  title: Mutual of Omaha eyes 2026 completion for reorganization ...
  url: https://www.spglobal.com/market-intelligence/en/news-insights/research/2025/10/mutual-of-omaha-eyes-2026-completion-for-reorganization-plan
random_paper: 20
rate_limits:
- limit_count: 0
  name: Mutual Of Omaha Insurance Rate Limits
  slug: mutual-of-omaha-insurance-rate-limits
score:
  band: emerging
  composite: 12.9
  coverage:
    artifact_dirs: 12
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 12.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Mutual Of Omaha Insurance Domain Security
  slug: mutual-of-omaha-insurance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mutual-of-omaha-insurance
tags:
- Insurance
- Life Insurance
- Medicare
- Employee Benefits
- Benefits Administration
- Group Insurance
- Financial-Services
- Annuities
- Disability Insurance
- Dental Insurance
website: https://www.mutualofomaha.com
---
