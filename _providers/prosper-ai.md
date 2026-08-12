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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.4
  scored_at: '2026-08-11'
api_count: 6
apis:
- description: The API Keys API from Prosper AI — 1 operation(s) for api keys.
  name: Prosper AI API Keys API
  slug: prosper-ai-api-keys-api
- description: The Call Logs API from Prosper AI — 2 operation(s) for call logs.
  name: Prosper AI Call Logs API
  slug: prosper-ai-call-logs-api
- description: The Campaigns API from Prosper AI — 7 operation(s) for campaigns.
  name: Prosper AI Campaigns API
  slug: prosper-ai-campaigns-api
- description: The Live Calls API from Prosper AI — 1 operation(s) for live calls.
  name: Prosper AI Live Calls API
  slug: prosper-ai-live-calls-api
- description: The Status API from Prosper AI — 1 operation(s) for status.
  name: Prosper AI Status API
  slug: prosper-ai-status-api
- description: The Targets API from Prosper AI — 1 operation(s) for targets.
  name: Prosper AI Targets API
  slug: prosper-ai-targets-api
artifact_total: 10
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/prosper-ai-voice-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prosper-ai-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform.getprosperapp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getprosperapp.com/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.getprosperapp.com/api-reference/call-logs/list-call-logs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.getprosperapp.com/quickstart/campaign-call
- group: agent
  title: ''
  type: MCPServer
  url: mcp/prosper-ai-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/prosper-ai-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/prosper-ai-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/prosper-ai-authentication.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/prosper-ai-conformance.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.getprosper.ai/get-started
- group: start
  title: ''
  type: Login
  url: https://platform.getprosperapp.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getprosper.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getprosper.ai/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.getprosper.ai/blog
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.getprosper.ai/faq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/prospertechnologies
created: '2026-07-17'
description: 'Prosper AI is an AI-native voice automation platform for healthcare operations, founded in 2023 and backed by Andreessen Horowitz (a16z), Emergence Capital, Base10, Company Ventures and Y Combinator. Prosper runs the voice-heavy work of clinic and revenue-cycle operations end-to-end: answering and placing patient phone calls, appointment scheduling directly into the EHR, insurance eligibility and benefits verification, prior authorization, and patient billing follow-up. The platform integrates with 80+ EHR, practice-management and clearinghouse systems (Epic, athenahealth, Cerner, MEDITECH, NextGen, Nextech, Allscripts/Altera, Availity, Healthie). Prosper exposes a public REST API (Prosper Voice, /api/v1) for driving campaigns, targets, live calls and call-log export, plus a hosted, OAuth-protected Model Context Protocol (MCP) server for agent access. Prosper is HIPAA compliant and SOC 2 Type II attested and signs Business Associate Agreements.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/prosper-ai.png
layout: provider
mcp_servers:
- description: ''
  name: prosper-ai-mcp.yml
  slug: prosper-ai-mcpyml
modified: '2026-07-20'
name: Prosper AI
nav: Providers
network: true
overview: 'Prosper AI publishes 6 APIs on the [APIs.io](https://apis.io/) network, including API Keys API, Call Logs API, Campaigns API, and 3 more. Tagged areas include Company, Healthcare, Voice AI, Revenue Cycle Management, and Patient Access.


  Prosper AI''s developer surface includes documentation, API reference, getting-started guide, authentication, signup flow, engineering blog, and 13 more developer resources.'
random_paper: 98
scopes:
- name: Prosper Ai Scopes
  scope_count: 1
  slug: prosper-ai-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 45.4
  delta: -0.3
  facets:
    commercial_clarity: 42.1
    contract_quality: 45.8
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 0.0
  previous_composite: 45.7
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Prosper Ai Authentication
  slug: prosper-ai-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Prosper Ai Domain Security
  slug: prosper-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: prosper-ai
tags:
- Company
- Healthcare
- Voice AI
- Revenue Cycle Management
- Patient Access
- EHR Integration
- AI Agents
- MCP
website: https://platform.getprosperapp.com/
---
