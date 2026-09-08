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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-07'
api_count: 6
apis:
- description: The DOJ News API exposes press releases and blog entries from the Office of Public Affairs as a JSON web service. The api_v1 reference documents four resources — list and detail views for press_releas
  name: DOJ News API
  slug: doj-news-api
- baseURL: https://api.foia.gov/api
  baseurl_source: declared
  description: The National FOIA Portal publishes a JSON:API web service on api.foia.gov covering agency components, the agency taxonomy, annual and quarterly FOIA report data, and Chief FOIA Officers Council meetin
  name: National FOIA Portal API
  slug: foia-annual-report-api
- description: The Bureau of Justice Statistics NCVS API provides REST access to the National Crime Victimization Survey datasets. Endpoints expose Personal Victimization, Personal Population, Household Victimizatio
  name: BJS National Crime Victimization Survey (NCVS) API
  slug: bjs-ncvs-api
- description: 'The Bureau of Justice Statistics NIBRS National Estimates API provides REST access to the National Incident-Based Reporting System estimates including victimization counts and rates. Endpoints return '
  name: BJS NIBRS National Estimates API
  slug: bjs-nibrs-api
- description: The Foreign Agents Registration Act e-File system exposes registrant data filed under FARA as JSON. The DOJ Developer Resources page describes the FARA.gov API as providing public access to registrati
  name: FARA e-File Registrant API
  slug: fara-efile-api
- description: DOJ publishes datasets through the Open Government program and the Department's Data Inventory. Datasets are also surfaced on Data.gov under the doj-gov organization and are accessible via the CKAN-co
  name: DOJ Open Data Catalog
  slug: doj-open-data-catalog
artifact_total: 13
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/department-of-justice-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/department-of-justice-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usdoj
- group: company
  title: ''
  type: Website
  url: https://www.justice.gov
- group: other
  title: ''
  type: X-OpenGovernment
  url: https://www.justice.gov/open
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.justice.gov/developer
- group: company
  title: ''
  type: Newsroom
  url: https://www.justice.gov/news
- group: other
  title: ''
  type: X-FOIA
  url: https://www.foia.gov
- group: other
  title: ''
  type: X-OfficeOfInformationPolicy
  url: https://www.justice.gov/oip
- group: other
  title: ''
  type: X-BureauOfJusticeStatistics
  url: https://bjs.ojp.gov
- group: other
  title: ''
  type: X-OfficeOfJusticePrograms
  url: https://www.ojp.gov
- group: other
  title: ''
  type: X-FBI
  url: https://www.fbi.gov
- group: other
  title: ''
  type: X-DEA
  url: https://www.dea.gov
- group: other
  title: ''
  type: X-ATF
  url: https://www.atf.gov
- group: other
  title: ''
  type: X-USMarshals
  url: https://www.usmarshals.gov
- group: other
  title: ''
  type: X-BureauOfPrisons
  url: https://www.bop.gov
- group: other
  title: ''
  type: X-DataCatalog
  url: https://www.justice.gov/data.json
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.justice.gov/legalpolicies
- group: operate
  title: ''
  type: Contact
  url: https://www.justice.gov/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usdoj
- group: design
  title: ''
  type: JSONLD
  url: json-ld/department-of-justice-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/department-of-justice-vocabulary.yml
- group: company
  title: ''
  type: Blog
  url: https://www.justice.gov/rss.xml
- group: docs
  title: ''
  type: Documentation
  url: https://www.justice.gov/developer/api-documentation/api_v1
- group: docs
  title: ''
  type: APIReference
  url: https://www.foia.gov/swagger.html
- group: operate
  title: ''
  type: Support
  url: https://www.justice.gov/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.justice.gov/legalpolicies
- group: build
  title: ''
  type: Packages
  url: packages/department-of-justice-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/department-of-justice-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/department-of-justice-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/department-of-justice-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/department-of-justice-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/department-of-justice-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/department-of-justice-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/department-of-justice-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/department-of-justice-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/department-of-justice-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/department-of-justice-finops.yml
created: '2024-12-03'
description: The U.S. Department of Justice (DOJ) is the federal executive department responsible for enforcing the law and defending the interests of the United States. DOJ exposes a portfolio of public APIs and data feeds including the DOJ News API for press releases, speeches, and blog entries from the Office of Public Affairs, the FOIA.gov developer APIs, the Bureau of Justice Statistics NCVS and NIBRS APIs, and the DOJ Open Data Catalog.
finops:
- name: Department Of Justice Finops
  service_category: API
  slug: department-of-justice-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/department-of-justice.png
jsonld:
- class_count: 0
  name: Department Of Justice Context
  property_count: 7
  slug: department-of-justice-context
layout: provider
mcp_servers:
- description: ''
  name: Department of Justice MCP Server
  slug: department-of-justice-mcp-server
modified: '2026-09-06'
name: Department of Justice
nav: Providers
network: true
overview: 'Department of Justice publishes 1 API on the [APIs.io](https://apis.io/) network: National FOIA Portal API. Tagged areas include Bureau of Justice Statistics, Crime, Federal-Government, FOIA, and Justice.


  The Department of Justice catalog on APIs.io includes 1 JSON-LD context.


  Department of Justice''s developer surface includes authentication, engineering blog, documentation, API reference, support, and 34 more developer resources.'
plans:
- name: Department Of Justice Plans Pricing
  plan_count: 0
  slug: department-of-justice-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 4
  name: Department Of Justice Rate Limits
  slug: department-of-justice-rate-limits
score:
  band: developing
  composite: 51.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 65.0
    catalog_earned_first_party: 12.0
    catalog_gap: 50.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 33.3
    contract_quality: 53.7
    developer_ergonomics: 47.0
    discoverability: 81.5
    governance: 33.3
    operational_transparency: 34.2
  previous_composite: 51.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 46.3
  schema_version: 0.20.0
  scored_at: '2026-09-07'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/department-of-justice/refs/heads/main/screenshots/department-of-justice-2026-06-20T175938.png
security:
- kind: authentication
  name: Department Of Justice Authentication
  slug: department-of-justice-authentication
  summary_line: apiKey/none · 2 schemes
- kind: domain-security
  name: Department Of Justice Domain Security
  slug: department-of-justice-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: department-of-justice
tags:
- Bureau of Justice Statistics
- Crime
- Federal-Government
- FOIA
- Justice
- News
- Open Data
- Press Releases
- Statistics
website: https://www.justice.gov
---
