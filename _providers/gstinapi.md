---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Gstinapi Agentic Access
  operation_count: 6
  slug: gstinapi-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 1
apis:
- baseURL: https://gstinapi.com
  baseurl_source: spec
  description: Verify a list of GSTINs as an asynchronous job.
  name: GSTIN API Bulk API
  slug: gstinapi-bulk-api
- baseURL: https://gstinapi.com
  baseurl_source: spec
  description: Verify a single GSTIN.
  name: GSTIN API Verification API
  slug: gstinapi-verification-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/gstinapi/agentic-access/gstinapi-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gstinapi-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/gstinapi/plans/gstinapi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gstinapi-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/gstinapi/rules/gstinapi-rules.yml
  title: ''
  type: Spectral
  url: rules/gstinapi-rules.yml
- group: design
  href: https://artifacts.apis.io/gstinapi/json-ld/gstinapi-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/gstinapi-context.jsonld
- group: design
  href: https://artifacts.apis.io/gstinapi/vocabulary/gstinapi-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/gstinapi-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/gstinapi/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/gstinapi/data-model/gstinapi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gstinapi-data-model.yml
- group: auth
  href: https://artifacts.apis.io/gstinapi/authentication/gstinapi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gstinapi-authentication.yml
- group: design
  href: https://artifacts.apis.io/gstinapi/errors/gstinapi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gstinapi-problem-types.yml
- group: design
  href: https://artifacts.apis.io/gstinapi/conformance/gstinapi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gstinapi-conformance.yml
- group: agent
  href: https://artifacts.apis.io/gstinapi/llms/gstinapi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gstinapi-llms.txt
- group: other
  href: https://artifacts.apis.io/gstinapi/hosts/gstinapi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gstinapi-hosts.yml
- group: other
  href: https://artifacts.apis.io/gstinapi/vendors/gstinapi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gstinapi-vendors.yml
- group: build
  href: https://artifacts.apis.io/gstinapi/packages/gstinapi-packages.yml
  title: ''
  type: SDKs
  url: packages/gstinapi-packages.yml
- group: build
  href: https://artifacts.apis.io/gstinapi/packages/gstinapi-packages.yml
  title: ''
  type: Packages
  url: packages/gstinapi-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gstinapi.com/terms
- group: operate
  title: ''
  type: Support
  url: https://gstinapi.com/google-sheets-gst-add-on/support
- group: operate
  title: ''
  type: StatusPage
  url: https://gstinapi.com/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gstinapi.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://gstinapi.com/pricing
- group: start
  title: ''
  type: Login
  url: https://gstinapi.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dlminds
- group: start
  title: ''
  type: DeveloperPortal
  url: https://gstinapi.com/developers
- group: company
  title: ''
  type: Blog
  url: https://gstinapi.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://gstinapi.com/blog/gst-verification-vendor-onboarding
- group: docs
  title: ''
  type: APIReference
  url: https://gstinapi.com/docs
- group: auth
  href: https://artifacts.apis.io/gstinapi/security/gstinapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gstinapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gstinapi.com/
created: '2026-10-17'
description: GSTIN API provides developer-friendly GST services for India, enabling real-time verification of GSTIN numbers, retrieval of taxpayer details, filing history, and e-invoicing status. The platform offers 20 free credits without requiring a credit card, making it accessible for developers and businesses to integrate GST compliance checks into their applications. It aims to simplify tax verification processes with a robust API, comprehensive documentation, and reliable performance.
image: https://gstinapi.com/images/og-image.png
json_schemas:
- name: BulkJobEnvelope
  property_count: 3
  slug: gstinapi-bulk-job-envelope
- name: BulkJobRequest
  property_count: 3
  slug: gstinapi-bulk-job-request
- name: BulkJob
  property_count: 11
  slug: gstinapi-bulk-job
- name: BulkResultRow
  property_count: 6
  slug: gstinapi-bulk-result-row
- name: Pagination
  property_count: 5
  slug: gstinapi-pagination
- name: TaxpayerEnvelope
  property_count: 4
  slug: gstinapi-taxpayer-envelope
jsonld:
- class_count: 9
  name: Gstinapi Context
  property_count: 47
  slug: gstinapi-context
layout: provider
modified: '2026-10-17'
name: GSTIN API
nav: Providers
network: true
overview: 'GSTIN API publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Bulk API and Verification API. Tagged areas include Company, GST, India, and Taxation.


  The GSTIN API catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  GSTIN API''s developer surface includes authentication, support, pricing, engineering blog, getting-started guide, API reference, and 22 more developer resources.'
plans:
- name: Gstinapi Plans Pricing
  plan_count: 2
  slug: gstinapi-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: GSTIN API API Rules
  rule_count: 18
  severity_counts:
    error: 17
    hint: 0
    info: 1
    warn: 0
  slug: gstinapi-rules
score:
  band: developing
  composite: 52.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 60.0
    catalog_earned_first_party: 8.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 65.8
    contract_governance: 19.7
    contract_quality: 66.2
    developer_ergonomics: 56.5
    discoverability: 48.2
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 53.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Gstinapi Authentication
  slug: gstinapi-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Gstinapi Domain Security
  slug: gstinapi-domain-security
  summary_line: TLSv1.3
skill_count: 1
skills:
- name: gstinapi-bulk-job-fetch
  slug: gstinapi-bulk-job-fetch
slug: gstinapi
tags:
- Company
- GST
- India
- Taxation
website: https://gstinapi.com/
---
