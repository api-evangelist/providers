---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Granola Agentic Access
  operation_count: 2
  slug: granola-agentic-access
  summary_line: 2 operations
api_count: 4
apis:
- description: Consumer desktop app (macOS / Windows) and iPhone app that records meeting audio locally, enhances notes with AI, and supports customizable templates for different meeting types.
  name: Granola Desktop & Mobile App
  slug: desktop-app
- description: REST API for programmatic access to meeting notes, transcripts, AI summaries, and folders. Authentication is Bearer token using API keys prefixed with `grn_`, created in Settings → Connectors → API ke
  name: Granola Public API
  slug: public-api
- description: Zapier integration for event-style automation connecting Granola to 8,000+ apps. Useful for webhook-like patterns until Granola ships native webhooks.
  name: Granola Zapier Integration
  slug: zapier
- description: The Notes API from Granola — 2 operation(s) for notes.
  name: Granola Notes API
  slug: granola-notes-api
artifact_total: 13
collections:
- collection_type: open
  name: Granola Public API
  slug: open-granola
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/granola-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/granola-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/granola-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/granola-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/granola-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/granola-ai
- group: company
  title: ''
  type: Website
  url: https://www.granola.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.granola.ai/introduction
- group: docs
  title: ''
  type: APIDocs
  url: https://docs.granola.ai/help-center/sharing/integrations/granola-api
- group: company
  title: ''
  type: Blog
  url: https://www.granola.ai/blog
- group: commercial
  title: ''
  type: Plans
  url: plans/granola-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/granola-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/granola-finops.yml
created: '2026-05-23'
description: Granola is an AI notepad for back-to-back meetings. It captures audio directly from the user's computer (no meeting bot), enhances handwritten notes with AI, and supports post-meeting tasks like follow-up drafting, action item extraction, and chat over the transcript. Works across Zoom, Google Meet, Webex, Microsoft Teams, and Slack. Granola exposes a public Granola API (Business and Enterprise plans) for programmatic access to notes, transcripts, and folders, plus an MCP server for conversational AI clients. Webhooks are on the roadmap; Zapier covers event-style automation today.
finops:
- name: Granola Finops
  service_category: API
  slug: granola-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/granola.png
layout: provider
modified: '2026-05-23'
name: Granola
nav: Providers
network: true
overview: 'Granola publishes 1 API on the [APIs.io](https://apis.io/) network: Notes API. Tagged areas include AI, Meeting Notes, Transcription, Productivity, and API.


  Granola''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Granola Plans Pricing
  plan_count: 1
  slug: granola-plans-pricing
random_paper: 75
rate_limits:
- limit_count: 2
  name: Granola Rate Limits
  slug: granola-rate-limits
score:
  band: thin
  composite: 37.4
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 62.0
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/granola/refs/heads/main/screenshots/granola-2026-06-20T182324.png
security:
- kind: authentication
  name: Granola Authentication
  slug: granola-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Granola Domain Security
  slug: granola-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Granola Vulnerability Disclosure
  slug: granola-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Granola Trust Center
  slug: granola-trust-center
  summary_line: SOC 2, GDPR
slug: granola
tags:
- AI
- Meeting Notes
- Transcription
- Productivity
- API
- MCP
- Zapier
- Business
- Enterprise
website: https://www.granola.ai/
---
