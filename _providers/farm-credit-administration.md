---
access_model:
  confidence: high
  label: Free and fully public — no account, no key, no quota published
  onboarding: unknown
  pricing: free
  public: true
  source:
  - https://wgis.fca.gov/arcgis/rest/services/FCA?f=json
  - https://wgis.fca.gov/arcgis/rest/services/FCA/hq/MapServer/0/query?where=1%3D1&returnCountOnly=true&f=json
  - https://www.fca.gov/data
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 10.1
  scored_at: '2026-09-08'
api_count: 1
apis:
- description: 'Public, anonymous Esri ArcGIS Server 12.0 REST services publishing the geography of the Farm Credit System: 55 ACA/FLCA institution headquarters (charter address, phone, county, CEO and chair surnames'
  name: FCA Farm Credit System Map Services
  slug: fca-farm-credit-system-map-services
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/farm-credit-administration-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/farm-credit-administration
- group: company
  title: ''
  type: Website
  url: https://www.fca.gov/
- group: other
  title: ''
  type: Call Reports
  url: https://www.fca.gov/bank-oversight/fcs-call-reports
- group: docs
  title: ''
  type: Examination Manual
  url: https://www.fca.gov/bank-oversight/examination-manual
- group: other
  title: ''
  type: Data
  url: https://www.fca.gov/data
- group: operate
  title: ''
  type: Support
  url: https://www.fca.gov/utility-pages/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fca.gov/required-notices/web-site-notices-and-policies
- group: auth
  title: ''
  type: Security
  url: security/farm-credit-administration-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/farm-credit-administration-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://www.fca.gov/required-notices/vulnerability-disclosure-policy
- group: other
  title: ''
  type: Institution Search
  url: https://apps.fca.gov/FCSPublicDirectory/PubSearchInstitution.aspx
- group: other
  title: ''
  type: Institution Directory
  url: https://apps.fca.gov/FCSPublicDirectory/PubViewInstitutionsBySysDist.aspx
- group: other
  title: ''
  type: FCS Directory and Map
  url: https://www.fca.gov/bank-oversight/fcs-directory-map
- group: other
  title: ''
  type: Consolidated Reporting System
  url: https://reports.fca.gov/CRS/SystemWideReportSelector.aspx
- group: other
  title: ''
  type: Call Report Data Download
  url: https://www.fca.gov/bank-oversight/call-report-data-for-download
- group: company
  title: ''
  type: News
  url: https://www.fca.gov/newsroom/news
- group: start
  title: ''
  type: Federal Register Documents
  url: https://ww3.fca.gov/readingrm/fedreg/Federal%20Register%20Documents/Forms/FCA.aspx
- group: other
  title: ''
  type: Regulations
  url: https://www.fca.gov/laws-and-regulations/fca-regulations
- group: other
  title: ''
  type: Laws and Regulations
  url: https://www.fca.gov/laws-and-regulations/laws-regulations
- group: other
  title: ''
  type: FCA Handbook
  url: https://ww3.fca.gov/readingrm/Handbook/FCA%20Regulation/Forms/AllItems.aspx
- group: other
  title: ''
  type: Reading Room
  url: https://ww3.fca.gov/readingrm/infomemo/Lists/InformationMemorandums/By%20Memorandum%20Date.aspx
- group: other
  title: ''
  type: FOIA
  url: https://www.fca.gov/required-notices/freedom-of-information-act
- group: company
  title: ''
  type: Careers
  url: https://www.fca.gov/about/careers-at-fca
- group: other
  title: ''
  type: Digital Strategy
  url: https://www.fca.gov/required-notices/digital-strategy
- group: other
  title: ''
  type: Reports and Publications
  url: https://www.fca.gov/about/reports-publications
- group: commercial
  title: ''
  type: Regulatory Projects Plan
  url: https://www.fca.gov/laws-and-regulations/regulatory-projects-plan
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCMLBjEdJAom6CaT3xRWV6oQ
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/farm-credit-administration-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/farm-credit-administration-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/farm-credit-administration-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/farm-credit-administration-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/farm-credit-administration-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/farm-credit-administration-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/farm-credit-administration-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/farm-credit-administration-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/farm-credit-administration-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/farm-credit-administration-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Examples
  url: examples/farm-credit-administration-hq-query-geojson.json
created: '2024-12-25'
description: 'The Farm Credit Administration (FCA) is an independent US federal agency that regulates and examines the Farm Credit System (FCS) — a nationwide network of cooperatively owned banks and associations providing credit and financial services to farmers, ranchers, agricultural cooperatives and rural infrastructure — and the Federal Agricultural Mortgage Corporation (Farmer Mac). FCA publishes no developer portal, no API documentation and no OpenAPI, and its own digital strategy still lists "make existing high-value data and content available through web APIs" as Not begun, due May 2013. It does, however, serve one live, anonymous, machine-readable API that is linked from no developer page: an Esri ArcGIS Server REST surface at wgis.fca.gov publishing Farm Credit System institution headquarters, branch offices and chartered-territory polygons as JSON, GeoJSON and PBF, keyed on the UNINUM institution identifier that also keys the quarterly Call Report bulk downloads.'
examples:
- key_count: 5
  name: Farm Credit Administration Branches Query Json
  slug: farm-credit-administration-branches-query-json
- key_count: 2
  name: Farm Credit Administration Hq Query Geojson
  slug: farm-credit-administration-hq-query-geojson
- key_count: 5
  name: Farm Credit Administration Hq Query Json
  slug: farm-credit-administration-hq-query-json
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/farm-credit-administration.png
layout: provider
modified: '2026-09-07'
name: Farm Credit Administration
nav: Providers
network: true
overview: 'Farm Credit Administration publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture, Farms, Federal-Government, Finance, and Regulations.


  Farm Credit Administration''s developer surface includes support, product news, YouTube channel, authentication, code examples, and 35 more developer resources.'
plans:
- name: Farm Credit Administration Plans Pricing
  plan_count: 0
  slug: farm-credit-administration-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Farm Credit Administration Rate Limits
  slug: farm-credit-administration-rate-limits
score:
  band: emerging
  composite: 24.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 6.7
    developer_ergonomics: 25.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 24.3
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 50.0
  schema_version: 0.20.0
  scored_at: '2026-09-08'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/farm-credit-administration/refs/heads/main/screenshots/farm-credit-administration-2026-06-20T181040.png
security:
- kind: authentication
  name: Farm Credit Administration Authentication
  slug: farm-credit-administration-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Farm Credit Administration Domain Security
  slug: farm-credit-administration-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Farm Credit Administration Vulnerability Disclosure
  slug: farm-credit-administration-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Farm Credit Administration Trust Center
  slug: farm-credit-administration-trust-center
  summary_line: trust center published
slug: farm-credit-administration
tags:
- Agriculture
- Farms
- Federal-Government
- Finance
- Regulations
- Geospatial
- Open-Data
- Banking
- Lending
- Government
website: https://www.fca.gov/
---
