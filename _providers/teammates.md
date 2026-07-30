---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.7
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Teammates Agentic Access
  operation_count: 2
  slug: teammates-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 2
apis:
- description: The Assign API from Teammates — 1 operation(s) for assign.
  name: Teammates Assign API
  slug: teammates-assign-api
- description: The Assignment API from Teammates — 1 operation(s) for assignment.
  name: Teammates Assignment API
  slug: teammates-assignment-api
artifact_total: 6
asyncapis:
- description: ''
  name: Teammates Webhooks
  slug: teammates-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://teammates.work
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.teammates.work/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.teammates.work/capabilities/smart-tools
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.teammates.work/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.teammates.work/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.teammates.work/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.teammates.work/public/create-a-teammate
- group: start
  title: ''
  type: Login
  url: https://app.teammates.work/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.teammates.work/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.teammates.work/privacy-policy
- group: operate
  title: ''
  type: Support
  url: mailto:support@teammates.work
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/teammates-work
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.teammates.work/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/teammates_work
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/teammates-work/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/teammates-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/teammates-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/teammates-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/teammates-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/teammates-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/teammates-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/teammates-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/teammates-agentic-access.yml
created: '2026-07-17'
description: Teammates ("AI that works") is Super Duper Labs' end-to-end platform for designing and managing a virtual AI workforce. Companies create AI teammates that autonomously execute natural-language assignments across the SaaS tools their human teams already use — Salesforce, GitHub, Gmail, Slack, Google Workspace, Microsoft 365, Jira, HubSpot and more — through Smart Tools connections, reusable skills, event-driven rules and triggers, a secure password manager, and human-in-the-loop escalation. The public SmartTools API (api.teammates.work/v1) lets developers enqueue assignments against a named tool with a natural-language prompt and retrieve results by polling or webhook. Usage-based pricing (Team / Business / Enterprise). Backed by Matrix Partners.
image: https://cdn.prod.website-files.com/66f1c713e9cce059a0faaf67/683bb044870f2478d1e2f664_page-cover-default.jpg
layout: provider
mcp_servers:
- description: ''
  name: teammates-mcp.yml
  slug: teammates-mcpyml
modified: '2026-07-21'
name: Teammates
nav: Providers
network: true
overview: 'Teammates publishes 2 APIs on the [APIs.io](https://apis.io/) network: Assign API and Assignment API. Tagged areas include Company, B2B, Artificial Intelligence, AI Agents, and Virtual Workforce.


  The Teammates catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Teammates'' developer surface includes documentation, getting-started guide, engineering blog, pricing, signup flow, support, changelog, and 17 more developer resources.'
random_paper: 59
score:
  band: developing
  composite: 45.2
  delta: -2.3
  facets:
    commercial_clarity: 52.6
    contract_quality: 54.2
    developer_ergonomics: 38.6
    discoverability: 87.0
    governance: 8.3
    operational_transparency: 28.9
  previous_composite: 47.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Teammates Domain Security
  slug: teammates-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: teammates
tags:
- Company
- B2B
- Artificial Intelligence
- AI Agents
- Virtual Workforce
- Automation
- Productivity
- SaaS
- MCP
website: https://teammates.work
---
