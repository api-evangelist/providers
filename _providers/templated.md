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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Templated Agentic Access
  operation_count: 6
  slug: templated-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 2
apis:
- description: The Renders API from Templated — 3 operation(s) for renders.
  name: Templated Renders API
  slug: templated-renders-api
- description: The Templates API from Templated — 2 operation(s) for templates.
  name: Templated Templates API
  slug: templated-templates-api
artifact_total: 9
collections:
- collection_type: open
  name: Templated API
  slug: open-templated
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/templated-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/templated-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/templated-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/templated-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/templated-io
- group: company
  title: ''
  type: Website
  url: https://templated.io/
- group: docs
  title: ''
  type: Documentation
  url: https://templated.io/docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/templated-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/templated-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/templated-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://templated.io/rss.xml
created: '2026-06-25'
description: Templated is an API for automated image, video, and PDF generation from reusable templates. Designers build templates in a drag-and-drop editor, then the REST API renders them at scale by overriding layer content, with synchronous and asynchronous rendering, batch and multi-page output, and webhook callbacks.
finops:
- name: Templated Finops
  service_category: Media and Content Generation
  slug: templated-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/templated.png
layout: provider
modified: '2026-06-25'
name: Templated
nav: Providers
network: true
overview: 'Templated publishes 2 APIs on the [APIs.io](https://apis.io/) network: Renders API and Templates API. Tagged areas include Image Generation, PDF Generation, Templates, Rendering, and Automation.


  Templated''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Templated Plans Pricing
  plan_count: 4
  slug: templated-plans-pricing
random_paper: 42
rate_limits:
- limit_count: 3
  name: Templated Rate Limits
  slug: templated-rate-limits
score:
  band: thin
  composite: 37.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.4
    developer_ergonomics: 21.7
    discoverability: 60.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 37.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Templated Authentication
  slug: templated-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Templated Domain Security
  slug: templated-domain-security
  summary_line: TLSv1.3 · DMARC
slug: templated
tags:
- Image Generation
- PDF Generation
- Templates
- Rendering
- Automation
website: https://templated.io/
---
