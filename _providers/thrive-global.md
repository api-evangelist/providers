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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.7
  scored_at: '2026-08-17'
api_count: 8
apis:
- description: Ambient soundscapes and narrated bedtime stories — audio for focus, relaxation, and sleep
  name: Thrive Global audio experiences API
  slug: thrive-global-audio-experiences-api
- description: Partner authentication
  name: Thrive Global auth API
  slug: thrive-global-auth-api
- description: Microsteps, challenges, courses, podcasts, and journey videos
  name: Thrive Global content API
  slug: thrive-global-content-api
- description: Guided meditations — video sessions for relaxation, sleep, and stress management
  name: Thrive Global meditations API
  slug: thrive-global-meditations-api
- description: Chronic condition programs (e.g. GLP-1 Companion)
  name: Thrive Global programs API
  slug: thrive-global-programs-api
- description: Thrive Reset video and audio content
  name: Thrive Global resets API
  slug: thrive-global-resets-api
- description: Search the full Thrive content library (premium capability — contact your Thrive Global representative to enable)
  name: Thrive Global search API
  slug: thrive-global-search-api
- description: Articles, role model stories, and recipes
  name: Thrive Global stories API
  slug: thrive-global-stories-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Thrive Global Partner audio experiences API
  slug: open-thrive-global-audio-experiences-api
- collection_type: open
  name: Thrive Global Partner audio experiences auth API
  slug: open-thrive-global-auth-api
- collection_type: open
  name: Thrive Global Partner audio experiences content API
  slug: open-thrive-global-content-api
- collection_type: open
  name: Thrive Global Partner audio experiences meditations API
  slug: open-thrive-global-meditations-api
- collection_type: open
  name: Thrive Global Partner audio experiences programs API
  slug: open-thrive-global-programs-api
- collection_type: open
  name: Thrive Global Partner audio experiences resets API
  slug: open-thrive-global-resets-api
- collection_type: open
  name: Thrive Global Partner audio experiences search API
  slug: open-thrive-global-search-api
- collection_type: open
  name: Thrive Global Partner audio experiences stories API
  slug: open-thrive-global-stories-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/thrive-global-partner-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.thriveglobal.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.thriveglobal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.thriveglobal.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.thriveglobal.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.thriveglobal.com/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.thriveglobal.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://thriveglobal.com/articles
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thriveglobal
- group: start
  title: ''
  type: Login
  url: https://app.thriveglobal.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thriveglobal.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thriveglobal.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://partners-api.thriveglobal.com/status
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/thrive-global-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/thrive-global-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/thrive-global-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/thrive-global-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/thrive-global-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/thrive-global-sandbox.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/thrive-global-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/thrive-global-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/thrive-global-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://thriveglobal.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/thrive-global-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thrive-global-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Thrive Global is the behavior-change technology company founded by Arianna Huffington that helps employers and healthcare organizations improve wellbeing through Microsteps across five daily behaviors: Connection, Food, Movement, Sleep, and Stress Management. Its Partner API (documented at developers.thriveglobal.com) serves the Thrive content library - Resets, stories, microsteps, challenges, learning courses, podcasts, meditations, soundscapes, bedtime stories, and chronic-condition programs - and an official MCP server at mcp.thriveglobal.com exposes user wellbeing data and actions to AI assistants.'
image: https://developers.thriveglobal.com/brand-team-leaf-2.svg
layout: provider
mcp_servers:
- description: ''
  name: thrive-global-mcp.yml
  slug: thrive-global-mcpyml
modified: '2026-07-21'
name: Thrive Global
nav: Providers
network: true
overview: 'Thrive Global publishes 8 APIs on the [APIs.io](https://apis.io/) network, including audio experiences API, auth API, content API, and 5 more. Tagged areas include Company, Consumer, Wellness, Wellbeing, and Behavior Change.


  Thrive Global''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, sandbox, and 19 more developer resources.'
random_paper: 136
score:
  band: developing
  composite: 49.4
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 61.9
    developer_ergonomics: 69.0
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 49.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Thrive Global Authentication
  slug: thrive-global-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Thrive Global Domain Security
  slug: thrive-global-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Thrive Global Trust Center
  slug: thrive-global-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: thrive-global
tags:
- Company
- Consumer
- Wellness
- Wellbeing
- Behavior Change
- Content
- Healthcare
- Employee Experience
website: https://www.thriveglobal.com
---
