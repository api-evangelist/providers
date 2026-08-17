---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Mockaroo Agentic Access
  operation_count: 11
  slug: mockaroo-agentic-access
  summary_line: 11 operations · 9 acting
api_count: 4
apis:
- description: Manage named CSV datasets used as lookup sources.
  name: Mockaroo Datasets API
  slug: mockaroo-datasets-api
- description: Manage long-running background generation jobs.
  name: Mockaroo Downloads API
  slug: mockaroo-downloads-api
- description: Generate mock data records on demand in multiple formats.
  name: Mockaroo Generate API
  slug: mockaroo-generate-api
- description: Discover available built-in field types.
  name: Mockaroo Types API
  slug: mockaroo-types-api
artifact_total: 75
collections:
- collection_type: postman
  name: Mockaroo Datasets API
  slug: postman-mockaroo-datasets-api
- collection_type: postman
  name: Mockaroo Datasets Downloads API
  slug: postman-mockaroo-downloads-api
- collection_type: postman
  name: Mockaroo Datasets Generate API
  slug: postman-mockaroo-generate-api
- collection_type: postman
  name: Mockaroo Datasets Types API
  slug: postman-mockaroo-types-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Mockaroo Datasets API
  slug: open-mockaroo-datasets-api
- collection_type: open
  name: Mockaroo Datasets Downloads API
  slug: open-mockaroo-downloads-api
- collection_type: open
  name: Mockaroo Datasets Generate API
  slug: open-mockaroo-generate-api
- collection_type: open
  name: Mockaroo Datasets Types API
  slug: open-mockaroo-types-api
- collection_type: open
  name: Mockaroo API
  slug: open-mockaroo
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/mockaroo/mockaroo-node/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/mockaroo/mockaroo-node/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/mockaroo/mockaroo-node/blob/master/LICENSE
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/mockaroo/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mockaroo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mockaroo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mockaroo-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.mockaroo.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.mockaroo.com/docs
- group: start
  title: ''
  type: Signup
  url: https://www.mockaroo.com/users/sign_up
- group: start
  title: ''
  type: Login
  url: https://www.mockaroo.com/users/sign_in
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mockaroo.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/mockaroo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mockaroo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mockaroo-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.mockaroo.com/blog
- group: other
  title: ''
  type: X
  url: https://x.com/mockaroodev
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mockaroo.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mockaroo.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.mockaroo.com/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mockaroo
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/mockaroo/mockaroo-node
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/mockaroo/mockaroo-enterprise
- group: build
  title: ''
  type: SDKs
  url: https://github.com/mockaroo/mockaroo-node
- group: build
  title: ''
  type: SDKs
  url: https://github.com/amogram/NMockaroo
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Ackara/Mockaroo.NET
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Scarvy/mockaroo-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/lockedata/mockaRoo
- group: build
  title: ''
  type: SDKs
  url: https://github.com/djhvscf/mockaroo.api
- group: build
  title: ''
  type: SDKs
  url: https://github.com/djuang1/mockaroo-connector
- group: design
  title: ''
  type: SpectralRules
  url: rules/mockaroo-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/mockaroo-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/mockaroo-context.jsonld
created: '2026-06-13'
description: Mockaroo is a realistic mock data generator and API mocking service used by developers and QA teams to produce JSON, CSV, TXT, custom-delimited, SQL, and XML test data. The platform combines a schema designer, 150+ built-in field types (Name, Internet, Address, Business, Date, Currency, Geographic, Phone, Health, Technology, and more), named datasets used as lookup sources, hosted mock APIs, formulas, projects, AI-assisted field generation, de-identification, and a REST API for programmatic generation. Mockaroo ships in four tiers (Free, Silver, Gold, Enterprise), with the Enterprise tier available as a Docker image for self-hosted, unlimited generation.
examples:
- key_count: 2
  name: Mockaroo Cancel Download Example
  slug: mockaroo-cancel-download-example
- key_count: 4
  name: Mockaroo Dataset Example
  slug: mockaroo-dataset-example
- key_count: 2
  name: Mockaroo Delete Dataset Example
  slug: mockaroo-delete-dataset-example
- key_count: 5
  name: Mockaroo Download Example
  slug: mockaroo-download-example
- key_count: 4
  name: Mockaroo Field Type Example
  slug: mockaroo-field-type-example
- key_count: 2
  name: Mockaroo Generate Csv Example
  slug: mockaroo-generate-csv-example
- key_count: 2
  name: Mockaroo Generate Custom Example
  slug: mockaroo-generate-custom-example
- key_count: 2
  name: Mockaroo Generate Json Example
  slug: mockaroo-generate-json-example
- key_count: 2
  name: Mockaroo Generate Sql Example
  slug: mockaroo-generate-sql-example
- key_count: 2
  name: Mockaroo Generate Txt Example
  slug: mockaroo-generate-txt-example
- key_count: 2
  name: Mockaroo Generate Xml Example
  slug: mockaroo-generate-xml-example
- key_count: 2
  name: Mockaroo Get Download Example
  slug: mockaroo-get-download-example
- key_count: 2
  name: Mockaroo List Types Example
  slug: mockaroo-list-types-example
- key_count: 2
  name: Mockaroo Upload Dataset Example
  slug: mockaroo-upload-dataset-example
features:
- description: Generate realistic test records using more than 150 built-in field types spanning names, addresses, business, internet, dates, currency, geography, phone, health, and technology categories.
  name: Realistic Mock Data Generation
- description: Export generated data as JSON, CSV, tab-separated TXT, custom delimiter, SQL INSERT statements, or XML.
  name: Multiple Output Formats
- description: Design, save, and reuse schemas in the web UI, then call them by name from the REST API.
  name: Schema Designer
- description: Upload CSV or plain-text datasets and use them as lookup sources in schemas via the Dataset Column field type.
  name: Datasets As Lookup Sources
- description: Host mock REST endpoints that return generated records on demand, including configurable error conditions.
  name: Mock APIs
- description: Submit large generation requests asynchronously and poll /api/downloads/{id} for status, progress, and the final download URL.
  name: Background Generation
- description: Transform generated values with reusable Mockaroo formula expressions and custom functions.
  name: Formulas And Custom Functions
- description: Generate field definitions and custom types using AI assistance in the schema editor.
  name: AI Field Generation
- description: Anonymize sensitive datasets via Mockaroo's de-identification tooling.
  name: De-identification
- description: Run Mockaroo as a self-hosted Docker container inside a private cloud or datacenter for unlimited, organization-wide generation.
  name: Enterprise Docker Deployment
finops:
- name: Mockaroo Finops
  service_category: Developer Tools
  slug: mockaroo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mockaroo.png
integrations:
- description: Official mockaroo-node Promise-based client for the Generate API.
  name: Node.js
- description: Community NMockaroo and Mockaroo.NET libraries.
  name: .NET / C#
- description: Community mockaroo-python wrapper.
  name: Python
- description: Community mockaRoo package for the Generate API.
  name: R
- description: Community mockaroo.api Java client.
  name: Java
- description: Community MuleSoft connector for invoking Mockaroo schemas.
  name: MuleSoft
- description: testdata sfdx plugin generates Salesforce test data via Mockaroo schemas.
  name: Salesforce CLI
- description: mockaroo2kafka scripts feed generated records into Kafka topics for streaming tests.
  name: Kafka
- description: Community mockaroo-mcp MCP server exposes Mockaroo's generate surface to LLM agents.
  name: MCP
- description: Mockaroo Enterprise is distributed as a Docker image for self-hosted deployment.
  name: Docker
json_schemas:
- name: Mockaroo Dataset
  property_count: 4
  slug: mockaroo-dataset
- name: Mockaroo Background Download
  property_count: 6
  slug: mockaroo-download
- name: Mockaroo Field Spec
  property_count: 4
  slug: mockaroo-field-spec
- name: Mockaroo Field Type
  property_count: 4
  slug: mockaroo-field-type
json_structures:
- name: Mockaroo Dataset Structure
  property_count: 4
  slug: mockaroo-dataset-structure
- name: Mockaroo Download Structure
  property_count: 6
  slug: mockaroo-download-structure
- name: Mockaroo Field Spec Structure
  property_count: 4
  slug: mockaroo-field-spec-structure
- name: Mockaroo Field Type Structure
  property_count: 4
  slug: mockaroo-field-type-structure
jsonld:
- class_count: 16
  name: Mockaroo Context
  property_count: 6
  slug: mockaroo-context
layout: provider
modified: '2026-06-13'
name: Mockaroo
nav: Providers
network: true
overview: 'Mockaroo publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Datasets API, Downloads API, Generate API, and 1 more. Tagged areas include Test Data, Mock Data, API Mocking, Data Generation, and Developer Tools.


  The Mockaroo catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Mockaroo''s developer surface includes authentication, documentation, signup flow, pricing, engineering blog, support, and 27 more developer resources.'
plans:
- name: Mockaroo Plans Pricing
  plan_count: 4
  slug: mockaroo-plans-pricing
random_paper: 114
rate_limits:
- limit_count: 9
  name: Mockaroo Rate Limits
  slug: mockaroo-rate-limits
rules:
- name: Mockaroo API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: mockaroo-jsonschema-spectral-rules
- name: Mockaroo API Rules
  rule_count: 10
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 3
  slug: mockaroo-rules
score:
  band: exemplar
  composite: 67.7
  delta: 0.0
  facets:
    commercial_clarity: 84.2
    contract_quality: 73.9
    developer_ergonomics: 45.7
    discoverability: 81.5
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 67.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mockaroo/refs/heads/main/screenshots/mockaroo-2026-06-20T185637.png
security:
- kind: authentication
  name: Mockaroo Authentication
  slug: mockaroo-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Mockaroo Domain Security
  slug: mockaroo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mockaroo
solutions:
- description: 1,000 records per file, 200 API requests per day.
  name: Free
- description: $60/year. 100,000 records per file, 1,000,000 records per day.
  name: Silver
- description: $500/year. 10,000,000 records per file, 10,000,000 records per day.
  name: Gold
- description: $7,500/year. Self-hosted Docker, unlimited generation, organization-wide access.
  name: Enterprise
tags:
- Test Data
- Mock Data
- API Mocking
- Data Generation
- Developer Tools
- QA Testing
- Realistic Data
- Schemas
- Datasets
- Public APIs
use_cases:
- description: Power UI prototypes with realistic request/response data so design reviews surface real edge cases (long names, Unicode, blanks).
  name: UI Prototyping
- description: Generate millions of realistic records to populate staging databases for load and performance testing.
  name: Load And Performance Testing
- description: Produce repeatable, schema-driven test data for automated test suites and continuous integration pipelines.
  name: QA Test Data
- description: Stand up demo environments with believable customer data without touching production.
  name: Demo And Sales Environments
- description: Replace sensitive production data with statistically similar but synthetic records for safe sharing.
  name: Data Anonymization
- description: Front-end and integration teams hit Mockaroo-hosted mock APIs while back-end services are still under construction.
  name: API Mocking
website: https://www.mockaroo.com
---
