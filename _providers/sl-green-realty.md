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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.4
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Conceptual GraphQL schema for SL Green Realty Corp. covering Property, Building, Floor, Suite, Lease, Tenant, Occupancy, Transaction, Contact, AmenityLevel, CertificationLevel, GreenInitiative, Invest
  name: SL Green Realty Corp. GraphQL Schema
  slug: sl-green-realty-corp-graphql-schema
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sl-green-realty-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://slgreen.com
- group: company
  title: ''
  type: AboutUs
  url: https://slgreen.com/about/
- group: other
  title: ''
  type: Properties
  url: https://slgreen.com/properties/
- group: other
  title: ''
  type: Leadership
  url: https://slgreen.com/about/
- group: company
  title: ''
  type: InvestorRelations
  url: https://slgreen.com/investors/
- group: operate
  title: ''
  type: PressReleases
  url: https://slgreen.com/news/
- group: company
  title: ''
  type: Careers
  url: https://slgreen.com/careers/
- group: other
  title: ''
  type: Sustainability
  url: https://slgreen.com/sustainability/
- group: start
  title: '"My Building" tenant services portal'
  type: TenantPortal
  url: https://slgreen.com/my-building/
- group: other
  title: SEC EDGAR 10-K filings (CIK 0001040971)
  type: SECFilings
  url: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001040971&type=10-K&dateb=&owner=include&count=40
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sl-green-realty-corp
created: '2026-05-23'
description: 'SL Green Realty Corp. (NYSE: SLG) is "Manhattan''s largest office landlord, a fully integrated real estate investment trust, or REIT, that is focused primarily on acquiring, managing and maximizing the value of Manhattan commercial properties." Founded in 1997 by Stephen L. Green (as successor to S.L. Green Properties, established 1980) and headquartered in New York City, SL Green is led by Chairman & CEO Marc Holliday. As of fiscal year-end 2024 the company reported 39 properties totaling approximately 25.3 million square feet, US$886M in revenue, US$10.47B in total assets, and 1,221 employees. The portfolio includes flagship trophy assets One Vanderbilt (1,401 ft, 1.75M sq ft, 62 stories, fully leased; home to Summit One Vanderbilt observation deck) and One Madison Avenue (2026 ULI Award for Excellence in Office Development), plus 420 Lexington Avenue, 1185 Avenue of the Americas, 1350 Avenue of the Americas, 800 Third Avenue, 825 Eighth Avenue, Worldwide Plaza, the Pershing
  Square Building, and 15 Laight Street in Tribeca. The company is the New York joint-venture partner for Caesars Palace Times Square, the proposed casino/entertainment complex at 1515 Broadway (and adjacent 1185 Avenue of the Americas redevelopment), pending issuance of one of three New York State downstate gaming licenses. Business divisions span leasing, finance, investments, construction, development, hospitality, property management, security & life safety, sustainability, and technology. SL Green publishes no public developer APIs, no OpenAPI/AsyncAPI specs, no SDKs, no developer portal, no public GitHub organization, and no public sandbox. Its tenant-facing technology surface is delivered through third-party platforms — the "My Building" tenant portal, RequestCom for building services, and ADP Workforce for recruitment — none of which expose a programmable interface attributable to SL Green. This profile documents the REIT, its portfolio, leadership, and verified absence of a public
  API footprint.'
features:
- finding: Public developer portal
  status: None — no developer.slgreen.com or equivalent
- finding: Public OpenAPI / AsyncAPI specs
  status: None published
- finding: Public REST or GraphQL APIs
  status: None — tenant services delivered via third-party portals
- finding: SDKs / CLI
  status: None published
- finding: GitHub organization
  status: None — no github.com/slgreen org found
- finding: Status page / changelog
  status: None public
- finding: Sandbox / Console
  status: None
- finding: Tenant technology surface
  status: Vendor-mediated — "My Building" portal, RequestCom, ADP Workforce
- finding: Tier rationale
  status: Tier 3 — no-apis. REIT with no programmable public surface.
graphqls:
- description: 'SL Green Realty Corp. (NYSE: SLG) is Manhattan''s largest office landlord and a fully integrated real estate investment trust (REIT) focused on acquiring, managing, and maximizing the value of Manhatta'
  name: SL Green Realty — GraphQL Schema
  slug: sl-green-realty-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sl-green-realty.png
jsonld:
- class_count: 31
  name: Sl Green Realty Context
  property_count: 0
  slug: sl-green-realty-context
layout: provider
modified: '2026-05-23'
name: SL Green Realty Corp.
nav: Providers
network: true
overview: 'SL Green Realty Corp. publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Casino Development, Commercial Real Estate, Manhattan, New York City, and NYSE Listed.


  The SL Green Realty Corp. catalog on APIs.io includes 1 JSON-LD context.'
random_paper: 9
score:
  band: emerging
  composite: 18.1
  delta: -1.4
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 52.2
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 19.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sl-green-realty/refs/heads/main/screenshots/sl-green-realty-2026-06-20T194019.png
security:
- kind: domain-security
  name: Sl Green Realty Domain Security
  slug: sl-green-realty-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sl-green-realty
tags:
- Casino Development
- Commercial Real Estate
- Manhattan
- New York City
- NYSE Listed
- Office Leasing
- Office Properties
- Property Management
- Real Estate
- REIT
website: https://slgreen.com
---
