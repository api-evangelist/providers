---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.7
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: The Bureau Of Economic Analysis Agentic Access
  operation_count: 10
  slug: the-bureau-of-economic-analysis-agentic-access
  summary_line: 10 operations
api_count: 1
apis:
- baseURL: https://apps.bea.gov/api/data
  baseurl_source: declared
  description: GDP by industry, input-output accounts, and sector-level data.
  name: The Bureau of Economic Analysis Industry API
  slug: the-bureau-of-economic-analysis-industry-api
- baseURL: https://apps.bea.gov/api/data
  baseurl_source: declared
  description: International transactions, investment position, and multinational enterprise data.
  name: The Bureau of Economic Analysis International API
  slug: the-bureau-of-economic-analysis-international-api
- baseURL: https://apps.bea.gov/api/data
  baseurl_source: declared
  description: Methods for discovering available datasets, parameters, and valid values.
  name: The Bureau of Economic Analysis Metadata API
  slug: the-bureau-of-economic-analysis-metadata-api
- baseURL: https://apps.bea.gov/api/data
  baseurl_source: declared
  description: National Income and Product Accounts, Fixed Assets, and related national economic statistics.
  name: The Bureau of Economic Analysis National Accounts API
  slug: the-bureau-of-economic-analysis-national-accounts-api
- baseURL: https://apps.bea.gov/api/data
  baseurl_source: declared
  description: State, metropolitan area, and county level economic data.
  name: The Bureau of Economic Analysis Regional API
  slug: the-bureau-of-economic-analysis-regional-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bureau of Economic Analysis Industry API
  slug: open-the-bureau-of-economic-analysis-industry-api
- collection_type: open
  name: Bureau of Economic Analysis Industry International API
  slug: open-the-bureau-of-economic-analysis-international-api
- collection_type: open
  name: Bureau of Economic Analysis Industry Metadata API
  slug: open-the-bureau-of-economic-analysis-metadata-api
- collection_type: open
  name: Bureau of Economic Analysis Industry National Accounts API
  slug: open-the-bureau-of-economic-analysis-national-accounts-api
- collection_type: open
  name: Bureau of Economic Analysis Industry Regional API
  slug: open-the-bureau-of-economic-analysis-regional-api
- collection_type: open
  name: Bureau of Economic Analysis API
  slug: open-the-bureau-of-economic-analysis
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/the-bureau-of-economic-analysis-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/the-bureau-of-economic-analysis-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/the-bureau-of-economic-analysis-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bureau-of-economic-analysis
- group: company
  title: ''
  type: Website
  url: https://www.bea.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bea.gov/resources/for-developers
- group: start
  title: ''
  type: Signup
  url: https://apps.bea.gov/api/signup/
- group: start
  title: ''
  type: GettingStarted
  url: https://apps.bea.gov/api/_pdf/bea_web_service_api_user_guide.pdf
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/us-bea
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/the-bureau-of-economic-analysis/refs/heads/main/openapi/the-bureau-of-economic-analysis-openapi.yml
- group: other
  title: ''
  type: InteractiveData
  url: https://apps.bea.gov/itable
- group: other
  title: ''
  type: RSS
  url: https://apps.bea.gov/rss/rss.xml
created: '2024-11-14'
description: The Bureau of Economic Analysis (BEA) is an agency within the U.S. Department of Commerce that provides economic data to policymakers, businesses, and the general public. The BEA collects and analyzes a wide range of economic indicators, including gross domestic product (GDP), personal income, and trade data. Through its reports and analysis, the BEA helps inform decision-making at all levels of government and helps businesses and individuals understand the state of the economy. The BEA Data API provides programmatic access to all published economic statistics including NIPA, regional data, international accounts, and industry-level data.
examples:
- key_count: 2
  name: The Bureau Of Economic Analysis Getdatasetlist Example
  slug: the-bureau-of-economic-analysis-getDatasetList-example
- key_count: 2
  name: The Bureau Of Economic Analysis Getnipadata Example
  slug: the-bureau-of-economic-analysis-getNIPAData-example
- key_count: 2
  name: The Bureau Of Economic Analysis Getregionaldata Example
  slug: the-bureau-of-economic-analysis-getRegionalData-example
finops:
- name: The Bureau Of Economic Analysis Finops
  service_category: API
  slug: the-bureau-of-economic-analysis-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/the-bureau-of-economic-analysis.png
json_schemas:
- name: BEA Data Point
  property_count: 9
  slug: the-bureau-of-economic-analysis-data-point
- name: BEA Dataset
  property_count: 2
  slug: the-bureau-of-economic-analysis-dataset
json_structures:
- name: The Bureau Of Economic Analysis Data Response Structure
  property_count: 0
  slug: the-bureau-of-economic-analysis-data-response-structure
jsonld:
- class_count: 8
  name: The Bureau Of Economic Analysis Context
  property_count: 20
  slug: the-bureau-of-economic-analysis-context
layout: provider
modified: '2026-05-19'
name: The Bureau of Economic Analysis
nav: Providers
network: true
overview: 'The Bureau of Economic Analysis publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Industry API, International API, Metadata API, and 2 more. Tagged areas include Economics, Federal-Government, GDP, National Accounts, and Open Data.


  The The Bureau of Economic Analysis catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  The Bureau of Economic Analysis'' developer surface includes authentication, documentation, signup flow, getting-started guide, and 8 more developer resources.'
plans:
- name: The Bureau Of Economic Analysis Plans Pricing
  plan_count: 3
  slug: the-bureau-of-economic-analysis-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: The Bureau Of Economic Analysis Rate Limits
  slug: the-bureau-of-economic-analysis-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: The Bureau of Economic Analysis API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: the-bureau-of-economic-analysis-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: The Bureau of Economic Analysis API Rules
  rule_count: 10
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 6
  slug: the-bureau-of-economic-analysis-rules
score:
  band: thin
  composite: 39.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 61.5
    catalog_earned_first_party: 0.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 13.6
    contract_quality: 61.6
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 10.5
  previous_composite: 39.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/the-bureau-of-economic-analysis/refs/heads/main/screenshots/the-bureau-of-economic-analysis-2026-06-20T195214.png
security:
- kind: authentication
  name: The Bureau Of Economic Analysis Authentication
  slug: the-bureau-of-economic-analysis-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: The Bureau Of Economic Analysis Domain Security
  slug: the-bureau-of-economic-analysis-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: the-bureau-of-economic-analysis
tags:
- Economics
- Federal-Government
- GDP
- National Accounts
- Open Data
- Statistics
website: https://www.bea.gov/
---
