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
    consent_identity: true
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.9
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Supernormal Agentic Access
  operation_count: 13
  slug: supernormal-agentic-access
  summary_line: 13 operations · 5 acting
api_count: 1
apis:
- baseURL: https://api.supernormal.com/api/v1
  baseurl_source: declared
  description: The Agent Sessions API from supernormal — 2 operation(s) for agent sessions.
  name: supernormal Agent Sessions API
  slug: supernormal-agent-sessions-api
- baseURL: https://api.supernormal.com/api/v1
  baseurl_source: declared
  description: Operations about agents
  name: supernormal Agents API
  slug: supernormal-agents-api
- baseURL: https://api.supernormal.com/api/v1
  baseurl_source: declared
  description: Operations about calendar
  name: supernormal Calendar Events API
  slug: supernormal-calendar-events-api
- baseURL: https://api.supernormal.com/api/v1
  baseurl_source: declared
  description: Operations about user
  name: supernormal Current User API
  slug: supernormal-current-user-api
- baseURL: https://api.supernormal.com/api/v1
  baseurl_source: declared
  description: Operations about posts
  name: supernormal Posts API
  slug: supernormal-posts-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Supernormal Agent Sessions API
  slug: open-supernormal-agent-sessions-api
- collection_type: open
  name: Supernormal Agent Sessions Agents API
  slug: open-supernormal-agents-api
- collection_type: open
  name: Supernormal Agent Sessions Calendar Events API
  slug: open-supernormal-calendar-events-api
- collection_type: open
  name: Supernormal Agent Sessions Current User API
  slug: open-supernormal-current-user-api
- collection_type: open
  name: Supernormal Agent Sessions Posts API
  slug: open-supernormal-posts-api
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/supernormal/refs/heads/main/agentic-access/supernormal-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/supernormal-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://supernormal.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.supernormal.com/api-reference/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://docs.supernormal.com/api-reference/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.supernormal.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.supernormal.com/api-reference/introduction
- group: start
  title: ''
  type: SignUp
  url: https://app.supernormal.com/settings
- group: operate
  title: ''
  type: Support
  url: https://help.supernormal.com/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.supernormal.com/en/
- group: operate
  title: ''
  type: StatusPage
  url: https://supernormal.statuspage.io/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/supernormal/refs/heads/main/llms/supernormal-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/supernormal-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/supernormal/refs/heads/main/mcp/supernormal-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/supernormal-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/supernormal/refs/heads/main/well-known/supernormal-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/supernormal-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/supernormal/refs/heads/main/well-known/supernormal-well-known.yml
  title: ''
  type: ContentSignal
  url: well-known/supernormal-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/supernormal/refs/heads/main/authentication/supernormal-authentication.yml
  title: ''
  type: Authentication
  url: authentication/supernormal-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/supernormal/refs/heads/main/scopes/supernormal-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/supernormal-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/supernormal/refs/heads/main/errors/supernormal-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/supernormal-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/supernormal/refs/heads/main/conventions/supernormal-conventions.yml
  title: ''
  type: Conventions
  url: conventions/supernormal-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/supernormal/refs/heads/main/lifecycle/supernormal-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/supernormal-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/supernormal/refs/heads/main/conformance/supernormal-conformance.yml
  title: ''
  type: Conformance
  url: conformance/supernormal-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/supernormal/refs/heads/main/data-model/supernormal-data-model.yml
  title: ''
  type: DataModel
  url: data-model/supernormal-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/supernormal/refs/heads/main/security/supernormal-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/supernormal-domain-security.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/supernormal/refs/heads/main/overlays/supernormal-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/supernormal-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/supernormal/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Supernormal is an AI meeting assistant and AI-agents platform (backed by Balderton Capital and EQT Ventures) that joins Google Meet, Zoom, and Microsoft Teams calls to capture, transcribe, and summarize meetings into shareable notes with action items. Beyond meeting notes, Supernormal offers configurable AI voice agents that can host or join calls, run surveys and screening interviews, and produce transcripts and structured posts. Its public REST API (https://api.supernormal.com/api/v1) exposes the current user, upcoming calendar events, meeting posts with notes and transcripts, agents, and agent sessions, authenticated with a scoped X-API-TOKEN API key. Supernormal additionally runs an OAuth 2.0 authorization server with dynamic client registration and PKCE, and a published, OAuth-protected Model Context Protocol (MCP) server so agents can access recordings and projects.
image: https://supernormal.com/og-card.png
layout: provider
modified: '2026-07-21'
name: supernormal
nav: Providers
network: true
overview: 'supernormal publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Agent Sessions API, Agents API, Calendar Events API, and 2 more. Tagged areas include Company, Meetings, Meeting Notes, Transcription, and AI Agents.


  supernormal''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, authentication, and 18 more developer resources.'
random_paper: 20
scopes:
- name: Supernormal Scopes
  scope_count: 11
  slug: supernormal-scopes
  summary_line: 11 scopes
score:
  band: thin
  composite: 35.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.4
  facets:
    access_clarity: 13.2
    contract_governance: 4.5
    contract_quality: 43.6
    developer_ergonomics: 56.5
    discoverability: 75.0
    operational_transparency: 15.8
  previous_composite: 35.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/supernormal/refs/heads/main/screenshots/supernormal-2026-09-02T161245.png
security:
- kind: authentication
  name: Supernormal Authentication
  slug: supernormal-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Supernormal Domain Security
  slug: supernormal-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: supernormal
tags:
- Company
- Meetings
- Meeting Notes
- Transcription
- AI Agents
- Voice Agents
- Productivity
- Collaboration
- MCP
- REST API
website: https://supernormal.com/
---
