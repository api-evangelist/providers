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
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.2
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Amazon Quicksight Agentic Access
  operation_count: 3
  slug: amazon-quicksight-agentic-access
  summary_line: 3 operations
api_count: 2
apis:
- description: Operations for creating and managing dashboards
  name: Amazon QuickSight Dashboards API
  slug: amazon-quicksight-dashboards-api
- description: Operations for managing datasets
  name: Amazon QuickSight Datasets API
  slug: amazon-quicksight-datasets-api
arazzos:
- description: Catalog the datasets and dashboards in an account and describe a sample dashboard.
  name: Amazon QuickSight Account BI Inventory
  slug: amazon-quicksight-account-bi-inventory-workflow
- description: List dashboards, describe one, and branch on whether its version failed to publish.
  name: Amazon QuickSight Audit Dashboard Publish Health
  slug: amazon-quicksight-audit-dashboard-publish-health-workflow
- description: List an account's datasets and branch on whether any use SPICE import mode.
  name: Amazon QuickSight Classify Datasets by Import Mode
  slug: amazon-quicksight-classify-datasets-by-import-mode-workflow
- description: List the dashboards in an account, then fetch the full detail for one of them.
  name: Amazon QuickSight Describe a Dashboard
  slug: amazon-quicksight-describe-dashboard-workflow
- description: Search the account dashboard list for a name match and describe the match.
  name: Amazon QuickSight Find a Dashboard by Name
  slug: amazon-quicksight-find-dashboard-by-name-workflow
- description: Repeatedly describe a dashboard until its version status settles, then branch.
  name: Amazon QuickSight Poll Dashboard Publish Status
  slug: amazon-quicksight-poll-dashboard-status-workflow
artifact_total: 36
collections:
- collection_type: postman
  name: Amazon QuickSight API
  slug: postman-amazon-quicksight
- collection_type: open
  name: Amazon QuickSight API
  slug: open-amazon-quicksight
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-quicksight-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-quicksight-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-quicksight-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-quicksight-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-quicksight/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-quicksight-account-bi-inventory-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-quicksight-audit-dashboard-publish-health-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-quicksight-classify-datasets-by-import-mode-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-quicksight-describe-dashboard-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-quicksight-find-dashboard-by-name-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-quicksight-poll-dashboard-status-workflow.yml
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/business-intelligence/category/analytics/amazon-quicksight/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: start
  title: ''
  type: Portal
  url: https://quicksight.aws.amazon.com/
- group: build
  title: ''
  type: CLI
  url: https://docs.aws.amazon.com/cli/latest/reference/quicksight/
- group: build
  title: ''
  type: SDKs
  url: https://aws.amazon.com/tools/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aws.amazon.com/
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/quicksight/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/quicksight/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/quicksight/pricing/
- group: start
  title: ''
  type: GettingStarted
  url: https://aws.amazon.com/quicksight/getting-started/
- group: operate
  title: ''
  type: FAQ
  url: https://aws.amazon.com/quicksight/faqs/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-quicksight
- group: build
  title: ''
  type: CodeExamples
  url: https://docs.aws.amazon.com/code-library/latest/ug/quicksight_code_examples.html
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-quicksight-openapi-dashboard-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-quicksight-openapi-dashboard-summary-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-quicksight-openapi-data-set-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-quicksight-schema.json-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-quicksight-openapi-dashboard-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-quicksight-openapi-dashboard-summary-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-quicksight-openapi-data-set-summary-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-quicksight-openapi-dashboard-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-quicksight-openapi-dashboard-summary-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-quicksight-openapi-data-set-summary-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-quicksight-structure.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-quicksight-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-quicksight-openapi-dashboard-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-quicksight-openapi-dashboard-summary-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-quicksight-openapi-data-set-summary-example.json
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-quicksight-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-quicksight-vocabulary.yaml
created: '2024-01-15'
description: Amazon QuickSight is a scalable, serverless, embeddable, machine learning-powered business intelligence service built for the cloud that enables you to create and publish interactive dashboards.
examples:
- key_count: 7
  name: Amazon Quicksight Example
  slug: amazon-quicksight-example
- key_count: 7
  name: Amazon Quicksight Openapi Dashboard Example
  slug: amazon-quicksight-openapi-dashboard-example
- key_count: 7
  name: Amazon Quicksight Openapi Dashboard Summary Example
  slug: amazon-quicksight-openapi-dashboard-summary-example
- key_count: 6
  name: Amazon Quicksight Openapi Data Set Summary Example
  slug: amazon-quicksight-openapi-data-set-summary-example
finops:
- name: Amazon Quicksight Finops
  service_category: API
  slug: amazon-quicksight-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: Dashboard
  property_count: 7
  slug: amazon-quicksight-openapi-dashboard
- name: DashboardSummary
  property_count: 7
  slug: amazon-quicksight-openapi-dashboard-summary
- name: DataSetSummary
  property_count: 6
  slug: amazon-quicksight-openapi-data-set-summary
- name: Amazon QuickSight Dashboard Definition
  property_count: 7
  slug: amazon-quicksight
json_structures:
- name: Amazon Quicksight Openapi Dashboard Structure
  property_count: 7
  slug: amazon-quicksight-openapi-dashboard-structure
- name: Amazon Quicksight Openapi Dashboard Summary Structure
  property_count: 7
  slug: amazon-quicksight-openapi-dashboard-summary-structure
- name: Amazon Quicksight Openapi Data Set Summary Structure
  property_count: 6
  slug: amazon-quicksight-openapi-data-set-summary-structure
- name: Amazon Quicksight Structure
  property_count: 7
  slug: amazon-quicksight-structure
jsonld:
- class_count: 0
  name: Amazon Quicksight Context
  property_count: 5
  slug: amazon-quicksight-context
- class_count: 1
  name: Amazon Quicksight Openapi Dashboard Context
  property_count: 9
  slug: amazon-quicksight-openapi-dashboard-context
- class_count: 1
  name: Amazon Quicksight Openapi Dashboard Summary Context
  property_count: 7
  slug: amazon-quicksight-openapi-dashboard-summary-context
- class_count: 1
  name: Amazon Quicksight Openapi Data Set Context
  property_count: 6
  slug: amazon-quicksight-openapi-data-set-context
- class_count: 1
  name: Amazon Quicksight Schema.Json Context
  property_count: 7
  slug: amazon-quicksight-schema.json-context
layout: provider
modified: '2026-05-19'
name: Amazon QuickSight
nav: Providers
network: true
overview: 'Amazon QuickSight publishes 2 APIs on the [APIs.io](https://apis.io/) network: Dashboards API and Datasets API. Tagged areas include Analytics, BI, Business Intelligence, Dashboards, and Machine Learning.


  The Amazon QuickSight catalog on APIs.io includes 5 JSON-LD contexts and 2 Spectral governance rulesets.


  Amazon QuickSight''s developer surface includes authentication, engineering blog, support, developer portal, CLI, documentation, pricing, and 39 more developer resources.'
plans:
- name: Amazon Quicksight Plans Pricing
  plan_count: 3
  slug: amazon-quicksight-plans-pricing
random_paper: 95
rate_limits:
- limit_count: 5
  name: Amazon Quicksight Rate Limits
  slug: amazon-quicksight-rate-limits
rules:
- name: Amazon QuickSight API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: amazon-quicksight-jsonschema-spectral-rules
- name: Amazon QuickSight API Rules
  rule_count: 25
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 16
  slug: amazon-quicksight-spectral-rules
score:
  band: strong
  composite: 61.2
  delta: 0.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 67.9
    developer_ergonomics: 63.0
    discoverability: 59.3
    governance: 68.8
    operational_transparency: 28.9
  previous_composite: 61.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-quicksight/refs/heads/main/screenshots/amazon-quicksight-2026-06-20T171805.png
security:
- kind: authentication
  name: Amazon Quicksight Authentication
  slug: amazon-quicksight-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Quicksight Domain Security
  slug: amazon-quicksight-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Quicksight Vulnerability Disclosure
  slug: amazon-quicksight-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: amazon-quicksight
tags:
- Analytics
- BI
- Business Intelligence
- Dashboards
- Machine Learning
- Reporting
- Visualization
website: https://quicksight.aws.amazon.com/
---
