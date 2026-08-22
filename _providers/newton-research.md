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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.newtonresearch.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.newtonresearch.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://www.newtonresearch.ai/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.newtonresearch.ai/privacy-policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/newton-research-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/newton-research-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.newtonresearch.ai/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/newton-research-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/newton-research-plans-pricing.yml
coverage:
  checked: '2026-08-12'
  detail: Newton Research claims in its CEO's own AdCP letter to leverage MCP and A2A "today", but serves no endpoint for either — all 18 /.well-known/ probes across both company hosts 404, no api/docs/developer/mcp subdomain resolves, and the only route to the platform is the "someone from our team will follow-up" contact form.
  evidence:
  - status: 404
    url: https://www.newtonresearch.ai/.well-known/agent-card.json
  - status: 404
    url: https://www.newtonresearch.ai/.well-known/adagents.json
  - status: 404
    url: https://www.newtonresearch.ai/mcp
  - status: 404
    url: https://www.newtonresearch.ai/pricing
  - status: 200
    url: https://www.newtonresearch.ai/contact
  reason: sales-gate
  state: gated
created: '2026-07-17'
description: Newton Research builds a team of specially trained AI agents for marketing analytics. Pre-built or custom agents connect to a customer's existing data infrastructure, write and execute code, and automate analytics workflows — data exploration and preparation, audience management, Customer 360, planning and activation, cross-channel measurement and attribution, anomaly detection, yield management, and automated reporting — with data remaining on the customer's own instance. Founded by John Hoctor, Matthew Emans, and Steven Bennett, the company is backed by Bessemer Venture Partners and is a member of the NVIDIA Inception program. Newton states SOC 2, GDPR, and CCPA compliance. No public developer API surface is published as of this profile.
image: https://cdn.prod.website-files.com/675abf0afaec64b833d93565/67783b3d62f5533326aa208d_newton%20OG.png
layout: provider
modified: '2026-08-12'
name: Newton Research
nav: Providers
network: true
overview: 'Newton Research is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Ml, Marketing Analytics, MarTech, and AdTech.


  Newton Research''s developer surface includes engineering blog, support, and 7 more developer resources.'
plans:
- name: Newton Research Plans Pricing
  plan_count: 0
  slug: newton-research-plans-pricing
random_paper: 3
score:
  band: emerging
  composite: 12.6
  delta: 0.4
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 12.2
  provenance:
    conformance: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/newton-research/refs/heads/main/screenshots/newton-research-2026-08-07T185140.png
security:
- kind: domain-security
  name: Newton Research Domain Security
  slug: newton-research-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: newton-research
tags:
- Company
- Ai Ml
- Marketing Analytics
- MarTech
- AdTech
- AI Agents
- Data Science
- Analytics
website: https://www.newtonresearch.ai/
---
