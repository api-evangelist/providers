---
access_model:
  confidence: high
  label: Paid subscription plus pay-as-you-go credits; free to self-host
  onboarding: unknown
  pricing: paid
  public: true
  source:
  - https://agpt.co/pricing
  - plans/autogpt-plans-pricing.yml
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.7
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: The documented, third-party-facing REST API of the AutoGPT Platform. Twenty operations that find and run AutoGPT agents, execute individual blocks, create agent graphs, read graph execution results, b
  name: AutoGPT External API
  slug: autogpt
- description: The AutoGPT Platform's own backend API — 293 paths, 347 operations and 458 schemas covering graphs, executions, schedules, the library, the agent marketplace, credits and billing, organizations, works
  name: AutoGPT Agent Server API
  slug: autogpt-agent-server
artifact_total: 10
asyncapis:
- description: ''
  name: Autogpt Webhooks
  slug: autogpt-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://agpt.co
- group: start
  title: ''
  type: DeveloperPortal
  url: https://agpt.co/docs
- group: docs
  title: ''
  type: Documentation
  url: https://agpt.co/docs
- group: docs
  title: ''
  type: APIReference
  url: https://backend.agpt.co/external-api/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://agpt.co/docs/platform/using-the-platform/getting-started-cloud
- group: company
  title: ''
  type: Blog
  url: https://agpt.co/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Significant-Gravitas
- group: operate
  title: ''
  type: Roadmap
  url: https://github.com/orgs/Significant-Gravitas/projects/2
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/autogpt
- group: commercial
  title: ''
  type: Pricing
  url: https://agpt.co/pricing
- group: start
  title: ''
  type: SignUp
  url: https://platform.agpt.co/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agpt.co/legal/platform-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agpt.co/legal/platform-privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/autogpt-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/autogpt-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/autogpt-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/autogpt-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/autogpt-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/autogpt-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/autogpt-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/autogpt-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/autogpt-packages.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/autogpt-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/autogpt-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/autogpt-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/autogpt-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: security/autogpt-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/autogpt-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/autogpt-domain-security.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/autogpt-finops.yml
created: '2026-03-27'
description: 'AutoGPT, from Significant Gravitas, is an open-source platform for building, deploying and running autonomous AI agents that automate digital work — research, outreach, content, support — without writing code. Agents are composed as graphs of reusable blocks in a visual builder, or described in plain language to AutoPilot, then run continuously on schedules and triggers across 45+ connected services. The platform is free to self-host from GitHub and also sold as a managed cloud at agpt.co, where work is metered in automation credits. Developers reach it through the AutoGPT External API at backend.agpt.co/external-api, a 20-operation REST surface authenticated with an X-API-Key header or an OAuth 2.0 token, which can find and run agents, execute individual blocks, create agent graphs, read execution results and manage the third-party credentials agents act on. AutoGPT is also a fluent MCP client: its MCP Tool block connects an agent to any Model Context Protocol server over
  Streamable HTTP with OAuth and PKCE.'
finops:
- name: Autogpt Finops
  service_category: API
  slug: autogpt-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/autogpt.png
layout: provider
modified: '2026-08-29'
name: AutoGPT
nav: Providers
network: true
overview: 'AutoGPT publishes 2 APIs on the [APIs.io](https://apis.io/) network: External API and Agent Server API. Tagged areas include AI Agents, AI Automation, Agent Platform, Workflow-Automation, and MCP.


  The AutoGPT catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AutoGPT''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 24 more developer resources.'
plans:
- name: Autogpt Plans Pricing
  plan_count: 4
  slug: autogpt-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Autogpt Rate Limits
  slug: autogpt-rate-limits
scopes:
- name: Autogpt Scopes
  scope_count: 0
  slug: autogpt-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 57.5
  coverage:
    artifact_dirs: 24
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 1.8
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 55.4
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 42.1
  previous_composite: 55.7
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/autogpt/refs/heads/main/screenshots/autogpt-2026-06-20T172646.png
security:
- kind: authentication
  name: Autogpt Authentication
  slug: autogpt-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Autogpt Domain Security
  slug: autogpt-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Autogpt Vulnerability Disclosure
  slug: autogpt-vulnerability-disclosure
  summary_line: disclosure policy published
slug: autogpt
tags:
- AI Agents
- AI Automation
- Agent Platform
- Workflow-Automation
- MCP
- Open-Source
- No-Code
- LLM Orchestration
- Agent Marketplace
website: https://agpt.co
---
