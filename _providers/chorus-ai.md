---
access_model:
  confidence: high
  label: Enterprise / Contact Sales
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - openapi
  - pricing-page
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.7
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: Search and retrieve calls, meetings, emails and engagement metadata. A capability area of the single published Chorus API contract, served at /v3/engagements and /api/v1/conversations.
  name: Chorus Engagements API
  slug: chorus-engagements-api
- description: Upload recordings, retrieve media files, transcripts and AI-generated insights, and build coaching moments, playlists and scorecards. A capability area of the single published Chorus API contract.
  name: Chorus Recordings & Transcripts API
  slug: chorus-recordings-transcripts-api
- description: Run AI sales-qualification analysis on a recording and write the extracted framework fields back to a CRM opportunity. A capability area of the single published Chorus API contract, served at /api/v1/
  name: Chorus CRM Sync API
  slug: chorus-crm-sync-api
artifact_total: 12
asyncapis:
- description: ''
  name: Chorus Ai Webhooks
  slug: chorus-ai-webhooks
collections:
- collection_type: open
  name: Chorus API
  slug: open-chorus-ai
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/chorus-ai-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chorus-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.chorus.ai/
- group: commercial
  title: ''
  type: Plans
  url: plans/chorus-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/chorus-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/chorus-ai-finops.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/chorus-ai-openapi.yml
- group: docs
  title: ''
  type: Documentation
  url: https://chorus.ai/api-docs/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.chorus.ai/
- group: build
  title: ''
  type: Postman
  url: https://api-docs.chorus.ai/
- group: design
  title: ''
  type: Conventions
  url: conventions/chorus-ai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/chorus-ai-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/chorus-ai-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/chorus-ai-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/chorus-ai-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/chorus-ai-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zoominfo.com/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/chorus-ai-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/chorus-ai-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/chorus-ai-openapi-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/chorus-ai-packages.yml
- group: auth
  title: ''
  type: Security
  url: security/chorus-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/chorus-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/chorus-ai-trust-center.yml
- group: operate
  title: ''
  type: Support
  url: https://www.zoominfo.com/about/help-center
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zoominfo.com/products/chorus/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zoominfo.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zoominfo.com/legal/privacy-policy
created: '2026-05-08'
description: Chorus.ai is a conversation intelligence platform, acquired by ZoomInfo in 2021 and sold as "Chorus by ZoomInfo", that records, transcribes and analyzes customer-facing calls, meetings and emails to surface deal insights and coach sales reps. It publishes a single public REST contract — the Chorus API, an OpenAPI 3.0.3 document with 81 operations served unauthenticated at https://chorus.ai/api/openapi.json — covering engagement search, recording upload and media retrieval, coaching moments and playlists, scorecards, AI sales-qualification analysis with CRM writeback, and webhook registration. The API is JSON:API shaped on its /api/v1 surface with an older flat /v3 surface alongside it. Notably, the chorus.ai marketing site has been retired to a redirect shell pointing at zoominfo.com, but the API and both of its documentation surfaces remain live on the original domain.
finops:
- name: Chorus Ai Finops
  service_category: Sales
  slug: chorus-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chorus-ai.png
layout: provider
modified: '2026-08-13'
name: Chorus.ai
nav: Providers
network: true
overview: 'Chorus.ai publishes 3 APIs on the [APIs.io](https://apis.io/) network: Chorus Engagements API, Chorus Recordings & Transcripts API, and Chorus CRM Sync API. Tagged areas include Sales, Revenue Intelligence, Conversation, Analytics, and ZoomInfo.


  The Chorus.ai catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Chorus.ai''s developer surface includes authentication, documentation, API reference, support, pricing, and 24 more developer resources.'
plans:
- name: Chorus Ai Plans Pricing
  plan_count: 0
  slug: chorus-ai-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Chorus Ai Rate Limits
  slug: chorus-ai-rate-limits
score:
  band: developing
  composite: 49.0
  delta: -0.5
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 30.3
    contract_quality: 59.9
    developer_ergonomics: 33.9
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 34.2
  previous_composite: 49.5
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chorus-ai/refs/heads/main/screenshots/chorus-ai-2026-08-17T082957.png
security:
- kind: authentication
  name: Chorus Ai Authentication
  slug: chorus-ai-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Chorus Ai Domain Security
  slug: chorus-ai-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Chorus Ai Vulnerability Disclosure
  slug: chorus-ai-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Chorus Ai Trust Center
  slug: chorus-ai-trust-center
  summary_line: source, source_status, verified, quote, held, frameworks, explicitly_not_held
slug: chorus-ai
tags:
- Sales
- Revenue Intelligence
- Conversation
- Analytics
- ZoomInfo
- Conversation Intelligence
- Sales Enablement
- Call Recording
- Transcription
- Speech Analytics
- CRM
- Coaching
website: https://www.chorus.ai/
---
