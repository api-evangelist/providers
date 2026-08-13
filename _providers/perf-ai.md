---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: PerfAI is an autonomous agentic AppSec and auto-fix platform for AI-built applications, automating privacy, security, and governance.
  name: Perf.ai
  slug: perf-ai
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/perf-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/perf-ai-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PerfAI-Inc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/perfai
- group: company
  title: ''
  type: Website
  url: https://perfai.ai/
- group: agent
  title: ''
  type: LlmsText
  url: https://perfai.ai/llms.txt
created: '2025-01-08'
description: PerfAI is an autonomous agentic AppSec and auto-fix platform for AI-built apps, helping teams deliver privacy, security, and governance for APIs and applications.
finops:
- name: Perf Ai Finops
  service_category: API
  slug: perf-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/perf-ai.png
layout: provider
modified: '2026-04-28'
name: Perf.ai
nav: Providers
network: true
overview: Perf.ai publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, AppSec, Security, Privacy, and Governance.
plans:
- name: Perf Ai Plans Pricing
  plan_count: 3
  slug: perf-ai-plans-pricing
random_paper: 76
rate_limits:
- limit_count: 5
  name: Perf Ai Rate Limits
  slug: perf-ai-rate-limits
score:
  band: minimal
  composite: 10.6
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 10.6
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/perf-ai/refs/heads/main/screenshots/perf-ai-2026-06-20T191559.png
security:
- kind: domain-security
  name: Perf Ai Domain Security
  slug: perf-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Perf Ai Vulnerability Disclosure
  slug: perf-ai-vulnerability-disclosure
  summary_line: disclosure policy published
slug: perf-ai
tags:
- AI
- AppSec
- Security
- Privacy
- Governance
website: https://perfai.ai/
---
