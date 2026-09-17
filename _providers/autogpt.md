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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.4
  scored_at: '2026-09-16'
api_count: 3
apis:
- baseURL: https://backend.agpt.co/external-api
  baseurl_source: declared
  description: The analytics API from AutoGPT — 2 operation(s) for analytics.
  name: AutoGPT Analytics API
  slug: autogpt-analytics-api
- baseURL: https://backend.agpt.co/external-api
  baseurl_source: declared
  description: The auth-email API from AutoGPT — 1 operation(s) for auth-email.
  name: AutoGPT Auth Email API
  slug: autogpt-auth-email-api
- baseURL: https://backend.agpt.co/external-api
  baseurl_source: declared
  description: The blocks API from AutoGPT — 2 operation(s) for blocks.
  name: AutoGPT Blocks API
  slug: autogpt-blocks-api
- baseURL: https://backend.agpt.co/external-api
  baseurl_source: declared
  description: The briefings API from AutoGPT — 1 operation(s) for briefings.
  name: AutoGPT Briefings API
  slug: autogpt-briefings-api
- baseURL: https://backend.agpt.co/external-api
  baseurl_source: declared
  description: The Copilot Webhooks API from AutoGPT — 6 operation(s) for copilot webhooks.
  name: AutoGPT Copilot Webhooks API
  slug: autogpt-copilot-webhooks-api
- baseURL: https://backend.agpt.co/external-api
  baseurl_source: declared
  description: The graphs API from AutoGPT — 3 operation(s) for graphs.
  name: AutoGPT Graphs API
  slug: autogpt-graphs-api
- baseURL: https://backend.agpt.co/external-api
  baseurl_source: declared
  description: The health API from AutoGPT — 1 operation(s) for health.
  name: AutoGPT Health API
  slug: autogpt-health-api
- baseURL: https://backend.agpt.co/external-api
  baseurl_source: declared
  description: The home API from AutoGPT — 1 operation(s) for home.
  name: AutoGPT Home API
  slug: autogpt-home-api
- baseURL: https://backend.agpt.co/external-api
  baseurl_source: declared
  description: The integrations API from AutoGPT — 6 operation(s) for integrations.
  name: AutoGPT Integrations API
  slug: autogpt-integrations-api
- baseURL: https://backend.agpt.co/external-api
  baseurl_source: declared
  description: The meta API from AutoGPT — 1 operation(s) for meta.
  name: AutoGPT Meta API
  slug: autogpt-meta-api
- baseURL: https://backend.agpt.co/external-api
  baseurl_source: declared
  description: The monitoring API from AutoGPT — 1 operation(s) for monitoring.
  name: AutoGPT Monitoring API
  slug: autogpt-monitoring-api
- baseURL: https://backend.agpt.co/external-api
  baseurl_source: declared
  description: The platform-linking API from AutoGPT — 8 operation(s) for platform-linking.
  name: AutoGPT Platform Linking API
  slug: autogpt-platform-linking-api
- baseURL: https://backend.agpt.co/external-api
  baseurl_source: declared
  description: The push API from AutoGPT — 3 operation(s) for push.
  name: AutoGPT Push API
  slug: autogpt-push-api
- baseURL: https://backend.agpt.co/external-api
  baseurl_source: declared
  description: The search API from AutoGPT — 1 operation(s) for search.
  name: AutoGPT Search API
  slug: autogpt-search-api
- baseURL: https://backend.agpt.co/external-api
  baseurl_source: declared
  description: The store API from AutoGPT — 4 operation(s) for store.
  name: AutoGPT Store API
  slug: autogpt-store-api
- baseURL: https://backend.agpt.co/external-api
  baseurl_source: declared
  description: The tools API from AutoGPT — 2 operation(s) for tools.
  name: AutoGPT Tools API
  slug: autogpt-tools-api
- baseURL: https://backend.agpt.co/external-api
  baseurl_source: declared
  description: The user API from AutoGPT — 1 operation(s) for user.
  name: AutoGPT User API
  slug: autogpt-user-api
- baseURL: https://backend.agpt.co/external-api
  baseurl_source: declared
  description: The v1 API from AutoGPT — 77 operation(s) for v1.
  name: AutoGPT V1 API
  slug: autogpt-v1-api
- baseURL: https://backend.agpt.co/external-api
  baseurl_source: declared
  description: The v2 API from AutoGPT — 174 operation(s) for v2.
  name: AutoGPT V2 API
  slug: autogpt-v2-api
- baseURL: https://backend.agpt.co/external-api
  baseurl_source: declared
  description: The workspace API from AutoGPT — 9 operation(s) for workspace.
  name: AutoGPT Workspace API
  slug: autogpt-workspace-api
- baseURL: https://backend.agpt.co/external-api
  baseurl_source: declared
  description: The oauth API from AutoGPT — 9 operation(s) for oauth.
  name: AutoGPT OAUTH API
  slug: autogpt-oauth-api
artifact_total: 29
asyncapis:
- description: ''
  name: Autogpt Webhooks
  slug: autogpt-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/autogpt/refs/heads/main/overlays/autogpt-external-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/autogpt-external-api-overlay.yaml
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
  href: https://raw.githubusercontent.com/api-evangelist/autogpt/refs/heads/main/changelog/autogpt-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/autogpt-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/autogpt/refs/heads/main/authentication/autogpt-authentication.yml
  title: ''
  type: Authentication
  url: authentication/autogpt-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/autogpt/refs/heads/main/scopes/autogpt-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/autogpt-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/autogpt/refs/heads/main/errors/autogpt-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/autogpt-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/autogpt/refs/heads/main/conventions/autogpt-conventions.yml
  title: ''
  type: Conventions
  url: conventions/autogpt-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/autogpt/refs/heads/main/lifecycle/autogpt-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/autogpt-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/autogpt/refs/heads/main/conformance/autogpt-conformance.yml
  title: ''
  type: Conformance
  url: conformance/autogpt-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/autogpt/refs/heads/main/data-model/autogpt-data-model.yml
  title: ''
  type: DataModel
  url: data-model/autogpt-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/autogpt/refs/heads/main/packages/autogpt-packages.yml
  title: ''
  type: Packages
  url: packages/autogpt-packages.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/autogpt/refs/heads/main/rate-limits/autogpt-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/autogpt-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/autogpt/refs/heads/main/plans/autogpt-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/autogpt-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/autogpt/refs/heads/main/llms/autogpt-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/autogpt-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/autogpt/refs/heads/main/asyncapi/autogpt-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/autogpt-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/autogpt/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/autogpt/refs/heads/main/security/autogpt-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/autogpt-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/autogpt/refs/heads/main/security/autogpt-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/autogpt-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/autogpt/refs/heads/main/security/autogpt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autogpt-domain-security.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/autogpt/refs/heads/main/finops/autogpt-finops.yml
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
overview: 'AutoGPT publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Auth Email API, Blocks API, and 18 more. Tagged areas include AI Agents, AI Automation, Agent Platform, Workflow-Automation, and MCP.


  The AutoGPT catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AutoGPT''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 25 more developer resources.'
plans:
- name: Autogpt Plans Pricing
  plan_count: 4
  slug: autogpt-plans-pricing
random_paper: 2
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
  composite: 58.8
  coverage:
    artifact_dirs: 24
    catalog_earned: 55.0
    catalog_earned_first_party: 12.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 56.6
    developer_ergonomics: 66.1
    discoverability: 81.5
    operational_transparency: 42.1
  previous_composite: 58.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 11.1
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
