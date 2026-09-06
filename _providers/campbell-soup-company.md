---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - finops
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
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Investor relations portal providing SEC filings, earnings releases, quarterly and annual reports, investor presentations, stock information, and ESG/governance disclosures for The Campbell's Company (
  name: The Campbell's Company Investor Relations
  slug: investor-relations
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/campbell-soup-company-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-campbells-company
- group: company
  title: ''
  type: Website
  url: https://www.thecampbellscompany.com/
- group: company
  title: ''
  type: Investor Relations
  url: https://investor.thecampbellscompany.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.thecampbellscompany.com/newsroom/
- group: company
  title: ''
  type: Careers
  url: https://careers.thecampbellscompany.com/
- group: other
  title: ''
  type: Suppliers
  url: https://www.thecampbellscompany.com/suppliers/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.thecampbellscompany.com/privacy-policy/
- group: operate
  title: ''
  type: Contact
  url: https://www.thecampbellscompany.com/contact-us/
created: '2026-03-23'
description: The Campbell's Company (formerly Campbell Soup Company) is an American manufacturer and marketer of branded convenience food products including soups, simple meals, beverages, and snacks. Major brands include Campbell's, Rao's, V8, Pace, Pepperidge Farm, Snyder's of Hanover, Lance, Cape Cod, Kettle Brand, Goldfish, and Prego. The company operates consumer-facing digital properties, an investor relations portal, a careers platform, and supplier resources, but does not publish general-purpose public APIs.
finops:
- name: Campbell Soup Company Finops
  service_category: Consumer Packaged Goods / Food
  slug: campbell-soup-company-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/campbell-soup-company.png
layout: provider
modified: '2026-07-25'
name: The Campbell's Company
nav: Providers
network: true
overview: The Campbell's Company publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Beverages, Consumer Packaged Goods, CPG, Food, and Meals.
plans:
- name: Campbell Soup Company Plans Pricing
  plan_count: 0
  slug: campbell-soup-company-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Campbell Soup Company Rate Limits
  slug: campbell-soup-company-rate-limits
score:
  band: emerging
  composite: 11.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/campbell-soup-company/refs/heads/main/screenshots/campbell-soup-company-2026-06-20T173910.png
security:
- kind: domain-security
  name: Campbell Soup Company Domain Security
  slug: campbell-soup-company-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: campbell-soup-company
tags:
- Beverages
- Consumer Packaged Goods
- CPG
- Food
- Meals
- Snacks
- Soup
- Fortune 500
website: https://www.thecampbellscompany.com/
---
