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
  url: https://www.motiva.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://help.plugin.motiva.ai/
- group: operate
  title: ''
  type: Support
  url: https://help.plugin.motiva.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.plugin.motiva.ai/en/collections/173873-getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.motiva.ai/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://help.plugin.motiva.ai/en/articles/3003565-how-much-does-motiva-ai-cost
- group: start
  title: ''
  type: SignUp
  url: https://www.motiva.ai/get-a-demo/
- group: start
  title: ''
  type: Login
  url: https://app.motiva.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.motiva.ai/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.motiva.ai/data-protection/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Motiva-AI
- group: auth
  title: ''
  type: Compliance
  url: https://www.motiva.ai/data-protection/
- group: auth
  title: ''
  type: TrustCenter
  url: security/motiva-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/motiva-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/motiva-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/motiva-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/motiva-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/motiva-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/motiva-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/motiva-lifecycle.yml
coverage:
  checked: '2026-08-13'
  detail: Motiva ships only as an installed Oracle Eloqua connector plus a customer web app — its one API-shaped host, api.motiva.ai, returns HTTP 403 {"message":"Forbidden"} on every anonymous path including all of /.well-known/, and the complete public Help Center index at help.plugin.motiva.ai/llms.txt (HTTP 200) documents connector setup with no API reference, no endpoint, no key issuance and no spec anywhere.
  evidence:
  - status: 403
    url: https://api.motiva.ai/openapi.json
  - status: 403
    url: https://api.motiva.ai/.well-known/agent-card.json
  - status: 200
    url: https://help.plugin.motiva.ai/llms.txt
  - status: 202
    url: https://www.motiva.ai/openapi.json
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Motiva AI is an artificial-intelligence layer for enterprise email marketing that plugs into Oracle Eloqua and other marketing-automation platforms to automate campaign decision-making. It runs multivariate (A/B/n) message testing, patented per-contact send-time optimization, frequency management, list and dark-pool cleanup via Smart Suppress, audience discovery, and generative-AI email content through Motiva Generator (including private-label custom LLMs). Motiva is delivered as an installed connector rather than a public developer API, is trusted by enterprises such as Cisco and Thermo Fisher, and maintains SOC 1/2/3 and ISO 27001 compliance with GDPR and HIPAA support.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/motiva.png
layout: provider
modified: '2026-08-13'
name: Motiva
nav: Providers
network: true
overview: 'Motiva is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Email Marketing, Marketing Automation, and Artificial Intelligence.


  Motiva''s developer surface includes documentation, support, getting-started guide, engineering blog, pricing, signup flow, and 14 more developer resources.'
plans:
- name: Motiva Plans Pricing
  plan_count: 1
  slug: motiva-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 0
  name: Motiva Rate Limits
  slug: motiva-rate-limits
score:
  band: emerging
  composite: 23.8
  delta: -6.8
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 30.6
  provenance:
    conformance: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/motiva/refs/heads/main/screenshots/motiva-2026-08-07T184328.png
security:
- kind: domain-security
  name: Motiva Domain Security
  slug: motiva-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Motiva Trust Center
  slug: motiva-trust-center
  summary_line: SOC 1, SOC 2, SOC 3, ISO 27001, SSAE 16, GDPR, HIPAA
slug: motiva
tags:
- Company
- Marketing
- Email Marketing
- Marketing Automation
- Artificial Intelligence
- Machine Learning
- Generative AI
- Oracle Eloqua
- Personalization
website: https://www.motiva.ai/
---
