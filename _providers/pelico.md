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
- group: auth
  title: ''
  type: TrustCenter
  url: security/pelico-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pelico-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pelico.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.pelico.ai/platform
- group: auth
  title: ''
  type: Compliance
  url: https://trust.pelico.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pelico.ai/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pelico.ai/legal/legal-notice
- group: company
  title: ''
  type: Blog
  url: https://www.pelico.ai/resources/our-articles
- group: operate
  title: ''
  type: Support
  url: https://www.pelico.ai/contact
- group: start
  title: ''
  type: SignUp
  url: https://www.pelico.ai/contact
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pelico-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/pelico-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pelico-rate-limits.yml
coverage:
  checked: '2026-08-17'
  detail: Pelico's platform page markets "APIs to ingest new data sources and push actions into existing enterprise systems", but there is no reference behind it — /docs, /developers, /api-docs and /pricing all 404, every conventional API subdomain (api, docs, developers, app, mcp) under pelico.ai is NXDOMAIN, and the 172-URL sitemap routes every API question to the /contact form.
  evidence:
  - status: 200
    url: https://www.pelico.ai/platform
  - status: 404
    url: https://www.pelico.ai/developers
  - status: 404
    url: https://www.pelico.ai/api-docs
  - status: 404
    url: https://www.pelico.ai/llms.txt
  - status: 404
    url: https://www.pelico.ai/.well-known/agent-card.json
  - status: 200
    url: https://www.pelico.ai/contact
  reason: sales-gate
  state: gated
created: '2026-07-17'
description: Pelico is a manufacturing orchestration platform that bridges the execution gap between planning and real-world production. It unifies data from suppliers, production, inventory, quality, maintenance, and customers into a single operational view across multi-level BOMs and multi-plant networks. Domain-specific AI agents continuously monitor disruptions, determine upstream and downstream impact, simulate recovery options (alternates, stock transfers, resequencing), and keep cross-functional teams synchronized in real time. Pelico integrates with major ERP systems (SAP, Oracle, Infor) and cloud providers (AWS, Azure, Google Cloud), exposing APIs to ingest new data sources and push actions into existing enterprise systems. The company is SOC 2 Type II and ISO 27001:2022 certified and GDPR compliant. This profile is maintained in the API Evangelist network; Pelico is a portfolio company of General Catalyst and does not publish a public developer API, portal, or OpenAPI at this time
  — its API surface is enterprise integration only.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pelico.png
layout: provider
modified: '2026-08-17'
name: Pelico
nav: Providers
network: true
overview: 'Pelico is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Manufacturing, Supply Chain, Orchestration, and Artificial Intelligence.


  Pelico''s developer surface includes documentation, engineering blog, support, signup flow, and 9 more developer resources.'
plans:
- name: Pelico Plans Pricing
  plan_count: 0
  slug: pelico-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 0
  name: Pelico Rate Limits
  slug: pelico-rate-limits
score:
  band: emerging
  composite: 19.1
  delta: 0.3
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 18.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Pelico Domain Security
  slug: pelico-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Pelico Trust Center
  slug: pelico-trust-center
  summary_line: SOC 2 Type II, ISO 27001:2022, GDPR
slug: pelico
tags:
- Company
- Manufacturing
- Supply Chain
- Orchestration
- Artificial Intelligence
- Operations
- ERP Integration
- Manufacturing Execution
website: https://www.pelico.ai/
---
