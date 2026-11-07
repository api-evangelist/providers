---
access_model:
  confidence: high
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
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Gptzero Agentic Access
  operation_count: 7
  slug: gptzero-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.gptzero.me/v2
  baseurl_source: declared
  description: Batch processing
  name: GPTZero Batch API
  slug: gptzero-batch-api
- baseURL: https://api.gptzero.me/v2
  baseurl_source: declared
  description: AI content detection
  name: GPTZero Detection API
  slug: gptzero-detection-api
- baseURL: https://api.gptzero.me/v2
  baseurl_source: declared
  description: Document analysis
  name: GPTZero Documents API
  slug: gptzero-documents-api
artifact_total: 16
collections:
- collection_type: open
  name: GPTZero Batch API
  slug: open-gptzero-batch-api
- collection_type: open
  name: GPTZero Batch Detection API
  slug: open-gptzero-detection-api
- collection_type: open
  name: GPTZero Batch Documents API
  slug: open-gptzero-documents-api
common:
- group: company
  title: ''
  type: Blog
  url: https://gptzero.me/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://gptzero.me/news/rss/
- group: company
  title: ''
  type: Website
  url: https://gptzero.me
- group: start
  title: ''
  type: DeveloperPortal
  url: https://gptzero.me/developers
- group: docs
  title: ''
  type: Documentation
  url: https://gptzero.stoplight.io/
- group: docs
  title: ''
  type: APIReference
  url: https://gptzero.stoplight.io/docs/gptzero-api/5bf295g49gwxp-gpt-zero-api
- group: start
  title: ''
  type: GettingStarted
  url: https://support.gptzero.me/hc/en-us/articles/15525014408215-How-can-I-get-the-API-and-request-code-samples
- group: operate
  title: ''
  type: Support
  url: https://support.gptzero.me
- group: company
  title: ''
  type: Blog
  url: https://gptzero.me/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GPTZero
- group: commercial
  title: ''
  type: Pricing
  url: https://gptzero.me/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.gptzero.me/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gptzero.me/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gptzero.me/privacy-policy.html
- group: docs
  href: https://artifacts.apis.io/gptzero/openapi/_original/gptzero-openapi-original.json
  title: ''
  type: OpenAPI
  url: openapi/_original/gptzero-openapi-original.json
- group: auth
  href: https://artifacts.apis.io/gptzero/authentication/gptzero-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gptzero-authentication.yml
- group: build
  href: https://artifacts.apis.io/gptzero/packages/gptzero-packages.yml
  title: ''
  type: Packages
  url: packages/gptzero-packages.yml
- group: build
  href: https://artifacts.apis.io/gptzero/packages/gptzero-packages.yml
  title: ''
  type: SDKs
  url: packages/gptzero-packages.yml
- group: agent
  href: https://artifacts.apis.io/gptzero/mcp/gptzero-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/gptzero-mcp.yml
- group: agent
  href: https://artifacts.apis.io/gptzero/skills/gptzero-detect-ai-text.md
  title: ''
  type: AgentSkill
  url: skills/gptzero-detect-ai-text.md
- group: agent
  href: https://artifacts.apis.io/gptzero/skills/gptzero-batch-analysis.md
  title: ''
  type: AgentSkill
  url: skills/gptzero-batch-analysis.md
- group: agent
  href: https://artifacts.apis.io/gptzero/llms/gptzero-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gptzero-llms.txt
- group: other
  href: https://artifacts.apis.io/gptzero/overlays/gptzero-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gptzero-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/gptzero/conformance/gptzero-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gptzero-conformance.yml
- group: design
  href: https://artifacts.apis.io/gptzero/conventions/gptzero-conventions.yml
  title: ''
  type: Conventions
  url: conventions/gptzero-conventions.yml
- group: design
  href: https://artifacts.apis.io/gptzero/lifecycle/gptzero-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/gptzero-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/gptzero/changelog/gptzero-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/gptzero-changelog.yml
- group: design
  href: https://artifacts.apis.io/gptzero/data-model/gptzero-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gptzero-data-model.yml
- group: operate
  href: https://artifacts.apis.io/gptzero/rate-limits/gptzero-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gptzero-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/gptzero/plans/gptzero-plans.yml
  title: ''
  type: Plans
  url: plans/gptzero-plans.yml
- group: auth
  href: https://artifacts.apis.io/gptzero/security/gptzero-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gptzero-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/gptzero/agentic-access/gptzero-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gptzero-agentic-access.yml
created: '2026-07-17'
description: GPTZero is an AI content detection company whose v2 API analyzes text and uploaded documents to determine whether content was written by a human, by AI, or is a mix of both. The API returns document-, paragraph-, and sentence-level probabilities along with supporting perplexity and burstiness signals, plus asynchronous batch analysis and aggregate reporting. Authentication is via an X-API-Key header, requests are rate limited to 30,000 per hour, and API access is bundled with the Professional plan. GPTZero was surfaced as a portfolio company of Uncork Capital and has been enriched into the API Evangelist network from its public developer surface.
finops:
- has_sources: true
  method: derived
  name: Gptzero Finops
  primary_unit: subscription
  service_category: ''
  slug: gptzero-finops
  template: false
image: https://gptzero.me/logo.png
layout: provider
modified: '2026-10-06'
name: GPTZero
nav: Providers
network: true
overview: 'GPTZero publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Batch API, Detection API, and Documents API. Tagged areas include Company, Artificial Intelligence, AI Detection, Content Moderation, and Machine Learning.


  The GPTZero catalog on APIs.io includes 1 Spectral governance ruleset.


  GPTZero''s developer surface includes engineering blog, documentation, API reference, getting-started guide, support, pricing, signup flow, and 25 more developer resources.'
plans:
- name: Gptzero Plans
  plan_count: 4
  slug: gptzero-plans
- name: Gptzero Price Estimates
  plan_count: 0
  slug: gptzero-price-estimates
random_paper: 11
rate_limits:
- limit_count: 1
  name: Gptzero Rate Limits
  slug: gptzero-rate-limits
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: GPTZero API Rules
  rule_count: 48
  severity_counts:
    error: 46
    hint: 0
    info: 1
    warn: 1
  slug: gptzero-rules
score:
  band: developing
  composite: 52.4
  coverage:
    artifact_dirs: 27
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 66.1
    discoverability: 73.2
    operational_transparency: 39.5
  previous_composite: 52.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/gptzero/gptzero-2026-07-25T220147.png
security:
- kind: authentication
  name: Gptzero Authentication
  slug: gptzero-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Gptzero Domain Security
  slug: gptzero-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Run a batch AI-detection job with GPTZero
  slug: gptzero-batch-analysis
- name: Detect AI-generated text with GPTZero
  slug: gptzero-detect-ai-text
slug: gptzero
tags:
- Company
- Artificial Intelligence
- AI Detection
- Content Moderation
- Machine Learning
- Text Analysis
- Natural Language Processing
- Education
website: https://gptzero.me
---
