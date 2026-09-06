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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.9
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'Programmatic access to Verbit''s transcription and captioning platform: live booking / real-time captioning, post-production transcription jobs, caption control, search, and AI insights.'
  name: Verbit Platform API
  slug: verbit-platform-api
artifact_total: 5
asyncapis:
- description: ''
  name: Verbit Webhooks
  slug: verbit-webhooks
common:
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/verbit-mcp.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/verbit-trust-center.yml
- group: auth
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
  title: ''
  type: ChangeLog
  url: changelog/verbit-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/verbit-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/verbit-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/verbit-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/verbit-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/verbit-packages.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/verbit-error-codes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/verbit-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/verbit-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/verbit-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/verbit-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/verbit-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/verbit-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/verbit-conventions.yml
created: '2026-07-17'
description: Verbit is an AI-based transcription and captioning company whose platform pairs a state-of-the-art automatic speech recognition (ASR) engine with professional human review to deliver accurate transcripts and captions for legal, courtroom, media & entertainment, higher education, corporate, and government use cases. Verbit exposes a developer platform (Verbit Platform API v3) covering live booking and real-time captioning over WebSocket, post-production transcription jobs, a Caption Control API for managing live sessions, a Search API for indexing caption/transcript assets, and an Insights (Gen V) API that generates AI summaries, keywords, quizzes, and chapters. Authentication uses a short-lived JWT bearer token minted from a customer API key. Backed by HV Capital and Sapphire Ventures.
image: https://verbit.ai/wp-content/themes/verbit/images/logo-final2.svg
layout: provider
modified: '2026-07-21'
name: VerbIT
nav: Providers
network: true
overview: 'VerbIT publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Enterprise Software, Transcription, Captioning, and Speech Recognition.


  The VerbIT catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  VerbIT''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, signup flow, pricing, and 25 more developer resources.'
random_paper: 1
score:
  band: developing
  composite: 46.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 52.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 50.0
  previous_composite: 46.6
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/verbit/refs/heads/main/screenshots/verbit-2026-08-17T082729.png
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
