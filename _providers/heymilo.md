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
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 58.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Heymilo Agentic Access
  operation_count: 56
  slug: heymilo-agentic-access
  summary_line: 56 operations · 20 acting
api_count: 18
apis:
- description: The ATS API from HeyMilo — 4 operation(s) for ats.
  name: HeyMilo ATS API
  slug: heymilo-ats-api
- description: Ingest candidates into an interviewer's workflow (sync or async, single or bulk) and list candidates with their progress.
  name: HeyMilo Candidates API
  slug: heymilo-candidates-api
- description: View grouped design template configurations.
  name: HeyMilo Design Template Groups API
  slug: heymilo-design-template-groups-api
- description: View design templates that control the candidate interview UI.
  name: HeyMilo Design Templates API
  slug: heymilo-design-templates-api
- description: Manage custom domains for white-labelled interview URLs.
  name: HeyMilo Domains API
  slug: heymilo-domains-api
- description: View grouped email template configurations.
  name: HeyMilo Email Template Groups API
  slug: heymilo-email-template-groups-api
- description: View email templates configured for candidate outreach.
  name: HeyMilo Email Templates API
  slug: heymilo-email-templates-api
- description: The Health API from HeyMilo — 1 operation(s) for health.
  name: HeyMilo Health API
  slug: heymilo-health-api
- description: View interview templates, reusable agent configurations cloned from a blueprint posting (workflow, questions, criteria, agent settings).
  name: HeyMilo Interview Templates API
  slug: heymilo-interview-templates-api
- description: Create, read, update, and manage interviewers. An interviewer (posting) combines job details with an AI agent configuration and agentic workflow.
  name: HeyMilo Interviewers API
  slug: heymilo-interviewers-api
- description: Retrieve full interview results (scorecard, transcript, resume evaluation) and manage per-interview metadata.
  name: HeyMilo Interviews API
  slug: heymilo-interviews-api
- description: List provisioned phone numbers for SMS and voice agents.
  name: HeyMilo Phone Numbers API
  slug: heymilo-phone-numbers-api
- description: 'Create, read, update, delete, and reorder questions and criteria for an interviewer''s workflow. Covers all modalities: voice, sms, form, resume_eligibility, resume_scoring, and voice_tags.'
  name: HeyMilo Questions API
  slug: heymilo-questions-api
- description: The Schema Discovery API from HeyMilo — 2 operation(s) for schema discovery.
  name: HeyMilo Schema Discovery API
  slug: heymilo-schema-discovery-api
- description: Manage sender email addresses used for candidate communications.
  name: HeyMilo Sender Emails API
  slug: heymilo-sender-emails-api
- description: Browse the workspace voice registry for AI interviewer voices.
  name: HeyMilo Voices API
  slug: heymilo-voices-api
- description: Register, list, and manage webhook endpoints that receive real-time event notifications.
  name: HeyMilo Webhooks API
  slug: heymilo-webhooks-api
- description: List the workspaces accessible to the authenticated caller. API-key callers receive a single entry; OAuth callers receive every workspace they are a member of.
  name: HeyMilo Workspaces API
  slug: heymilo-workspaces-api
artifact_total: 25
asyncapis:
- description: HeyMilo delivers real-time HTTP notifications across the candidate interview lifecycle. Register a webhook via the Public REST API (POST /api/v2/webhooks) with a destination URL, an event_type, and th
  name: HeyMilo Webhooks
  slug: heymilo-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/heymilo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/heymilo-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.heymilo.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.heymilo.ai/documentation/get-started/landing
- group: docs
  title: ''
  type: APIReference
  url: https://docs.heymilo.ai/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.heymilo.ai/documentation/get-started/what-is-heymilo
- group: company
  title: ''
  type: Website
  url: https://www.heymilo.ai
- group: start
  title: ''
  type: SignUp
  url: https://www.heymilo.ai/book-a-demo
- group: company
  title: ''
  type: Blog
  url: https://www.heymilo.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://docs.heymilo.ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/heymilo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.heymilo.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.heymilo.ai/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.heymilo.ai
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.heymilo.ai
- group: auth
  title: ''
  type: Compliance
  url: https://trust.warden-ai.com/heymilo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/heymilo/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/heymilo-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/heymilo-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/heymilo-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/heymilo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/heymilo-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/heymilo-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/heymilo-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/heymilo-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/heymilo-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/heymilo-webhooks.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/heymilo-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/heymilo-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/heymilo-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/heymilo-openapi-overlay.yaml
created: '2026-07-17'
description: HeyMilo AI is an agentic recruiting platform for high-volume hiring teams — staffing agencies, corporate recruiters, BPOs, franchises, and data-annotation operations. It combines candidate sourcing from your ATS, conversational SMS and smart-form pre-screening, resume analysis, and live AI voice and video interviews (with built-in cheat detection), then scores and ranks candidates with analytics, reporting, and fully white-labeled workflows. The HeyMilo Public API (v2.0.0, base https://api.heymilo.ai) exposes programmatic control over interviewers (postings), candidate ingestion, interview data and transcripts, questions, webhooks, templates, voices, phone numbers, domains, and ATS push/resolve — authenticated with an X-API-KEY header and rate limited to 300 requests per minute. A read-only hosted MCP server at https://mcp.heymilo.ai/mcp lets any MCP client query candidates, jobs, and interviews in natural language. HeyMilo raised $6M to scale agentic recruiting and is backed
  by Canaan Partners.
image: https://www.heymilo.ai/images/og-default.png
layout: provider
mcp_servers:
- description: ''
  name: heymilo-mcp.yml
  slug: heymilo-mcpyml
modified: '2026-07-19'
name: HeyMilo
nav: Providers
network: true
overview: 'HeyMilo publishes 18 APIs on the [APIs.io](https://apis.io/) network, including ATS API, Candidates API, Design Template Groups API, and 15 more. Tagged areas include Company, Recruiting, Hiring, Human Resources, and HR Tech.


  The HeyMilo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  HeyMilo''s developer surface includes documentation, API reference, getting-started guide, signup flow, engineering blog, support, authentication, and 25 more developer resources.'
random_paper: 48
rate_limits:
- limit_count: 1
  name: Heymilo Rate Limits
  slug: heymilo-rate-limits
score:
  band: strong
  composite: 57.7
  delta: 0.4
  facets:
    commercial_clarity: 50.0
    contract_quality: 67.7
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 50.0
  previous_composite: 57.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/heymilo/refs/heads/main/screenshots/heymilo-2026-07-25T221122.png
security:
- kind: authentication
  name: Heymilo Authentication
  slug: heymilo-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Heymilo Domain Security
  slug: heymilo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Heymilo Trust Center
  slug: heymilo-trust-center
  summary_line: trust center published
slug: heymilo
tags:
- Company
- Recruiting
- Hiring
- Human Resources
- HR Tech
- Artificial Intelligence
- AI Agents
- Interviewing
- Candidate Screening
- Voice AI
- Webhooks
- ATS Integration
website: https://www.heymilo.ai
---
