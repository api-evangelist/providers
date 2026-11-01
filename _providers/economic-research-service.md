---
access_model:
  confidence: high
  label: Free
  onboarding: unknown
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.9
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Access ERS data products in machine-readable formats for analysis or integration into your own applications. Delivered via api.data.gov as REST endpoints. Requires an api.data.gov key.
  name: USDA ERS Data APIs
  slug: ers-data-apis
- description: Integrate ERS map layers into the GIS package of your choice, on their own or mashed up with other geospatial data.
  name: USDA ERS Geospatial APIs
  slug: ers-geospatial-apis
artifact_total: 7
common:
- group: auth
  href: https://artifacts.apis.io/economic-research-service/security/economic-research-service-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/economic-research-service-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usda-ers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usda-economic-research-service
- group: company
  title: ''
  type: Website
  url: https://www.ers.usda.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ers.usda.gov/developer/
- group: company
  title: ''
  type: Blog
  url: https://www.ers.usda.gov/amber-waves
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.ers.usda.gov/developer/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ers.usda.gov/developer/api-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ers.usda.gov/privacy/privacy-statement
- group: operate
  title: ''
  type: Support
  url: https://www.ers.usda.gov/contact-us
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/USDA-REE-ERS
- group: company
  title: ''
  type: Twitter
  url: https://x.com/USDA_ERS
- group: design
  href: https://artifacts.apis.io/economic-research-service/conformance/economic-research-service-conformance.yml
  title: ''
  type: Conformance
  url: conformance/economic-research-service-conformance.yml
- group: auth
  href: https://artifacts.apis.io/economic-research-service/authentication/economic-research-service-authentication.yml
  title: ''
  type: Authentication
  url: authentication/economic-research-service-authentication.yml
- group: design
  href: https://artifacts.apis.io/economic-research-service/conventions/economic-research-service-conventions.yml
  title: ''
  type: Conventions
  url: conventions/economic-research-service-conventions.yml
- group: design
  href: https://artifacts.apis.io/economic-research-service/errors/economic-research-service-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/economic-research-service-problem-types.yml
- group: design
  href: https://artifacts.apis.io/economic-research-service/lifecycle/economic-research-service-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/economic-research-service-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/economic-research-service/changelog/economic-research-service-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/economic-research-service-changelog.yml
- group: operate
  href: https://artifacts.apis.io/economic-research-service/rate-limits/economic-research-service-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/economic-research-service-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/economic-research-service/plans/economic-research-service-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/economic-research-service-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/economic-research-service/packages/economic-research-service-packages.yml
  title: ''
  type: Packages
  url: packages/economic-research-service-packages.yml
- group: design
  href: https://artifacts.apis.io/economic-research-service/components/economic-research-service-components.yml
  title: ''
  type: Components
  url: components/economic-research-service-components.yml
- group: design
  href: https://artifacts.apis.io/economic-research-service/data-model/economic-research-service-data-model.yml
  title: ''
  type: DataModel
  url: data-model/economic-research-service-data-model.yml
- group: start
  href: https://artifacts.apis.io/economic-research-service/sandbox/economic-research-service-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/economic-research-service-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/economic-research-service/mcp/economic-research-service-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/economic-research-service-mcp.yml
- group: agent
  href: https://artifacts.apis.io/economic-research-service/llms/economic-research-service-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/economic-research-service-llms.txt
- group: commercial
  href: https://artifacts.apis.io/economic-research-service/finops/economic-research-service-finops.yml
  title: ''
  type: FinOps
  url: finops/economic-research-service-finops.yml
created: '2024-12-25'
description: The Economic Research Service (ERS) is a division of the United States Department of Agriculture (USDA) that conducts economic research and analysis related to agriculture, food, and rural development. ERS provides policymakers, stakeholders, and the public with valuable information and data to help inform decision-making and policy development.
finops:
- has_sources: true
  method: derived
  name: Economic Research Service Finops
  primary_unit: ''
  service_category: ''
  slug: economic-research-service-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/economic-research-service.png
layout: provider
modified: '2026-09-06'
name: Economic Research Service
nav: Providers
network: true
overview: 'Economic Research Service is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture, Economics, Federal Government, Research, and Open Data.


  Economic Research Service''s developer surface includes documentation, engineering blog, support, authentication, changelog, sandbox, and 21 more developer resources.'
plans:
- name: Economic Research Service Plans Pricing
  plan_count: 0
  slug: economic-research-service-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 3
  name: Economic Research Service Rate Limits
  slug: economic-research-service-rate-limits
score:
  band: thin
  composite: 35.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 73.2
    operational_transparency: 52.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 35.3
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/economic-research-service/economic-research-service-2026-06-20T180437.png
security:
- kind: authentication
  name: Economic Research Service Authentication
  slug: economic-research-service-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Economic Research Service Domain Security
  slug: economic-research-service-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: economic-research-service
tags:
- Agriculture
- Economics
- Federal Government
- Research
- Open Data
- Geospatial
- Statistics
website: https://www.ers.usda.gov/
---
