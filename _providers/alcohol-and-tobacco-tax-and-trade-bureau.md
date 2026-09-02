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
    auth_clarity: bearer
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
  score: 5.0
  scored_at: '2026-09-01'
api_count: 3
apis:
- description: TTB's open data surface is a set of static, anonymously downloadable files rather than a request/response API. Production and operations reports for beer, wine, distilled spirits and tobacco are publi
  name: TTB Open Data
  slug: ttb-open-data-api
- description: The Public COLA Registry holds every approved, expired, surrendered or revoked Certificate of Label Approval (TTB F 5100.31) for wine, distilled spirits and malt beverages. It needs no registration or
  name: TTB Public COLA Registry
  slug: ttb-cola-registry
- description: Permits Online is the electronic system for applying for and maintaining federal basic permits, brewer's notices, distilled spirits plant registrations and tobacco permits. There is no fee at the fede
  name: TTB Permits Online (PONL)
  slug: ttb-permits-online
artifact_total: 27
common:
- group: company
  title: ''
  type: Website
  url: https://www.ttb.gov
- group: start
  title: ''
  type: Portal
  url: https://www.ttb.gov/data
- group: docs
  title: ''
  type: Documentation
  url: https://www.ttb.gov/statistics/reports-and-data
- group: start
  title: ''
  type: DataPortal
  url: https://www.ttb.gov/statistics
- group: start
  title: ''
  type: GettingStarted
  url: https://www.ttb.gov/public-information/researcher-resources
- group: operate
  title: ''
  type: Support
  url: https://www.ttb.gov/about-ttb/contact-us
- group: operate
  title: ''
  type: Contact
  url: https://www.ttb.gov/about-ttb/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ttb.gov/about-ttb/privacy-policy
- group: other
  title: ''
  type: OpenGovernment
  url: https://www.ttb.gov/about-ttb/other/open-government
- group: other
  title: ''
  type: Regulations
  url: https://www.ttb.gov/laws-regulations-and-public-guidance
- group: other
  title: ''
  type: FOIA
  url: https://www.ttb.gov/public-information/foia
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/alcohol-and-tobacco-tax-and-trade-bureau
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alcohol-and-tobacco-tax-and-trade-bureau-llms.txt
- group: other
  title: ''
  type: DataCatalog
  url: json-ld/alcohol-and-tobacco-tax-and-trade-bureau-dcat-us.jsonld
- group: design
  title: ''
  type: Conformance
  url: conformance/alcohol-and-tobacco-tax-and-trade-bureau-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/alcohol-and-tobacco-tax-and-trade-bureau-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/alcohol-and-tobacco-tax-and-trade-bureau-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/alcohol-and-tobacco-tax-and-trade-bureau-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/alcohol-and-tobacco-tax-and-trade-bureau-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/alcohol-and-tobacco-tax-and-trade-bureau-plans-pricing.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alcohol-and-tobacco-tax-and-trade-bureau-domain-security.yml
created: '2024-11-21T00:00:00.000Z'
description: The Alcohol and Tobacco Tax and Trade Bureau (TTB), statutorily named the Tax and Trade Bureau, is a bureau of the United States Department of the Treasury. TTB regulates and collects federal excise taxes on alcohol, tobacco, firearms, and ammunition. The bureau enforces Federal laws and regulations related to alcohol and tobacco products, issues permits for producers, importers, and wholesalers, approves label applications for alcohol beverages, and provides open data on tax collections, permit holders, and approved product labels. TTB administers approximately $20 billion in annual federal excise tax collections from the alcohol and tobacco industries.
features:
- description: Annual and monthly federal excise tax collections broken down by alcohol and tobacco commodity type and by state.
  name: Excise Tax Data
- description: Public searchable database of all approved Certificate of Label Approval (COLA) records for wine, spirits, and malt beverages.
  name: COLA Registry
- description: Open data on federal basic permit holders including producers, importers, wholesalers, and retailers of alcohol beverages.
  name: Permit Holder Data
- description: TTB datasets are published on the Socrata platform, accessible via the standard Socrata Open Data API (SODA) with JSON and CSV output.
  name: Socrata SODA API
- description: Annual statistical reports on alcohol and tobacco tax collections, industry production volumes, and commodity statistics.
  name: Statistical Reports
- description: Electronic Freedom of Information Act (eFOIA) request submission and tracking for TTB records not available through open data.
  name: eFOIA Portal
finops:
- name: Alcohol And Tobacco Tax And Trade Bureau Finops
  service_category: API
  slug: alcohol-and-tobacco-tax-and-trade-bureau-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alcohol-and-tobacco-tax-and-trade-bureau.png
integrations:
- description: TTB datasets are accessible through api.data.gov, the government-wide API management platform hosted by GSA.
  name: api.data.gov
- description: TTB open datasets are cataloged on data.gov, the federal open data portal managed by GSA.
  name: Data.gov Catalog
- description: TTB uses the Socrata platform (data.ttb.gov) to publish and provide API access to regulatory datasets.
  name: Socrata Open Data Platform
- description: TTB coordinates with the Internal Revenue Service on excise tax administration and data sharing.
  name: IRS
- description: TTB coordinates with U.S. Customs and Border Protection on alcohol and tobacco import regulation and taxation.
  name: CBP (US Customs)
- description: TTB works with the Bureau of Alcohol, Tobacco, Firearms and Explosives on shared jurisdiction over alcohol and tobacco regulation.
  name: ATF
jsonld:
- class_count: 0
  name: Alcohol And Tobacco Tax And Trade Bureau Dcat Us Context
  property_count: 0
  slug: alcohol-and-tobacco-tax-and-trade-bureau-dcat-us
layout: provider
modified: '2026-09-01'
name: Alcohol and Tobacco Tax and Trade Bureau
nav: Providers
network: true
overview: 'Alcohol and Tobacco Tax and Trade Bureau publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Alcohol, Tobacco, Federal-Government, Excise Tax, and Regulations.


  The Alcohol and Tobacco Tax and Trade Bureau catalog on APIs.io includes 1 JSON-LD context.


  Alcohol and Tobacco Tax and Trade Bureau''s developer surface includes developer portal, documentation, getting-started guide, support, authentication, and 16 more developer resources.'
plans:
- name: Alcohol And Tobacco Tax And Trade Bureau Plans Pricing
  plan_count: 0
  slug: alcohol-and-tobacco-tax-and-trade-bureau-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Alcohol And Tobacco Tax And Trade Bureau Rate Limits
  slug: alcohol-and-tobacco-tax-and-trade-bureau-rate-limits
score:
  band: emerging
  composite: 25.1
  coverage:
    artifact_dirs: 14
    catalog_gap: 67.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 10.6
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 6.7
    developer_ergonomics: 38.1
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 14.5
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 38.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/alcohol-and-tobacco-tax-and-trade-bureau/refs/heads/main/screenshots/alcohol-and-tobacco-tax-and-trade-bureau-2026-06-20T171512.png
security:
- kind: authentication
  name: Alcohol And Tobacco Tax And Trade Bureau Authentication
  slug: alcohol-and-tobacco-tax-and-trade-bureau-authentication
  summary_line: none/session-login · 2 schemes
- kind: domain-security
  name: Alcohol And Tobacco Tax And Trade Bureau Domain Security
  slug: alcohol-and-tobacco-tax-and-trade-bureau-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: alcohol-and-tobacco-tax-and-trade-bureau
tags:
- Alcohol
- Tobacco
- Federal-Government
- Excise Tax
- Regulations
- Treasury
use_cases:
- description: Producers, importers, and retailers use TTB permit and label data to verify compliance status and competitive market intelligence.
  name: Alcohol Industry Compliance Research
- description: Policy researchers and economists analyze TTB excise tax collection data to study alcohol and tobacco market trends.
  name: Tax Revenue Analysis
- description: Alcohol beverage companies track COLA approval status and research competitor label approvals in the public registry.
  name: Label Approval Tracking
- description: Industry analysts use production volume statistics and permit holder counts to assess market size and industry structure.
  name: Market Research
- description: Public health researchers use TTB consumption proxy data (tax collection volumes) to study alcohol consumption patterns.
  name: Academic Research
- description: Journalists and public interest groups use TTB open data and FOIA to investigate regulatory compliance and enforcement actions.
  name: Journalism and FOIA Research
website: https://www.ttb.gov
---
