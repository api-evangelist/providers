---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Patch Agentic Access
  operation_count: 12
  slug: patch-agentic-access
  summary_line: 12 operations · 7 acting
api_count: 4
apis:
- description: Manage individual line items within draft orders
  name: Patch Order Line Items API
  slug: patch-order-line-items-api
- description: Create and manage carbon offset orders
  name: Patch Orders API
  slug: patch-orders-api
- description: Browse and retrieve carbon removal projects
  name: Patch Projects API
  slug: patch-projects-api
- description: Retrieve available carbon removal technology types
  name: Patch Technology Types API
  slug: patch-technology-types-api
artifact_total: 17
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/patch-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/patch-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/patch-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/patch-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.patch.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.patch.io/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/patch-technology
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usepatch
- group: company
  title: ''
  type: Blog
  url: https://www.patch.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.patch.io/how-it-works
- group: operate
  title: ''
  type: StatusPage
  url: https://status.patch.io
- group: other
  title: ''
  type: X
  url: https://x.com/usepatch
- group: commercial
  title: ''
  type: Plans
  url: plans/patch-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/patch-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/patch-finops.yml
created: '2026-06-13'
description: Patch is a carbon removal and offsetting REST API platform that enables businesses to programmatically purchase high-quality carbon credits and integrate sustainability directly into their products and services. The API provides access to a curated marketplace of vetted carbon removal projects including reforestation, direct air capture, enhanced weathering, and other negative emissions technologies. Developers can embed carbon removal at the order level, calculating emissions estimates and placing orders ranging from a single gram to thousands of tonnes of CO2 equivalent. Patch combines an API-first approach with deep carbon market expertise, diligence, and portfolio management tools to help organizations meet science-based net-zero targets with integrity and transparency.
examples:
- key_count: 4
  name: Patch Create Order Example
  slug: patch-create-order-example
- key_count: 4
  name: Patch Retrieve Projects Example
  slug: patch-retrieve-projects-example
finops:
- name: Patch Finops
  service_category: ''
  slug: patch-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/patch.png
json_schemas:
- name: Patch Order
  property_count: 13
  slug: patch-order
- name: Patch Project
  property_count: 20
  slug: patch-project
jsonld:
- class_count: 30
  name: Patch Context
  property_count: 27
  slug: patch-context
layout: provider
modified: '2026-06-13'
name: Patch
nav: Providers
network: true
overview: 'Patch publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Order Line Items API, Orders API, Projects API, and 1 more. Tagged areas include Carbon, Carbon Credits, Carbon Removal, Carbon Offsets, and Sustainability.


  The Patch catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Patch''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Patch Plans Pricing
  plan_count: 2
  slug: patch-plans-pricing
random_paper: 76
rate_limits:
- limit_count: 0
  name: Patch Rate Limits
  slug: patch-rate-limits
rules:
- name: Patch API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: patch-jsonschema-spectral-rules
score:
  band: developing
  composite: 47.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 72.1
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 47.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/patch/refs/heads/main/screenshots/patch-2026-06-20T191437.png
security:
- kind: authentication
  name: Patch Authentication
  slug: patch-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Patch Domain Security
  slug: patch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Patch Vulnerability Disclosure
  slug: patch-vulnerability-disclosure
  summary_line: disclosure policy published
slug: patch
tags:
- Carbon
- Carbon Credits
- Carbon Removal
- Carbon Offsets
- Sustainability
- Climate Tech
- Net Zero
- ESG
website: https://www.patch.io/
---
