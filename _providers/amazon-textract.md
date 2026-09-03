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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
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
  score: 17.3
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Amazon Textract Agentic Access
  operation_count: 6
  slug: amazon-textract-agentic-access
  summary_line: 6 operations · 6 acting
api_count: 1
apis:
- baseURL: https://textract.amazonaws.com
  baseurl_source: declared
  description: Operations for asynchronous document processing.
  name: Amazon Textract Async Operations API
  slug: amazon-textract-async-operations-api
- baseURL: https://textract.amazonaws.com
  baseurl_source: declared
  description: Operations for analyzing document structure and content.
  name: Amazon Textract Document Analysis API
  slug: amazon-textract-document-analysis-api
- baseURL: https://textract.amazonaws.com
  baseurl_source: declared
  description: Operations for analyzing expense documents.
  name: Amazon Textract Expense Analysis API
  slug: amazon-textract-expense-analysis-api
- baseURL: https://textract.amazonaws.com
  baseurl_source: declared
  description: Operations for analyzing identity documents.
  name: Amazon Textract ID Analysis API
  slug: amazon-textract-id-analysis-api
- baseURL: https://textract.amazonaws.com
  baseurl_source: declared
  description: Operations for detecting text in documents.
  name: Amazon Textract Text Detection API
  slug: amazon-textract-text-detection-api
artifact_total: 35
collections:
- collection_type: postman
  name: Amazon Textract Async Operations API
  slug: postman-amazon-textract-async-operations-api
- collection_type: postman
  name: Amazon Textract Async Operations Document Analysis API
  slug: postman-amazon-textract-document-analysis-api
- collection_type: postman
  name: Amazon Textract Async Operations Expense Analysis API
  slug: postman-amazon-textract-expense-analysis-api
- collection_type: postman
  name: Amazon Textract Async Operations ID Analysis API
  slug: postman-amazon-textract-id-analysis-api
- collection_type: postman
  name: Amazon Textract Async Operations Text Detection API
  slug: postman-amazon-textract-text-detection-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Textract Async Operations API
  slug: open-amazon-textract-async-operations-api
- collection_type: open
  name: Amazon Textract Async Operations Document Analysis API
  slug: open-amazon-textract-document-analysis-api
- collection_type: open
  name: Amazon Textract Async Operations Expense Analysis API
  slug: open-amazon-textract-expense-analysis-api
- collection_type: open
  name: Amazon Textract Async Operations ID Analysis API
  slug: open-amazon-textract-id-analysis-api
- collection_type: open
  name: Amazon Textract Async Operations Text Detection API
  slug: open-amazon-textract-text-detection-api
- collection_type: open
  name: Amazon Textract
  slug: open-amazon-textract
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-textract/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-textract-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-textract-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-textract-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-textract-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/textract/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/textract/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/textract/
- group: start
  title: ''
  type: Signup
  url: https://signin.aws.amazon.com/signup?request_type=register
- group: start
  title: ''
  type: Login
  url: https://aws.amazon.com/console/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/amazon-textract/refs/heads/main/rules/amazon-textract-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/amazon-textract/refs/heads/main/vocabulary/amazon-textract-vocabulary.yaml
created: '2024-01-15'
description: Amazon Textract is a machine learning service that automatically extracts text, handwriting, and structured data from scanned documents. It goes beyond simple optical character recognition (OCR) to identify and extract data from forms and tables, enabling automated document processing workflows without manual review or custom code.
examples:
- key_count: 2
  name: Amazon Textract Example
  slug: amazon-textract-example
features:
- description: Automate operational tasks with Amazon Textract.
  name: Automation
- description: Programmatic access to Amazon Textract resources.
  name: API Access
finops:
- name: Amazon Textract Finops
  service_category: API
  slug: amazon-textract-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: DocumentAnalysis
  property_count: 3
  slug: amazon-textract-document-analysis
- name: DocumentAnalysis
  property_count: 3
  slug: amazon-textract-documentanalysis
json_structures:
- name: Amazon Textract Document Analysis Structure
  property_count: 0
  slug: amazon-textract-document-analysis-structure
- name: Amazon Textract Documentanalysis Structure
  property_count: 0
  slug: amazon-textract-documentanalysis-structure
jsonld:
- class_count: 0
  name: Amazon Textract Context
  property_count: 8
  slug: amazon-textract-context
layout: provider
modified: '2026-05-19'
name: Amazon Textract
nav: Providers
network: true
overview: 'Amazon Textract publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Async Operations API, Document Analysis API, Expense Analysis API, and 2 more. Tagged areas include Document Processing, Machine-Learning, and OCR.


  The Amazon Textract catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Textract''s developer surface includes developer portal, documentation, support, developer console, signup flow, and 14 more developer resources.'
plans:
- name: Amazon Textract Plans Pricing
  plan_count: 3
  slug: amazon-textract-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Amazon Textract Rate Limits
  slug: amazon-textract-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon Textract API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-textract-jsonschema-spectral-rules
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: Amazon Textract API Rules
  rule_count: 12
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 8
  slug: amazon-textract-spectral-rules
score:
  band: developing
  composite: 45.1
  coverage:
    artifact_dirs: 16
    catalog_gap: 59.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 61.8
    commercial_clarity: 61.8
    contract_governance: 28.8
    contract_quality: 48.3
    developer_ergonomics: 35.7
    discoverability: 66.7
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 45.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-textract/refs/heads/main/screenshots/amazon-textract-2026-06-20T171833.png
security:
- kind: domain-security
  name: Amazon Textract Domain Security
  slug: amazon-textract-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Textract Vulnerability Disclosure
  slug: amazon-textract-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Textract Trust Center
  slug: amazon-textract-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-textract
tags:
- Document Processing
- Machine-Learning
- OCR
use_cases:
- description: Use Amazon Textract to manage and automate cloud operations.
  name: Cloud Operations
website: https://aws.amazon.com/textract/
---
