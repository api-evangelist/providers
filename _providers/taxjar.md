---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.0
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Taxjar Agentic Access
  operation_count: 22
  slug: taxjar-agentic-access
  summary_line: 22 operations · 11 acting
api_count: 1
apis:
- baseURL: https://api.taxjar.com/v2/
  baseurl_source: declared
  description: Product tax categories
  name: TaxJar Categories API
  slug: taxjar-categories-api
- baseURL: https://api.taxjar.com/v2/
  baseurl_source: declared
  description: Customer exemption management
  name: TaxJar Customers API
  slug: taxjar-customers-api
- baseURL: https://api.taxjar.com/v2/
  baseurl_source: declared
  description: Nexus region tracking
  name: TaxJar Nexus API
  slug: taxjar-nexus-api
- baseURL: https://api.taxjar.com/v2/
  baseurl_source: declared
  description: Sales tax rate lookups
  name: TaxJar Rates API
  slug: taxjar-rates-api
- baseURL: https://api.taxjar.com/v2/
  baseurl_source: declared
  description: Summarized sales tax rates by region
  name: TaxJar Summary Rates API
  slug: taxjar-summary-rates-api
- baseURL: https://api.taxjar.com/v2/
  baseurl_source: declared
  description: Sales tax calculation
  name: TaxJar Taxes API
  slug: taxjar-taxes-api
- baseURL: https://api.taxjar.com/v2/
  baseurl_source: declared
  description: Order transaction management
  name: TaxJar Transactions - Orders API
  slug: taxjar-transactions-orders-api
- baseURL: https://api.taxjar.com/v2/
  baseurl_source: declared
  description: Refund transaction management
  name: TaxJar Transactions - Refunds API
  slug: taxjar-transactions-refunds-api
- baseURL: https://api.taxjar.com/v2/
  baseurl_source: declared
  description: Address and VAT validation
  name: TaxJar Validations API
  slug: taxjar-validations-api
artifact_total: 42
collections:
- collection_type: postman
  name: TaxJar Sales Tax Categories API
  slug: postman-taxjar-categories-api
- collection_type: postman
  name: TaxJar Sales Tax Categories Customers API
  slug: postman-taxjar-customers-api
- collection_type: postman
  name: TaxJar Sales Tax Categories Nexus API
  slug: postman-taxjar-nexus-api
- collection_type: postman
  name: TaxJar Sales Tax Categories Rates API
  slug: postman-taxjar-rates-api
- collection_type: postman
  name: TaxJar Sales Tax Categories Summary Rates API
  slug: postman-taxjar-summary-rates-api
- collection_type: postman
  name: TaxJar Sales Tax Categories Taxes API
  slug: postman-taxjar-taxes-api
- collection_type: postman
  name: TaxJar Sales Tax Categories Transactions - Orders API
  slug: postman-taxjar-transactions-orders-api
- collection_type: postman
  name: TaxJar Sales Tax Categories Transactions - Refunds API
  slug: postman-taxjar-transactions-refunds-api
- collection_type: postman
  name: TaxJar Sales Tax Categories Validations API
  slug: postman-taxjar-validations-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TaxJar Sales Tax Categories API
  slug: open-taxjar-categories-api
- collection_type: open
  name: TaxJar Sales Tax Categories Customers API
  slug: open-taxjar-customers-api
- collection_type: open
  name: TaxJar Sales Tax Categories Nexus API
  slug: open-taxjar-nexus-api
- collection_type: open
  name: TaxJar Sales Tax Categories Rates API
  slug: open-taxjar-rates-api
- collection_type: open
  name: TaxJar Sales Tax Categories Summary Rates API
  slug: open-taxjar-summary-rates-api
- collection_type: open
  name: TaxJar Sales Tax Categories Taxes API
  slug: open-taxjar-taxes-api
- collection_type: open
  name: TaxJar Sales Tax Categories Transactions - Orders API
  slug: open-taxjar-transactions-orders-api
- collection_type: open
  name: TaxJar Sales Tax Categories Transactions - Refunds API
  slug: open-taxjar-transactions-refunds-api
- collection_type: open
  name: TaxJar Sales Tax Categories Validations API
  slug: open-taxjar-validations-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/taxjar/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/taxjar-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/taxjar-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/taxjar-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/taxjar-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.taxjar.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.taxjar.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.taxjar.com/api/reference/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/taxjar
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/taxjar
- group: company
  title: ''
  type: Blog
  url: https://developers.taxjar.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.taxjar.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.taxjar.com
- group: other
  title: ''
  type: X
  url: https://x.com/taxjardev
- group: operate
  title: ''
  type: Support
  url: https://support.taxjar.com/category/233-taxjar-api
- group: start
  title: ''
  type: Signup
  url: https://app.taxjar.com/api_sign_up/
- group: commercial
  title: ''
  type: Plans
  url: plans/taxjar-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/taxjar-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/taxjar-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/taxjar-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/taxjar-context.jsonld
- group: company
  title: ''
  type: BlogFeed
  url: blogs/blogs.json
created: '2026-06-12'
description: TaxJar is a sales tax automation platform, now a Stripe company, providing APIs for real-time sales tax calculations, rooftop-level rate lookups, transaction recording, and automated filing across US states and international jurisdictions. The platform supports e-commerce businesses of all sizes with sub-20ms response times, 99.999% historical uptime, and AI-powered product tax classification. TaxJar handles nexus tracking, exemption certificate management, and AutoFile returns so merchants can stay compliant without manual effort. Official client libraries are available for Ruby, Python, PHP, Node.js, C#/.NET, Java, and Go.
examples:
- key_count: 13
  name: Calculate Tax Request
  slug: calculate-tax-request
- key_count: 1
  name: Calculate Tax Response
  slug: calculate-tax-response
- key_count: 17
  name: Create Order Request
  slug: create-order-request
finops:
- name: Taxjar Finops
  service_category: ''
  slug: taxjar-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/taxjar.png
json_schemas:
- name: TaxJar Order Transaction
  property_count: 20
  slug: taxjar-order
- name: TaxJar Tax Calculation Response
  property_count: 1
  slug: taxjar-tax-calculation
jsonld:
- class_count: 9
  name: Taxjar Context
  property_count: 53
  slug: taxjar-context
layout: provider
modified: '2026-06-12'
name: TaxJar
nav: Providers
network: true
overview: 'TaxJar publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Categories API, Customers API, Nexus API, and 6 more. Tagged areas include Sales Tax, Tax Compliance, E-Commerce, Tax Calculation, and Tax Automation.


  The TaxJar catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  TaxJar''s developer surface includes authentication, documentation, API reference, engineering blog, pricing, support, signup flow, and 15 more developer resources.'
plans:
- name: Taxjar Plans Pricing
  plan_count: 2
  slug: taxjar-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Taxjar Rate Limits
  slug: taxjar-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: TaxJar API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: taxjar-jsonschema-spectral-rules
score:
  band: developing
  composite: 53.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 85.3
    catalog_earned_first_party: 0.0
    catalog_gap: 29.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 25.0
    contract_quality: 74.6
    developer_ergonomics: 36.9
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 39.5
  previous_composite: 53.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/taxjar/refs/heads/main/screenshots/taxjar-2026-06-20T194935.png
security:
- kind: authentication
  name: Taxjar Authentication
  slug: taxjar-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Taxjar Domain Security
  slug: taxjar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Taxjar Trust Center
  slug: taxjar-trust-center
  summary_line: SOC 2, GDPR
slug: taxjar
tags:
- Sales Tax
- Tax Compliance
- E-Commerce
- Tax Calculation
- Tax Automation
- Stripe
- Fintech
website: https://www.taxjar.com
---
