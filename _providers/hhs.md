---
access_model:
  confidence: medium
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.7
  scored_at: '2026-07-28'
api_count: 21
apis:
- description: OpenFDA provides RESTful APIs and raw download access to high-value FDA public datasets including drug adverse events, drug labels, drug recalls, medical device 510(k) clearances, device classificatio
  name: openFDA API
  slug: openfda-api
- description: The MyHealthfinder API (Version 4) allows developers to add evidence-based, plain language health content to their websites and applications. Content is available in English and Spanish and is complet
  name: MyHealthfinder API
  slug: myhealthfinder-api
- description: The ONC Health IT Open Data API provides access to open datasets published by the Office of the National Coordinator for Health Information Technology. Supports filtering by state and year, and return
  name: ONC Health IT Open Data API
  slug: onc-health-it-open-data-api
- description: The HRSA Health Center Data Web Service allows querying for federally qualified health centers by state, county, or ZIP code. A separate service provides access to Ryan White HIV/AIDS Medical Care Pro
  name: HRSA Health Center Data Web Service
  slug: hrsa-health-center-data-web-service
- description: The HealthData.gov Catalog API uses CKAN and provides machine-readable access to the HHS health data catalog. Developers can find newly added datasets, search the catalog, download catalog metadata fo
  name: HealthData.gov Catalog API
  slug: healthdatagov-catalog-api
- description: The Agency v1 API from HHS (US Department of Health and Human Services) — 1 operation(s) for agency v1.
  name: HHS (US Department of Health and Human Services) Agency v1 API
  slug: hhs-agency-v1-api
- description: The Application Alpha API from HHS (US Department of Health and Human Services) — 11 operation(s) for application alpha.
  name: HHS (US Department of Health and Human Services) Application Alpha API
  slug: hhs-application-alpha-api
- description: The Award Recommendation Alpha API from HHS (US Department of Health and Human Services) — 11 operation(s) for award recommendation alpha.
  name: HHS (US Department of Health and Human Services) Award Recommendation Alpha API
  slug: hhs-award-recommendation-alpha-api
- description: CommonGrants-compliant API routes for searching opportunities to promote interoperability across grant systems. Learn more by visiting CommonGrants.org
  name: HHS (US Department of Health and Human Services) CommonGrants Protocol API
  slug: hhs-commongrants-protocol-api
- description: The Competition Alpha API from HHS (US Department of Health and Human Services) — 3 operation(s) for competition alpha.
  name: HHS (US Department of Health and Human Services) Competition Alpha API
  slug: hhs-competition-alpha-api
- description: The Extract v1 API from HHS (US Department of Health and Human Services) — 1 operation(s) for extract v1.
  name: HHS (US Department of Health and Human Services) Extract v1 API
  slug: hhs-extract-v1-api
- description: The File v1 API from HHS (US Department of Health and Human Services) — 1 operation(s) for file v1.
  name: HHS (US Department of Health and Human Services) File v1 API
  slug: hhs-file-v1-api
- description: The Form Alpha API from HHS (US Department of Health and Human Services) — 2 operation(s) for form alpha.
  name: HHS (US Department of Health and Human Services) Form Alpha API
  slug: hhs-form-alpha-api
- description: The Health API from HHS (US Department of Health and Human Services) — 1 operation(s) for health.
  name: HHS (US Department of Health and Human Services) Health API
  slug: hhs-health-api
- description: The Internal v1 - Admin Only API from HHS (US Department of Health and Human Services) — 1 operation(s) for internal v1 - admin only.
  name: HHS (US Department of Health and Human Services) Internal v1 - Admin Only API
  slug: hhs-internal-v1-admin-only-api
- description: The LOCAL ONLY API from HHS (US Department of Health and Human Services) — 1 operation(s) for local only.
  name: HHS (US Department of Health and Human Services) LOCAL ONLY API
  slug: hhs-local-only-api
- description: The Opportunity v1 API from HHS (US Department of Health and Human Services) — 4 operation(s) for opportunity v1.
  name: HHS (US Department of Health and Human Services) Opportunity v1 API
  slug: hhs-opportunity-v1-api
- description: The Opportunity v1 - for Grantors API from HHS (US Department of Health and Human Services) — 8 operation(s) for opportunity v1 - for grantors.
  name: HHS (US Department of Health and Human Services) Opportunity v1 - for Grantors API
  slug: hhs-opportunity-v1-for-grantors-api
- description: The Organization v1 API from HHS (US Department of Health and Human Services) — 10 operation(s) for organization v1.
  name: HHS (US Department of Health and Human Services) Organization v1 API
  slug: hhs-organization-v1-api
- description: The User v1 - Internal Only API from HHS (US Department of Health and Human Services) — 23 operation(s) for user v1 - internal only.
  name: HHS (US Department of Health and Human Services) User v1 - Internal Only API
  slug: hhs-user-v1-internal-only-api
- description: The Workflow API from HHS (US Department of Health and Human Services) — 4 operation(s) for workflow.
  name: HHS (US Department of Health and Human Services) Workflow API
  slug: hhs-workflow-api
artifact_total: 40
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hhs-domain-security.yml
- group: build
  title: ''
  type: GitHub
  url: https://github.com/HHS
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hhs.gov/web/policies-and-standards/hhs-web-policies/terms-of-service/index.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hhs.gov/web/policies-and-standards/hhs-web-policies/privacy/index.html
- group: other
  title: ''
  type: OpenData
  url: https://healthdata.gov/
- group: operate
  title: ''
  type: Status
  url: https://www.hhs.gov/
- group: company
  title: ''
  type: Blog
  url: https://www.hhs.gov/about/news/index.html
- group: other
  title: ''
  type: Accessibility
  url: https://www.hhs.gov/web/policies-and-standards/hhs-web-policies/accessibility/index.html
created: '2026-06-13'
description: The US Department of Health and Human Services provides data APIs for health programs, public health datasets, grants data, and interoperability standards for health information. HHS operates a broad ecosystem of APIs spanning FDA drug and device data, grants opportunity search, health IT open data, HRSA health center locators, and public health content syndication through its agencies including FDA, HRSA, ONC, and ODPHP.
examples:
- key_count: 3
  name: Opportunity Search Request
  slug: opportunity-search-request
- key_count: 7
  name: Opportunity
  slug: opportunity
- key_count: 2
  name: V1_Agencies_Search_Post_Request
  slug: v1_agencies_search_post_request
- key_count: 1
  name: V1_Extracts_Post_Request
  slug: v1_extracts_post_request
- key_count: 2
  name: V1_Opportunities_Search_Csv_Post_Request
  slug: v1_opportunities_search_csv_post_request
- key_count: 7
  name: V1_Opportunities_Search_Post_Request
  slug: v1_opportunities_search_post_request
finops:
- name: Overview
  service_category: ''
  slug: overview
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hhs.png
json_schemas:
- name: AgencyV1Schema
  property_count: 8
  slug: agencyv1
- name: ErrorResponseSchema
  property_count: 5
  slug: errorresponse
- name: HealthcheckResponseSchema
  property_count: 3
  slug: healthcheckresponse
- name: OpportunitySearchResponseV1Schema
  property_count: 5
  slug: opportunitysearchresponsev1
- name: OpportunityV1Schema
  property_count: 16
  slug: opportunityv1
- name: PaginationInfoSchema
  property_count: 5
  slug: paginationinfo
layout: provider
modified: '2026-06-13'
name: HHS (US Department of Health and Human Services)
nav: Providers
network: true
overview: 'HHS (US Department of Health and Human Services) publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Agency v1 API, Application Alpha API, Award Recommendation Alpha API, and 13 more. Tagged areas include Health, Public Health, Grants, Interoperability, and FHIR.


  The HHS (US Department of Health and Human Services) catalog on APIs.io includes 1 Spectral governance ruleset.


  HHS (US Department of Health and Human Services)''s developer surface includes GitHub presence, status page, engineering blog, and 5 more developer resources.'
plans:
- name: Openfda
  plan_count: 2
  slug: openfda
- name: Simpler Grants
  plan_count: 2
  slug: simpler-grants
random_paper: 77
rate_limits:
- limit_count: 0
  name: Openfda
  slug: openfda
- limit_count: 0
  name: Simpler Grants
  slug: simpler-grants
rules:
- name: HHS (US Department of Health and Human Services) API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: hhs-jsonschema-spectral-rules
score:
  band: thin
  composite: 36.7
  delta: -6.8
  facets:
    commercial_clarity: 50.0
    contract_quality: 58.0
    developer_ergonomics: 2.2
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 43.5
  provenance:
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/hhs/refs/heads/main/screenshots/hhs-2026-06-20T182722.png
security:
- kind: domain-security
  name: Hhs Domain Security
  slug: hhs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: hhs
tags:
- Health
- Public Health
- Grants
- Interoperability
- FHIR
- Government
- Open Data
- FDA
- HRSA
- ONC
---
