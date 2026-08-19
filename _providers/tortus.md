---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: 'TypeScript Embed SDK plus the server-side launch endpoint used to embed AI-powered medical consultations, dictations and meetings into a healthcare application. The backend mints a short-lived launch '
  name: TORTUS Embed SDK
  slug: tortus-embed-sdk
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://tortus.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tortus.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tortus.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tortus.ai/reference/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tortus.ai/quickstart
- group: company
  title: ''
  type: Blog
  url: https://tortus.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://tortus.ai/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tortus-ai
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tortus.ai/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.tortus.ai/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.tortus.ai/
- group: auth
  title: ''
  type: Authentication
  url: authentication/tortus-authentication.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tortus-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/tortus-packages.yml
- group: design
  title: ''
  type: Components
  url: components/tortus-components.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tortus-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tortus-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tortus-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tortus-error-codes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tortus-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/tortus-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tortus-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tortus-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tortus-llms.txt
created: '2026-07-17'
description: TORTUS is a healthcare AI company whose ambient voice technology (AVT) platform automatically transcribes and documents clinical consultations. It captures speaker-diarized, locally-encrypted audio, generates structured clinical notes, letters and referrals, suggests diagnostic and procedural codes, and files findings into the electronic health record after clinician approval. TORTUS is live across 1,000+ NHS organisations with 2.5M+ consultations processed and integrates with Epic, EMIS Health, TPP SystmOne, Oracle Health, Access Rio and Medicus. Developers embed the experience with the TORTUS Embed SDK (@tortus-ai/embed-client), a TypeScript client that mounts a sandboxed iframe and authenticates via short-lived launch tokens minted server-side against the api.tortus.ai launch endpoint. TORTUS is a UKCA Class IIa medical device with ISO 27001, ISO 13485, Cyber Essentials Plus, NHS DTAC and DSPT posture.
image: https://pub-bb2e103a32db4e198524a2e9ed8f35b4.r2.dev/0dbb3f54-9b72-4a98-8408-b287decae2b3/id-preview-17c5b15e--d126be98-e1f2-44fe-a8b2-bc92ca2cb3f8.lovable.app-1780992136068.png
layout: provider
modified: '2026-07-21'
name: Tortus
nav: Providers
network: true
overview: 'Tortus publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Artificial Intelligence, Ambient Clinical Documentation, and Medical Scribe.


  Tortus'' developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, changelog, and 17 more developer resources.'
random_paper: 93
score:
  band: thin
  composite: 29.7
  delta: -0.8
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 30.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 26.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Tortus Authentication
  slug: tortus-authentication
  summary_line: http-basic/publishable-key/launch-token · 3 schemes
- kind: domain-security
  name: Tortus Domain Security
  slug: tortus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Tortus Trust Center
  slug: tortus-trust-center
  summary_line: ISO 27001, ISO 13485, Cyber Essentials Plus, UKCA Class IIa Medical Device
slug: tortus
tags:
- Company
- Healthcare
- Artificial Intelligence
- Ambient Clinical Documentation
- Medical Scribe
- Speech to Text
- EHR Integration
- NHS
- Embed SDK
website: https://tortus.ai/
---
