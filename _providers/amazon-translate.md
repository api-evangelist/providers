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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Amazon Translate Agentic Access
  operation_count: 4
  slug: amazon-translate-agentic-access
  summary_line: 4 operations · 3 acting
api_count: 1
apis:
- baseURL: https://translate.amazonaws.com
  baseurl_source: declared
  description: The Batch Translation API from Amazon Translate — 2 operation(s) for batch translation.
  name: Amazon Translate Batch Translation API
  slug: amazon-translate-batch-translation-api
- baseURL: https://translate.amazonaws.com
  baseurl_source: declared
  description: The Terminology API from Amazon Translate — 1 operation(s) for terminology.
  name: Amazon Translate Terminology API
  slug: amazon-translate-terminology-api
- baseURL: https://translate.amazonaws.com
  baseurl_source: declared
  description: The Translation API from Amazon Translate — 1 operation(s) for translation.
  name: Amazon Translate Translation API
  slug: amazon-translate-translation-api
- baseURL: https://translate.amazonaws.com
  baseurl_source: declared
  description: The Translate Operations API from Amazon Translate — 7 operation(s) for translate operations.
  name: Amazon Translate Translate Operations API
  slug: amazon-translate-operations-api
- baseURL: https://translate.amazonaws.com
  baseurl_source: declared
  description: The Translate Parallel Data API from Amazon Translate — 5 operation(s) for translate parallel data.
  name: Amazon Translate Translate Parallel Data API
  slug: amazon-translate-parallel-data-api
artifact_total: 31
collections:
- collection_type: postman
  name: Amazon Translate Batch Translation API
  slug: postman-amazon-translate-batch-translation-api
- collection_type: postman
  name: Amazon Translate Batch Translation Terminology API
  slug: postman-amazon-translate-terminology-api
- collection_type: postman
  name: Amazon Translate Batch Translation API
  slug: postman-amazon-translate-translation-api
- collection_type: open
  name: Amazon Translate Batch Translation API
  slug: open-amazon-translate-batch-translation-api
- collection_type: open
  name: Amazon Translate Batch Translation Terminology API
  slug: open-amazon-translate-terminology-api
- collection_type: open
  name: Amazon Translate Batch Translation API
  slug: open-amazon-translate-translation-api
- collection_type: open
  name: Amazon Translate API
  slug: open-amazon-translate
common:
- group: other
  href: https://artifacts.apis.io/amazon-translate/capabilities/amazon-translate-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/amazon-translate-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/amazon-translate/plans/amazon-translate-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/amazon-translate-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/amazon-translate/rate-limits/amazon-translate-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/amazon-translate-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/amazon-translate/finops/amazon-translate-finops.yml
  title: ''
  type: FinOps
  url: finops/amazon-translate-finops.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-translate/overview
- group: agent
  href: https://artifacts.apis.io/amazon-translate/agentic-access/amazon-translate-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-translate-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/amazon-translate/security/amazon-translate-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/amazon-translate-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/amazon-translate/security/amazon-translate-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-translate-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/amazon-translate/security/amazon-translate-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amazon-translate-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/amazon-translate/authentication/amazon-translate-authentication.yml
  title: ''
  type: Authentication
  url: authentication/amazon-translate-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/translate/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/translate/
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
  url: https://console.aws.amazon.com/translate/
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
  url: https://stackoverflow.com/questions/tagged/amazon-translate
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/amazon-translate/refs/heads/main/rules/amazon-translate-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/amazon-translate/refs/heads/main/vocabulary/amazon-translate-vocabulary.yaml
created: '2024-01-15'
description: Amazon Translate is a neural machine translation service that delivers fast, high-quality, affordable, and customizable language translation for applications and content.
examples:
- key_count: 2
  name: Amazon Translate Example
  slug: amazon-translate-example
features:
- description: Automate operational tasks with Amazon Translate.
  name: Automation
- description: Programmatic access to Amazon Translate resources.
  name: API Access
finops:
- has_sources: true
  method: derived
  name: Amazon Translate Finops
  primary_unit: million characters
  service_category: ''
  slug: amazon-translate-finops
  template: false
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: Amazon Translate Translation Job
  property_count: 12
  slug: amazon-translate-job
- name: Tag
  property_count: 2
  slug: amazon-translate-tag
json_structures:
- name: Amazon Translate Job Structure
  property_count: 0
  slug: amazon-translate-job-structure
- name: Amazon Translate Tag Structure
  property_count: 0
  slug: amazon-translate-tag-structure
jsonld:
- class_count: 7
  name: Amazon Translate Context
  property_count: 5
  slug: amazon-translate-context
layout: provider
modified: '2026-05-19'
name: Amazon Translate
nav: Providers
network: true
overview: 'Amazon Translate publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Batch Translation API, Terminology API, Translation API, and 2 more. Tagged areas include Language Processing, Localization, Machine Translation, Natural Language Processing, and Translation.


  The Amazon Translate catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Translate''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 21 more developer resources.'
plans:
- name: Amazon Translate Plans Pricing
  plan_count: 6
  slug: amazon-translate-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Amazon Translate Rate Limits
  slug: amazon-translate-rate-limits
rules:
- authorship: generated
  effective_rule_count: 4
  extends: []
  name: Amazon Translate — jsonschema rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: amazon-translate-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Amazon Translate API Rules
  rule_count: 12
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 8
  slug: amazon-translate-spectral-rules
score:
  band: strong
  composite: 66.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 72.4
    catalog_earned_first_party: 12.0
    catalog_gap: 42.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.5
  facets:
    access_clarity: 92.1
    contract_governance: 27.3
    contract_quality: 62.4
    developer_ergonomics: 72.6
    discoverability: 64.3
    operational_transparency: 39.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 63.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 40.0
      total: 5
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
screenshot: https://apis.io/screenshots/amazon-translate/amazon-translate-2026-06-20T171839.png
security:
- kind: authentication
  name: Amazon Translate Authentication
  slug: amazon-translate-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Translate Domain Security
  slug: amazon-translate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Translate Vulnerability Disclosure
  slug: amazon-translate-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Translate Trust Center
  slug: amazon-translate-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-translate
tags:
- Language Processing
- Localization
- Machine Translation
- Natural Language Processing
- Translation
use_cases:
- description: Use Amazon Translate to manage and automate cloud operations.
  name: Cloud Operations
website: https://aws.amazon.com/translate/
---
