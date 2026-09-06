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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Bloom Credit Agentic Access
  operation_count: 6
  slug: bloom-credit-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 5
apis:
- baseURL: https://api.bloomcredit.io/v1
  baseurl_source: spec
  description: Consumer identity and registration
  name: Bloom Credit Consumers API
  slug: bloom-credit-consumers-api
- baseURL: https://api.bloomcredit.io/v1
  baseurl_source: spec
  description: Full credit bureau report retrieval
  name: Bloom Credit Credit Reports API
  slug: bloom-credit-credit-reports-api
- baseURL: https://api.bloomcredit.io/v1
  baseurl_source: spec
  description: Credit score retrieval
  name: Bloom Credit Credit Scores API
  slug: bloom-credit-credit-scores-api
- baseURL: https://api.bloomcredit.io/v1
  baseurl_source: spec
  description: Credit monitoring and alerts
  name: Bloom Credit Monitoring API
  slug: bloom-credit-monitoring-api
- baseURL: https://api.bloomcredit.io/v1
  baseurl_source: spec
  description: Individual account and trade line data
  name: Bloom Credit Trade Lines API
  slug: bloom-credit-trade-lines-api
artifact_total: 53
collections:
- collection_type: postman
  name: Bloom Credit Consumers API
  slug: postman-bloom-credit-consumers-api
- collection_type: postman
  name: Bloom Credit Consumers Credit Reports API
  slug: postman-bloom-credit-credit-reports-api
- collection_type: postman
  name: Bloom Credit Consumers Credit Scores API
  slug: postman-bloom-credit-credit-scores-api
- collection_type: postman
  name: Bloom Credit Consumers Monitoring API
  slug: postman-bloom-credit-monitoring-api
- collection_type: postman
  name: Bloom Credit Consumers Trade Lines API
  slug: postman-bloom-credit-trade-lines-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bloom Credit Consumers API
  slug: open-bloom-credit-consumers-api
- collection_type: open
  name: Bloom Credit Consumers Credit Reports API
  slug: open-bloom-credit-credit-reports-api
- collection_type: open
  name: Bloom Credit Consumers Credit Scores API
  slug: open-bloom-credit-credit-scores-api
- collection_type: open
  name: Bloom Credit Consumers Monitoring API
  slug: open-bloom-credit-monitoring-api
- collection_type: open
  name: Bloom Credit Consumers Trade Lines API
  slug: open-bloom-credit-trade-lines-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/bloom-credit/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bloom-credit-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloom-credit-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bloom-credit-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bloomcredit
- group: company
  title: ''
  type: Website
  url: https://bloomcredit.io/
- group: docs
  title: ''
  type: Documentation
  url: https://bloomcredit.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://bloomcredit.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bloomcredit
- group: build
  title: Python SDK
  type: SDKs
  url: https://github.com/bloomcredit/bloomPy
- group: build
  title: TypeScript SDK
  type: SDKs
  url: https://github.com/bloomcredit/bloomTypescript
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bloomcredit.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bloomcredit.io/privacy
- group: design
  title: ''
  type: SpectralRules
  url: rules/bloom-credit-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/bloom-credit-vocabulary.yaml
- group: agent
  title: ''
  type: LlmsText
  url: https://bloomcredit.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://bloomcredit.io/feed/
created: '2025-02-24'
description: Bloom Credit is a fintech infrastructure company providing API access to consumer credit data from all three major credit bureaus (Equifax, Experian, TransUnion). The platform enables fintechs, lenders, and financial services applications to retrieve credit reports, credit scores, trade line data, and enroll consumers in real-time credit monitoring. Bloom Credit provides multi-language SDKs (Python, Ruby, TypeScript, R, Go) and supports the Metro 2 credit reporting format.
examples:
- key_count: 8
  name: Bloom Credit Consumer Example
  slug: bloom-credit-consumer-example
- key_count: 2
  name: Bloom Credit Credit Score Example
  slug: bloom-credit-credit-score-example
- key_count: 8
  name: Bloom Credit Monitoring Enrollment Example
  slug: bloom-credit-monitoring-enrollment-example
- key_count: 2
  name: Bloom Credit Trade Line Example
  slug: bloom-credit-trade-line-example
features:
- description: Pull full credit reports from Equifax, Experian, and TransUnion in a single API call with structured trade line, inquiry, and public record data.
  name: Tri-Bureau Credit Reports
- description: Access FICO 8, VantageScore 3.0, and other scoring models from all three major credit bureaus for comprehensive creditworthiness assessment.
  name: Credit Score Retrieval
- description: Retrieve individual account and trade line records including payment history, balances, credit limits, and account status across bureaus.
  name: Trade Line Data
- description: Enroll consumers in monitoring subscriptions that trigger webhook alerts for new accounts, inquiries, derogatory marks, and score changes.
  name: Real-Time Credit Monitoring
- description: Built-in consumer registration and consent workflow ensuring FCRA-compliant access to credit bureau data with auditable consent records.
  name: Consumer Consent Management
- description: Official SDKs for Python, TypeScript, Ruby, R, and Go enabling rapid integration into existing fintech and data science workflows.
  name: Multi-Language SDKs
finops:
- name: Bloom Credit Finops
  service_category: API
  slug: bloom-credit-finops
graphqls:
- description: This conceptual GraphQL schema models the Bloom Credit API, which provides fintech infrastructure for accessing consumer credit data from all three major credit bureaus — Equifax, Experian, and TransU
  name: Bloom Credit GraphQL Schema
  slug: bloom-credit-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloom-credit.png
integrations:
- description: Direct integration with Equifax for credit report and score data including FICO 8 and other proprietary scoring models.
  name: Equifax
- description: Direct integration with Experian for credit reports, FICO scores, and VantageScore data with real-time data freshness.
  name: Experian
- description: Direct integration with TransUnion for credit reports and scores with support for TransUnion-specific data attributes.
  name: TransUnion
- description: Complementary integration where Bloom Credit's credit data can be combined with Plaid's bank account and income verification for full financial profiles.
  name: Plaid
json_schemas:
- name: Consumer
  property_count: 6
  slug: bloom-credit-consumer
- name: CreditScore
  property_count: 6
  slug: bloom-credit-credit-score
- name: MonitoringEnrollment
  property_count: 5
  slug: bloom-credit-monitoring-enrollment
- name: TradeLine
  property_count: 10
  slug: bloom-credit-trade-line
json_structures:
- name: Bloom Credit Consumer Structure
  property_count: 0
  slug: bloom-credit-consumer-structure
- name: Bloom Credit Credit Score Structure
  property_count: 0
  slug: bloom-credit-credit-score-structure
- name: Bloom Credit Monitoring Enrollment Structure
  property_count: 0
  slug: bloom-credit-monitoring-enrollment-structure
- name: Bloom Credit Trade Line Structure
  property_count: 0
  slug: bloom-credit-trade-line-structure
jsonld:
- class_count: 48
  name: Bloom Credit Context
  property_count: 0
  slug: bloom-credit-context
layout: provider
modified: '2026-05-19'
name: Bloom Credit
nav: Providers
network: true
overview: 'Bloom Credit publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Consumers API, Credit Reports API, Credit Scores API, and 2 more. Tagged areas include Credit Bureau, Credit Reports, Credit Scores, Fintech, and Lending.


  The Bloom Credit catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Bloom Credit''s developer surface includes authentication, documentation, getting-started guide, engineering blog, and 13 more developer resources.'
plans:
- name: Bloom Credit Plans Pricing
  plan_count: 3
  slug: bloom-credit-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Bloom Credit Rate Limits
  slug: bloom-credit-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Bloom Credit API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: bloom-credit-jsonschema-spectral-rules
- effective_rule_count: 78
  extends:
  - spectral:oas
  name: Bloom Credit API Rules
  rule_count: 37
  severity_counts:
    error: 11
    hint: 0
    info: 5
    warn: 21
  slug: bloom-credit-spectral-rules
score:
  band: thin
  composite: 32.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 61.5
    catalog_earned_first_party: 0.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 28.8
    contract_quality: 26.5
    developer_ergonomics: 44.0
    discoverability: 72.2
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 32.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloom-credit/refs/heads/main/screenshots/bloom-credit-2026-06-20T173402.png
security:
- kind: authentication
  name: Bloom Credit Authentication
  slug: bloom-credit-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bloom Credit Domain Security
  slug: bloom-credit-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bloom-credit
tags:
- Credit Bureau
- Credit Reports
- Credit Scores
- Fintech
- Lending
- Personal Finance
use_cases:
- description: Lenders pull tri-bureau credit reports and scores during loan origination to assess creditworthiness and determine loan terms.
  name: Loan Underwriting
- description: Consumer fintech applications provide users with free credit score monitoring and personalized recommendations to improve their credit profiles.
  name: Credit Building Apps
- description: Property management platforms use Bloom Credit to run credit checks during rental application processing.
  name: Tenant Screening
- description: Financial advisors and credit counselors access full credit reports and trade line data to create personalized debt management plans.
  name: Credit Counseling
- description: Financial institutions use credit data during account opening to verify identity and assess risk for credit card and deposit products.
  name: Account Origination
website: https://bloomcredit.io/
---
