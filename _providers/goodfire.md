---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Hosted mechanistic-interpretability API. OpenAI-compatible chat-completions sampling plus feature discovery (semantic/contrastive search, AutoSteer), feature inspection/context, and model-variant crea
  name: Ember API
  slug: ember-api
artifact_total: 6
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://www.goodfire.com/pricing
- group: commercial
  href: https://artifacts.apis.io/goodfire/plans/goodfire-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/goodfire-plans-pricing.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/goodfire-ai/goodfire-sdk/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/goodfire-ai/goodfire-sdk/blob/main/LICENSE
- group: company
  title: ''
  type: Website
  url: https://goodfire.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform.goodfire.ai
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/goodfire-ai/goodfire-sdk
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/goodfire-ai/goodfire-sdk#readme
- group: start
  title: ''
  type: SignUp
  url: https://platform.goodfire.ai
- group: company
  title: ''
  type: Blog
  url: https://www.goodfire.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://www.goodfire.ai/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/goodfire-ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cdn.prod.website-files.com/67b4608695ee3b31a669d3a9/67b856d25635919af723e246_TermsOfUse.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cdn.prod.website-files.com/67b4608695ee3b31a669d3a9/67b856d26882aaeb845674e4_PrivacyPolicy.pdf
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.goodfire.ai/
- group: build
  href: https://artifacts.apis.io/goodfire/packages/goodfire-packages.yml
  title: ''
  type: Packages
  url: packages/goodfire-packages.yml
- group: build
  href: https://artifacts.apis.io/goodfire/packages/goodfire-packages.yml
  title: ''
  type: SDKs
  url: packages/goodfire-packages.yml
- group: auth
  href: https://artifacts.apis.io/goodfire/authentication/goodfire-authentication.yml
  title: ''
  type: Authentication
  url: authentication/goodfire-authentication.yml
- group: design
  href: https://artifacts.apis.io/goodfire/conventions/goodfire-conventions.yml
  title: ''
  type: Conventions
  url: conventions/goodfire-conventions.yml
- group: design
  href: https://artifacts.apis.io/goodfire/lifecycle/goodfire-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/goodfire-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/goodfire/lifecycle/goodfire-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/goodfire-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/goodfire/conformance/goodfire-conformance.yml
  title: ''
  type: Conformance
  url: conformance/goodfire-conformance.yml
- group: operate
  href: https://artifacts.apis.io/goodfire/changelog/goodfire-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/goodfire-changelog.yml
- group: agent
  href: https://artifacts.apis.io/goodfire/llms/goodfire-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/goodfire-llms.txt
- group: auth
  href: https://artifacts.apis.io/goodfire/security/goodfire-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/goodfire-domain-security.yml
created: '2026-07-17'
description: Goodfire is an AI interpretability research lab building tools to understand, debug, and intentionally design neural networks by surfacing the internal features (via sparse autoencoders) that drive model behavior. Its Ember API/SDK was the first hosted mechanistic-interpretability API, offering an OpenAI-compatible inference endpoint plus feature discovery, inspection, and steering over open models such as Llama 3.3 70B and Llama 3.1 8B. The company is now consolidating this interpretability work into its Silico platform, which spans large language models, life sciences, and robotics/vision. Backed by Lightspeed, Menlo Ventures, and Wing Venture Capital.
finops:
- has_sources: true
  method: derived
  name: Goodfire Finops
  primary_unit: subscription
  service_category: ''
  slug: goodfire-finops
  template: false
image: https://cdn.prod.website-files.com/67b4608695ee3b31a669d3a9/67f8223b7a5017e5e1e983ac_opengraph.png
layout: provider
modified: '2026-07-19'
name: Goodfire
nav: Providers
network: true
overview: 'Goodfire is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Machine Learning, Interpretability, and LLM.


  Goodfire''s developer surface includes pricing, documentation, getting-started guide, signup flow, engineering blog, support, authentication, and 18 more developer resources.'
plans:
- name: Goodfire Plans Pricing
  plan_count: 2
  slug: goodfire-plans-pricing
- name: Goodfire Price Estimates
  plan_count: 0
  slug: goodfire-price-estimates
random_paper: 7
score:
  band: developing
  composite: 40.5
  coverage:
    artifact_dirs: 14
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 81.6
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 66.1
    operational_transparency: 28.9
  previous_composite: 38.9
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/goodfire/goodfire-2026-07-25T220044.png
security:
- kind: authentication
  name: Goodfire Authentication
  slug: goodfire-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Goodfire Domain Security
  slug: goodfire-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: goodfire
tags:
- Company
- Artificial Intelligence
- Machine Learning
- Interpretability
- LLM
- Model Steering
- Inference
- Developer Tools
- Research
website: https://goodfire.ai
---
