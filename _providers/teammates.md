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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Teammates Agentic Access
  operation_count: 2
  slug: teammates-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.teammates.work/v1
  baseurl_source: declared
  description: The Assign API from Teammates — 1 operation(s) for assign.
  name: Teammates Assign API
  slug: teammates-assign-api
- baseURL: https://api.teammates.work/v1
  baseurl_source: declared
  description: The Assignment API from Teammates — 1 operation(s) for assignment.
  name: Teammates Assignment API
  slug: teammates-assignment-api
artifact_total: 8
asyncapis:
- description: ''
  name: Teammates Webhooks
  slug: teammates-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Teammates SmartTools Assign API
  slug: open-teammates-assign-api
- collection_type: open
  name: Teammates SmartTools Assign Assignment API
  slug: open-teammates-assignment-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/teammates-smarttools-overlay.yaml
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
  type: X-MCPServerCandidate
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
modified: '2026-07-21'
name: Teammates
nav: Providers
network: true
overview: 'Teammates publishes 2 APIs on the [APIs.io](https://apis.io/) network: Assign API and Assignment API. Tagged areas include Company, B2B, Artificial Intelligence, AI Agents, and Virtual Workforce.


  The Teammates catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Teammates'' developer surface includes documentation, getting-started guide, engineering blog, pricing, signup flow, support, changelog, and 18 more developer resources.'
random_paper: 16
score:
  band: thin
  composite: 38.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 50.3
    developer_ergonomics: 45.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 38.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/teammates/refs/heads/main/screenshots/teammates-2026-08-17T082257.png
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
- Software-as-a-Service
- MCP
website: https://teammates.work
---
