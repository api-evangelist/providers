---
access_model:
  confidence: high
  label: Paid per-seat subscription with a free trial; no free tier
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - https://docs.lindy.ai/pricing
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.4
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Lindy's callable surface. There is no public REST API and no published OpenAPI. The one documented HTTP endpoint is an inbound webhook trigger at https://public.lindy.ai/api/v1/webhooks/[unique-id], a
  name: Lindy
  slug: lindy
artifact_total: 10
asyncapis:
- description: ''
  name: Lindy Webhooks
  slug: lindy-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.lindy.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lindy.ai
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lindy.ai/start-here/quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.lindy.ai/blog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/lindy-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lindy.ai/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lindy-lifecycle.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lindy.ai/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/lindy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lindy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lindy-finops.yml
- group: start
  title: ''
  type: SignUp
  url: https://chat.lindy.ai/signup
- group: start
  title: ''
  type: Login
  url: https://chat.lindy.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lindy.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lindy.ai/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:support@lindy.ai
- group: auth
  title: ''
  type: Security
  url: https://www.lindy.ai/security
- group: auth
  title: ''
  type: Compliance
  url: https://www.lindy.ai/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lindy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/lindy-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lindy-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lindy-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lindy-conventions.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lindy-mcp.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/lindy-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lindy-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.lindy.ai/llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/lindy-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lindy-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/lindy-packages.yml
- group: design
  title: ''
  type: Components
  url: components/lindy-components.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lindy-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lindyai
created: '2026-03-27'
description: 'Lindy is an AI automation platform for building and running AI agents that do real work across a company''s tools. The current product, Lindy Teammate, lives in Slack and handles inbox triage and drafting, meeting recording, notes and scheduling, daily briefs and scheduled routines, backed by an agent builder that turns a natural-language prompt into a working agent and connects to thousands of third-party apps through OAuth integrations, stored credentials and any hosted MCP server. Lindy publishes no public REST API contract: its machine-readable surface is agent-native rather than contract-native — a live anonymous MCP server and a conformant A2A agent card on its documentation host, a published Agent Skill, llms.txt on two hosts, and a single bearer-authenticated inbound webhook endpoint that triggers an agent workflow.'
finops:
- name: Lindy Finops
  service_category: API
  slug: lindy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lindy.png
layout: provider
mcp_servers:
- description: A live, anonymous, remote MCP server on Lindy's own documentation host. It is a documentation-retrieval server generated by the Mintlify platform that runs docs.lindy.ai, not a server over the Lindy p
  name: Lindy Documentation MCP Server
  slug: lindy-documentation-mcp-server
modified: '2026-08-29'
name: Lindy
nav: Providers
network: true
overview: 'Lindy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Agents, AI Automation, Agentic AI, MCP, and Workflow-Automation.


  The Lindy catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Lindy''s developer surface includes documentation, getting-started guide, engineering blog, changelog, pricing, signup flow, support, and 27 more developer resources.'
plans:
- name: Lindy Plans Pricing
  plan_count: 4
  slug: lindy-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Lindy Rate Limits
  slug: lindy-rate-limits
score:
  band: strong
  composite: 56.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 47.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 52.6
  previous_composite: 56.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lindy/refs/heads/main/screenshots/lindy-2026-06-20T184536.png
security:
- kind: authentication
  name: Lindy Authentication
  slug: lindy-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Lindy Domain Security
  slug: lindy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lindy Vulnerability Disclosure
  slug: lindy-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Lindy Trust Center
  slug: lindy-trust-center
  summary_line: SOC 2, ISO 27001
slug: lindy
tags:
- AI Agents
- AI Automation
- Agentic AI
- MCP
- Workflow-Automation
- Virtual Assistant
- Productivity
- Email
- Meetings
- Slack
website: https://www.lindy.ai
---
