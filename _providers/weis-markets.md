---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.8
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: The Weis Markets Vendor Integration API enables supplier and vendor partners to exchange purchase orders, invoices, item management data, and vendor contact information electronically. The platform us
  name: Weis Markets Vendor Integration API
  slug: vendor-integration-api
- description: The Weis Markets Loyalty Rewards API supports the Weis Rewards program, enabling digital loyalty card management, points accumulation, personalized offers, and integration with third-party platforms i
  name: Weis Markets Loyalty Rewards API
  slug: loyalty-rewards-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/weis-markets-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/weis-markets
- group: company
  title: ''
  type: Website
  url: https://www.weismarkets.com
- group: start
  title: ''
  type: VendorPortal
  url: https://weismarkets.streamcollab.com/
- group: other
  title: ''
  type: MobileApp
  url: https://www.weismarkets.com/wendys-app
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/weis-markets
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/weis-markets-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/weis-markets-vocabulary.yml
description: Weis Markets is a regional supermarket chain operating grocery stores in the mid-Atlantic United States, with 197 store locations across Pennsylvania, Maryland, Delaware, New Jersey, New York, Virginia, and West Virginia. The company operates a digital commerce platform, loyalty rewards program (Weis Rewards), mobile app, and vendor/supplier integration ecosystem using EDI and supply chain APIs. Weis Markets uses Toshiba ELERA commerce platform for unified in-store and online commerce.
examples:
- key_count: 2
  name: Weis Markets Vendor Purchase Order Example
  slug: weis-markets-vendor-purchase-order-example
finops:
- name: Weis Markets Finops
  service_category: API
  slug: weis-markets-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/weis-markets.png
jsonld:
- class_count: 6
  name: Weis Markets Context
  property_count: 23
  slug: weis-markets-context
layout: provider
modified: '2026-05-03'
name: Weis Markets
nav: Providers
network: true
overview: 'Weis Markets publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 1000.


  The Weis Markets catalog on APIs.io includes 1 JSON-LD context.'
plans:
- name: Weis Markets Plans Pricing
  plan_count: 3
  slug: weis-markets-plans-pricing
press:
- date: '2026-05-25'
  title: WEIS MARKETS REPORTS FOURTH QUARTER AND ...
  url: https://www.prnewswire.com/news-releases/weis-markets-reports-fourth-quarter-and-fiscal-year-2025-results-302712905.html
- date: '2026-05-25'
  title: WEIS MARKETS, INC_December 27, 2025
  url: https://www.sec.gov/Archives/edgar/data/105418/000010541826000024/wmk-20251227x10k.htm
- date: '2026-05-25'
  title: Weis Markets ensures product freshness with AI
  url: https://chainstoreage.com/weis-markets-ensures-product-freshness-ai
- date: '2026-05-25'
  title: Weis Markets partners with Cognira to enhance promotion ...
  url: https://cognira.com/news/weis-markets-partners-with-cognira-to-enhance-promotion-efficiency-and-results/
- date: '2026-05-25'
  title: Weis Markets Partners With Cognira to Enhance Promotion ...
  url: https://www.businesswire.com/news/home/20251001115503/en/Weis-Markets-Partners-With-Cognira-to-Enhance-Promotion-Efficiency-and-Results
random_paper: 5
rate_limits:
- limit_count: 5
  name: Weis Markets Rate Limits
  slug: weis-markets-rate-limits
score:
  band: emerging
  composite: 21.2
  coverage:
    artifact_dirs: 11
    catalog_gap: 61.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 15.2
    contract_quality: 21.3
    developer_ergonomics: 19.0
    discoverability: 53.7
    governance: 15.2
    operational_transparency: 13.2
  previous_composite: 21.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Weis Markets Domain Security
  slug: weis-markets-domain-security
  summary_line: TLSv1.3 · DMARC
slug: weis-markets
tags:
- Fortune 1000
website: https://www.weismarkets.com
---
