---
access_model:
  confidence: high
  label: Free tier plus paid plans
  onboarding: self-serve
  pricing: freemium
  public: true
  source:
  - https://edgelabs.ai/pricing
  - https://github.com/agent-defense/parallax
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 21.9
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: 'Self-hosted HTTP API of Parallax, the Apache-2.0 runtime security engine Scalarr publishes for AI agents. Two endpoints: POST /evaluate takes a lifecycle event (message.before, tool.before, tool.after'
  name: Parallax Evaluation API
  slug: parallax-evaluation-api
- description: The HTTP API behind the AI EdgeLabs customer console at portal.edgelabs.ai. Confirmed live on 2026-08-13 - every path under /api/ answered HTTP 401 with a structured JSON envelope {"message","status",
  name: AI EdgeLabs Portal API
  slug: ai-edgelabs-portal-api
artifact_total: 8
asyncapis:
- description: ''
  name: Scalarr Parallax Webhooks
  slug: scalarr-parallax-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://scalarr.io
- group: company
  title: ''
  type: Website
  url: https://edgelabs.ai
- group: company
  title: ''
  type: Blog
  url: https://edgelabs.ai/blog
- group: company
  title: ''
  type: Blog
  url: https://scalarr.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://edgelabs.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://portal.edgelabs.ai
- group: operate
  title: ''
  type: Support
  url: https://edgelabs.ai/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/agent-defense
- group: operate
  title: ''
  type: Roadmap
  url: https://github.com/agent-defense/parallax#-roadmap
- group: commercial
  title: ''
  type: TermsOfService
  url: https://scalarr.io/document/services_agreement/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://edgelabs.ai/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://scalarr.io/document/scalarr-privacy-policy/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://edgelabs.ai/privacy-notice
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/scalarr-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/scalarr-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/scalarr-security.txt
- group: auth
  title: ''
  type: Security
  url: security/scalarr-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/scalarr-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scalarr-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/scalarr-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/scalarr-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/scalarr-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/scalarr-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/scalarr-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/scalarr-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/scalarr-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/scalarr-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/scalarr-parallax-webhooks.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/scalarr-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/scalarr-rate-limits.yml
created: '2026-07-17'
description: 'Scalarr Inc. is a cybersecurity company that now operates primarily as AI EdgeLabs (edgelabs.ai), an AI-native runtime detection and response platform for workloads, containers, GPU environments, AI agents and edge infrastructure, with local inference, zero data egress, and out-of-the-box NIS2 and Cyber Resilience Act control mapping in its Compliance Center. It publishes Parallax, an Apache-2.0 runtime security engine for AI agents written in Rust, which ships as a single binary exposing a two-endpoint HTTP evaluation API (POST /evaluate, GET /health) plus a proxy mode that sits between an agent and the LLM API, 54 curated rules across five evaluator engines, and first-party integrations for OpenClaw, Claude Code and the Codex CLI. Scalarr''s original business - the machine-learning mobile ad-fraud Protection Suite and DeepView on scalarr.io - appears dormant: the site is still served but its content and sitemap have not been updated since 2022-2023 and api.scalarr.io answers
  every path with a default OpenResty 404. Scalarr is a portfolio company of Speedinvest. The hosted AI EdgeLabs platform API at portal.edgelabs.ai/api/ is real but undocumented and authentication-gated; no OpenAPI, AsyncAPI, GraphQL schema or MCP server is published for any surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/scalarr.png
layout: provider
modified: '2026-08-13'
name: Scalarr
nav: Providers
network: true
overview: 'Scalarr publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Runtime Security, AI Agent Security, and Container Security.


  The Scalarr catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Scalarr''s developer surface includes engineering blog, pricing, signup flow, support, CLI, changelog, authentication, and 23 more developer resources.'
plans:
- name: Scalarr Plans Pricing
  plan_count: 5
  slug: scalarr-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Scalarr Rate Limits
  slug: scalarr-rate-limits
score:
  band: developing
  composite: 49.5
  coverage:
    artifact_dirs: 16
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 54.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 49.5
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/scalarr/refs/heads/main/screenshots/scalarr-2026-08-17T081729.png
security:
- kind: authentication
  name: Scalarr Authentication
  slug: scalarr-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Scalarr Domain Security
  slug: scalarr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Scalarr Vulnerability Disclosure
  slug: scalarr-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: scalarr
tags:
- Company
- Cybersecurity
- Runtime Security
- AI Agent Security
- Container Security
- Kubernetes
- Edge Computing
- Vulnerability Management
- Compliance
- NIS2
- Machine-Learning
- Artificial Intelligence
- Open-Source
- Fraud Detection
- Mobile Ad Fraud
website: https://scalarr.io
---
