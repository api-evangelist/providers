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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Tl Dv Agentic Access
  operation_count: 8
  slug: tl-dv-agentic-access
  summary_line: 8 operations · 1 acting
api_count: 1
apis:
- description: List, retrieve, import and download meetings
  name: tl;dv Meetings API
  slug: tl-dv-meetings-api
- description: Retrieve AI-generated meeting notes
  name: tl;dv Notes API
  slug: tl-dv-notes-api
- description: Service health
  name: tl;dv System API
  slug: tl-dv-system-api
- description: Retrieve meeting transcripts
  name: tl;dv Transcripts API
  slug: tl-dv-transcripts-api
artifact_total: 18
asyncapis:
- description: Webhook events delivered by tl;dv when a meeting finishes processing or a transcript becomes available. Webhooks are configurable at user, team or organization level.
  name: tl;dv Webhooks
  slug: tl-dv-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: tl;dv Meetings API
  slug: open-tl-dv-meetings-api
- collection_type: open
  name: tl;dv Meetings Notes API
  slug: open-tl-dv-notes-api
- collection_type: open
  name: tl;dv Meetings System API
  slug: open-tl-dv-system-api
- collection_type: open
  name: tl;dv Meetings Transcripts API
  slug: open-tl-dv-transcripts-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tl-dv-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/tl-dv-import-and-retrieve.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tl-dv-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/tl-dv-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://tldv.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://doc.tldv.io
- group: docs
  title: ''
  type: Documentation
  url: https://doc.tldv.io
- group: docs
  title: ''
  type: APIReference
  url: https://doc.tldv.io
- group: start
  title: ''
  type: GettingStarted
  url: https://doc.tldv.io
- group: company
  title: ''
  type: Blog
  url: https://tldv.io/blog/
- group: operate
  title: ''
  type: Support
  url: https://intercom.help/tldv/en
- group: commercial
  title: ''
  type: Pricing
  url: https://tldv.io/app/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://tldv.io/app/signup
- group: start
  title: ''
  type: Login
  url: https://tldv.io/app/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tldv.io/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tldv.io/privacy/
- group: auth
  title: ''
  type: Security
  url: https://tldv.io/features/security-commitment/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.tldv.io/
- group: auth
  title: ''
  type: Compliance
  url: https://tldv.io/features/security-commitment/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tl-dv-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tl-dv-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tl-dv-well-known.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/tl-dv-tool-crosswalk.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tl-dv-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/tl-dv-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tl-dv-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tl-dv-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/tl-dv-pull-meeting-intelligence.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tldv-public
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/tldv-public/tldv-mcp-server
created: '2026-07-17'
description: tl;dv is an AI meeting notetaker for Zoom, Google Meet and Microsoft Teams that automatically records, transcribes and summarizes meetings in 30+ languages and syncs the resulting insights into CRMs and productivity tools. Its public API (base URL https://pasta.tldv.io, version v1alpha1) gives developers programmatic access to meetings, speaker-attributed transcripts and AI-generated notes, plus meeting import from a URL and webhook delivery of MeetingReady and TranscriptReady events. Authentication is via an x-api-key header issued from account settings, and API access requires a Business or Enterprise plan. tl;dv also ships an official Model Context Protocol server — an open-source stdio build at github.com/tldv-public/tldv-mcp-server exposing four read tools, plus a live OAuth-protected hosted endpoint at https://mcp.tldv.io/mcp — making meetings, transcripts and highlights callable directly by AI agents.
image: https://api.tldv.io/assets/images/logo_login.png
layout: provider
mcp_servers:
- description: ''
  name: tl;dv MCP Server
  slug: tldv-mcp-server
modified: '2026-08-14'
name: tl;dv
nav: Providers
network: true
overview: 'tl;dv publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Meetings API, Notes API, System API, and 1 more. Tagged areas include Company, Artificial Intelligence, Meetings, Transcription, and Note Taking.


  The tl;dv catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  tl;dv''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 23 more developer resources.'
plans:
- name: Tl Dv Plans Pricing
  plan_count: 5
  slug: tl-dv-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Tl Dv Rate Limits
  slug: tl-dv-rate-limits
scopes:
- name: Tl Dv Scopes
  scope_count: 1
  slug: tl-dv-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 46.5
  coverage:
    artifact_dirs: 22
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 4.5
    contract_quality: 21.6
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 21.1
  previous_composite: 46.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tl-dv/refs/heads/main/screenshots/tl-dv-2026-08-17T082359.png
security:
- kind: authentication
  name: Tl Dv Authentication
  slug: tl-dv-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Tl Dv Domain Security
  slug: tl-dv-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Tl Dv Trust Center
  slug: tl-dv-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: tl-dv
tags:
- Company
- Artificial Intelligence
- Meetings
- Transcription
- Note Taking
- Conversation Intelligence
- Productivity
- Video
- Webhook
website: https://tldv.io
---
