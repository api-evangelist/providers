---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
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
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The DOJ News API exposes press releases and blog entries from the Office of Public Affairs as a JSON web service. The api_v1 reference documents four resources — list and detail views for press_releas
  name: DOJ News API
  slug: doj-news-api
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
- baseURL: https://www.justice.gov/api/v1
  baseurl_source: declared
  description: The Agency Component API from Department of Justice — 3 operation(s) for agency component.
  name: Department of Justice Agency Component API
  slug: department-of-justice-agency-component-api
- baseURL: https://www.justice.gov/api/v1
  baseurl_source: declared
  description: The Agency Taxonomy API from Department of Justice — 2 operation(s) for agency taxonomy.
  name: Department of Justice Agency Taxonomy API
  slug: department-of-justice-agency-taxonomy-api
- baseURL: https://www.justice.gov/api/v1
  baseurl_source: declared
  description: The Annual FOIA Report Data API from Department of Justice — 3 operation(s) for annual foia report data.
  name: Department of Justice Annual FOIA Report Data API
  slug: department-of-justice-annual-foia-report-data-api
- baseURL: https://www.justice.gov/api/v1
  baseurl_source: declared
  description: The CFO Committee API from Department of Justice — 4 operation(s) for cfo committee.
  name: Department of Justice CFO Committee API
  slug: department-of-justice-cfo-committee-api
- baseURL: https://www.justice.gov/api/v1
  baseurl_source: declared
  description: The CFO Council API from Department of Justice — 2 operation(s) for cfo council.
  name: Department of Justice CFO Council API
  slug: department-of-justice-cfo-council-api
- baseURL: https://www.justice.gov/api/v1
  baseurl_source: declared
  description: The CFO Meeting API from Department of Justice — 5 operation(s) for cfo meeting.
  name: Department of Justice CFO Meeting API
  slug: department-of-justice-cfo-meeting-api
- baseURL: https://www.justice.gov/api/v1
  baseurl_source: declared
  description: The CFO Page API from Department of Justice — 3 operation(s) for cfo page.
  name: Department of Justice CFO Page API
  slug: department-of-justice-cfo-page-api
- baseURL: https://www.justice.gov/api/v1
  baseurl_source: declared
  description: The Quarterly FOIA Report Data API from Department of Justice — 2 operation(s) for quarterly foia report data.
  name: Department of Justice Quarterly FOIA Report Data API
  slug: department-of-justice-quarterly-foia-report-data-api
artifact_total: 25
common:
- group: other
  href: https://artifacts.apis.io/department-of-justice/capabilities/department-of-justice-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/department-of-justice-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/department-of-justice/overlays/department-of-justice-foia-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/department-of-justice-foia-api-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/department-of-justice/authentication/department-of-justice-authentication.yml
  title: ''
  type: Authentication
  url: authentication/department-of-justice-authentication.yml
- group: auth
  href: https://artifacts.apis.io/department-of-justice/security/department-of-justice-domain-security.yml
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
  href: https://artifacts.apis.io/department-of-justice/json-ld/department-of-justice-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/department-of-justice-context.jsonld
- group: design
  href: https://artifacts.apis.io/department-of-justice/vocabulary/department-of-justice-vocabulary.yml
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
  href: https://artifacts.apis.io/department-of-justice/packages/department-of-justice-packages.yml
  title: ''
  type: Packages
  url: packages/department-of-justice-packages.yml
- group: agent
  href: https://artifacts.apis.io/department-of-justice/llms/department-of-justice-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/department-of-justice-llms.txt
- group: agent
  href: https://artifacts.apis.io/department-of-justice/mcp/department-of-justice-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/department-of-justice-mcp.yml
- group: design
  href: https://artifacts.apis.io/department-of-justice/conformance/department-of-justice-conformance.yml
  title: ''
  type: Conformance
  url: conformance/department-of-justice-conformance.yml
- group: design
  href: https://artifacts.apis.io/department-of-justice/errors/department-of-justice-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/department-of-justice-problem-types.yml
- group: design
  href: https://artifacts.apis.io/department-of-justice/lifecycle/department-of-justice-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/department-of-justice-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/department-of-justice/conventions/department-of-justice-conventions.yml
  title: ''
  type: Conventions
  url: conventions/department-of-justice-conventions.yml
- group: design
  href: https://artifacts.apis.io/department-of-justice/data-model/department-of-justice-data-model.yml
  title: ''
  type: DataModel
  url: data-model/department-of-justice-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/department-of-justice/plans/department-of-justice-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/department-of-justice-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/department-of-justice/rate-limits/department-of-justice-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/department-of-justice-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/department-of-justice/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/department-of-justice/finops/department-of-justice-finops.yml
  title: ''
  type: FinOps
  url: finops/department-of-justice-finops.yml
created: '2024-12-03'
description: The U.S. Department of Justice (DOJ) is the federal executive department responsible for enforcing the law and defending the interests of the United States. DOJ exposes a portfolio of public APIs and data feeds including the DOJ News API for press releases, speeches, and blog entries from the Office of Public Affairs, the FOIA.gov developer APIs, the Bureau of Justice Statistics NCVS and NIBRS APIs, and the DOJ Open Data Catalog.
finops:
- has_sources: true
  method: derived
  name: Department Of Justice Finops
  primary_unit: ''
  service_category: ''
  slug: department-of-justice-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/department-of-justice.png
jsonld:
- class_count: 0
  name: Department Of Justice Context
  property_count: 7
  slug: department-of-justice-context
layout: provider
mcp_servers:
- description: MCP server; 24 tools listed. A candidate, not confirmed as published by the provider.
  name: Department of Justice MCP Server
  slug: department-of-justice-mcp-yml
modified: '2026-09-06'
name: Department of Justice
nav: Providers
network: true
overview: 'Department of Justice publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agency Component API, Agency Taxonomy API, Annual FOIA Report Data API, and 10 more. Tagged areas include Bureau of Justice Statistics, Crime, Federal Government, FOIA, and Justice.


  The Department of Justice catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Department of Justice''s developer surface includes authentication, engineering blog, documentation, API reference, support, and 36 more developer resources.'
plans:
- name: Department Of Justice Plans Pricing
  plan_count: 0
  slug: department-of-justice-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 4
  name: Department Of Justice Rate Limits
  slug: department-of-justice-rate-limits
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Department of Justice API Rules
  rule_count: 56
  severity_counts:
    error: 47
    hint: 0
    info: 2
    warn: 7
  slug: department-of-justice-rules
score:
  band: developing
  composite: 47.5
  coverage:
    artifact_dirs: 27
    catalog_earned: 63.0
    catalog_earned_first_party: 12.0
    catalog_gap: 52.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 45.5
    contract_quality: 49.0
    developer_ergonomics: 47.0
    discoverability: 74.1
    operational_transparency: 34.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 47.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/department-of-justice/department-of-justice-2026-06-20T175938.png
security:
- kind: authentication
  name: Department Of Justice Authentication
  slug: department-of-justice-authentication
  summary_line: apiKey/none · 2 schemes
- kind: domain-security
  name: Department Of Justice Domain Security
  slug: department-of-justice-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 4
skills:
- name: agency-component-directory
  slug: department-of-justice-agency-component-directory
- name: bjs-crime-statistics
  slug: department-of-justice-bjs-crime-statistics
- name: foia-annual-report-lookup
  slug: department-of-justice-foia-annual-report-lookup
- name: doj-news-feed-harvest
  slug: department-of-justice-news-feed-harvest
slug: department-of-justice
tags:
- Bureau of Justice Statistics
- Crime
- Federal Government
- FOIA
- Justice
- News
- Open Data
- Press Releases
- Statistics
website: https://www.justice.gov
---
