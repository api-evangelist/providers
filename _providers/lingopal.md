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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Lingopal Agentic Access
  operation_count: 13
  slug: lingopal-agentic-access
  summary_line: 13 operations · 8 acting
api_count: 4
apis:
- description: Work with reusable registered jobs, their workflows, status, and outputs.
  name: Lingopal Jobs API
  slug: lingopal-jobs-api
- description: List supported language capabilities for dubbing, text, and other workflows.
  name: Lingopal Languages API
  slug: lingopal-languages-api
- description: Start media, document, subtitle, and text translation workflows.
  name: Lingopal Translate API
  slug: lingopal-translate-api
- description: Create storage uploads and register jobs for later use.
  name: Lingopal Upload API
  slug: lingopal-upload-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://lingopal.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.lingopal.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lingopal.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.lingopal.ai/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lingopal.ai/guides/getting-started
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/lingopal-openapi-original.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/lingopal-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lingopal-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lingopal-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lingopal-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lingopal-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lingopal-conformance.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/lingopal-v2-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lingopal-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lingopal-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lingopal-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lingopal-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://lingopal.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lingopal-ai
- group: operate
  title: ''
  type: Support
  url: mailto:support@lingopal.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://lingopal.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.lingopal.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lingopal.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lingopal.ai/policy
created: '2026-07-17'
description: Lingopal is an AI translation company building a real-time language layer for live and on-demand video. Its platform delivers sub-10-second AI dubbing and captioning for livestreams across 100+ languages, preserving speaker characteristics through voice cloning, and targets sports and news broadcasters, streaming and FAST channel operators, live events, faith organizations, and contact centers. Lingopal also publishes a public v2 REST API for uploading media and documents, starting translation and dubbing workflows, generating subtitle tracks, translating text synchronously, and downloading generated transcripts and subtitles. The API is documented at docs.lingopal.ai with a machine-readable OpenAPI 3.1 specification, is authenticated with an X-API-Key header, and exposes 112 locales with per-locale text, dubbing, and voice-cloning capability flags.
image: https://lingopal.ai/header_image.png
layout: provider
mcp_servers:
- description: ''
  name: lingopal-mcp.yml
  slug: lingopal-mcpyml
modified: '2026-07-19'
name: Lingopal
nav: Providers
network: true
overview: 'Lingopal publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Jobs API, Languages API, Translate API, and 1 more. Tagged areas include Company, Frontier Tech, Artificial Intelligence, Translation, and Localization.


  Lingopal''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, pricing, and 18 more developer resources.'
random_paper: 42
score:
  band: developing
  composite: 47.5
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 64.1
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 47.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lingopal/refs/heads/main/screenshots/lingopal-2026-07-25T225250.png
security:
- kind: authentication
  name: Lingopal Authentication
  slug: lingopal-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Lingopal Domain Security
  slug: lingopal-domain-security
  summary_line: TLSv1.3 · DMARC
slug: lingopal
tags:
- Company
- Frontier Tech
- Artificial Intelligence
- Translation
- Localization
- Speech
- Media
- Broadcasting
- Video
- Subtitles
- Voice Cloning
website: https://lingopal.ai/
---
