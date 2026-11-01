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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Amazon Personalize Agentic Access
  operation_count: 1
  slug: amazon-personalize-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://personalize.amazonaws.com
  baseurl_source: declared
  description: Operations for managing datasets and dataset groups
  name: Amazon Personalize Datasets API
  slug: amazon-personalize-datasets-api
- baseURL: https://personalize.amazonaws.com
  baseurl_source: declared
  description: The Personalize Batch Inference Job API from Amazon Personalize — 3 operation(s) for personalize batch inference job.
  name: Amazon Personalize Personalize Batch Inference Job API
  slug: amazon-personalize-batch-inference-job-api
- baseURL: https://personalize.amazonaws.com
  baseurl_source: declared
  description: The Personalize Batch Segment Job API from Amazon Personalize — 3 operation(s) for personalize batch segment job.
  name: Amazon Personalize Personalize Batch Segment Job API
  slug: amazon-personalize-batch-segment-job-api
- baseURL: https://personalize.amazonaws.com
  baseurl_source: declared
  description: The Personalize Campaign API from Amazon Personalize — 5 operation(s) for personalize campaign.
  name: Amazon Personalize Personalize Campaign API
  slug: amazon-personalize-campaign-api
- baseURL: https://personalize.amazonaws.com
  baseurl_source: declared
  description: The Personalize Data Deletion Job API from Amazon Personalize — 3 operation(s) for personalize data deletion job.
  name: Amazon Personalize Personalize Data Deletion Job API
  slug: amazon-personalize-data-deletion-job-api
- baseURL: https://personalize.amazonaws.com
  baseurl_source: declared
  description: The Personalize Dataset Export Job API from Amazon Personalize — 3 operation(s) for personalize dataset export job.
  name: Amazon Personalize Personalize Dataset Export Job API
  slug: amazon-personalize-dataset-export-job-api
- baseURL: https://personalize.amazonaws.com
  baseurl_source: declared
  description: The Personalize Dataset Group API from Amazon Personalize — 4 operation(s) for personalize dataset group.
  name: Amazon Personalize Personalize Dataset Group API
  slug: amazon-personalize-dataset-group-api
- baseURL: https://personalize.amazonaws.com
  baseurl_source: declared
  description: The Personalize Dataset Import Job API from Amazon Personalize — 3 operation(s) for personalize dataset import job.
  name: Amazon Personalize Personalize Dataset Import Job API
  slug: amazon-personalize-dataset-import-job-api
- baseURL: https://personalize.amazonaws.com
  baseurl_source: declared
  description: The Personalize Event Tracker API from Amazon Personalize — 4 operation(s) for personalize event tracker.
  name: Amazon Personalize Personalize Event Tracker API
  slug: amazon-personalize-event-tracker-api
- baseURL: https://personalize.amazonaws.com
  baseurl_source: declared
  description: The Personalize Filter API from Amazon Personalize — 4 operation(s) for personalize filter.
  name: Amazon Personalize Personalize Filter API
  slug: amazon-personalize-filter-api
- baseURL: https://personalize.amazonaws.com
  baseurl_source: declared
  description: The Personalize Metric Attribution API from Amazon Personalize — 5 operation(s) for personalize metric attribution.
  name: Amazon Personalize Personalize Metric Attribution API
  slug: amazon-personalize-metric-attribution-api
- baseURL: https://personalize.amazonaws.com
  baseurl_source: declared
  description: The Personalize Operations API from Amazon Personalize — 10 operation(s) for personalize operations.
  name: Amazon Personalize Personalize Operations API
  slug: amazon-personalize-operations-api
- baseURL: https://personalize.amazonaws.com
  baseurl_source: declared
  description: The Personalize Recommender API from Amazon Personalize — 7 operation(s) for personalize recommender.
  name: Amazon Personalize Personalize Recommender API
  slug: amazon-personalize-recommender-api
- baseURL: https://personalize.amazonaws.com
  baseurl_source: declared
  description: The Personalize Schema API from Amazon Personalize — 4 operation(s) for personalize schema.
  name: Amazon Personalize Personalize Schema API
  slug: amazon-personalize-schema-api
- baseURL: https://personalize.amazonaws.com
  baseurl_source: declared
  description: The Personalize Solution API from Amazon Personalize — 5 operation(s) for personalize solution.
  name: Amazon Personalize Personalize Solution API
  slug: amazon-personalize-solution-api
- baseURL: https://personalize.amazonaws.com
  baseurl_source: declared
  description: The Personalize Solution Version API from Amazon Personalize — 3 operation(s) for personalize solution version.
  name: Amazon Personalize Personalize Solution Version API
  slug: amazon-personalize-solution-version-api
arazzos:
- description: Create an empty Amazon Personalize dataset group for organizing training datasets.
  name: Amazon Personalize Create a Dataset Group
  slug: amazon-personalize-create-dataset-group-workflow
artifact_total: 47
collections:
- collection_type: postman
  name: Amazon Personalize API
  slug: postman-amazon-personalize
- collection_type: open
  name: Amazon Personalize Datasets API
  slug: open-amazon-personalize-datasets-api
- collection_type: open
  name: Amazon Personalize API
  slug: open-amazon-personalize
common:
- group: other
  href: https://artifacts.apis.io/amazon-personalize/capabilities/amazon-personalize-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/amazon-personalize-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/amazon-personalize/plans/amazon-personalize-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/amazon-personalize-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/amazon-personalize/rate-limits/amazon-personalize-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/amazon-personalize-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/amazon-personalize/finops/amazon-personalize-finops.yml
  title: ''
  type: FinOps
  url: finops/amazon-personalize-finops.yml
- group: agent
  href: https://artifacts.apis.io/amazon-personalize/agentic-access/amazon-personalize-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-personalize-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/amazon-personalize/security/amazon-personalize-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/amazon-personalize-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/amazon-personalize/security/amazon-personalize-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-personalize-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/amazon-personalize/security/amazon-personalize-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amazon-personalize-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/amazon-personalize/authentication/amazon-personalize-authentication.yml
  title: ''
  type: Authentication
  url: authentication/amazon-personalize-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-personalize/overview
- group: design
  href: https://artifacts.apis.io/amazon-personalize/arazzo/amazon-personalize-create-dataset-group-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/amazon-personalize-create-dataset-group-workflow.yml
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-personalize/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/personalize/
- group: docs
  title: ''
  type: CLI Reference
  url: https://docs.aws.amazon.com/cli/latest/reference/personalize/
- group: build
  title: ''
  type: SDKs
  url: https://aws.amazon.com/tools/
- group: operate
  title: ''
  type: Service Status
  url: https://status.aws.amazon.com/
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/personalize/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/personalize/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/personalize/pricing/
- group: start
  title: ''
  type: GettingStarted
  url: https://aws.amazon.com/personalize/getting-started/
- group: operate
  title: ''
  type: FAQ
  url: https://aws.amazon.com/personalize/faqs/
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
  url: https://stackoverflow.com/questions/tagged/amazon-personalize
- group: build
  title: ''
  type: Code Examples
  url: https://docs.aws.amazon.com/code-library/latest/ug/personalize_code_examples.html
- group: design
  href: https://artifacts.apis.io/amazon-personalize/rules/amazon-personalize-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/amazon-personalize-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/amazon-personalize/vocabulary/amazon-personalize-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-personalize-vocabulary.yaml
- group: design
  href: https://artifacts.apis.io/amazon-personalize/json-ld/amazon-personalize-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/amazon-personalize-context.jsonld
- group: design
  href: https://artifacts.apis.io/amazon-personalize/json-ld/amazon-personalize-openapi-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/amazon-personalize-openapi-context.jsonld
- group: docs
  href: https://artifacts.apis.io/amazon-personalize/json-schema/amazon-personalize-schema.json
  title: Amazon Personalize
  type: JSONSchema
  url: json-schema/amazon-personalize-schema.json
- group: docs
  href: https://artifacts.apis.io/amazon-personalize/json-schema/openapi-campaign-schema.json
  title: Openapi Campaign
  type: JSONSchema
  url: json-schema/openapi-campaign-schema.json
- group: docs
  href: https://artifacts.apis.io/amazon-personalize/json-schema/openapi-create-dataset-group-request-schema.json
  title: Openapi Create Dataset Group Request
  type: JSONSchema
  url: json-schema/openapi-create-dataset-group-request-schema.json
- group: docs
  href: https://artifacts.apis.io/amazon-personalize/json-schema/openapi-dataset-group-schema.json
  title: Openapi Dataset Group
  type: JSONSchema
  url: json-schema/openapi-dataset-group-schema.json
- group: docs
  href: https://artifacts.apis.io/amazon-personalize/json-schema/openapi-solution-schema.json
  title: Openapi Solution
  type: JSONSchema
  url: json-schema/openapi-solution-schema.json
created: '2024-01-15'
description: Amazon Personalize is a fully managed machine learning service that enables developers to create individualized recommendations for customers using their applications.
examples:
- key_count: 12
  name: Amazon Personalize Example
  slug: amazon-personalize-example
- key_count: 5
  name: Openapi Campaign Example
  slug: openapi-campaign-example
- key_count: 2
  name: Openapi Create Dataset Group Request Example
  slug: openapi-create-dataset-group-request-example
- key_count: 5
  name: Openapi Dataset Group Example
  slug: openapi-dataset-group-example
- key_count: 5
  name: Openapi Solution Example
  slug: openapi-solution-example
finops:
- has_sources: true
  method: derived
  name: Amazon Personalize Finops
  primary_unit: 1,000 recommendations
  service_category: ''
  slug: amazon-personalize-finops
  template: false
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: Amazon Personalize Dataset Group Definition
  property_count: 12
  slug: amazon-personalize
- name: Campaign
  property_count: 5
  slug: openapi-campaign
- name: CreateDatasetGroupRequest
  property_count: 2
  slug: openapi-create-dataset-group-request
- name: DatasetGroup
  property_count: 5
  slug: openapi-dataset-group
- name: Solution
  property_count: 5
  slug: openapi-solution
json_structures:
- name: Amazon Personalize Structure
  property_count: 12
  slug: amazon-personalize-structure
- name: Openapi Campaign Structure
  property_count: 5
  slug: openapi-campaign-structure
- name: Openapi Create Dataset Group Request Structure
  property_count: 2
  slug: openapi-create-dataset-group-request-structure
- name: Openapi Dataset Group Structure
  property_count: 5
  slug: openapi-dataset-group-structure
- name: Openapi Solution Structure
  property_count: 5
  slug: openapi-solution-structure
jsonld:
- class_count: 0
  name: Amazon Personalize Context
  property_count: 5
  slug: amazon-personalize-context
- class_count: 4
  name: Amazon Personalize Openapi Context
  property_count: 10
  slug: amazon-personalize-openapi-context
layout: provider
modified: '2026-05-19'
name: Amazon Personalize
nav: Providers
network: true
overview: 'Amazon Personalize publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Datasets API, Personalize Batch Inference Job API, Personalize Batch Segment Job API, and 13 more. Tagged areas include Artificial Intelligence, Customer Experience, Machine Learning, Personalization, and Recommendations.


  The Amazon Personalize catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Amazon Personalize''s developer surface includes authentication, engineering blog, support, developer console, documentation, pricing, getting-started guide, and 31 more developer resources.'
plans:
- name: Amazon Personalize Plans Pricing
  plan_count: 24
  slug: amazon-personalize-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Amazon Personalize Rate Limits
  slug: amazon-personalize-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Amazon Personalize — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: amazon-personalize-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 66
  extends:
  - spectral:oas
  name: Amazon Personalize API Rules
  rule_count: 25
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 13
  slug: amazon-personalize-spectral-rules
score:
  band: strong
  composite: 63.6
  coverage:
    artifact_dirs: 22
    catalog_earned: 72.4
    catalog_earned_first_party: 12.0
    catalog_gap: 42.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.1
  facets:
    access_clarity: 100.0
    contract_governance: 27.3
    contract_quality: 62.4
    developer_ergonomics: 63.1
    discoverability: 64.3
    operational_transparency: 23.7
  previous_composite: 61.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 93.8
      total: 16
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/amazon-personalize/amazon-personalize-2026-06-20T171758.png
security:
- kind: authentication
  name: Amazon Personalize Authentication
  slug: amazon-personalize-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Personalize Domain Security
  slug: amazon-personalize-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Personalize Vulnerability Disclosure
  slug: amazon-personalize-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Personalize Trust Center
  slug: amazon-personalize-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-personalize
tags:
- Artificial Intelligence
- Customer Experience
- Machine Learning
- Personalization
- Recommendations
website: https://aws.amazon.com/personalize/
---
