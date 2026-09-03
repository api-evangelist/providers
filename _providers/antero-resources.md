---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: 'Antero Resources Corporation (NYSE: AR) files annual reports (10-K), quarterly reports (10-Q), current reports (8-K), proxy statements, and other regulatory disclosures with the U.S. Securities and Ex'
  name: Antero Resources SEC EDGAR Filings
  slug: antero-resources-sec-edgar-filings
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/antero-resources-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/antero-resources
- group: company
  title: ''
  type: Website
  url: https://www.anteroresources.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.anteroresources.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.anteroresources.com/privacy-notice
- group: company
  title: ''
  type: Blog
  url: https://www.anteroresources.com/news-events/press-releases/rss
- group: operate
  title: ''
  type: Support
  url: https://www.anteroresources.com/contact-us
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/antero-resources-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/antero-resources-conformance.yml
coverage:
  checked: '2026-09-02'
  detail: Antero Resources is an Appalachian Basin natural-gas and NGL producer whose product is a hydrocarbon, not software; its entire web estate is 47 pages of investor-relations HTML and PDF forms (its own sitemap.xml lists no developer, API or integration page), and every contract-discovery path - /openapi.json, /swagger.json, /api-docs, /llms.txt and all seven named /.well-known/ paths - returns HTTP 404 on www.anteroresources.com.
  evidence:
  - status: 404
    url: https://www.anteroresources.com/openapi.json
  - status: 404
    url: https://www.anteroresources.com/.well-known/agent-card.json
  - status: 404
    url: https://www.anteroresources.com/llms.txt
  - status: 200
    url: https://www.anteroresources.com/sitemap.xml
  - status: 200
    url: https://data.sec.gov/submissions/CIK0001433270.json
  reason: not-a-software-company
  state: none
created: '2026-03-23'
description: Antero Resources is an independent oil and natural gas company engaged in the exploration, development, and production of natural gas, NGLs, and oil properties in the Appalachian Basin (West Virginia and Ohio). It is one of the largest natural gas producers in the United States, with operations focused on the Marcellus and Utica Shale formations.
finops:
- name: Antero Resources Finops
  service_category: Public Filings
  slug: antero-resources-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/antero-resources.png
layout: provider
modified: '2026-09-02'
name: Antero Resources
nav: Providers
network: true
overview: 'Antero Resources publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Natural Gas, NGL, Oil and Gas, and Upstream.


  Antero Resources'' developer surface includes engineering blog, support, and 7 more developer resources.'
plans:
- name: Antero Resources Plans Pricing
  plan_count: 1
  slug: antero-resources-plans-pricing
press:
- date: '2026-05-25'
  title: 10-K Filing
  url: https://www.anteroresources.com/investors/sec-filings/all-sec-filings/content/0001558370-24-001162/ar-20231231x10k.htm
- date: '2026-05-25'
  title: Why Antero Resources Corporation (AR) Is Skyrocketing ...
  url: https://finance.yahoo.com/news/why-antero-resources-corporation-ar-112447343.html
- date: '2026-05-25'
  title: Antero Resources to acquire HG Energy assets for $2.8 ...
  url: https://in.investing.com/news/company-news/antero-resources-to-acquire-hg-energy-assets-for-28-billion-93CH-5142178
- date: '2026-05-25'
  title: Antero Resources Announces First Quarter 2026 Financial ...
  url: https://www.prnewswire.com/news-releases/antero-resources-announces-first-quarter-2026-financial-and-operating-results-302757804.html
- date: '2026-05-25'
  title: XBRL Viewer
  url: https://www.sec.gov/ix?doc=/Archives/edgar/data/0001433270/000110465925042687/tm2513565d1_8k.htm
- date: '2026-04-29'
  title: Antero Resources Announces First Quarter 2026 Financial and Operating Results
  url: https://www.anteroresources.com/news-events/press-releases/detail/257/antero-resources-announces-first-quarter-2026-financial-and
- date: '2026-04-15'
  title: Antero Resources Announces First Quarter 2026 Earnings Release Date and Conference Call
  url: https://www.anteroresources.com/news-events/press-releases/detail/256/antero-resources-announces-first-quarter-2026-earnings
- date: '2026-02-11'
  title: Antero Resources Announces Fourth Quarter 2025 Results and 2026 Guidance
  url: https://www.anteroresources.com/news-events/press-releases/detail/255/antero-resources-announces-fourth-quarter-2025-results-and
random_paper: 1
rate_limits:
- limit_count: 1
  name: Antero Resources Rate Limits
  slug: antero-resources-rate-limits
score:
  band: emerging
  composite: 18.5
  coverage:
    artifact_dirs: 11
    catalog_gap: 65.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 4.3
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 21.1
  previous_composite: 14.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 14.9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/antero-resources/refs/heads/main/screenshots/antero-resources-2026-06-20T172022.png
security:
- kind: domain-security
  name: Antero Resources Domain Security
  slug: antero-resources-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: antero-resources
tags:
- Energy
- Natural Gas
- NGL
- Oil and Gas
- Upstream
website: https://www.anteroresources.com
---
