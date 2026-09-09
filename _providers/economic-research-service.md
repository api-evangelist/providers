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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-09-08'
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
  title: ''
  type: Conformance
  url: conformance/economic-research-service-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/economic-research-service-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/economic-research-service-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/economic-research-service-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/economic-research-service-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/economic-research-service-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/economic-research-service-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/economic-research-service-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/economic-research-service-packages.yml
- group: design
  title: ''
  type: Components
  url: components/economic-research-service-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/economic-research-service-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/economic-research-service-sandbox.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/economic-research-service-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/economic-research-service-llms.txt
- group: commercial
  title: ''
  type: FinOps
  url: finops/economic-research-service-finops.yml
created: '2024-12-25'
description: The Economic Research Service (ERS) is a division of the United States Department of Agriculture (USDA) that conducts economic research and analysis related to agriculture, food, and rural development. ERS provides policymakers, stakeholders, and the public with valuable information and data to help inform decision-making and policy development.
finops:
- name: Economic Research Service Finops
  service_category: API
  slug: economic-research-service-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/economic-research-service.png
layout: provider
modified: '2026-09-06'
name: Economic Research Service
nav: Providers
network: true
overview: 'Economic Research Service publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture, Economics, Federal-Government, Research, and Open-Data.


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
  band: developing
  composite: 45.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 26.7
    developer_ergonomics: 52.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 50.0
  previous_composite: 45.5
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 46.3
  schema_version: 0.20.0
  scored_at: '2026-09-08'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/economic-research-service/refs/heads/main/screenshots/economic-research-service-2026-06-20T180437.png
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
- Federal-Government
- Research
- Open-Data
- Geospatial
- Statistics
website: https://www.ers.usda.gov/
---
