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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.jeeva.ai/
- group: start
  title: ''
  type: SignUp
  url: https://app.jeeva.ai/?join-growth=1
- group: start
  title: ''
  type: Login
  url: https://app.jeeva.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.jeeva.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.jeeva.ai/blog
- group: operate
  title: ''
  type: Roadmap
  url: https://www.jeeva.ai/roadmap
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jeeva.ai/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jeeva.ai/privacy-policies
- group: operate
  title: ''
  type: StatusPage
  url: https://www.jeeva.ai/system-status
- group: auth
  title: ''
  type: TrustCenter
  url: security/jeeva-ai-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.jeeva.ai/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jeeva-ai-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jeeva-ai-llms.txt
- group: docs
  title: ''
  type: Documentation
  url: https://www.jeeva.ai/jeeva-university
- group: start
  title: ''
  type: GettingStarted
  url: https://www.jeeva.ai/quick-start-guide
- group: operate
  title: ''
  type: Support
  url: https://www.jeeva.ai/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Involve-AI
- group: commercial
  title: ''
  type: Plans
  url: plans/jeeva-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/jeeva-ai-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/jeeva-ai-packages.yml
- group: design
  title: ''
  type: Components
  url: components/jeeva-ai-components.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/jeeva-ai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/jeeva-ai-conformance.yml
coverage:
  checked: '2026-08-14'
  detail: 'Jeeva AI ships an end-user sales-automation SaaS and no developer program: its 705-URL sitemap contains no developer portal, API reference or docs host, no pricing tier grants API access, and the only API host, api.jeeva.ai, is an AWS API Gateway that returns 403 {"message":"Missing Authentication Token"} to every unauthenticated path including /openapi.json, /graphql, /mcp and /.well-known/*.'
  evidence:
  - status: 403
    url: https://api.jeeva.ai/openapi.json
  - status: 404
    url: https://www.jeeva.ai/llms.txt
  - status: 404
    url: https://www.jeeva.ai/.well-known/agent-card.json
  - status: 200
    url: https://www.jeeva.ai/sitemap.xml
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Jeeva AI builds, deploys, and governs autonomous digital workers — AI agents that perceive, reason, act, and remember context across business systems. Workers are deployed with natural-language (no-code) descriptions and automate workflows across revenue, IT, customer service, operations, finance, security, and HR. Revenue workers are live today; a Worker Builder Platform and IT and customer-service worker categories are in early access on a shared runtime. The platform serves 36,000+ active users and is backed by Sapphire Ventures, Alt Capital and Bonfire Ventures. Jeeva AI is sold as an end-user SaaS product with a free tier, self-serve Growth and Scale plans and a custom Enterprise tier; it publishes no public API, no developer portal, no API reference, no OpenAPI/AsyncAPI/GraphQL definition, no SDK in any package registry and no MCP server. The api.jeeva.ai host is an AWS API Gateway that answers 403 Missing Authentication Token on every path. Coverage here is identity,
  commercial, trust and security posture.
image: https://framerusercontent.com/assets/RErQi3dkoXX4oN1AdLpYpcxBPY.png
layout: provider
modified: '2026-08-14'
name: Jeeva AI
nav: Providers
network: true
overview: 'Jeeva AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai, AI Agents, Digital Workers, and Sales Automation.


  Jeeva AI''s developer surface includes signup flow, pricing, engineering blog, documentation, getting-started guide, support, and 17 more developer resources.'
plans:
- name: Jeeva Ai Plans Pricing
  plan_count: 4
  slug: jeeva-ai-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Jeeva Ai Rate Limits
  slug: jeeva-ai-rate-limits
score:
  band: thin
  composite: 34.9
  delta: -0.5
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 35.4
  provenance:
    conformance: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jeeva-ai/refs/heads/main/screenshots/jeeva-ai-2026-07-25T223125.png
security:
- kind: domain-security
  name: Jeeva Ai Domain Security
  slug: jeeva-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Jeeva Ai Trust Center
  slug: jeeva-ai-trust-center
  summary_line: SOC 2, GDPR
slug: jeeva-ai
tags:
- Company
- Ai
- AI Agents
- Digital Workers
- Sales Automation
- Revenue Operations
- No-Code
- Automation
website: https://www.jeeva.ai/
---
