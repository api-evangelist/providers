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
    well_known_catalog: true
  schema_version: 0.2
  score: 6.4
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tiyaro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tiyaro.ai/
- group: company
  title: ''
  type: About
  url: https://www.tiyaro.ai/about-us/
- group: company
  title: ''
  type: Blog
  url: https://www.tiyaro.ai/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tiyaro.ai/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tiyaro.ai/terms-of-service/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tiyaro
- group: build
  title: ''
  type: Packages
  url: packages/tiyaro-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tiyaro-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/tiyaro-cli.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tiyaro-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tiyaro-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/tiyaro-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tiyaro-rate-limits.yml
coverage:
  checked: '2026-08-14'
  detail: Tiyaro retired its 2021-2022 developer platform without notice - api.tiyaro.ai, console.tiyaro.ai and docs.tiyaro.ai all return NXDOMAIN, so the live https://www.tiyaro.ai/docs/ page renders an empty iframe of the dead docs host, and the current DeepQuery product is sold entirely through a book-a-demo form with no developer surface.
  evidence:
  - status: 200
    url: https://www.tiyaro.ai/docs/
  - status: 0
    url: https://docs.tiyaro.ai/
  - status: 0
    url: https://api.tiyaro.ai/v1/ent
  - status: 0
    url: https://console.tiyaro.ai/
  - status: 200
    url: https://www.tiyaro.ai/.well-known/agent-card.json
  - status: 200
    url: https://pypi.org/pypi/tiyaro/json
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Tiyaro is an enterprise AI company whose product, DeepQuery, replicates complete business processes as AI agents that can be described in plain English. Rather than rules engines or brittle integration workflows, DeepQuery uses LLMs combined with enterprise-specific product and customer data to identify a solution strategy and execute it across multiple steps using built-in tools. Its flagship application targets customer support and IT service desks - an "IT SuperAgent" trained on hundreds of third-party product procedures that recommends and executes resolution steps for incoming tickets - alongside revenue-operations and sales/marketing automation use cases. The company was founded by a team that previously built an edge software stack for hosting AI applications, and is backed by General Catalyst. Tiyaro goes to market as an enterprise product engaged through a book-a-demo motion rather than a self-serve developer API.
image: https://www.tiyaro.ai/icons/icon-512x512.png
layout: provider
modified: '2026-08-14'
name: Tiyaro
nav: Providers
network: true
overview: 'Tiyaro is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Agents, Agentic AI, and Customer Support.


  Tiyaro''s developer surface includes engineering blog, CLI, and 12 more developer resources.'
plans:
- name: Tiyaro Plans Pricing
  plan_count: 0
  slug: tiyaro-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Tiyaro Rate Limits
  slug: tiyaro-rate-limits
score:
  band: emerging
  composite: 11.1
  delta: -3.7
  facets:
    access_clarity: 5.3
    commercial_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 14.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Tiyaro Domain Security
  slug: tiyaro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tiyaro
tags:
- Company
- Artificial Intelligence
- AI Agents
- Agentic AI
- Customer Support
- IT Service Management
- Business Process Automation
- Enterprise Software
- LLM
- Revenue Operations
website: https://www.tiyaro.ai/
---
