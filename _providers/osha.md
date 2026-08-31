---
access_model:
  confidence: high
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.4
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: OSHA's own API for electronically submitting establishment injury and illness records — Form 300A summaries and Form 300/301 case data — under 29 CFR 1904.41. Nine documented operations across establi
  name: OSHA Injury Tracking Application (ITA) API
  slug: osha-injury-tracking-application
- description: 'Read-only access to OSHA enforcement records — inspections, violations, citation history, general duty clause citations, accidents, accident abstracts and accident injuries — published as ten related '
  name: OSHA Enforcement Data API
  slug: osha-enforcement-data
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.osha.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://www.osha.gov/data/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://usdepartmentoflabor.github.io/Developer/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.osha.gov/injuryreporting
- group: docs
  title: ''
  type: APIReference
  url: https://www.osha.gov/sites/default/files/ita/documentation/osha_injury-tracking-application-api-documentation-v1.pdf
- group: operate
  title: ''
  type: Support
  url: https://www.osha.gov/contactus/
- group: company
  title: ''
  type: Blog
  url: https://www.osha.gov/rss.xml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/osha
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/USDepartmentofLabor
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dol.gov/general/privacynotice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://usdepartmentoflabor.github.io/Developer/terms-of-service/
- group: start
  title: ''
  type: Login
  url: https://www.osha.gov/injuryreporting/ita
- group: auth
  title: ''
  type: Authentication
  url: authentication/osha-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/osha-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/osha-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/osha-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/osha-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/osha-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/osha-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/osha-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/osha-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/osha-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/osha-llms.txt
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/osha-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/osha-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/osha-finops.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/osha-domain-security.yml
created: '2026-03-16'
description: 'The Occupational Safety and Health Administration is the U.S. federal agency, part of the Department of Labor, responsible for setting and enforcing workplace safety and health standards. OSHA operates two very different API surfaces. The Injury Tracking Application (ITA) API at www.osha.gov/oshaApi/v1 is a write channel employers are legally required to use under 29 CFR 1904.41 to submit OSHA Form 300A summaries and Form 300/301 case data, secured with a bearer token issued from a logged-in ITA account and backed by a separate preview.osha.gov sandbox. The OSHA enforcement datasets — inspections, violations, citations, accidents and injuries, roughly 90,000 inspections a year — are published as read-only tables through the Department of Labor''s data API. Neither surface publishes an OpenAPI: the ITA contract is distributed as a PDF.'
finops:
- name: Osha Finops
  service_category: API
  slug: osha-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/osha.png
layout: provider
modified: '2026-08-27'
name: OSHA
nav: Providers
network: true
overview: 'OSHA publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Compliance, Government, Health Standards, Regulatory, and Workplace Safety.


  OSHA''s developer surface includes documentation, getting-started guide, API reference, support, engineering blog, authentication, changelog, and 20 more developer resources.'
plans:
- name: Osha Plans Pricing
  plan_count: 0
  slug: osha-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Osha Rate Limits
  slug: osha-rate-limits
score:
  band: thin
  composite: 37.8
  coverage:
    artifact_dirs: 18
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 37.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 46.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Osha Authentication
  slug: osha-authentication
  summary_line: http/apiKey · 3 schemes
- kind: domain-security
  name: Osha Domain Security
  slug: osha-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: osha
tags:
- Compliance
- Government
- Health Standards
- Regulatory
- Workplace Safety
- Federal
- Open Data
- Enforcement
- Occupational Health
- Injury Reporting
website: https://www.osha.gov/
---
