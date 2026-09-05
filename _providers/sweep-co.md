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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 12.9
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sweep-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sweep.net
- group: other
  title: ''
  type: Platform
  url: https://www.sweep.net/platform
- group: other
  title: ''
  type: CarbonAccounting
  url: https://www.sweep.net/landing/carbon-accounting-software
- group: other
  title: ''
  type: ESGSoftware
  url: https://www.sweep.net/landing/software-esg
- group: other
  title: ''
  type: SustainabilityReporting
  url: https://www.sweep.net/landing/sustainability-reporting-software
- group: other
  title: ''
  type: TrackData
  url: https://www.sweep.net/track-your-carbon-and-esg-data
- group: company
  title: ''
  type: About
  url: https://www.sweep.net/about
- group: company
  title: ''
  type: Blog
  url: https://www.sweep.net/blog
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.sweep.net
- group: other
  title: ''
  type: Application
  url: https://app.sweep.net
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sweep-net
- group: docs
  title: ''
  type: GraphQL
  url: graphql/sweep-co-graphql.md
created: '2026-05-25'
description: Sweep is an enterprise carbon and ESG data management platform helping large organizations measure, manage, report, and reduce their carbon emissions and broader sustainability performance across Scope 1, 2, and 3 following the GHG Protocol. Its platform centralizes sustainability data across an organization and its value chain to produce audit-ready data from a single source, covering carbon accounting, ESG disclosure, value-chain engagement with supplier portals and automated data collection, audit and assurance trails, and business intelligence with dashboards and scenario modeling. Sweep supports compliance with the CSRD, ISSB, GRI, CDP, SFDR, TCFD, UK SRS, the GHG Protocol, and US state regulation including California SB 253 and SB 261, with vertical solutions for asset managers, asset owners, private markets, banks, healthcare, manufacturing, retail, energy, and consumer goods. Sweep was named a Leader in the IDC MarketScape 2026 for Carbon Management and recognized in
  the Verdantix 2026 Green Quadrant. The platform exposes data ingestion via API and SFTP and integrates with ERP, procurement, and HRMS systems, but Sweep does not publish a public developer portal, OpenAPI specification, SDKs, or open-source repos — API access is delivered through customer engagements rather than a self-serve developer surface.
graphqls:
- description: Sweep is a carbon management platform for companies to track, reduce, and report emissions. The API covers emissions data, reduction actions, supplier collaboration, offset projects, and regulatory re
  name: Sweep GraphQL API
  slug: sweep-co-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sweep-co.png
layout: provider
modified: '2026-05-25'
name: Sweep
nav: Providers
network: true
overview: 'Sweep is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Sustainability, Carbon Management, Carbon Accounting, ESG, and ESG Reporting.


  Sweep''s developer surface includes engineering blog and 12 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sweep-co/refs/heads/main/screenshots/sweep-co-2026-06-20T194759.png
security:
- kind: domain-security
  name: Sweep Co Domain Security
  slug: sweep-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sweep-co
tags:
- Sustainability
- Carbon Management
- Carbon Accounting
- ESG
- ESG Reporting
- Climate
- Greenhouse Gas
- GHG Protocol
- Scope 3 Emissions
- Financed Emissions
- CSRD
- ISSB
- SB 253
- TCFD
- SFDR
- CDP
- Supply Chain
- Value Chain
- Compliance
- Disclosure
- Audit
website: https://www.sweep.net
---
