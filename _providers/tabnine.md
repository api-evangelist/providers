---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: VS Code, JetBrains (IntelliJ, PhpStorm, etc.), and Eclipse plugins surfacing autocomplete, chat, and agentic workflows. Communicates with Tabnine's hosted or self-hosted backend over a proprietary pro
  name: Tabnine IDE Plugins
  slug: plugins
- description: Enterprise SKU with admin console (data analytics, model provisioning, context permissions, SSO), Enterprise Context Engine (codebase indexing), and flexible deployment (SaaS / VPC / Local / Air-Gappe
  name: Tabnine Enterprise (Admin Suite + Context Engine)
  slug: enterprise
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/tabnine-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tabnine-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/codota
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tabnine
- group: company
  title: ''
  type: Website
  url: https://www.tabnine.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tabnine.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/tabnine-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tabnine-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tabnine-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.tabnine.com/blog/feed/
created: '2026-05-08'
description: Tabnine provides AI code completion, chat, and agentic workflows across IDEs and CLI, with strong support for SaaS, VPC, and air-gapped on-prem deployments. The Enterprise Context Engine indexes a customer's codebase, dependencies, and architecture. Tabnine's consumer surface is via IDE plugins (VS Code, JetBrains, Eclipse) and the Tabnine CLI; there is no general-purpose public REST inference API for end-developers.
finops:
- name: Tabnine Finops
  service_category: AI
  slug: tabnine-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tabnine.png
layout: provider
modified: '2026-05-08'
name: Tabnine
nav: Providers
network: true
overview: 'Tabnine publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Developer Tools, Code Completion, Self-Hosted, and Enterprise.


  Tabnine''s developer surface includes documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Tabnine Plans Pricing
  plan_count: 1
  slug: tabnine-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Tabnine Rate Limits
  slug: tabnine-rate-limits
score:
  band: emerging
  composite: 19.8
  delta: -2.4
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 22.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tabnine/refs/heads/main/screenshots/tabnine-2026-06-20T194849.png
security:
- kind: domain-security
  name: Tabnine Domain Security
  slug: tabnine-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Tabnine Trust Center
  slug: tabnine-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: tabnine
tags:
- AI
- Developer Tools
- Code Completion
- Self-Hosted
- Enterprise
- Privacy
website: https://www.tabnine.com/
---
