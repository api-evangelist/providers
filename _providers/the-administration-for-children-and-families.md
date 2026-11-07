---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  - '{''url'': ''https://www.acf.hhs.gov/'', ''status'': 301, ''note'': ''declared website redirects to https://acf.gov:443/ — a different registrable domain (hhs.gov -> acf.gov), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: The Administration For Children And Families Agentic Access
  operation_count: 48
  slug: the-administration-for-children-and-families-agentic-access
  summary_line: 48 operations · 15 acting
api_count: 1
apis:
- description: The TANF Data Portal (TDP) is a secure, web-based data reporting system for state agencies to submit Temporary Assistance for Needy Families (TANF) program data to ACF. It provides data submission wor
  name: TANF Data Portal
  slug: tanf-data-portal
- description: NDACAN is the central repository for datasets related to child abuse, neglect, and child welfare at Cornell University, funded by ACF. Provides access to AFCARS (foster care/adoption), NCANDS (child a
  name: National Data Archive on Child Abuse and Neglect
  slug: ndacan
- description: ACF's primary data and research portal providing access to program data, statistical reports, and research findings across all ACF program offices. Includes TANF caseload data, CCDF data, Head Start p
  name: ACF Data and Research Portal
  slug: acf-data-research
- baseURL: https://tanfdata.acf.hhs.gov/
  baseurl_source: declared
  description: The plg_auth_check API from The Administration for Children and Families — 1 operation(s) for plg_auth_check.
  name: The Administration for Children and Families Plg Auth Check API
  slug: the-administration-for-children-and-families-plg-auth-check-api
- baseURL: https://tanfdata.acf.hhs.gov/
  baseurl_source: declared
  description: The Auth Check API from The Administration for Children and Families — 1 operation(s) for auth check.
  name: The Administration for Children and Families Auth Check API
  slug: the-administration-for-children-and-families-auth-check-api
- baseURL: https://tanfdata.acf.hhs.gov/
  baseurl_source: declared
  description: The Change Request Logs API from The Administration for Children and Families — 2 operation(s) for change request logs.
  name: The Administration for Children and Families Change Request Logs API
  slug: the-administration-for-children-and-families-change-request-logs-api
- baseURL: https://tanfdata.acf.hhs.gov/
  baseurl_source: declared
  description: The Change Requests API from The Administration for Children and Families — 2 operation(s) for change requests.
  name: The Administration for Children and Families Change Requests API
  slug: the-administration-for-children-and-families-change-requests-api
- baseURL: https://tanfdata.acf.hhs.gov/
  baseurl_source: declared
  description: The Data Files API from The Administration for Children and Families — 6 operation(s) for data files.
  name: The Administration for Children and Families Data Files API
  slug: the-administration-for-children-and-families-data-files-api
- baseURL: https://tanfdata.acf.hhs.gov/
  baseurl_source: declared
  description: The Feature Flags API from The Administration for Children and Families — 2 operation(s) for feature flags.
  name: The Administration for Children and Families Feature Flags API
  slug: the-administration-for-children-and-families-feature-flags-api
- baseURL: https://tanfdata.acf.hhs.gov/
  baseurl_source: declared
  description: The Feedback API from The Administration for Children and Families — 2 operation(s) for feedback.
  name: The Administration for Children and Families Feedback API
  slug: the-administration-for-children-and-families-feedback-api
- baseURL: https://tanfdata.acf.hhs.gov/
  baseurl_source: declared
  description: The Login API from The Administration for Children and Families — 1 operation(s) for login.
  name: The Administration for Children and Families Login API
  slug: the-administration-for-children-and-families-login-api
- baseURL: https://tanfdata.acf.hhs.gov/
  baseurl_source: declared
  description: The Logout API from The Administration for Children and Families — 1 operation(s) for logout.
  name: The Administration for Children and Families Logout API
  slug: the-administration-for-children-and-families-logout-api
- baseURL: https://tanfdata.acf.hhs.gov/
  baseurl_source: declared
  description: The Logs API from The Administration for Children and Families — 1 operation(s) for logs.
  name: The Administration for Children and Families Logs API
  slug: the-administration-for-children-and-families-logs-api
- baseURL: https://tanfdata.acf.hhs.gov/
  baseurl_source: declared
  description: The Oidc API from The Administration for Children and Families — 1 operation(s) for oidc.
  name: The Administration for Children and Families Oidc API
  slug: the-administration-for-children-and-families-oidc-api
- baseURL: https://tanfdata.acf.hhs.gov/
  baseurl_source: declared
  description: The Reports API from The Administration for Children and Families — 5 operation(s) for reports.
  name: The Administration for Children and Families Reports API
  slug: the-administration-for-children-and-families-reports-api
- baseURL: https://tanfdata.acf.hhs.gov/
  baseurl_source: declared
  description: The Roles API from The Administration for Children and Families — 1 operation(s) for roles.
  name: The Administration for Children and Families Roles API
  slug: the-administration-for-children-and-families-roles-api
- baseURL: https://tanfdata.acf.hhs.gov/
  baseurl_source: declared
  description: The Security API from The Administration for Children and Families — 2 operation(s) for security.
  name: The Administration for Children and Families Security API
  slug: the-administration-for-children-and-families-security-api
- baseURL: https://tanfdata.acf.hhs.gov/
  baseurl_source: declared
  description: The Stts API from The Administration for Children and Families — 3 operation(s) for stts.
  name: The Administration for Children and Families Stts API
  slug: the-administration-for-children-and-families-stts-api
- baseURL: https://tanfdata.acf.hhs.gov/
  baseurl_source: declared
  description: The Users API from The Administration for Children and Families — 5 operation(s) for users.
  name: The Administration for Children and Families Users API
  slug: the-administration-for-children-and-families-users-api
artifact_total: 33
collections:
- collection_type: open
  name: TDP plg_auth_check API
  slug: open-the-administration-for-children-and-families-plg-auth-check-api
- collection_type: open
  name: TDP plg_auth_check v1 API
  slug: open-the-administration-for-children-and-families-v1-api
- collection_type: open
  name: TDP API
  slug: open-the-administration-for-children-and-families
common:
- group: commercial
  href: https://artifacts.apis.io/the-administration-for-children-and-families/plans/the-administration-for-children-and-families-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/the-administration-for-children-and-families-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/the-administration-for-children-and-families/rate-limits/the-administration-for-children-and-families-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/the-administration-for-children-and-families-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/the-administration-for-children-and-families/finops/the-administration-for-children-and-families-finops.yml
  title: ''
  type: FinOps
  url: finops/the-administration-for-children-and-families-finops.yml
- group: other
  href: https://artifacts.apis.io/the-administration-for-children-and-families/capabilities/the-administration-for-children-and-families-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/the-administration-for-children-and-families-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/HHS/TANF-app/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/HHS/TANF-app/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/HHS/TANF-app/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/HHS/TANF-app/blob/main/CONTRIBUTING.md
- group: agent
  href: https://artifacts.apis.io/the-administration-for-children-and-families/agentic-access/the-administration-for-children-and-families-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/the-administration-for-children-and-families-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/the-administration-for-children-and-families/security/the-administration-for-children-and-families-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/the-administration-for-children-and-families-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/the-administration-for-children-and-families/authentication/the-administration-for-children-and-families-authentication.yml
  title: ''
  type: Authentication
  url: authentication/the-administration-for-children-and-families-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/administration-for-children-and-families
- group: company
  title: ''
  type: Website
  url: https://www.acf.hhs.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://acf.gov/acf-data-research
- group: start
  title: ''
  type: Data Portal
  url: https://tanfdata.acf.hhs.gov/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HHS
- group: other
  title: ''
  type: Data Catalog
  url: https://catalog.data.gov/organization/hhs-acf
- group: other
  title: ''
  type: Interoperability
  url: https://acf.gov/about/interoperability
- group: docs
  href: https://artifacts.apis.io/the-administration-for-children-and-families/json-schema/acf-child-welfare-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/acf-child-welfare-schema.json
- group: docs
  href: https://artifacts.apis.io/the-administration-for-children-and-families/json-schema/acf-tanf-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/acf-tanf-schema.json
- group: design
  href: https://artifacts.apis.io/the-administration-for-children-and-families/json-ld/acf-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/acf-context.jsonld
- group: design
  href: https://artifacts.apis.io/the-administration-for-children-and-families/vocabulary/acf-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/acf-vocabulary.yml
created: '2024-11-20T00:00:00.000Z'
description: The Administration for Children and Families (ACF) is a division of the U.S. Department of Health and Human Services dedicated to promoting the economic and social well-being of children, families, and communities. ACF administers programs including TANF (cash assistance), CCDF (child care), Head Start, LIHEAP (energy assistance), child welfare, and refugee assistance. ACF collects administrative data via systems including AFCARS (foster care and adoption), NCANDS (child abuse and neglect), NYTD (youth in transition), TANF data reporting, and CCDF data. ACF is pursuing interoperability standards using HL7 FHIR and USCDI+ for human services data exchange. The TANF Data Portal (tanfdata.acf.hhs.gov) provides state agencies with a data submission and analysis interface.
finops:
- has_sources: false
  method: generated
  name: The Administration For Children And Families Finops
  primary_unit: request
  service_category: API
  slug: the-administration-for-children-and-families-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/the-administration-for-children-and-families.png
json_schemas:
- name: ACF Child Welfare Data
  property_count: 0
  slug: acf-child-welfare
- name: ACF TANF Data
  property_count: 0
  slug: acf-tanf
json_structures:
- name: Acf Data Structure
  property_count: 0
  slug: acf-data-structure
jsonld:
- class_count: 7
  name: Acf Context
  property_count: 21
  slug: acf-context
layout: provider
modified: '2026-07-25'
name: The Administration for Children and Families
nav: Providers
network: true
overview: 'The Administration for Children and Families publishes 19 API contracts indexed on the [APIs.io](https://apis.io/) network, including Plg Auth Check API, Auth Check API, Change Request Logs API, and 16 more. Tagged areas include Children, Families, Federal Government, Health And Human Services, and Human Services.


  The The Administration for Children and Families catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  The Administration for Children and Families'' developer surface includes authentication, documentation, and 20 more developer resources.'
plans:
- name: The Administration For Children And Families Plans Pricing
  plan_count: 3
  slug: the-administration-for-children-and-families-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: The Administration For Children And Families Rate Limits
  slug: the-administration-for-children-and-families-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: The Administration for Children and Families — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: the-administration-for-children-and-families-jsonschema-spectral-rules
score:
  band: thin
  composite: 30.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 61.8
    catalog_earned_first_party: 0.0
    catalog_gap: 53.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 23.5
    contract_quality: 52.4
    developer_ergonomics: 21.4
    discoverability: 66.1
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 30.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/the-administration-for-children-and-families/the-administration-for-children-and-families-2026-06-20T195211.png
security:
- kind: authentication
  name: The Administration For Children And Families Authentication
  slug: the-administration-for-children-and-families-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: The Administration For Children And Families Domain Security
  slug: the-administration-for-children-and-families-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: the-administration-for-children-and-families
tags:
- Children
- Families
- Federal Government
- Health And Human Services
- Human Services
- Social Safety Net
website: https://www.acf.hhs.gov/
---
