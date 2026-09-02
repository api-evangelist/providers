---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.1
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Amazon Billing And Cost Management Agentic Access
  operation_count: 24
  slug: amazon-billing-and-cost-management-agentic-access
  summary_line: 24 operations · 24 acting
api_count: 2
apis:
- description: The AWS Price List API allows programmatic querying of AWS service pricing information in JSON or CSV format. Retrieve price lists for all AWS services, filter by region and attributes, and stay curre
  name: AWS Price List API
  slug: aws-price-list-api
- description: Detect and manage cost anomalies
  name: Amazon Billing And Cost Management Anomaly Detection API
  slug: amazon-billing-and-cost-management-anomaly-detection-api
- description: Automated actions when budget thresholds are exceeded
  name: Amazon Billing And Cost Management Budget Actions API
  slug: amazon-billing-and-cost-management-budget-actions-api
- description: Create and manage cost budgets
  name: Amazon Billing And Cost Management Budgets API
  slug: amazon-billing-and-cost-management-budgets-api
- description: Query cost and usage data
  name: Amazon Billing And Cost Management Cost And Usage API
  slug: amazon-billing-and-cost-management-cost-and-usage-api
- description: Organize costs with custom categories
  name: Amazon Billing And Cost Management Cost Categories API
  slug: amazon-billing-and-cost-management-cost-categories-api
- description: Generate cost and usage forecasts
  name: Amazon Billing And Cost Management Forecasting API
  slug: amazon-billing-and-cost-management-forecasting-api
- description: Manage budget alert notifications
  name: Amazon Billing And Cost Management Notifications API
  slug: amazon-billing-and-cost-management-notifications-api
- description: Cost optimization recommendations
  name: Amazon Billing And Cost Management Recommendations API
  slug: amazon-billing-and-cost-management-recommendations-api
- description: Manage cost allocation tags
  name: Amazon Billing And Cost Management Tags API
  slug: amazon-billing-and-cost-management-tags-api
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AWS Budgets Anomaly Detection API
  slug: open-amazon-billing-and-cost-management-anomaly-detection-api
- collection_type: open
  name: AWS Budgets Anomaly Detection Budget Actions API
  slug: open-amazon-billing-and-cost-management-budget-actions-api
- collection_type: open
  name: AWS Anomaly Detection Budgets API
  slug: open-amazon-billing-and-cost-management-budgets-api
- collection_type: open
  name: AWS Budgets Anomaly Detection Cost And Usage API
  slug: open-amazon-billing-and-cost-management-cost-and-usage-api
- collection_type: open
  name: AWS Budgets Anomaly Detection Cost Categories API
  slug: open-amazon-billing-and-cost-management-cost-categories-api
- collection_type: open
  name: AWS Budgets Anomaly Detection Forecasting API
  slug: open-amazon-billing-and-cost-management-forecasting-api
- collection_type: open
  name: AWS Budgets Anomaly Detection Notifications API
  slug: open-amazon-billing-and-cost-management-notifications-api
- collection_type: open
  name: AWS Budgets Anomaly Detection Recommendations API
  slug: open-amazon-billing-and-cost-management-recommendations-api
- collection_type: open
  name: AWS Budgets Anomaly Detection Tags API
  slug: open-amazon-billing-and-cost-management-tags-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/amazon-billing-and-cost-management-aws-budgets-api-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-billing-and-cost-management-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-billing-and-cost-management-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-billing-and-cost-management-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-billing-and-cost-management-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-billing-and-cost-management-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/aws-cost-management/
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/cost-management/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/cost-management/latest/userguide/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/aws-cost-management/pricing/
- group: operate
  title: ''
  type: FAQ
  url: https://aws.amazon.com/aws-cost-management/faqs/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/aws-cloud-financial-management/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: build
  title: ''
  type: Packages
  url: packages/amazon-billing-and-cost-management-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amazon-billing-and-cost-management-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/amazon-billing-and-cost-management-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/amazon-billing-and-cost-management-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amazon-billing-and-cost-management-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/amazon-billing-and-cost-management-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/amazon-billing-and-cost-management-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amazon-billing-and-cost-management-lifecycle.yml
created: '2026-03-16'
description: AWS Billing and Cost Management is a suite of tools and APIs that enables organizations to view, analyze, forecast, budget, and optimize their AWS spending. It includes AWS Cost Explorer for cost analysis, AWS Budgets for budget tracking and alerts, Cost Anomaly Detection for ML-powered anomaly identification, Cost Categories for spend organization, and the AWS Price List API for programmatic pricing queries. The suite supports consolidated billing across AWS Organizations and chargeback/showback workflows.
examples:
- key_count: 2
  name: Create Anomaly Monitor Example
  slug: create-anomaly-monitor-example
- key_count: 2
  name: Create Budget Example
  slug: create-budget-example
- key_count: 2
  name: Get Cost And Usage Example
  slug: get-cost-and-usage-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-billing-and-cost-management.png
json_schemas:
- name: AWS Budget
  property_count: 8
  slug: cost-budget
json_structures:
- name: Billing Resource Structure
  property_count: 0
  slug: billing-resource-structure
jsonld:
- class_count: 19
  name: context Context
  property_count: 2
  slug: context
layout: provider
mcp_servers:
- description: ''
  name: Amazon Billing And Cost Management MCP Server
  slug: amazon-billing-and-cost-management-mcp-server
modified: '2026-06-20'
name: Amazon Billing And Cost Management
nav: Providers
network: true
overview: 'Amazon Billing And Cost Management publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Anomaly Detection API, Budget Actions API, Budgets API, and 6 more. Tagged areas include Billing, Cost Management, Cost Explorer, Budgets, and Cost Optimization.


  The Amazon Billing And Cost Management catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Amazon Billing And Cost Management''s developer surface includes authentication, developer portal, developer console, documentation, pricing, FAQ, engineering blog, and 18 more developer resources.'
random_paper: 4
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon Billing And Cost Management API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-billing-and-cost-management-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.5
  coverage:
    artifact_dirs: 22
    catalog_gap: 61.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 29.5
    contract_quality: 62.6
    developer_ergonomics: 47.6
    discoverability: 75.9
    governance: 29.5
    operational_transparency: 2.6
  previous_composite: 44.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-billing-and-cost-management/refs/heads/main/screenshots/amazon-billing-and-cost-management-2026-07-25T195936.png
security:
- kind: authentication
  name: Amazon Billing And Cost Management Authentication
  slug: amazon-billing-and-cost-management-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Billing And Cost Management Domain Security
  slug: amazon-billing-and-cost-management-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Billing And Cost Management Vulnerability Disclosure
  slug: amazon-billing-and-cost-management-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Billing And Cost Management Trust Center
  slug: amazon-billing-and-cost-management-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-billing-and-cost-management
tags:
- Billing
- Cost Management
- Cost Explorer
- Budgets
- Cost Optimization
- FinOps
- Amazon Web Services
website: https://aws.amazon.com/aws-cost-management/
---
