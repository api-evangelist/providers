---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
api_count: 1
apis:
- description: 'REST API in OpenAI Chat Completions wire format. Primary endpoint POST /v1/chat/completions with SSE streaming and tool/function-calling passthrough. Supporting endpoints for ping, usage, ledger, and '
  name: Vynaris Gateway API
  slug: vynaris-gateway-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.vynaris.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vynaris-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vynaris-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vynaris-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vynaris-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vynaris-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vynaris-authentication.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/vynaris-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/vynaris-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vynaris-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vynaris-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://vynaris.com/docs#quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://vynaris.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.vynaris.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vynaris.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vynaris.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://vynaris.com/blog
- group: operate
  title: ''
  type: Support
  url: mailto:hello@vynaris.com
created: '2026-08-26'
description: OpenAI-compatible LLM inference gateway with evidence-based model routing and a per-request cost receipt attached to every response. Offers routed inference at provider list price plus a small markup, Vynaris-hosted reduced-refusal models, and enterprise self-hosted deployments. Early beta.
image: https://vynaris.com/icon.png
layout: provider
modified: '2026-08-26'
name: Vynaris
nav: Providers
network: true
overview: 'Vynaris publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, LLM Gateway, LLM Router / Aggregator, Inference / Model Serving, and AI Cost Management / FinOps.


  Vynaris'' developer surface includes authentication, getting-started guide, pricing, signup flow, engineering blog, support, and 13 more developer resources.'
plans:
- name: Vynaris Plans Pricing
  plan_count: 5
  slug: vynaris-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Vynaris Rate Limits
  slug: vynaris-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/vynaris/refs/heads/main/screenshots/vynaris-2026-09-02T170341.png
security:
- kind: authentication
  name: Vynaris Authentication
  slug: vynaris-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Vynaris Domain Security
  slug: vynaris-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vynaris
tags:
- Artificial Intelligence
- LLM Gateway
- LLM Router / Aggregator
- Inference / Model Serving
- AI Cost Management / FinOps
- Developer Tools
- Agent Infrastructure
website: https://www.vynaris.com/
---
