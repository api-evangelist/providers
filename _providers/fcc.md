---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
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
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-10'
api_count: 19
apis:
- description: Provides information about FCC-issued licenses for use of the nation's airwaves, including snapshots of license counts across different radio services such as 700 MHz, 800 MHz Cellular, AWS, PCS, BRS,
  name: FCC License View API
  slug: license-view
- description: Returns a high-level overview of spectrum ownership across the United States within the 225 MHz to 3700 MHz frequency range, including call sign, licensee name, common name, radio service code, and ma
  name: FCC Spectrum Dashboard API
  slug: spectrum-dashboard
- description: Enables external users and organizations to search the FCC Electronic Comment Filing System (ECFS) for regulatory filings and public comments without using the web interface. Free API key registration
  name: FCC Electronic Comment Filing System (ECFS) API
  slug: ecfs
- description: Provides access to consumer complaint data submitted to the FCC, including complaints about telephone, internet, television, and radio services.
  name: FCC Consumer Complaints Center Data API
  slug: consumer-complaints
- description: Provides programmatic access to public inspection files for broadcast, cable, satellite, and wireless telecommunications entities regulated by the FCC.
  name: FCC Public Inspection Files API
  slug: public-inspection-files
- description: Allows ISPs and developers to interface with the FCC Broadband Data Collection system via API endpoints, including the ability to respond to fixed availability challenges programmatically.
  name: FCC Broadband Data Collection (BDC) API
  slug: broadband-data-collection
- description: Makes FCC website content accessible to applications, leveraging Drupal as a content management system to deliver news, documents, and regulatory content programmatically.
  name: FCC Content API
  slug: content
- description: Get AM antenna pattern data
  name: FCC (Federal Communications Commission) Am Pattern API
  slug: fcc-am-pattern-api
- description: Get antenna pattern data for TV and FM stations
  name: FCC (Federal Communications Commission) Antenna API
  slug: fcc-antenna-api
- description: Get market area data by latitude and longitude
  name: FCC (Federal Communications Commission) Area API
  slug: fcc-area-api
- description: Get census block, county, and state FIPS codes by latitude and longitude
  name: FCC (Federal Communications Commission) Block API
  slug: fcc-block-api
- description: Convert between decimal degrees and degrees-minutes-seconds
  name: FCC (Federal Communications Commission) Coordinate Conversion API
  slug: fcc-coordinate-conversion-api
- description: Get service contour for TV and FM stations
  name: FCC (Federal Communications Commission) Coverage API
  slug: fcc-coverage-api
- description: Calculate distance using F-curve propagation curves
  name: FCC (Federal Communications Commission) Distance API
  slug: fcc-distance-api
- description: Get terrain elevation data at a given location
  name: FCC (Federal Communications Commission) Elevation API
  slug: fcc-elevation-api
- description: Get coverage contour by entity (call sign, facility ID, or application ID)
  name: FCC (Federal Communications Commission) Entity API
  slug: fcc-entity-api
- description: Get Height Above Average Terrain (HAAT) data
  name: FCC (Federal Communications Commission) Haat API
  slug: fcc-haat-api
- description: Get terrain elevation profile between two points
  name: FCC (Federal Communications Commission) Profile API
  slug: fcc-profile-api
- description: Project coordinates between coordinate reference systems
  name: FCC (Federal Communications Commission) Projection API
  slug: fcc-projection-api
artifact_total: 23
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fcc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fcc.gov
- group: docs
  title: ''
  type: Documentation
  url: https://www.fcc.gov/reports-research/developers
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/FCC
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/federal-communications-commission
- group: company
  title: ''
  type: Blog
  url: https://www.fcc.gov/news-events
- group: commercial
  title: ''
  type: Pricing
  url: https://www.fcc.gov/reports-research/developers/api-terms-service
- group: operate
  title: ''
  type: StatusPage
  url: https://www.fcc.gov
- group: other
  title: ''
  type: X
  url: https://x.com/FCC
- group: commercial
  title: ''
  type: Plans
  url: plans/fcc-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fcc-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fcc-finops.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fcc.gov/reports-research/developers/api-terms-service
created: '2026-06-13'
description: The Federal Communications Commission provides free public REST APIs for radio station license lookup, broadband coverage maps, spectrum auction data, broadcast contours, census block conversions, consumer complaint databases, electronic comment filings, and regulatory data. All APIs are free with no authentication required for most endpoints.
finops:
- name: Fcc Finops
  service_category: ''
  slug: fcc-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fcc.png
layout: provider
modified: '2026-06-13'
name: FCC (Federal Communications Commission)
nav: Providers
network: true
overview: 'FCC (Federal Communications Commission) publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Am Pattern API, Antenna API, Area API, and 9 more. Tagged areas include Federal Government, Telecommunications, Radio, Broadband, and Spectrum.


  FCC (Federal Communications Commission)''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Fcc Plans Pricing
  plan_count: 1
  slug: fcc-plans-pricing
random_paper: 68
rate_limits:
- limit_count: 0
  name: Fcc Rate Limits
  slug: fcc-rate-limits
score:
  band: thin
  composite: 32.3
  delta: -0.5
  facets:
    commercial_clarity: 50.0
    contract_quality: 52.7
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 32.8
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 13.9
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fcc/refs/heads/main/screenshots/fcc-2026-06-20T181103.png
security:
- kind: domain-security
  name: Fcc Domain Security
  slug: fcc-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: fcc
tags:
- Federal Government
- Telecommunications
- Radio
- Broadband
- Spectrum
- Licensing
- Regulatory
website: https://www.fcc.gov
---
