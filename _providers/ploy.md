---
access_model:
  confidence: high
  label: Self-serve signup with a free tier
  onboarding: self-serve
  pricing: freemium
  public: true
  source:
  - https://ploy.ai/pricing
  - https://docs.ploy.ai/quick-start
  trial: true
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: The only public HTTP endpoint Ploy documents. An authenticated inbound ingest endpoint that accepts any well-formed JSON object (up to 1 MB) from an external system — Clay, Stripe, Zapier, or a custom
  name: Ploy Webhook Ingest API
  slug: webhook-ingest
artifact_total: 8
asyncapis:
- description: ''
  name: Ploy Webhooks
  slug: ploy-webhooks
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ploy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/ploy-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ploy-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/ploy-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ploy-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/ploy-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.ploy.ai
- group: design
  title: ''
  type: Conformance
  url: conformance/ploy-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ploy-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ploy-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ploy-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ploy-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ploy.ai
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ploy-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/ploy-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/ploy-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ploy-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ploy-webhooks.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ploy-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ploy-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ploy-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ploy-docs-llms.txt
- group: company
  title: ''
  type: Website
  url: https://ploy.ai
- group: company
  title: ''
  type: Blog
  url: https://ploy.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://ploy.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://ploy.ai
- group: start
  title: ''
  type: Login
  url: https://ploy.ai/workspaces
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ploy.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ploy.ai/cli
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ploy.ai/cli/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ploy.ai/quick-start
- group: operate
  title: ''
  type: Support
  url: https://docs.ploy.ai/faq
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Ploy-AI
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ploy.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ploy.ai/privacy
created: '2026-07-17'
description: 'Ploy is an AI-powered web marketing automation platform that turns a company''s marketing website into a growth channel. Founded in 2025 by former Webflow CTO Bryant Chou, backed by Y Combinator and First Round Capital ($27M), Ploy runs AI agents that build and optimize Astro/Tailwind marketing sites, write copy, run technical SEO and answer-engine optimization, identify visiting companies without cookies, launch ad campaigns, and execute reusable multi-step workflows called Ploybooks. Its programmable surface is deliberately CLI-first rather than REST-first: Ploy publishes no OpenAPI and no public API reference, but it does ship a standalone `ploy` CLI binary (workspaces, sites, publishing, variables and secrets, documents, Ploybooks, databases, Code Sync, and design-system inspection) authenticated by workspace-scoped API tokens for headless CI and remote coding agents, an installable Agent Skills catalog (`ploy skills init`), and one public HTTP endpoint — an authenticated
  inbound webhook ingest at /api/v1/webhook/{endpointSlug} that stores arbitrary JSON and triggers a Ploybook.'
image: https://cdn.ploy.ai/d21bf4ad-2458-43ee-9561-54c28ab0e85f/user/095160ed-og-home-alt.jpg
layout: provider
modified: '2026-08-12'
name: Ploy
nav: Providers
network: true
overview: 'Ploy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Marketing Automation, Artificial Intelligence, and AI Agents.


  The Ploy catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ploy''s developer surface includes authentication, changelog, CLI, engineering blog, pricing, signup flow, documentation, and 29 more developer resources.'
plans:
- name: Ploy Plans Pricing
  plan_count: 4
  slug: ploy-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Ploy Rate Limits
  slug: ploy-rate-limits
score:
  band: strong
  composite: 59.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 73.7
  previous_composite: 59.8
  provenance:
    conformance: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ploy/refs/heads/main/screenshots/ploy-2026-08-17T081308.png
security:
- kind: authentication
  name: Ploy Authentication
  slug: ploy-authentication
  summary_line: http · 3 schemes
- kind: domain-security
  name: Ploy Domain Security
  slug: ploy-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Ploy Vulnerability Disclosure
  slug: ploy-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Ploy Trust Center
  slug: ploy-trust-center
  summary_line: SOC 2 Type II
slug: ploy
tags:
- Company
- Marketing
- Marketing Automation
- Artificial Intelligence
- AI Agents
- SEO
- Website Builder
- Growth
- Advertising
- Webhook
- CLI
- Agent Skills
website: https://ploy.ai
---
