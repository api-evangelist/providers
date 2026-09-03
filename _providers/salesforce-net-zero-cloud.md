---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 24.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Salesforce Net Zero Cloud Agentic Access
  operation_count: 16
  slug: salesforce-net-zero-cloud-agentic-access
  summary_line: 16 operations · 7 acting
api_count: 1
apis:
- description: API endpoints for carbon footprint calculations, emission factors, and sustainability metrics aggregation. Enables retrieval of emission factors and calculation of CO2e from activity data.
  name: Carbon Accounting API
  slug: carbon-accounting-api
- description: API for accessing and managing sustainability data including energy consumption, waste management, water usage, and renewable energy tracking.
  name: Sustainability Data API
  slug: sustainability-data-api
- baseURL: https://yourinstance.my.salesforce.com/services/data/v59.0/
  baseurl_source: declared
  description: Carbon emission record management
  name: Salesforce Net Zero Cloud Carbon Emissions API
  slug: salesforce-net-zero-cloud-carbon-emissions-api
- baseURL: https://yourinstance.my.salesforce.com/services/data/v59.0/
  baseurl_source: declared
  description: Emission factor data and calculations
  name: Salesforce Net Zero Cloud Emission Factors API
  slug: salesforce-net-zero-cloud-emission-factors-api
- baseURL: https://yourinstance.my.salesforce.com/services/data/v59.0/
  baseurl_source: declared
  description: Energy usage tracking and management
  name: Salesforce Net Zero Cloud Energy Consumption API
  slug: salesforce-net-zero-cloud-energy-consumption-api
- baseURL: https://yourinstance.my.salesforce.com/services/data/v59.0/
  baseurl_source: declared
  description: Environmental, Social, and Governance reporting
  name: Salesforce Net Zero Cloud ESG Reporting API
  slug: salesforce-net-zero-cloud-esg-reporting-api
- baseURL: https://yourinstance.my.salesforce.com/services/data/v59.0/
  baseurl_source: declared
  description: Net zero and sustainability target management
  name: Salesforce Net Zero Cloud Sustainability Goals API
  slug: salesforce-net-zero-cloud-sustainability-goals-api
- baseURL: https://yourinstance.my.salesforce.com/services/data/v59.0/
  baseurl_source: declared
  description: Waste and recycling data management
  name: Salesforce Net Zero Cloud Waste Management API
  slug: salesforce-net-zero-cloud-waste-management-api
- baseURL: https://yourinstance.my.salesforce.com/services/data/v59.0/
  baseurl_source: declared
  description: Water consumption tracking
  name: Salesforce Net Zero Cloud Water Usage API
  slug: salesforce-net-zero-cloud-water-usage-api
artifact_total: 40
collections:
- collection_type: postman
  name: Salesforce Net Zero Cloud REST Carbon Emissions API
  slug: postman-salesforce-net-zero-cloud-carbon-emissions-api
- collection_type: postman
  name: Salesforce Net Zero Cloud REST Carbon Emissions Emission Factors API
  slug: postman-salesforce-net-zero-cloud-emission-factors-api
- collection_type: postman
  name: Salesforce Net Zero Cloud REST Carbon Emissions Energy Consumption API
  slug: postman-salesforce-net-zero-cloud-energy-consumption-api
- collection_type: postman
  name: Salesforce Net Zero Cloud REST Carbon Emissions ESG Reporting API
  slug: postman-salesforce-net-zero-cloud-esg-reporting-api
- collection_type: postman
  name: Salesforce Net Zero Cloud REST Carbon Emissions Sustainability Goals API
  slug: postman-salesforce-net-zero-cloud-sustainability-goals-api
- collection_type: postman
  name: Salesforce Net Zero Cloud REST Carbon Emissions Waste Management API
  slug: postman-salesforce-net-zero-cloud-waste-management-api
- collection_type: postman
  name: Salesforce Net Zero Cloud REST Carbon Emissions Water Usage API
  slug: postman-salesforce-net-zero-cloud-water-usage-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Salesforce Net Zero Cloud REST Carbon Emissions API
  slug: open-salesforce-net-zero-cloud-carbon-emissions-api
- collection_type: open
  name: Salesforce Net Zero Cloud REST Carbon Emissions Emission Factors API
  slug: open-salesforce-net-zero-cloud-emission-factors-api
- collection_type: open
  name: Salesforce Net Zero Cloud REST Carbon Emissions Energy Consumption API
  slug: open-salesforce-net-zero-cloud-energy-consumption-api
- collection_type: open
  name: Salesforce Net Zero Cloud REST Carbon Emissions ESG Reporting API
  slug: open-salesforce-net-zero-cloud-esg-reporting-api
- collection_type: open
  name: Salesforce Net Zero Cloud REST API
  slug: open-salesforce-net-zero-cloud-rest-api
- collection_type: open
  name: Salesforce Net Zero Cloud REST Carbon Emissions Sustainability Goals API
  slug: open-salesforce-net-zero-cloud-sustainability-goals-api
- collection_type: open
  name: Salesforce Net Zero Cloud REST Carbon Emissions Waste Management API
  slug: open-salesforce-net-zero-cloud-waste-management-api
- collection_type: open
  name: Salesforce Net Zero Cloud REST Carbon Emissions Water Usage API
  slug: open-salesforce-net-zero-cloud-water-usage-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/salesforce-net-zero-cloud/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/salesforce-net-zero-cloud-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/salesforce-net-zero-cloud-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/salesforce-net-zero-cloud-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/salesforce-net-zero-cloud-scopes.yml
- group: company
  title: ''
  type: Blog
  url: https://developer.salesforce.com/blogs/feed
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.salesforce.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://trailhead.salesforce.com/content/learn/modules/net-zero-cloud-basics
- group: auth
  title: ''
  type: Authentication
  url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_oauth_and_connected_apps.htm
- group: operate
  title: ''
  type: StatusPage
  url: https://status.salesforce.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.salesforce.com/company/legal/agreements/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.salesforce.com/company/privacy/
- group: learn
  title: ''
  type: Trailhead Learning
  url: https://trailhead.salesforce.com/content/learn/trails/get-started-with-net-zero-cloud
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://help.salesforce.com/s/articleView?id=release-notes.salesforce_release_notes.htm
- group: operate
  title: ''
  type: Support
  url: https://help.salesforce.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/salesforce
- group: design
  title: ''
  type: SpectralRules
  url: rules/salesforce-net-zero-cloud-rules.yml
- group: docs
  title: Carbon Emission Schema
  type: JSONSchema
  url: json-schema/salesforce-net-zero-cloud-carbon-emission-schema.json
- group: docs
  title: Sustainability Goal Schema
  type: JSONSchema
  url: json-schema/salesforce-net-zero-cloud-sustainability-goal-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/salesforce-net-zero-cloud-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/salesforce-net-zero-cloud-vocabulary.yml
created: '2024'
description: The Salesforce Net Zero Cloud API enables organizations to track, analyze, and report on their carbon emissions and sustainability data. It provides programmatic access to environmental data, carbon accounting, and ESG reporting capabilities including Scope 1, 2, and 3 emissions tracking, energy consumption, waste management, water usage, and sustainability goal management.
examples:
- key_count: 7
  name: Salesforce Net Zero Cloud Create Carbon Emission Example
  slug: salesforce-net-zero-cloud-create-carbon-emission-example
- key_count: 7
  name: Salesforce Net Zero Cloud List Sustainability Goals Example
  slug: salesforce-net-zero-cloud-list-sustainability-goals-example
finops:
- name: Salesforce Net Zero Cloud Finops
  service_category: Sustainability / ESG
  slug: salesforce-net-zero-cloud-finops
image: https://www.salesforce.com/content/dam/web/en_us/www/images/logo-salesforce.svg
json_schemas:
- name: Salesforce Net Zero Cloud Carbon Emission
  property_count: 14
  slug: salesforce-net-zero-cloud-carbon-emission
- name: Salesforce Net Zero Cloud Sustainability Goal
  property_count: 10
  slug: salesforce-net-zero-cloud-sustainability-goal
json_structures:
- name: Salesforce Net Zero Cloud Carbon Emission Structure
  property_count: 0
  slug: salesforce-net-zero-cloud-carbon-emission-structure
jsonld:
- class_count: 0
  name: Salesforce Net Zero Cloud Context
  property_count: 26
  slug: salesforce-net-zero-cloud-context
layout: provider
modified: '2026-05-19'
name: Salesforce Net Zero Cloud
nav: Providers
network: true
overview: 'Salesforce Net Zero Cloud publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Carbon Emissions API, Emission Factors API, Energy Consumption API, and 4 more. Tagged areas include Carbon Accounting, Carbon Emissions, Climate, Environmental, and ESG.


  The Salesforce Net Zero Cloud catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Salesforce Net Zero Cloud''s developer surface includes authentication, engineering blog, getting-started guide, release notes, support, and 16 more developer resources.'
plans:
- name: Salesforce Net Zero Cloud Plans Pricing
  plan_count: 1
  slug: salesforce-net-zero-cloud-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Salesforce Net Zero Cloud Rate Limits
  slug: salesforce-net-zero-cloud-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Salesforce Net Zero Cloud API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: salesforce-net-zero-cloud-jsonschema-spectral-rules
- effective_rule_count: 9
  extends: []
  name: Salesforce Net Zero Cloud API Rules
  rule_count: 9
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 4
  slug: salesforce-net-zero-cloud-rules
scopes:
- name: Salesforce Net Zero Cloud Scopes
  scope_count: 1
  slug: salesforce-net-zero-cloud-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 47.2
  coverage:
    artifact_dirs: 18
    catalog_gap: 54.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 25.0
    contract_quality: 63.0
    developer_ergonomics: 54.8
    discoverability: 75.9
    governance: 25.0
    operational_transparency: 23.7
  previous_composite: 47.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/salesforce-net-zero-cloud/refs/heads/main/screenshots/salesforce-net-zero-cloud-2026-06-20T193349.png
security:
- kind: authentication
  name: Salesforce Net Zero Cloud Authentication
  slug: salesforce-net-zero-cloud-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Salesforce Net Zero Cloud Domain Security
  slug: salesforce-net-zero-cloud-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: salesforce-net-zero-cloud
tags:
- Carbon Accounting
- Carbon Emissions
- Climate
- Environmental
- ESG
- Net Zero
- Sustainability
website: https://developer.salesforce.com/
---
