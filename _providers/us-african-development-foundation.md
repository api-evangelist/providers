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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.1
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Us African Development Foundation Agentic Access
  operation_count: 7
  slug: us-african-development-foundation-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 5
apis:
- description: USADF agency spending and budget data
  name: US African Development Foundation Agency API
  slug: us-african-development-foundation-agency-api
- description: USADF grant award data
  name: US African Development Foundation Awards API
  slug: us-african-development-foundation-awards-api
- description: USADF grant opportunity listings on Grants.gov
  name: US African Development Foundation Opportunities API
  slug: us-african-development-foundation-opportunities-api
- description: Organizations receiving USADF grants
  name: US African Development Foundation Recipients API
  slug: us-african-development-foundation-recipients-api
- description: USADF spending breakdowns and analytics
  name: US African Development Foundation Spending API
  slug: us-african-development-foundation-spending-api
artifact_total: 70
collections:
- collection_type: open
  name: USADF Grant Opportunities API
  slug: open-usadf-grant-opportunities-api
- collection_type: open
  name: USADF Grants Data API
  slug: open-usadf-grants-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/us-african-development-foundation-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/us-african-development-foundation-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usadf
- group: company
  title: ''
  type: Website
  url: https://www.usadf.gov
- group: start
  title: USASpending Spending Profile
  type: Portal
  url: https://www.usaspending.gov/agency/african-development-foundation
- group: other
  title: USASpending API
  type: DataAPI
  url: https://api.usaspending.gov
- group: other
  title: Grants.gov USADF Listings
  type: DataAPI
  url: https://www.grants.gov/search-grants?agencyCode=ADF
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usadf
- group: design
  title: ''
  type: JSONLD
  url: json-ld/us-african-development-foundation-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/us-african-development-foundation-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/us-african-development-foundation-vocabulary.yaml
created: '2024-11-20'
description: The US African Development Foundation (USADF) is an independent federal agency established by Congress in 1980 to invest directly in African grassroots enterprises and social entrepreneurs. USADF provides grant capital of up to $250,000, capacity-building assistance, and convening opportunities to develop, grow, and scale African enterprises and entrepreneurs. USADF grant data is publicly accessible via the USASpending.gov API, and grant opportunities are posted to Grants.gov. Between 2019 and 2023, USADF awarded more than $141 million in grants to over 1,050 community enterprises in Africa, directly affecting 6.2 million people.
examples:
- key_count: 2
  name: Grant Opportunities Api Apierror Example
  slug: grant-opportunities-api-apierror-example
- key_count: 19
  name: Grant Opportunities Api Opportunity Example
  slug: grant-opportunities-api-opportunity-example
- key_count: 7
  name: Grant Opportunities Api Opportunitysearchrequest Example
  slug: grant-opportunities-api-opportunitysearchrequest-example
- key_count: 5
  name: Grant Opportunities Api Opportunitysearchresponse Example
  slug: grant-opportunities-api-opportunitysearchresponse-example
- key_count: 6
  name: Grants Api Agencyawardsummary Example
  slug: grants-api-agencyawardsummary-example
- key_count: 2
  name: Grants Api Apierror Example
  slug: grants-api-apierror-example
- key_count: 13
  name: Grants Api Award Example
  slug: grants-api-award-example
- key_count: 6
  name: Grants Api Awardsearchrequest Example
  slug: grants-api-awardsearchrequest-example
- key_count: 3
  name: Grants Api Awardsearchresponse Example
  slug: grants-api-awardsearchresponse-example
- key_count: 3
  name: Grants Api Placeofperformance Example
  slug: grants-api-placeofperformance-example
- key_count: 7
  name: Grants Api Recipient Example
  slug: grants-api-recipient-example
- key_count: 2
  name: Grants Api Recipientsummary Example
  slug: grants-api-recipientsummary-example
- key_count: 3
  name: Grants Api Spendingbygeographyrequest Example
  slug: grants-api-spendingbygeographyrequest-example
- key_count: 3
  name: Grants Api Spendingbygeographyresponse Example
  slug: grants-api-spendingbygeographyresponse-example
features:
- description: USADF grant award data publicly accessible via USASpending.gov API, including recipient, country, amount, and award period for all USADF grants.
  name: Grant Award Transparency
- description: USADF posts open grant solicitations on Grants.gov for African grassroots enterprises seeking funding up to $250,000.
  name: Grant Opportunity Listings
- description: Comprehensive USADF spending data accessible through USASpending.gov including account data, award breakdowns, and budget authority.
  name: Agency Spending Profile
- description: Data on organizations receiving USADF grants across 24 African countries, including grant amounts, periods of performance, and program areas.
  name: Recipient Data
finops:
- name: Us African Development Foundation Finops
  service_category: API
  slug: us-african-development-foundation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/us-african-development-foundation.png
integrations:
- description: Federal awards transparency platform providing API access to all USADF grant awards, recipient data, and spending profiles.
  name: USASpending.gov
- description: Federal grant opportunity portal where USADF posts open solicitations for African grassroots enterprise grants.
  name: Grants.gov
- description: System for Award Management where USADF grant recipients register to receive federal award funding.
  name: SAM.gov
- description: Federal Procurement Data System tracking USADF contract and interagency agreement spending.
  name: FPDS-NG
- description: USAID Office of Inspector General providing independent oversight of USADF grants administration and partnerships.
  name: USAID OIG
json_schemas:
- name: APIError
  property_count: 2
  slug: grant-opportunities-api-apierror
- name: Opportunity
  property_count: 19
  slug: grant-opportunities-api-opportunity
- name: OpportunitySearchRequest
  property_count: 7
  slug: grant-opportunities-api-opportunitysearchrequest
- name: OpportunitySearchResponse
  property_count: 5
  slug: grant-opportunities-api-opportunitysearchresponse
- name: AgencyAwardSummary
  property_count: 6
  slug: grants-api-agencyawardsummary
- name: APIError
  property_count: 2
  slug: grants-api-apierror
- name: Award
  property_count: 13
  slug: grants-api-award
- name: AwardSearchRequest
  property_count: 6
  slug: grants-api-awardsearchrequest
- name: AwardSearchResponse
  property_count: 3
  slug: grants-api-awardsearchresponse
- name: PlaceOfPerformance
  property_count: 3
  slug: grants-api-placeofperformance
- name: Recipient
  property_count: 7
  slug: grants-api-recipient
- name: RecipientSummary
  property_count: 2
  slug: grants-api-recipientsummary
- name: SpendingByGeographyRequest
  property_count: 3
  slug: grants-api-spendingbygeographyrequest
- name: SpendingByGeographyResponse
  property_count: 3
  slug: grants-api-spendingbygeographyresponse
json_structures:
- name: Grant Opportunities Api Apierror Structure
  property_count: 0
  slug: grant-opportunities-api-apierror-structure
- name: Grant Opportunities Api Opportunity Structure
  property_count: 0
  slug: grant-opportunities-api-opportunity-structure
- name: Grant Opportunities Api Opportunitysearchrequest Structure
  property_count: 0
  slug: grant-opportunities-api-opportunitysearchrequest-structure
- name: Grant Opportunities Api Opportunitysearchresponse Structure
  property_count: 0
  slug: grant-opportunities-api-opportunitysearchresponse-structure
- name: Grants Api Agencyawardsummary Structure
  property_count: 0
  slug: grants-api-agencyawardsummary-structure
- name: Grants Api Apierror Structure
  property_count: 0
  slug: grants-api-apierror-structure
- name: Grants Api Award Structure
  property_count: 0
  slug: grants-api-award-structure
- name: Grants Api Awardsearchrequest Structure
  property_count: 0
  slug: grants-api-awardsearchrequest-structure
- name: Grants Api Awardsearchresponse Structure
  property_count: 0
  slug: grants-api-awardsearchresponse-structure
- name: Grants Api Placeofperformance Structure
  property_count: 0
  slug: grants-api-placeofperformance-structure
- name: Grants Api Recipient Structure
  property_count: 0
  slug: grants-api-recipient-structure
- name: Grants Api Recipientsummary Structure
  property_count: 0
  slug: grants-api-recipientsummary-structure
- name: Grants Api Spendingbygeographyrequest Structure
  property_count: 0
  slug: grants-api-spendingbygeographyrequest-structure
- name: Grants Api Spendingbygeographyresponse Structure
  property_count: 0
  slug: grants-api-spendingbygeographyresponse-structure
jsonld:
- class_count: 51
  name: Us African Development Foundation Context
  property_count: 29
  slug: us-african-development-foundation-context
layout: provider
modified: '2026-05-19'
name: US African Development Foundation
nav: Providers
network: true
overview: 'US African Development Foundation publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Agency API, Awards API, Opportunities API, and 2 more. Tagged areas include Federal Government, International Development, Africa, Grants, and Nonprofit.


  The US African Development Foundation catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  US African Development Foundation''s developer surface includes developer portal and 10 more developer resources.'
plans:
- name: Us African Development Foundation Plans Pricing
  plan_count: 3
  slug: us-african-development-foundation-plans-pricing
random_paper: 109
rate_limits:
- limit_count: 5
  name: Us African Development Foundation Rate Limits
  slug: us-african-development-foundation-rate-limits
rules:
- name: US African Development Foundation API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: us-african-development-foundation-jsonschema-spectral-rules
- name: US African Development Foundation API Rules
  rule_count: 31
  severity_counts:
    error: 7
    hint: 8
    info: 1
    warn: 15
  slug: us-african-development-foundation-spectral-rules
score:
  band: thin
  composite: 28.5
  delta: -9.5
  facets:
    commercial_clarity: 15.8
    contract_quality: 30.4
    developer_ergonomics: 8.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 13.2
  previous_composite: 38.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/us-african-development-foundation/refs/heads/main/screenshots/us-african-development-foundation-2026-06-20T200541.png
security:
- kind: domain-security
  name: Us African Development Foundation Domain Security
  slug: us-african-development-foundation-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: us-african-development-foundation
tags:
- Federal Government
- International Development
- Africa
- Grants
- Nonprofit
- Economic Development
use_cases:
- description: Researchers and journalists accessing USADF grant award data through USASpending API to analyze funding patterns across African countries.
  name: Grant Transparency Research
- description: African enterprises and NGOs finding and applying for USADF grant opportunities through Grants.gov listings.
  name: Grant Opportunity Discovery
- description: Policy analysts tracking USADF budget authority, obligations, and outlays through USASpending federal account data.
  name: Federal Spending Analysis
- description: Development finance institutions and donors assessing USADF program reach and impact through award data and recipient profiles.
  name: Development Impact Tracking
website: https://www.usadf.gov
---
