---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Programmatic access to Verbit''s transcription and captioning platform: live booking / real-time captioning, post-production transcription jobs, caption control, search, and AI insights.'
  name: Verbit Platform API
  slug: verbit-platform-api
artifact_total: 7
asyncapis:
- description: ''
  name: Verbit Webhooks
  slug: verbit-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/verbit/plans/verbit-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/verbit-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://verbit.ai/feed/
- group: agent
  href: https://artifacts.apis.io/verbit/mcp/verbit-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/verbit-mcp.yml
- group: auth
  href: https://artifacts.apis.io/verbit/security/verbit-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/verbit-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/verbit/security/verbit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/verbit-domain-security.yml
- group: auth
  title: ''
  type: Compliance
  url: https://verbit.ai/trust-data-policy/
- group: company
  title: ''
  type: Website
  url: https://verbit.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://verbit.readme.io/
- group: docs
  title: ''
  type: Documentation
  url: https://verbit.readme.io/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://verbit.readme.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://verbit.readme.io/docs/getting-started
- group: auth
  href: https://artifacts.apis.io/verbit/authentication/verbit-authentication.yml
  title: ''
  type: Authentication
  url: authentication/verbit-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://verbit.ai/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/verbit-ai
- group: start
  title: ''
  type: SignUp
  url: https://users.verbit.co/
- group: commercial
  title: ''
  type: Pricing
  url: https://verbit.ai/pricing-package/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://verbit.ai/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://verbit.ai/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://verbit.ai/contact-us/
- group: operate
  title: ''
  type: StatusPage
  url: https://verbit.statuspal.io/
- group: operate
  href: https://artifacts.apis.io/verbit/changelog/verbit-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/verbit-changelog.yml
- group: operate
  href: https://artifacts.apis.io/verbit/lifecycle/verbit-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/verbit-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/verbit/lifecycle/verbit-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/verbit-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/verbit/llms/verbit-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/verbit-llms.txt
- group: build
  href: https://artifacts.apis.io/verbit/packages/verbit-packages.yml
  title: ''
  type: Packages
  url: packages/verbit-packages.yml
- group: build
  href: https://artifacts.apis.io/verbit/packages/verbit-packages.yml
  title: ''
  type: SDKs
  url: packages/verbit-packages.yml
- group: design
  href: https://artifacts.apis.io/verbit/errors/verbit-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/verbit-error-codes.yml
- group: start
  href: https://artifacts.apis.io/verbit/sandbox/verbit-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/verbit-sandbox.yml
- group: design
  href: https://artifacts.apis.io/verbit/components/verbit-components.yml
  title: ''
  type: Components
  url: components/verbit-components.yml
- group: design
  href: https://artifacts.apis.io/verbit/data-model/verbit-data-model.yml
  title: ''
  type: DataModel
  url: data-model/verbit-data-model.yml
- group: design
  href: https://artifacts.apis.io/verbit/asyncapi/verbit-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/verbit-webhooks.yml
- group: design
  href: https://artifacts.apis.io/verbit/conformance/verbit-conformance.yml
  title: ''
  type: Conformance
  url: conformance/verbit-conformance.yml
- group: design
  href: https://artifacts.apis.io/verbit/conventions/verbit-conventions.yml
  title: ''
  type: Conventions
  url: conventions/verbit-conventions.yml
- group: design
  href: https://artifacts.apis.io/verbit/conventions/verbit-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/verbit-conventions.yml
created: '2026-07-17'
description: Verbit is an AI-based transcription and captioning company whose platform pairs a state-of-the-art automatic speech recognition (ASR) engine with professional human review to deliver accurate transcripts and captions for legal, courtroom, media & entertainment, higher education, corporate, and government use cases. Verbit exposes a developer platform (Verbit Platform API v3) covering live booking and real-time captioning over WebSocket, post-production transcription jobs, a Caption Control API for managing live sessions, a Search API for indexing caption/transcript assets, and an Insights (Gen V) API that generates AI summaries, keywords, quizzes, and chapters. Authentication uses a short-lived JWT bearer token minted from a customer API key. Backed by HV Capital and Sapphire Ventures.
finops:
- has_sources: true
  method: derived
  name: Verbit Finops
  primary_unit: ''
  service_category: ''
  slug: verbit-finops
  template: true
image: https://verbit.ai/wp-content/themes/verbit/images/logo-final2.svg
layout: provider
modified: '2026-10-06'
name: VerbIT
nav: Providers
network: true
overview: 'VerbIT is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Enterprise Software, Transcription, Captioning, and Speech Recognition.


  The VerbIT catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  VerbIT''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, signup flow, pricing, and 27 more developer resources.'
plans:
- name: Verbit Plans Pricing
  plan_count: 10
  slug: verbit-plans-pricing
random_paper: 4
score:
  band: strong
  composite: 56.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.1
  facets:
    access_clarity: 78.9
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 67.9
    discoverability: 73.2
    operational_transparency: 50.0
  previous_composite: 53.8
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/verbit/verbit-2026-08-17T082729.png
security:
- kind: authentication
  name: Verbit Authentication
  slug: verbit-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Verbit Domain Security
  slug: verbit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Verbit Trust Center
  slug: verbit-trust-center
  summary_line: SOC 2, ISO 27001
slug: verbit
tags:
- Company
- Ai Enterprise Software
- Transcription
- Captioning
- Speech Recognition
- Accessibility
- Artificial Intelligence
- Media
website: https://verbit.ai/
---
