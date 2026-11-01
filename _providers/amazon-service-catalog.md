---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 5
  human_in_the_loop: 1
  name: Amazon Service Catalog Agentic Access
  operation_count: 9
  slug: amazon-service-catalog-agentic-access
  summary_line: 9 operations · 5 acting · 1 human-in-the-loop
api_count: 12
apis:
- baseURL: https://servicecatalog.amazonaws.com
  baseurl_source: declared
  description: Portfolio management operations
  name: Amazon Service Catalog Portfolios API
  slug: amazon-service-catalog-portfolios-api
- baseURL: https://servicecatalog.amazonaws.com
  baseurl_source: declared
  description: Product management operations
  name: Amazon Service Catalog Products API
  slug: amazon-service-catalog-products-api
- baseURL: https://servicecatalog.amazonaws.com
  baseurl_source: declared
  description: Provisioned product management
  name: Amazon Service Catalog Provisioned Products API
  slug: amazon-service-catalog-provisioned-products-api
- baseURL: https://servicecatalog.amazonaws.com
  baseurl_source: declared
  description: The Service Catalog Budget API from Amazon Service Catalog — 3 operation(s) for service catalog budget.
  name: Amazon Service Catalog Service Catalog Budget API
  slug: amazon-service-catalog-budget-api
- baseURL: https://servicecatalog.amazonaws.com
  baseurl_source: declared
  description: The Service Catalog Constraint API from Amazon Service Catalog — 5 operation(s) for service catalog constraint.
  name: Amazon Service Catalog Service Catalog Constraint API
  slug: amazon-service-catalog-constraint-api
- baseURL: https://servicecatalog.amazonaws.com
  baseurl_source: declared
  description: The Service Catalog Operations API from Amazon Service Catalog — 29 operation(s) for service catalog operations.
  name: Amazon Service Catalog Service Catalog Operations API
  slug: amazon-service-catalog-operations-api
- baseURL: https://servicecatalog.amazonaws.com
  baseurl_source: declared
  description: The Service Catalog Portfolio Share API from Amazon Service Catalog — 6 operation(s) for service catalog portfolio share.
  name: Amazon Service Catalog Service Catalog Portfolio Share API
  slug: amazon-service-catalog-portfolio-share-api
- baseURL: https://servicecatalog.amazonaws.com
  baseurl_source: declared
  description: The Service Catalog Principal API from Amazon Service Catalog — 3 operation(s) for service catalog principal.
  name: Amazon Service Catalog Service Catalog Principal API
  slug: amazon-service-catalog-principal-api
- baseURL: https://servicecatalog.amazonaws.com
  baseurl_source: declared
  description: The Service Catalog Provisioned Product Plan API from Amazon Service Catalog — 5 operation(s) for service catalog provisioned product plan.
  name: Amazon Service Catalog Service Catalog Provisioned Product Plan API
  slug: amazon-service-catalog-provisioned-product-plan-api
- baseURL: https://servicecatalog.amazonaws.com
  baseurl_source: declared
  description: The Service Catalog Provisioning Artifact API from Amazon Service Catalog — 6 operation(s) for service catalog provisioning artifact.
  name: Amazon Service Catalog Service Catalog Provisioning Artifact API
  slug: amazon-service-catalog-provisioning-artifact-api
- baseURL: https://servicecatalog.amazonaws.com
  baseurl_source: declared
  description: The Service Catalog Service Action API from Amazon Service Catalog — 10 operation(s) for service catalog service action.
  name: Amazon Service Catalog Service Catalog Service Action API
  slug: amazon-service-catalog-service-action-api
- baseURL: https://servicecatalog.amazonaws.com
  baseurl_source: declared
  description: The Service Catalog Tag Option API from Amazon Service Catalog — 7 operation(s) for service catalog tag option.
  name: Amazon Service Catalog Service Catalog Tag Option API
  slug: amazon-service-catalog-tag-option-api
artifact_total: 40
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
  name: Amazon Service Catalog Portfolios API
  slug: open-amazon-service-catalog-portfolios-api
- collection_type: open
  name: Amazon Service Catalog Portfolios Products API
  slug: open-amazon-service-catalog-products-api
- collection_type: open
  name: Amazon Service Catalog Portfolios Provisioned Products API
  slug: open-amazon-service-catalog-provisioned-products-api
- collection_type: open
  name: Amazon Service Catalog API
  slug: open-amazon-service-catalog
common:
- group: commercial
  href: https://artifacts.apis.io/amazon-service-catalog/plans/amazon-service-catalog-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/amazon-service-catalog-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/amazon-service-catalog/rate-limits/amazon-service-catalog-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/amazon-service-catalog-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/amazon-service-catalog/finops/amazon-service-catalog-finops.yml
  title: ''
  type: FinOps
  url: finops/amazon-service-catalog-finops.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-service-catalog/overview
- group: agent
  href: https://artifacts.apis.io/amazon-service-catalog/agentic-access/amazon-service-catalog-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-service-catalog-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/amazon-service-catalog/security/amazon-service-catalog-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/amazon-service-catalog-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/amazon-service-catalog/security/amazon-service-catalog-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-service-catalog-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/amazon-service-catalog/security/amazon-service-catalog-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amazon-service-catalog-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/amazon-service-catalog/authentication/amazon-service-catalog-authentication.yml
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
  href: https://artifacts.apis.io/amazon-service-catalog/json-ld/amazon-service-catalog-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/amazon-service-catalog-context.jsonld
- group: docs
  href: https://artifacts.apis.io/amazon-service-catalog/json-schema/amazon-service-catalog-portfolio-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/amazon-service-catalog-portfolio-schema.json
- group: docs
  href: https://artifacts.apis.io/amazon-service-catalog/json-schema/amazon-service-catalog-product-view-summary-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/amazon-service-catalog-product-view-summary-schema.json
- group: docs
  href: https://artifacts.apis.io/amazon-service-catalog/json-schema/amazon-service-catalog-provisioned-product-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/amazon-service-catalog-provisioned-product-schema.json
- group: design
  href: https://artifacts.apis.io/amazon-service-catalog/json-structure/amazon-service-catalog-portfolio-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/amazon-service-catalog-portfolio-structure.json
- group: design
  href: https://artifacts.apis.io/amazon-service-catalog/json-structure/amazon-service-catalog-product-view-summary-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/amazon-service-catalog-product-view-summary-structure.json
- group: design
  href: https://artifacts.apis.io/amazon-service-catalog/json-structure/amazon-service-catalog-provisioned-product-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/amazon-service-catalog-provisioned-product-structure.json
- group: build
  href: https://artifacts.apis.io/amazon-service-catalog/examples/amazon-service-catalog-portfolio-example.json
  title: ''
  type: Examples
  url: examples/amazon-service-catalog-portfolio-example.json
- group: build
  href: https://artifacts.apis.io/amazon-service-catalog/examples/amazon-service-catalog-product-view-summary-example.json
  title: ''
  type: Examples
  url: examples/amazon-service-catalog-product-view-summary-example.json
- group: build
  href: https://artifacts.apis.io/amazon-service-catalog/examples/amazon-service-catalog-provisioned-product-example.json
  title: ''
  type: Examples
  url: examples/amazon-service-catalog-provisioned-product-example.json
- group: design
  href: https://artifacts.apis.io/amazon-service-catalog/rules/amazon-service-catalog-spectral-rules.yml
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
- has_sources: true
  method: derived
  name: Amazon Service Catalog Finops
  primary_unit: api call
  service_category: ''
  slug: amazon-service-catalog-finops
  template: false
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
overview: 'Amazon Service Catalog is listed with 12 APIs on the [APIs.io](https://apis.io/) network, including Portfolios API, Products API, Provisioned Products API, and 9 more. Tagged areas include Cloud Governance, Compliance, IT Governance, and Service Catalog.


  The Amazon Service Catalog catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Service Catalog''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 26 more developer resources.'
plans:
- name: Amazon Service Catalog Plans Pricing
  plan_count: 2
  slug: amazon-service-catalog-plans-pricing
- name: Amazon Service Catalog Price Estimates
  plan_count: 0
  slug: amazon-service-catalog-price-estimates
random_paper: 12
rate_limits:
- limit_count: 5
  name: Amazon Service Catalog Rate Limits
  slug: amazon-service-catalog-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Amazon Service Catalog — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-service-catalog-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 67
  extends:
  - spectral:oas
  name: Amazon Service Catalog API Rules
  rule_count: 26
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 15
  slug: amazon-service-catalog-spectral-rules
score:
  band: strong
  composite: 58.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 61.5
    catalog_earned_first_party: 8.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.1
  facets:
    access_clarity: 81.6
    contract_governance: 13.6
    contract_quality: 59.0
    developer_ergonomics: 58.3
    discoverability: 62.5
    operational_transparency: 39.5
  previous_composite: 58.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 76.9
      total: 13
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/amazon-service-catalog/amazon-service-catalog-2026-06-20T171823.png
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
