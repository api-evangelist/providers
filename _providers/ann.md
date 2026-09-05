---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
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
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Ann Taylor's affiliate program enables publishers and content creators to earn commissions on sales generated through affiliate links to anntaylor.com. Available through affiliate networks including F
  name: Ann Taylor Affiliate Program
  slug: ann-taylor-affiliate-api
artifact_total: 5
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/ascena-retail-group/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ann-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ann-taylor-inc
- group: company
  title: ''
  type: Website
  url: https://www.anntaylor.com/
- group: company
  title: ''
  type: Website
  url: https://www.loft.com/
- group: company
  title: ''
  type: Website
  url: https://www.knitwellgroup.com/
- group: other
  title: ''
  type: AffiliateProgram
  url: https://www.flexoffers.com/affiliate-programs/ann-taylor-affiliate-program/
- group: company
  title: ''
  type: Jobs
  url: https://jobs.knitwellgroup.com/
- group: operate
  title: ''
  type: Support
  url: https://www.anntaylor.com/customer-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.anntaylor.com/ann-privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.anntaylor.com/terms-of-use/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ann-llms.txt
coverage:
  checked: '2026-09-02'
  detail: ANN Inc. is a women's apparel retailer (Ann Taylor, LOFT) held by KnitWell Group under Sycamore Partners; its only programmable surface is an affiliate program whose link, feed and reporting APIs belong to FlexOffers and CJ Affiliate, and full STEP 0b contract discovery found no first-party spec — api.anntaylor.com and developer.anntaylor.com do not resolve at all, while www.anntaylor.com and www.loft.com are Salesforce Commerce Cloud storefronts that answer HTTP 200 with the same storefront shell for every path including /openapi.json, /graphql, /llms.txt and a control path that cannot exist.
  evidence:
  - status: 0
    url: https://api.anntaylor.com/openapi.json
  - status: 0
    url: https://developer.anntaylor.com/
  - status: 200
    url: https://www.anntaylor.com/openapi.json
  - status: 200
    url: https://www.anntaylor.com/.well-known/ann-negative-control-7f3ab91c.json
  - status: 404
    url: https://www.knitwellgroup.com/.well-known/api-catalog
  - status: 404
    url: https://www.knitwellgroup.com/openapi.json
  - status: 200
    url: https://www.loft.com/graphql
  reason: not-a-software-company
  state: none
created: '2026-03-23'
description: ANN Inc. is the former parent company of Ann Taylor and LOFT, specialty retailers of women's apparel, shoes, and accessories. ANN Inc. was acquired by Ascena Retail Group in 2015 and subsequently sold to Sycamore Partners in December 2020 for $540 million, alongside Lane Bryant and Lou & Grey brands. The brands now operate under KnitWell Group (formerly Premium Apparel LLC), a Sycamore Partners holding company that also owns Talbots. Ann Taylor and LOFT offer affiliate programs for digital publishers.
finops:
- name: Ann Finops
  service_category: Affiliate Marketing
  slug: ann-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ann.png
layout: provider
modified: '2026-09-02'
name: ANN Inc.
nav: Providers
network: true
overview: 'ANN Inc. publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Ann Taylor, Fashion, KnitWell, LOFT, and Lou And Grey.


  ANN Inc.''s developer surface includes support and 11 more developer resources.'
plans:
- name: Ann Plans Pricing
  plan_count: 1
  slug: ann-plans-pricing
press:
- date: '2026-05-25'
  title: The case for placing AI at the heart of digitally robust ...
  url: https://www.brookings.edu/articles/the-case-for-placing-ai-at-the-heart-of-digitally-robust-financial-regulation/
- date: '2026-05-25'
  title: Department of War's Artificial Intelligence-First Agenda
  url: https://www.hklaw.com/en/insights/publications/2026/02/department-of-wars-ai-first-agenda-a-new-era-for-defense-contractors
- date: '2026-05-25'
  title: Exploring Artificial Intelligence and the Future of Primary Care
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11237194/
- date: '2026-05-25'
  title: Incyte Launches The Unseen Journey to Elevate ...
  url: https://investor.incyte.com/news-releases/news-release-details/incyte-launches-unseen-journey-elevate-hidden-impact
- date: '2026-05-25'
  title: How Artificial Intelligence is Powering Education with Dr. Ann ...
  url: https://www.youtube.com/watch?v=2h3LcP7IAiQ
random_paper: 2
rate_limits:
- limit_count: 1
  name: Ann Rate Limits
  slug: ann-rate-limits
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 0.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 17.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ann/refs/heads/main/screenshots/ann-2026-06-20T172011.png
security:
- kind: domain-security
  name: Ann Domain Security
  slug: ann-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: ann
tags:
- Ann Taylor
- Fashion
- KnitWell
- LOFT
- Lou And Grey
- Retail
- Sycamore Partners
- Women's Apparel
website: https://www.anntaylor.com/
---
