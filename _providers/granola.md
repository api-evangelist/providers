---
access_model:
  confidence: medium
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Granola Agentic Access
  operation_count: 2
  slug: granola-agentic-access
  summary_line: 2 operations
api_count: 1
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
- baseURL: https://www.granola.ai
  baseurl_source: declared
  description: The Notes API from Granola — 2 operation(s) for notes.
  name: Granola Notes API
  slug: granola-notes-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Granola Public Notes API
  slug: open-granola-notes-api
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
overview: 'Granola publishes 1 API on the [APIs.io](https://apis.io/) network: Notes API. Tagged areas include Artificial Intelligence, Meeting Notes, Transcription, Productivity, and MCP.


  Granola''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Granola Plans Pricing
  plan_count: 1
  slug: granola-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 2
  name: Granola Rate Limits
  slug: granola-rate-limits
score:
  band: thin
  composite: 35.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 56.0
    catalog_earned_first_party: 0.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 54.4
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 35.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
- Artificial Intelligence
- Meeting Notes
- Transcription
- Productivity
- MCP
- Zapier
- Business
- Enterprise
website: https://www.granola.ai/
---
