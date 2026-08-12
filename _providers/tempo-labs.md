---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
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
  scored_at: '2026-08-11'
api_count: 2
apis:
- description: The Tempo product itself - a hosted AI app builder where users prompt, generate, edit, and preview React / Next.js applications in the browser. Combines a visual canvas, AI-generated code, and live pr
  name: Tempo Web App
  slug: web-app
- description: Official documentation for using Tempo - prompts and generation, working with the canvas, code editing, integrations with auth / database / hosting providers, and exporting projects.
  name: Tempo Documentation
  slug: docs
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tempo-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tempo.new/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tempo.new/
- group: other
  title: ''
  type: X
  url: https://x.com/tempolabs_ai
created: '2026-05-23'
description: Tempo (Tempo Labs) is an AI app builder at tempo.new positioned around the "Prompt. Develop. Design. Collaborate." loop - users describe an app in natural language, Tempo generates code, and developers iterate either in the visual canvas or directly in code. The product targets design-to-code and prompt-to-code workflows for React / Next.js apps and is primarily consumed as a hosted web product rather than as an API. Public developer surface is limited; integrations and connected services (auth, database, hosting) are surfaced inside the product rather than via a documented public API.
finops:
- name: Tempo Labs Finops
  service_category: API
  slug: tempo-labs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tempo-labs.png
layout: provider
modified: '2026-05-23'
name: Tempo Labs
nav: Providers
network: true
overview: 'Tempo Labs publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI App Builder, Design to Code, Prompt to Code, Low Code, and React.


  Tempo Labs'' developer surface includes documentation and 3 more developer resources.'
plans:
- name: Tempo Labs Plans Pricing
  plan_count: 1
  slug: tempo-labs-plans-pricing
random_paper: 84
rate_limits:
- limit_count: 2
  name: Tempo Labs Rate Limits
  slug: tempo-labs-rate-limits
score:
  band: emerging
  composite: 17.1
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 17.1
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tempo-labs/refs/heads/main/screenshots/tempo-labs-2026-06-20T195100.png
security:
- kind: domain-security
  name: Tempo Labs Domain Security
  slug: tempo-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tempo-labs
tags:
- AI App Builder
- Design to Code
- Prompt to Code
- Low Code
- React
- Next.js
- Developer Tools
website: https://tempo.new/
---
