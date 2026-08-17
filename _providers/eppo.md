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
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Eppo Agentic Access
  operation_count: 13
  slug: eppo-agentic-access
  summary_line: 13 operations · 7 acting
api_count: 6
apis:
- description: Eppo Cloud REST API provides programmatic access to feature flags, experiments, allocations, metrics, and assignments configuration.
  name: Eppo Cloud REST API
  slug: eppo-cloud-api
- description: The Allocations API from Eppo — 1 operation(s) for allocations.
  name: Eppo Allocations API
  slug: eppo-allocations-api
- description: The Assignments API from Eppo — 1 operation(s) for assignments.
  name: Eppo Assignments API
  slug: eppo-assignments-api
- description: The Experiments API from Eppo — 2 operation(s) for experiments.
  name: Eppo Experiments API
  slug: eppo-experiments-api
- description: The Flags API from Eppo — 2 operation(s) for flags.
  name: Eppo Flags API
  slug: eppo-flags-api
- description: The Metrics API from Eppo — 1 operation(s) for metrics.
  name: Eppo Metrics API
  slug: eppo-metrics-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Eppo Cloud REST Allocations API
  slug: open-eppo-allocations-api
- collection_type: open
  name: Eppo Cloud REST Allocations Assignments API
  slug: open-eppo-assignments-api
- collection_type: open
  name: Eppo Cloud REST Allocations Experiments API
  slug: open-eppo-experiments-api
- collection_type: open
  name: Eppo Cloud REST Allocations Flags API
  slug: open-eppo-flags-api
- collection_type: open
  name: Eppo Cloud REST Allocations Metrics API
  slug: open-eppo-metrics-api
- collection_type: open
  name: Eppo Cloud REST API
  slug: open-eppo
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/eppo-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/eppo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eppo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/eppo-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/eppo-exp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/geteppo
- group: company
  title: ''
  type: Website
  url: https://www.geteppo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://eppo.cloud/api/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/eppo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/eppo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/eppo-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.geteppo.com/blog
created: '2026-05-08'
description: Eppo is a next-generation feature flagging and experimentation platform built for warehouse-native analytics and rigorous experimentation.
finops:
- name: Eppo Finops
  service_category: A/B Testing
  slug: eppo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eppo.png
layout: provider
modified: '2026-05-08'
name: Eppo
nav: Providers
network: true
overview: 'Eppo publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Allocations API, Assignments API, Experiments API, and 2 more. Tagged areas include Experimentation, Feature Flags, AB Testing, Analytics, and Statistics.


  Eppo''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Eppo Plans Pricing
  plan_count: 1
  slug: eppo-plans-pricing
random_paper: 138
rate_limits:
- limit_count: 1
  name: Eppo Rate Limits
  slug: eppo-rate-limits
score:
  band: thin
  composite: 28.6
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 55.2
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 28.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eppo/refs/heads/main/screenshots/eppo-2026-06-20T180759.png
security:
- kind: authentication
  name: Eppo Authentication
  slug: eppo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Eppo Domain Security
  slug: eppo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Eppo Vulnerability Disclosure
  slug: eppo-vulnerability-disclosure
  summary_line: disclosure policy published
slug: eppo
tags:
- Experimentation
- Feature Flags
- AB Testing
- Analytics
- Statistics
website: https://www.geteppo.com/
---
