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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 4
apis:
- description: The CKAN Action API exposes the full Data.gov catalog programmatically. It provides read access to packages (datasets), resources (file/URL distributions), organizations (publishers — federal agencies
  name: Data.gov CKAN Action API
  slug: ckan-action-api
- description: Every U.S. federal executive branch agency is required by the Open Government Data Act of 2018 (and predecessor OMB M-13-13) to publish a public enterprise data inventory as a JSON document at /data.j
  name: Project Open Data (data.json) Catalog API
  slug: project-open-data
- description: The Data.gov harvester service ingests dataset metadata from federal, state, local, and tribal data.json endpoints, CKAN sources, and other CSW/WAF sources on a scheduled cadence and writes records in
  name: Data.gov Harvester (datagov-harvester)
  slug: datajson-harvester
- description: 'Inventory.data.gov is a second CKAN instance (also running CKAN 2.11) used by federal agencies as a publishing inventory before public release on catalog.data.gov. Most actions require authorization, '
  name: Inventory.data.gov CKAN API
  slug: inventory-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-gov-domain-security.yml
- group: build
  title: ''
  type: GitHub
  url: https://github.com/GSA/data.gov
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GSA
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/GSA/catalog.data.gov
- group: start
  title: ''
  type: Portal
  url: https://data.gov/
- group: other
  title: ''
  type: Catalog
  url: https://catalog.data.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://resources.data.gov/
- group: other
  title: ''
  type: Strategy
  url: https://strategy.data.gov/
- group: company
  title: ''
  type: Blog
  url: https://data.gov/news/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/usdatagov
- group: other
  title: ''
  type: Standards
  url: https://resources.data.gov/resources/dcat-us/
- group: operate
  title: ''
  type: Legislation
  url: https://www.congress.gov/115/plaws/publ435/PLAW-115publ435.pdf
- group: operate
  title: ''
  type: Contact
  url: https://data.gov/contact/
- group: commercial
  title: ''
  type: Privacy
  url: https://data.gov/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://data.gov/privacy-policy/#data-policy
created: '2026-05-25'
description: Data.gov is the United States federal government's open data catalog, operated by the General Services Administration (GSA) Technology Transformation Services. It indexes over 300,000 datasets, tools, and resources from federal, state, local, and tribal governments, as well as universities and non-profits. The catalog runs on CKAN 2.11 and exposes the standard CKAN Action API at catalog.data.gov/api/3/action for programmatic discovery and retrieval of datasets, organizations, groups, tags, and resources. Data.gov also publishes the federal Project Open Data (POD) schema (data.json) catalog endpoint at /data.json on every federal agency site, which Data.gov harvests into the central catalog. Related properties include inventory.data.gov (publisher-facing CKAN inventory), resources.data.gov (open data policy resources), and the api.data.gov shared API gateway used by 25+ federal agencies for 450+ APIs.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-gov.png
layout: provider
modified: '2026-05-25'
name: Data.gov
nav: Providers
network: true
overview: 'Data.gov publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Government, Open Data, Catalog, CKAN, and Datasets.


  Data.gov''s developer surface includes GitHub presence, developer portal, documentation, engineering blog, privacy policy, and 10 more developer resources.'
random_paper: 49
score:
  band: emerging
  composite: 19.0
  delta: -2.9
  facets:
    commercial_clarity: 21.1
    contract_quality: 9.7
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 21.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 25.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/data-gov/refs/heads/main/screenshots/data-gov-2026-06-20T175527.png
security:
- kind: domain-security
  name: Data Gov Domain Security
  slug: data-gov-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: data-gov
tags:
- Government
- Open Data
- Catalog
- CKAN
- Datasets
- Federal
- GSA
- Open Government
website: https://data.gov/
---
