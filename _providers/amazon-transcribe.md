---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Amazon Transcribe Agentic Access
  operation_count: 5
  slug: amazon-transcribe-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 1
apis:
- baseURL: https://transcribe.amazonaws.com
  baseurl_source: declared
  description: The Transcription Jobs API from Amazon Transcribe — 4 operation(s) for transcription jobs.
  name: Amazon Transcribe Transcription Jobs API
  slug: amazon-transcribe-transcription-jobs-api
- baseURL: https://transcribe.amazonaws.com
  baseurl_source: declared
  description: The Vocabularies API from Amazon Transcribe — 1 operation(s) for vocabularies.
  name: Amazon Transcribe Vocabularies API
  slug: amazon-transcribe-vocabularies-api
- baseURL: https://transcribe.amazonaws.com
  baseurl_source: declared
  description: The Transcribe Call Analytics Category API from Amazon Transcribe — 5 operation(s) for transcribe call analytics category.
  name: Amazon Transcribe Transcribe Call Analytics Category API
  slug: amazon-transcribe-call-analytics-category-api
- baseURL: https://transcribe.amazonaws.com
  baseurl_source: declared
  description: The Transcribe Call Analytics Job API from Amazon Transcribe — 4 operation(s) for transcribe call analytics job.
  name: Amazon Transcribe Transcribe Call Analytics Job API
  slug: amazon-transcribe-call-analytics-job-api
- baseURL: https://transcribe.amazonaws.com
  baseurl_source: declared
  description: The Transcribe Language Model API from Amazon Transcribe — 5 operation(s) for transcribe language model.
  name: Amazon Transcribe Transcribe Language Model API
  slug: amazon-transcribe-language-model-api
- baseURL: https://transcribe.amazonaws.com
  baseurl_source: declared
  description: The Transcribe Medical Scribe Job API from Amazon Transcribe — 4 operation(s) for transcribe medical scribe job.
  name: Amazon Transcribe Transcribe Medical Scribe Job API
  slug: amazon-transcribe-medical-scribe-job-api
- baseURL: https://transcribe.amazonaws.com
  baseurl_source: declared
  description: The Transcribe Medical Transcription Job API from Amazon Transcribe — 4 operation(s) for transcribe medical transcription job.
  name: Amazon Transcribe Transcribe Medical Transcription Job API
  slug: amazon-transcribe-medical-transcription-job-api
- baseURL: https://transcribe.amazonaws.com
  baseurl_source: declared
  description: The Transcribe Medical Vocabulary API from Amazon Transcribe — 5 operation(s) for transcribe medical vocabulary.
  name: Amazon Transcribe Transcribe Medical Vocabulary API
  slug: amazon-transcribe-medical-vocabulary-api
- baseURL: https://transcribe.amazonaws.com
  baseurl_source: declared
  description: The Transcribe Operations API from Amazon Transcribe — 3 operation(s) for transcribe operations.
  name: Amazon Transcribe Transcribe Operations API
  slug: amazon-transcribe-operations-api
- baseURL: https://transcribe.amazonaws.com
  baseurl_source: declared
  description: The Transcribe Vocabulary Filter API from Amazon Transcribe — 5 operation(s) for transcribe vocabulary filter.
  name: Amazon Transcribe Transcribe Vocabulary Filter API
  slug: amazon-transcribe-vocabulary-filter-api
artifact_total: 36
collections:
- collection_type: postman
  name: Amazon Transcribe Transcription Jobs API
  slug: postman-amazon-transcribe-transcription-jobs-api
- collection_type: postman
  name: Amazon Transcribe Transcription Jobs Vocabularies API
  slug: postman-amazon-transcribe-vocabularies-api
- collection_type: open
  name: Amazon Transcribe Transcription Jobs API
  slug: open-amazon-transcribe-transcription-jobs-api
- collection_type: open
  name: Amazon Transcribe Transcription Jobs Vocabularies API
  slug: open-amazon-transcribe-vocabularies-api
- collection_type: open
  name: Amazon Transcribe API
  slug: open-amazon-transcribe
common:
- group: other
  href: https://artifacts.apis.io/amazon-transcribe/capabilities/amazon-transcribe-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/amazon-transcribe-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/amazon-transcribe/plans/amazon-transcribe-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/amazon-transcribe-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/amazon-transcribe/rate-limits/amazon-transcribe-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/amazon-transcribe-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/amazon-transcribe/finops/amazon-transcribe-finops.yml
  title: ''
  type: FinOps
  url: finops/amazon-transcribe-finops.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-transcribe/overview
- group: agent
  href: https://artifacts.apis.io/amazon-transcribe/agentic-access/amazon-transcribe-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-transcribe-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/amazon-transcribe/security/amazon-transcribe-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/amazon-transcribe-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/amazon-transcribe/security/amazon-transcribe-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-transcribe-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/amazon-transcribe/security/amazon-transcribe-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amazon-transcribe-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/amazon-transcribe/authentication/amazon-transcribe-authentication.yml
  title: ''
  type: Authentication
  url: authentication/amazon-transcribe-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/transcribe/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/transcribe/
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
  url: https://aws.amazon.com/blogs/machine-learning/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/transcribe/
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
- group: other
  title: ''
  type: Knowledge Center
  url: https://repost.aws/knowledge-center
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-transcribe
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/amazon-transcribe/refs/heads/main/rules/amazon-transcribe-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/amazon-transcribe/refs/heads/main/vocabulary/amazon-transcribe-vocabulary.yaml
created: '2024-01-15'
description: Amazon Transcribe is a speech-to-text service that uses machine learning models to convert audio to text, supporting real-time streaming and batch transcription with automatic speech recognition (ASR).
examples:
- key_count: 2
  name: Amazon Transcribe Example
  slug: amazon-transcribe-example
features:
- description: Automate operational tasks with Amazon Transcribe.
  name: Automation
- description: Programmatic access to Amazon Transcribe resources.
  name: API Access
finops:
- has_sources: true
  method: derived
  name: Amazon Transcribe Finops
  primary_unit: minute
  service_category: ''
  slug: amazon-transcribe-finops
  template: false
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: Amazon Transcribe Transcription Job
  property_count: 13
  slug: amazon-transcribe-job
- name: Tag
  property_count: 2
  slug: amazon-transcribe-tag
- name: TranscriptionJob
  property_count: 8
  slug: amazon-transcribe-transcription-job
json_structures:
- name: Amazon Transcribe Job Structure
  property_count: 0
  slug: amazon-transcribe-job-structure
- name: Amazon Transcribe Tag Structure
  property_count: 0
  slug: amazon-transcribe-tag-structure
- name: Amazon Transcribe Transcription Job Structure
  property_count: 0
  slug: amazon-transcribe-transcription-job-structure
jsonld:
- class_count: 7
  name: Amazon Transcribe Context
  property_count: 5
  slug: amazon-transcribe-context
layout: provider
modified: '2026-05-19'
name: Amazon Transcribe
nav: Providers
network: true
overview: 'Amazon Transcribe publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Transcription Jobs API, Vocabularies API, Transcribe Call Analytics Category API, and 7 more. Tagged areas include Audio Processing, Amazon Web Services, Machine Learning, Speech Recognition, and Speech-to-Text.


  The Amazon Transcribe catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Transcribe''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 21 more developer resources.'
plans:
- name: Amazon Transcribe Plans Pricing
  plan_count: 6
  slug: amazon-transcribe-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Amazon Transcribe Rate Limits
  slug: amazon-transcribe-rate-limits
rules:
- authorship: generated
  effective_rule_count: 4
  extends: []
  name: Amazon Transcribe — jsonschema rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: amazon-transcribe-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Amazon Transcribe API Rules
  rule_count: 13
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 9
  slug: amazon-transcribe-spectral-rules
score:
  band: strong
  composite: 66.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 77.4
    catalog_earned_first_party: 12.0
    catalog_gap: 37.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.5
  facets:
    access_clarity: 85.5
    contract_governance: 27.3
    contract_quality: 68.3
    developer_ergonomics: 72.6
    discoverability: 73.2
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 64.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 10
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/amazon-transcribe/amazon-transcribe-2026-06-20T171840.png
security:
- kind: authentication
  name: Amazon Transcribe Authentication
  slug: amazon-transcribe-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Transcribe Domain Security
  slug: amazon-transcribe-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Transcribe Vulnerability Disclosure
  slug: amazon-transcribe-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Transcribe Trust Center
  slug: amazon-transcribe-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-transcribe
tags:
- Audio Processing
- Amazon Web Services
- Machine Learning
- Speech Recognition
- Speech-to-Text
- Transcription
use_cases:
- description: Use Amazon Transcribe to manage and automate cloud operations.
  name: Cloud Operations
website: https://aws.amazon.com/transcribe/
---
