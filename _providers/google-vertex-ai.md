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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 24.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Google Vertex Ai Agentic Access
  operation_count: 8
  slug: google-vertex-ai-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 1
apis:
- baseURL: https://us-central1-aiplatform.googleapis.com/v1
  baseurl_source: declared
  description: Manage training datasets
  name: Google Vertex AI Datasets API
  slug: google-vertex-ai-datasets-api
- baseURL: https://us-central1-aiplatform.googleapis.com/v1
  baseurl_source: declared
  description: Manage prediction endpoints
  name: Google Vertex AI Endpoints API
  slug: google-vertex-ai-endpoints-api
- baseURL: https://us-central1-aiplatform.googleapis.com/v1
  baseurl_source: declared
  description: Manage ML models
  name: Google Vertex AI Models API
  slug: google-vertex-ai-models-api
- baseURL: https://us-central1-aiplatform.googleapis.com/v1
  baseurl_source: declared
  description: Run predictions using deployed models
  name: Google Vertex AI Predictions API
  slug: google-vertex-ai-predictions-api
- baseURL: https://us-central1-aiplatform.googleapis.com/v1
  baseurl_source: declared
  description: Manage training pipelines
  name: Google Vertex AI TrainingPipelines API
  slug: google-vertex-ai-trainingpipelines-api
artifact_total: 26
collections:
- collection_type: postman
  name: Google Vertex AI Datasets API
  slug: postman-google-vertex-ai-datasets-api
- collection_type: postman
  name: Google Vertex AI Datasets Endpoints API
  slug: postman-google-vertex-ai-endpoints-api
- collection_type: postman
  name: Google Vertex AI Datasets Models API
  slug: postman-google-vertex-ai-models-api
- collection_type: postman
  name: Google Vertex AI Datasets Predictions API
  slug: postman-google-vertex-ai-predictions-api
- collection_type: postman
  name: Google Vertex AI Datasets TrainingPipelines API
  slug: postman-google-vertex-ai-trainingpipelines-api
- collection_type: open
  name: Google Vertex AI Datasets API
  slug: open-google-vertex-ai-datasets-api
- collection_type: open
  name: Google Vertex AI Datasets Endpoints API
  slug: open-google-vertex-ai-endpoints-api
- collection_type: open
  name: Google Vertex AI Datasets Models API
  slug: open-google-vertex-ai-models-api
- collection_type: open
  name: Google Vertex AI Datasets Predictions API
  slug: open-google-vertex-ai-predictions-api
- collection_type: open
  name: Google Vertex AI Datasets TrainingPipelines API
  slug: open-google-vertex-ai-trainingpipelines-api
- collection_type: open
  name: Google Vertex AI API
  slug: open-openapi
common:
- group: operate
  href: https://artifacts.apis.io/google-vertex-ai/rate-limits/google-vertex-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/google-vertex-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/google-vertex-ai/finops/google-vertex-ai-finops.yml
  title: ''
  type: FinOps
  url: finops/google-vertex-ai-finops.yml
- group: commercial
  href: https://artifacts.apis.io/google-vertex-ai/plans/google-vertex-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/google-vertex-ai-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/google-vertex-ai/capabilities/google-vertex-ai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/google-vertex-ai-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.google.com/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-vertex-ai/overview
- group: agent
  href: https://artifacts.apis.io/google-vertex-ai/agentic-access/google-vertex-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/google-vertex-ai-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/google-vertex-ai/security/google-vertex-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-vertex-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/google-vertex-ai/security/google-vertex-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-vertex-ai-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/google-vertex-ai/authentication/google-vertex-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/google-vertex-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/google-vertex-ai/scopes/google-vertex-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/google-vertex-ai-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleapis
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/vertex-ai
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/vertex-ai/docs/start/introduction-unified-platform
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/vertex-ai/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/vertex-ai/docs/general/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/vertex-ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloud.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/vertex-ai/docs/support
- group: design
  href: https://artifacts.apis.io/google-vertex-ai/json-ld/json-ld.yml
  title: ''
  type: JSONLDContext
  url: json-ld/json-ld.yml
- group: company
  title: ''
  type: Blog
  url: https://docs.cloud.google.com/feeds/vertex-ai-release-notes.xml
created: '2026-03-13'
description: Google Vertex AI is a machine learning platform that enables developers and data scientists to build, deploy, and scale ML models, including generative AI models, with pre-trained APIs, AutoML, and custom training capabilities.
finops:
- has_sources: true
  method: derived
  name: Google Vertex Ai Finops
  primary_unit: hour
  service_category: ''
  slug: google-vertex-ai-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-vertex-ai.png
layout: provider
modified: '2026-05-19'
name: Google Vertex AI
nav: Providers
network: true
overview: 'Google Vertex AI publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Datasets API, Endpoints API, Models API, and 2 more. Tagged areas include Artificial Intelligence, Generative AI, Google Cloud, Machine Learning, and ML Models.


  The Google Vertex AI catalog on APIs.io includes 1 Spectral governance ruleset.


  Google Vertex AI''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, engineering blog, and 16 more developer resources.'
plans:
- name: Google Vertex Ai Plans Pricing
  plan_count: 10
  slug: google-vertex-ai-plans-pricing
- name: Google Vertex Ai Price Estimates
  plan_count: 0
  slug: google-vertex-ai-price-estimates
random_paper: 15
rate_limits:
- limit_count: 5
  name: Google Vertex Ai Rate Limits
  slug: google-vertex-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Google Vertex AI — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-vertex-ai-jsonschema-spectral-rules
scopes:
- name: Google Vertex Ai Scopes
  scope_count: 1
  slug: google-vertex-ai-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 48.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 63.7
    catalog_earned_first_party: 12.0
    catalog_gap: 51.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    contract_governance: 9.8
    contract_quality: 52.7
    developer_ergonomics: 34.5
    discoverability: 66.1
    operational_transparency: 36.8
  previous_composite: 48.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 32.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/google-vertex-ai/google-vertex-ai-2026-06-20T182247.png
security:
- kind: authentication
  name: Google Vertex Ai Authentication
  slug: google-vertex-ai-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Vertex Ai Domain Security
  slug: google-vertex-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Vertex Ai Vulnerability Disclosure
  slug: google-vertex-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-vertex-ai
tags:
- Artificial Intelligence
- Generative AI
- Google Cloud
- Machine Learning
- ML Models
website: https://www.google.com/
---
