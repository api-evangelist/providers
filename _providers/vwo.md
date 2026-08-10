---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Vwo Agentic Access
  operation_count: 12
  slug: vwo-agentic-access
  summary_line: 12 operations · 5 acting
api_count: 5
apis:
- description: VWO Data API exposes account data, campaign and goal configuration, reporting, and segmentation across the VWO experimentation platform.
  name: VWO Data API
  slug: vwo-data-api
- description: A/B, split, and personalization campaigns.
  name: VWO Campaigns API
  slug: vwo-campaigns-api
- description: Feature management (FME) feature flags and rules.
  name: VWO Feature Flags API
  slug: vwo-feature-flags-api
- description: Metric and campaign reports.
  name: VWO Reports API
  slug: vwo-reports-api
- description: Websites configured under an account.
  name: VWO Websites API
  slug: vwo-websites-api
artifact_total: 13
collections:
- collection_type: open
  name: VWO Data API
  slug: open-vwo
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vwo-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/vwo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vwo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vwo-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wingify
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vwo
- group: company
  title: ''
  type: Website
  url: https://vwo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.vwo.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/vwo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vwo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/vwo-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://vwo.com/blog/feed/
created: '2026-05-08'
description: VWO is a digital experience optimization platform offering A/B testing, personalization, feature management, behavior analytics, and insights.
finops:
- name: Vwo Finops
  service_category: A/B Testing
  slug: vwo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vwo.png
layout: provider
modified: '2026-05-08'
name: VWO
nav: Providers
network: true
overview: 'VWO publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Campaigns API, Feature Flags API, Reports API, and 1 more. Tagged areas include Experimentation, AB Testing, Personalization, Conversion Optimization, and Feature Flags.


  VWO''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Vwo Plans Pricing
  plan_count: 1
  slug: vwo-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Vwo Rate Limits
  slug: vwo-rate-limits
score:
  band: thin
  composite: 34.6
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 58.5
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 34.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vwo/refs/heads/main/screenshots/vwo-2026-06-20T201152.png
security:
- kind: authentication
  name: Vwo Authentication
  slug: vwo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Vwo Domain Security
  slug: vwo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Vwo Vulnerability Disclosure
  slug: vwo-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: vwo
tags:
- Experimentation
- AB Testing
- Personalization
- Conversion Optimization
- Feature Flags
website: https://vwo.com/
---
