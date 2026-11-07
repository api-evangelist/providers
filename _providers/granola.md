---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 54.8
  scored_at: '2026-11-06'
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
- baseURL: https://public-api.granola.ai/v1
  baseurl_source: declared
  description: Lease, acknowledge, and release inbox messages
  name: Granola Inbox Messages API
  slug: granola-inbox-messages-api
- baseURL: https://public-api.granola.ai/v1
  baseurl_source: declared
  description: Create and manage trigger inboxes
  name: Granola Inboxes API
  slug: granola-inboxes-api
- baseURL: https://public-api.granola.ai/v1
  baseurl_source: declared
  description: The Trigger Inbox API API from Granola — 0 operation(s) for trigger inbox api.
  name: Granola Trigger Inbox API
  slug: granola-trigger-inbox-api-api
artifact_total: 18
collections:
- collection_type: open
  name: Granola Public Notes API
  slug: open-granola-notes-api
- collection_type: open
  name: Granola Public API
  slug: open-granola
common:
- group: agent
  href: https://artifacts.apis.io/granola/agentic-access/granola-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/granola-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/granola/security/granola-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/granola-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/granola/security/granola-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/granola-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/granola/security/granola-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/granola-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/granola/authentication/granola-authentication.yml
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
  href: https://artifacts.apis.io/granola/plans/granola-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/granola-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/granola/rate-limits/granola-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/granola-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/granola/finops/granola-finops.yml
  title: ''
  type: FinOps
  url: finops/granola-finops.yml
created: '2026-05-23'
description: Granola is an AI notepad for back-to-back meetings. It captures audio directly from the user's computer (no meeting bot), enhances handwritten notes with AI, and supports post-meeting tasks like follow-up drafting, action item extraction, and chat over the transcript. Works across Zoom, Google Meet, Webex, Microsoft Teams, and Slack. Granola exposes a public Granola API (Business and Enterprise plans) for programmatic access to notes, transcripts, and folders, plus an MCP server for conversational AI clients. Webhooks are on the roadmap; Zapier covers event-style automation today.
finops:
- has_sources: false
  method: generated
  name: Granola Finops
  primary_unit: ''
  service_category: API
  slug: granola-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/granola.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.granola.ai over HTTP.
  name: Granola MCP Server
  slug: granola
modified: '2026-05-23'
name: Granola
nav: Providers
network: true
overview: 'Granola publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Inbox Messages API, Inboxes API, Trigger Inbox API, and 3 more. Tagged areas include Artificial Intelligence, Meeting Notes, Transcription, Productivity, and MCP.


  The Granola catalog on APIs.io includes 1 Spectral governance ruleset.


  Granola''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Granola Plans Pricing
  plan_count: 1
  slug: granola-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 2
  name: Granola Rate Limits
  slug: granola-rate-limits
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: Granola API Rules
  rule_count: 62
  severity_counts:
    error: 55
    hint: 0
    info: 1
    warn: 6
  slug: granola-rules
score:
  band: thin
  composite: 32.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 40.5
    catalog_earned_first_party: 0.0
    catalog_gap: 74.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 13.2
    contract_governance: 13.6
    contract_quality: 59.7
    developer_ergonomics: 23.8
    discoverability: 60.0
    operational_transparency: 15.8
  previous_composite: 31.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 40.0
      total: 5
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/granola/granola-2026-06-20T182324.png
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
