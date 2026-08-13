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
  scored_at: '2026-08-12'
api_count: 3
apis:
- description: Figma and Adobe XD plugin that tags layers, applies responsive behavior, and exports production-ready front-end code (React, Next.js, HTML/CSS, React Native, Gatsby). Acts as the primary entry point i
  name: Locofy Lightning
  slug: lightning
- description: Web-based workspace for refining AI-generated components and screens, wiring data and interactivity, and exporting or syncing code to a Git repository. Sits downstream of Lightning in the design-to-co
  name: Locofy Builder
  slug: builder
- description: AI layer that powers automatic tagging, responsive layout suggestions, component detection, and code generation across Lightning and Builder. Exposed through the products rather than a standalone publ
  name: Locofy AI
  slug: ai
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/locofy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.locofy.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.locofy.ai/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/locofy
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Locofy
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/LocofyAI
- group: company
  title: ''
  type: Blog
  url: https://www.locofy.ai/blog
created: '2026-05-23'
description: Locofy.ai is an AI-assisted design-to-code platform that converts Figma and Adobe XD designs into production-ready front-end code. The flagship product Locofy Lightning is a Figma/Adobe XD plugin that tags designs and exports responsive code; Locofy Builder is a web-based workspace for refining the generated app, wiring data, and shipping to repositories. Output targets include React, Next.js, React Native, HTML/CSS, and Gatsby. The platform is primarily delivered as plugins and a web app rather than a public REST API.
finops:
- name: Locofy Finops
  service_category: API
  slug: locofy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/locofy.png
layout: provider
modified: '2026-05-23'
name: Locofy
nav: Providers
network: true
overview: 'Locofy publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Design to Code, Figma, Adobe XD, Frontend, and AI Code Generation.


  Locofy''s developer surface includes documentation, GitHub presence, engineering blog, and 4 more developer resources.'
plans:
- name: Locofy Plans Pricing
  plan_count: 1
  slug: locofy-plans-pricing
random_paper: 52
rate_limits:
- limit_count: 2
  name: Locofy Rate Limits
  slug: locofy-rate-limits
score:
  band: emerging
  composite: 18.8
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 18.8
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/locofy/refs/heads/main/screenshots/locofy-2026-06-20T184650.png
security:
- kind: domain-security
  name: Locofy Domain Security
  slug: locofy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: locofy
tags:
- Design to Code
- Figma
- Adobe XD
- Frontend
- AI Code Generation
- Low-Code
website: https://www.locofy.ai/
---
