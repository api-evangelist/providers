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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: The TTB Open Data API provides programmatic access to TTB statistical and regulatory datasets via the Socrata Open Data API (SODA). Available datasets include alcohol beverage tax collections by commo
  name: TTB Open Data API
  slug: ttb-open-data-api
- description: The TTB Public COLA (Certificate of Label Approval) Registry provides access to approved alcohol beverage labels. Users and industry members can search for approved labels by product type, brand name,
  name: TTB COLA Registry
  slug: ttb-cola-registry
- description: TTB Permits Online is the electronic portal for applying for and managing federal basic permits, brewer's notices, distilled spirits plant permits, and tobacco permits. The system allows industry memb
  name: TTB Permits Online
  slug: ttb-permits-online
artifact_total: 25
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alcohol-and-tobacco-tax-and-trade-bureau-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/alcohol-and-tobacco-tax-and-trade-bureau
- group: company
  title: ''
  type: Website
  url: https://www.ttb.gov
- group: start
  title: ''
  type: Portal
  url: https://www.ttb.gov/open-government/open-data
- group: start
  title: ''
  type: DataPortal
  url: https://data.ttb.gov
- group: docs
  title: ''
  type: Documentation
  url: https://www.ttb.gov/about-ttb/laws-and-regulations
- group: operate
  title: ''
  type: Contact
  url: https://www.ttb.gov/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ttb.gov/about-ttb/privacy-policy
- group: other
  title: ''
  type: FOIA
  url: https://www.ttb.gov/about-ttb/foia
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ttb-gov
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
layout: provider
modified: '2026-04-19'
name: Alcohol and Tobacco Tax and Trade Bureau
nav: Providers
network: true
overview: 'Alcohol and Tobacco Tax and Trade Bureau publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Alcohol, Tobacco, Federal Government, Excise Tax, and Regulation.


  Alcohol and Tobacco Tax and Trade Bureau''s developer surface includes developer portal, documentation, and 8 more developer resources.'
plans:
- name: Alcohol And Tobacco Tax And Trade Bureau Plans Pricing
  plan_count: 3
  slug: alcohol-and-tobacco-tax-and-trade-bureau-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Alcohol And Tobacco Tax And Trade Bureau Rate Limits
  slug: alcohol-and-tobacco-tax-and-trade-bureau-rate-limits
score:
  band: emerging
  composite: 14.5
  delta: -2.7
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 17.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 18.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alcohol-and-tobacco-tax-and-trade-bureau/refs/heads/main/screenshots/alcohol-and-tobacco-tax-and-trade-bureau-2026-06-20T171512.png
security:
- kind: domain-security
  name: Alcohol And Tobacco Tax And Trade Bureau Domain Security
  slug: alcohol-and-tobacco-tax-and-trade-bureau-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: alcohol-and-tobacco-tax-and-trade-bureau
tags:
- Alcohol
- Tobacco
- Federal Government
- Excise Tax
- Regulation
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
