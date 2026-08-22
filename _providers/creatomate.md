---
access_model:
  confidence: high
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Creatomate Agentic Access
  operation_count: 6
  slug: creatomate-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 2
apis:
- description: Create renders and check their status.
  name: Creatomate Renders API
  slug: creatomate-renders-api
- description: List and retrieve project templates.
  name: Creatomate Templates API
  slug: creatomate-templates-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Creatomate Renders API
  slug: open-creatomate-renders-api
- collection_type: open
  name: Creatomate Renders Templates API
  slug: open-creatomate-templates-api
- collection_type: open
  name: Creatomate API
  slug: open-creatomate
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/creatomate-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/creatomate-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/creatomate-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/creatomate
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/creatomate
- group: company
  title: ''
  type: Website
  url: https://creatomate.com/
- group: docs
  title: ''
  type: Documentation
  url: https://creatomate.com/docs/api/quick-start/introduction
- group: commercial
  title: ''
  type: Plans
  url: plans/creatomate-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/creatomate-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/creatomate-finops.yml
created: '2026-06-20'
description: Creatomate is a media-automation platform that generates videos and images at scale from reusable templates. Its REST API renders MP4/GIF/image output by applying per-element modifications to a template, runs asynchronously, and notifies callers via polling or webhooks. Billing is credit-based per rendered output.
finops:
- name: Creatomate Finops
  service_category: Media and Content
  slug: creatomate-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/creatomate.png
layout: provider
modified: '2026-06-20'
name: Creatomate
nav: Providers
network: true
overview: 'Creatomate publishes 2 APIs on the [APIs.io](https://apis.io/) network: Renders API and Templates API. Tagged areas include Media, Video Generation, Image Generation, Automation, and Templates.


  Creatomate''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Creatomate Plans Pricing
  plan_count: 5
  slug: creatomate-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 3
  name: Creatomate Rate Limits
  slug: creatomate-rate-limits
score:
  band: thin
  composite: 37.9
  delta: -1.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 57.7
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 38.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/creatomate/refs/heads/main/screenshots/creatomate-2026-06-20T175219.png
security:
- kind: authentication
  name: Creatomate Authentication
  slug: creatomate-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Creatomate Domain Security
  slug: creatomate-domain-security
  summary_line: TLSv1.3 · DMARC
slug: creatomate
tags:
- Media
- Video Generation
- Image Generation
- Automation
- Templates
- Rendering
website: https://creatomate.com/
---
