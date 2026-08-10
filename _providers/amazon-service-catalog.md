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
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 5
  human_in_the_loop: 1
  name: Amazon Service Catalog Agentic Access
  operation_count: 9
  slug: amazon-service-catalog-agentic-access
  summary_line: 9 operations · 5 acting · 1 human-in-the-loop
api_count: 3
apis:
- description: Portfolio management operations
  name: Amazon Service Catalog Portfolios API
  slug: amazon-service-catalog-portfolios-api
- description: Product management operations
  name: Amazon Service Catalog Products API
  slug: amazon-service-catalog-products-api
- description: Provisioned product management
  name: Amazon Service Catalog Provisioned Products API
  slug: amazon-service-catalog-provisioned-products-api
artifact_total: 27
collections:
- collection_type: postman
  name: Amazon Service Catalog Portfolios API
  slug: postman-amazon-service-catalog-portfolios-api
- collection_type: postman
  name: Amazon Service Catalog Portfolios Products API
  slug: postman-amazon-service-catalog-products-api
- collection_type: postman
  name: Amazon Service Catalog Portfolios Provisioned Products API
  slug: postman-amazon-service-catalog-provisioned-products-api
- collection_type: open
  name: Amazon Service Catalog API
  slug: open-amazon-service-catalog
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-service-catalog/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-service-catalog-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-service-catalog-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-service-catalog-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-service-catalog-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-service-catalog-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/servicecatalog/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/servicecatalog/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/servicecatalog/
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
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/mt/tag/aws-service-catalog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/servicecatalog/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: start
  title: ''
  type: Login
  url: https://signin.aws.amazon.com/
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
  type: JSONLD
  url: json-ld/amazon-service-catalog-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-service-catalog-portfolio-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-service-catalog-product-view-summary-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-service-catalog-provisioned-product-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-service-catalog-portfolio-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-service-catalog-product-view-summary-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-service-catalog-provisioned-product-structure.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-service-catalog-portfolio-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-service-catalog-product-view-summary-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-service-catalog-provisioned-product-example.json
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-service-catalog-spectral-rules.yml
created: '2026-03-16'
description: AWS Service Catalog enables organizations to create and manage catalogs of IT services that are approved for use on AWS. IT administrators can create and manage a portfolio of products (services, applications, and others) and control which users have access to which products.
examples:
- key_count: 6
  name: Amazon Service Catalog Portfolio Example
  slug: amazon-service-catalog-portfolio-example
- key_count: 6
  name: Amazon Service Catalog Product View Summary Example
  slug: amazon-service-catalog-product-view-summary-example
- key_count: 1
  name: Amazon Service Catalog Provisioned Product Example
  slug: amazon-service-catalog-provisioned-product-example
finops:
- name: Amazon Service Catalog Finops
  service_category: API
  slug: amazon-service-catalog-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-service-catalog.png
json_schemas:
- name: Portfolio
  property_count: 6
  slug: amazon-service-catalog-portfolio
- name: ProductViewSummary
  property_count: 6
  slug: amazon-service-catalog-product-view-summary
- name: ProvisionedProduct
  property_count: 1
  slug: amazon-service-catalog-provisioned-product
json_structures:
- name: Amazon Service Catalog Portfolio Structure
  property_count: 6
  slug: amazon-service-catalog-portfolio-structure
- name: Amazon Service Catalog Product View Summary Structure
  property_count: 6
  slug: amazon-service-catalog-product-view-summary-structure
- name: Amazon Service Catalog Provisioned Product Structure
  property_count: 1
  slug: amazon-service-catalog-provisioned-product-structure
jsonld:
- class_count: 3
  name: Amazon Service Catalog Context
  property_count: 12
  slug: amazon-service-catalog-context
layout: provider
modified: '2026-05-19'
name: Amazon Service Catalog
nav: Providers
network: true
overview: 'Amazon Service Catalog publishes 3 APIs on the [APIs.io](https://apis.io/) network: Portfolios API, Products API, and Provisioned Products API. Tagged areas include Cloud Governance, Compliance, IT Governance, and Service Catalog.


  The Amazon Service Catalog catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Service Catalog''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 23 more developer resources.'
plans:
- name: Amazon Service Catalog Plans Pricing
  plan_count: 3
  slug: amazon-service-catalog-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Amazon Service Catalog Rate Limits
  slug: amazon-service-catalog-rate-limits
rules:
- name: Amazon Service Catalog API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-service-catalog-jsonschema-spectral-rules
- name: Amazon Service Catalog API Rules
  rule_count: 26
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 15
  slug: amazon-service-catalog-spectral-rules
score:
  band: developing
  composite: 51.3
  delta: 0.0
  facets:
    commercial_clarity: 81.6
    contract_quality: 22.3
    developer_ergonomics: 45.7
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 51.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-service-catalog/refs/heads/main/screenshots/amazon-service-catalog-2026-06-20T171823.png
security:
- kind: authentication
  name: Amazon Service Catalog Authentication
  slug: amazon-service-catalog-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Service Catalog Domain Security
  slug: amazon-service-catalog-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Service Catalog Vulnerability Disclosure
  slug: amazon-service-catalog-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Service Catalog Trust Center
  slug: amazon-service-catalog-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-service-catalog
tags:
- Cloud Governance
- Compliance
- IT Governance
- Service Catalog
website: https://aws.amazon.com/servicecatalog/
---
