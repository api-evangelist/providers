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
overview: 'Tiyaro is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Agents, Agentic AI, and Customer-Support.


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
screenshot: https://raw.githubusercontent.com/api-evangelist/tiyaro/refs/heads/main/screenshots/tiyaro-2026-09-02T163826.png
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
- Customer-Support
- ITSM
- Business Process Automation
- Enterprise Software
- LLM
- Revenue Operations
website: https://www.tiyaro.ai/
---
