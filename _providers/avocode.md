---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
api_count: 1
apis:
- description: The Avocode REST API provided programmatic access to projects, design files, shared screens, annotations, and design spec data, enabling integrations with third-party tools and automation of design-to
  name: Avocode API
  slug: avocode-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/avocode-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://avocode.com/
- group: docs
  title: ''
  type: Documentation
  url: https://avocode.com/integrations
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/avocode
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/avocode-inc-
- group: company
  title: ''
  type: Blog
  url: https://blog.avocode.com
- group: commercial
  title: ''
  type: Pricing
  url: https://avocode.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://avocode.statuspage.io
- group: other
  title: ''
  type: X
  url: https://x.com/avocode
- group: commercial
  title: ''
  type: Plans
  url: plans/avocode-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/avocode-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/avocode-finops.yml
created: '2026-06-13'
description: Avocode was a design handoff platform with a REST API for managing projects, design files, shared screens, annotations, and design spec exports for developer-designer collaboration. Acquired by Ceros in October 2021 and sunset on October 1, 2023, Avocode supported design files from Sketch, Figma, Adobe XD, Photoshop, and Illustrator, enabling developers to inspect designs, extract CSS, SVG, image assets, fonts, and colors without requiring access to the original design tools.
finops:
- name: Avocode Finops
  service_category: ''
  slug: avocode-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/avocode.png
jsonld:
- class_count: 0
  name: Avocode Context
  property_count: 9
  slug: avocode-context
layout: provider
modified: '2026-06-13'
name: Avocode
nav: Providers
network: true
overview: 'Avocode publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Design, Design Handoff, Developer Collaboration, Inspect, and Design Files.


  The Avocode catalog on APIs.io includes 1 JSON-LD context.


  Avocode''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Avocode Plans Pricing
  plan_count: 2
  slug: avocode-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 3
  name: Avocode Rate Limits
  slug: avocode-rate-limits
score:
  band: emerging
  composite: 25.8
  delta: -2.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 8.1
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 28.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/avocode/refs/heads/main/screenshots/avocode-2026-06-20T172727.png
security:
- kind: domain-security
  name: Avocode Domain Security
  slug: avocode-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: avocode
tags:
- Design
- Design Handoff
- Developer Collaboration
- Inspect
- Design Files
- Sketch
- Figma
- Adobe XD
- CSS Export
website: https://avocode.com/
---
