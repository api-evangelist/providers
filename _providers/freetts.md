---
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'REST/JSON API for text-to-speech synthesis, audio and SRT subtitle download, and voice listing. Uses x-api-key header auth. Endpoints: POST /api/v1/tts, GET /api/audio/{file_id}, GET /api/srt/{file_id'
  name: FreeTTS REST API
  slug: freetts-rest-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/freetts-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://freetts.org/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://freetts.org/pricing
- group: start
  title: ''
  type: SignUp
  url: https://freetts.org/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://freetts.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://freetts.org/privacy
- group: operate
  title: ''
  type: Support
  url: https://freetts.org/contact
- group: company
  title: ''
  type: Blog
  url: https://freetts.org/blog
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/freetts-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/freetts-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/freetts-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/freetts-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/freetts-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/freetts-components.yml
created: '2026-08-28'
description: 'Cloud text-to-speech / AI voice service (freetts.org) offering neural voices across 75+ languages via a small REST/JSON API, plus speech-to-text, AI video and voiceover, audiobook generation, an SRT subtitle surface, and first-party Chrome, Edge and Firefox extensions. Built and operated by Outline Technologies (outline.ad), bootstrapped, founded 2025, hosted on Hetzner in Falkenstein DE behind Cloudflare. The API is a proxy over third-party neural TTS: the live GET /api/voices catalogue probed 2026-08-28 returned 1,410 voices across 152 locales sourced from Google (788), Microsoft Edge (318) and Microsoft Azure (304), of which the 318 Edge voices are the free tier. FreeTTS publishes no OpenAPI, no apis.json, no MCP server and no agent card.'
image: https://freetts.org/images/og-image.webp
json_schemas:
- name: FreeTTS Voice
  property_count: 15
  slug: freetts-voice
layout: provider
modified: '2026-08-28'
name: FreeTTS
nav: Providers
network: true
overview: 'FreeTTS publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Text-to-Speech, Speech Synthesis, AI-voice, Audio, and Media.


  FreeTTS''s developer surface includes pricing, signup flow, support, engineering blog, and 10 more developer resources.'
plans:
- name: Freetts Plans Pricing
  plan_count: 3
  slug: freetts-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Freetts Rate Limits
  slug: freetts-rate-limits
score:
  band: developing
  composite: 42.6
  coverage:
    artifact_dirs: 16
    catalog_gap: 48.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 8.0
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 31.6
  previous_composite: 42.6
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Freetts Authentication
  slug: freetts-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Freetts Domain Security
  slug: freetts-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: freetts
tags:
- Text-to-Speech
- Speech Synthesis
- AI-voice
- Audio
- Media
- Accessibility
- Speech-to-Text
- Content Creation
- Developer Tools
website: https://freetts.org/developers
---
