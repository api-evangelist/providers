---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 29.7
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: The authenticated backend for the Pavoot AI event platform. A FastAPI service publishing a complete OpenAPI 3.1.0 document at https://api.pavoot.com/openapi.json covering 248 operations and 56 request
  name: Pavoot Application API
  slug: pavoot-application-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pavoot-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/pavoot-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pavoot.com/client/gtc
- group: start
  title: ''
  type: Login
  url: https://app.pavoot.com/
- group: company
  title: ''
  type: Website
  url: https://pavoot.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pavoot.com/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:hello@pavoot.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pavoot-llms.txt
created: '2026-07-17'
description: Pavoot is a Y Combinator-backed AI event-management platform that operates as an autonomous AI agent for running events end-to-end. It sources and matches the right attendees, personalizes invitations, captures and checks in guests on-site, automatically follows up with context from each interaction, tags event media (photos, faces, and logos) with AI, and attributes the resulting pipeline and ROI. The product targets field marketers, GTM leaders, sales teams, CMO/VP Marketing roles, and founders who want to turn events into pipeline. Pavoot runs no developer program — it issues no API keys, publishes no developer documentation and ships no SDKs — but its application backend at api.pavoot.com does serve a complete, publicly readable OpenAPI 3.1.0 describing 248 operations across event projects, media upload and AI tagging, face and person identity resolution, sponsor brand and logo recognition, attendee registration and follow-up email, gallery sharing, and organization permissions,
  together with FastAPI Swagger UI and ReDoc. The API itself is authenticated with Clerk-issued session tokens against Pavoot's own OAuth 2.0 / OpenID Connect authorization server at clerk.pavoot.com, so the contract is observable but not consumable by third parties.
image: https://pavoot.com/og/pavoot-home.jpg
layout: provider
modified: '2026-08-13'
name: Pavoot
nav: Providers
network: true
overview: 'Pavoot publishes 1 API on the [APIs.io](https://apis.io/) network: Application API. Tagged areas include Company, Event, Event Management, Marketing, and AI Agent.


  Pavoot''s developer surface includes support and 8 more developer resources.'
plans:
- name: Pavoot Plans Pricing
  plan_count: 0
  slug: pavoot-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Pavoot Rate Limits
  slug: pavoot-rate-limits
scopes:
- name: Pavoot Scopes
  scope_count: 0
  slug: pavoot-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.8
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 16.7
    contract_quality: 45.0
    developer_ergonomics: 6.5
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 28.8
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pavoot/refs/heads/main/screenshots/pavoot-2026-08-07T191608.png
security:
- kind: authentication
  name: Pavoot Authentication
  slug: pavoot-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Pavoot Domain Security
  slug: pavoot-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pavoot
tags:
- Company
- Event
- Event Management
- Marketing
- AI Agent
- Attendee Intelligence
- Go-To-Market
- Field Marketing
- Pipeline
website: https://pavoot.com
---
