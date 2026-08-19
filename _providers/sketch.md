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
api_count: 1
apis:
- description: REST API for managing Sketch workspaces, members, and documents in the Sketch cloud collaboration platform. Supports Personal Access Token and OAuth 2.0 authentication with scopes for reading and writ
  name: Sketch Cloud API
  slug: sketch-cloud-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/sketch-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sketch-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sketch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sketch.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.sketch.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/sketch-hq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sketchbv
- group: company
  title: ''
  type: Blog
  url: https://www.sketch.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sketch.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sketch.com/
- group: other
  title: ''
  type: X
  url: https://x.com/sketch
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/sketch/refs/heads/main/plans/sketch-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/sketch/refs/heads/main/rate-limits/sketch-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/sketch/refs/heads/main/finops/sketch-finops.yml
created: '2026-06-13'
description: Sketch is a digital design tool for Mac providing a REST API for managing workspaces, documents, libraries, components, prototypes, and share links in the Sketch cloud collaboration environment. The Cloud REST API (api.sketch.cloud/v1) supports Personal Access Token and OAuth 2.0 authentication, enabling workspace member management, document access, and SCIM provisioning for enterprise identity workflows.
finops:
- name: Sketch Finops
  service_category: ''
  slug: sketch-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sketch.png
layout: provider
modified: '2026-06-13'
name: Sketch
nav: Providers
network: true
overview: 'Sketch publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Design, Collaboration, Prototyping, Workspaces, and Documents.


  Sketch''s developer surface includes documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Sketch Plans Pricing
  plan_count: 5
  slug: sketch-plans-pricing
random_paper: 46
rate_limits:
- limit_count: 0
  name: Sketch Rate Limits
  slug: sketch-rate-limits
score:
  band: emerging
  composite: 21.5
  delta: -1.9
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 23.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sketch/refs/heads/main/screenshots/sketch-2026-06-20T194008.png
security:
- kind: domain-security
  name: Sketch Domain Security
  slug: sketch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sketch Vulnerability Disclosure
  slug: sketch-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Sketch Trust Center
  slug: sketch-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: sketch
tags:
- Design
- Collaboration
- Prototyping
- Workspaces
- Documents
- Libraries
- Components
website: https://www.sketch.com/
---
