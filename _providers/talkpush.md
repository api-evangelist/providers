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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.7
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Talkpush Agentic Access
  operation_count: 44
  slug: talkpush-agentic-access
  summary_line: 44 operations · 23 acting
api_count: 14
apis:
- description: Collection of endpoints related to AI Agents (SmartCall Settings). Agents are configurable AI-powered voice/interview agents that can be linked to campaigns, question sets, and candidate attribute ext
  name: TalkPush Agents API API
  slug: talkpush-agents-api-api
- description: Collection of endpoints related to calls data
  name: TalkPush Calls API API
  slug: talkpush-calls-api-api
- description: Collection of endpoints related to Talkpush Campaigns
  name: TalkPush Campaigns API API
  slug: talkpush-campaigns-api-api
- description: List and create candidate (lead) custom attribute definitions at the company level. Definitions appear in the recruiter UI and can be written on leads via the `others` field using the attribute key. B
  name: TalkPush Candidate Attributes API API
  slug: talkpush-candidate-attributes-api-api
- description: Collection of endpoints related to Document Tags (Templates)
  name: TalkPush Document Tags API API
  slug: talkpush-document-tags-api-api
- description: Collection of endpoints related to folders
  name: TalkPush Folders API API
  slug: talkpush-folders-api-api
- description: 'Collection of endpoints related to candidate labels. Labels are simple, company-wide tags that recruiters use to flag and filter candidates (for example: "Priority", "Referral", "Needs Review"). The s'
  name: TalkPush Labels API API
  slug: talkpush-labels-api-api
- description: Collection of endpoints related to leads management
  name: TalkPush Leads API API
  slug: talkpush-leads-api-api
- description: 'Endpoint for listing the company''s managers (platform users with role-based permissions). Use the returned IDs to discover valid managers before assigning them to campaign permissions, targeting them '
  name: TalkPush Managers API API
  slug: talkpush-managers-api-api
- description: Endpoints for managing Message Templates — the structured, token-based messages used by autoflows and integrations for standardised communications (interview invitations, rejection notices, offer lett
  name: TalkPush Message Templates API API
  slug: talkpush-message-templates-api-api
- description: Collection of endpoints related to sending messages
  name: TalkPush Messaging API API
  slug: talkpush-messaging-api-api
- description: Endpoint for listing the company's candidate movement reasons — the configurable Shortlist Reasons and Reject Reasons that recruiters select when shortlisting or rejecting a candidate. Use these IDs/n
  name: TalkPush Movement Reasons API API
  slug: talkpush-movement-reasons-api-api
- description: Collection of endpoints related to RMS Integration
  name: TalkPush Requisition Management System API
  slug: talkpush-requisition-management-system-api
- description: 'Endpoint for discovering the message tokens available for use inside Message Templates. Returns both system-level reserved tokens (e.g. `candidate_name`, `job_title`) and any custom tokens configured '
  name: TalkPush Tokens API API
  slug: talkpush-tokens-api-api
artifact_total: 18
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/talkpush-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/talkpush-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.talkpush.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.talkpush.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.talkpush.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.talkpush.com/reference/get_campaigns
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.talkpush.com/docs/getting-started
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/talkpush-llms.txt
- group: operate
  title: ''
  type: Support
  url: https://help.talkpush.com/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.talkpush.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.talkpush.com/talkpush-blog-all
- group: commercial
  title: ''
  type: Pricing
  url: https://www.talkpush.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://talkpush.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://talkpush.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/talkpush
- group: auth
  title: ''
  type: Authentication
  url: authentication/talkpush-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/talkpush-mcp.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/talkpush-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/talkpush-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/talkpush-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/talkpush-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'TalkPush is a conversational recruiting and recruitment-automation CRM that helps high-volume employers source, screen, and engage job candidates across messaging channels (WhatsApp, SMS, Messenger, email) and AI voice agents. Its public REST API — the Talkpush API v2.0 — lets you plug external lead sources and HR/ATS technology into the platform: create and search leads (campaign invitations), manage recruiting campaigns and folders, run and complete interviews, send quick-reply and message templates, configure AI calling agents, and manage company labels, candidate attributes, movement reasons, and managers. Authentication is via an api_key query parameter, and the docs are published on a ReadMe developer hub with an llms.txt index for AI agents. Surfaced as a Seedcamp portfolio company and enriched by the API Evangelist pipeline from TalkPush''s own published developer documentation.'
image: https://files.readme.io/2a5f3f7-small-logov1.png
layout: provider
mcp_servers:
- description: ''
  name: talkpush-mcp.yml
  slug: talkpush-mcpyml
modified: '2026-07-21'
name: TalkPush
nav: Providers
network: true
overview: 'TalkPush publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Agents API API, Calls API API, Campaigns API API, and 11 more. Tagged areas include Company, Recruiting, Recruitment Automation, Human Resources, and Hiring.


  TalkPush''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 15 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 39.8
  delta: -3.4
  facets:
    commercial_clarity: 31.6
    contract_quality: 52.0
    developer_ergonomics: 56.0
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 43.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 34.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Talkpush Authentication
  slug: talkpush-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Talkpush Domain Security
  slug: talkpush-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: talkpush
tags:
- Company
- Recruiting
- Recruitment Automation
- Human Resources
- Hiring
- Applicant Tracking
- Conversational AI
- Messaging
- CRM
website: https://www.talkpush.com
---
