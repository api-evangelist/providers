---
access_model:
  confidence: medium
  label: Free · Requires approval
  onboarding: approval
  pricing: free
  public: false
  source:
  - plans
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Dropzone AI's primary "API surface" is its catalog of 90+ outbound integrations to SIEM, EDR/XDR, identity, cloud, and threat intel tools. The autonomous SOC analyst consumes alerts and enrichment dat
  name: Dropzone AI Platform Integrations
  slug: platform-integrations
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dropzone-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dropzone-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dropzone.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dropzone.ai/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dropzoneai
- group: commercial
  title: ''
  type: Plans
  url: plans/dropzone-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dropzone-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dropzone-ai-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.dropzone.ai/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.dropzone.ai/blog
created: '2026-05-23'
description: Dropzone AI delivers an Agentic SOC platform built around an autonomous AI SOC Analyst that handles tier-1 alert triage and threat hunting 24/7. The platform ships pre-trained, is coachable in natural language, and connects via secure APIs to 90+ existing security tools (SIEM, EDR/XDR, identity, cloud, threat intel). Dropzone does not publish a customer-facing REST API; integration is delivered through its outbound connectors and partner program.
finops:
- name: Dropzone Ai Finops
  service_category: API
  slug: dropzone-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dropzone-ai.png
layout: provider
modified: '2026-05-23'
name: Dropzone AI
nav: Providers
network: true
overview: 'Dropzone AI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Security, SOC, AI Agent, Autonomous, and Triage.


  Dropzone AI''s developer surface includes documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Dropzone Ai Plans Pricing
  plan_count: 1
  slug: dropzone-ai-plans-pricing
random_paper: 84
rate_limits:
- limit_count: 2
  name: Dropzone Ai Rate Limits
  slug: dropzone-ai-rate-limits
score:
  band: emerging
  composite: 17.6
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 17.6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dropzone-ai/refs/heads/main/screenshots/dropzone-ai-2026-06-20T180248.png
security:
- kind: domain-security
  name: Dropzone Ai Domain Security
  slug: dropzone-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Dropzone Ai Vulnerability Disclosure
  slug: dropzone-ai-vulnerability-disclosure
  summary_line: disclosure policy published
slug: dropzone-ai
tags:
- Security
- SOC
- AI Agent
- Autonomous
- Triage
- SIEM
- EDR
- XDR
- Gated
website: https://www.dropzone.ai/
---
