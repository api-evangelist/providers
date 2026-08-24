---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
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
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Deepnote Agentic Access
  operation_count: 12
  slug: deepnote-agentic-access
  summary_line: 12 operations · 6 acting
api_count: 6
apis:
- description: Publish and embed Deepnote notebooks and data apps in external sites and dashboards via shareable embed/app URLs. This is a publishing/embedding surface rather than a JSON REST API.
  name: Deepnote Embed
  slug: embed-api
- description: Legacy endpoint to trigger execution of an existing notebook.
  name: Deepnote Execute (v1) API
  slug: deepnote-execute-v1-api
- description: Information about the calling API key and its workspace.
  name: Deepnote Me API
  slug: deepnote-me-api
- description: Notebooks, their blocks, runs, and schedules.
  name: Deepnote Notebooks API
  slug: deepnote-notebooks-api
- description: Projects and their contents.
  name: Deepnote Projects API
  slug: deepnote-projects-api
- description: Notebook executions.
  name: Deepnote Runs API
  slug: deepnote-runs-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Deepnote Public Execute (v1) Execute (v1) Execute (v1) API
  slug: open-deepnote-execute-v1-api
- collection_type: open
  name: Deepnote Public Execute (v1) Execute (v1) Me API
  slug: open-deepnote-me-api
- collection_type: open
  name: Deepnote Public Execute (v1) Execute (v1) Notebooks API
  slug: open-deepnote-notebooks-api
- collection_type: open
  name: Deepnote Public Execute (v1) Execute (v1) Projects API
  slug: open-deepnote-projects-api
- collection_type: open
  name: Deepnote Public Execute (v1) Execute (v1) Runs API
  slug: open-deepnote-runs-api
- collection_type: open
  name: Deepnote Public API
  slug: open-deepnote
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/deepnote-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/deepnote-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/deepnote-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/deepnote-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/deepnote
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/deepnote
- group: company
  title: ''
  type: Website
  url: https://deepnote.com
- group: docs
  title: ''
  type: Documentation
  url: https://deepnote.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/deepnote-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/deepnote-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/deepnote-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://deepnote.com/blog
created: '2026-06-20'
description: Deepnote is a collaborative data-science notebook and analytics/app platform. Its Public API v2 (preview) lets you programmatically run notebooks, poll execution runs, and manage projects, notebooks, files, and integrations, with notebooks also embeddable as data apps. Authentication is a workspace API key sent as a Bearer token.
finops:
- name: Deepnote Finops
  service_category: Analytics and Data Science
  slug: deepnote-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/deepnote.png
layout: provider
modified: '2026-06-20'
name: Deepnote
nav: Providers
network: true
overview: 'Deepnote publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Execute (v1) API, Me API, Notebooks API, and 2 more. Tagged areas include Data Science, Notebooks, Analytics, Collaboration, and Data Apps.


  Deepnote''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Deepnote Plans Pricing
  plan_count: 3
  slug: deepnote-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 3
  name: Deepnote Rate Limits
  slug: deepnote-rate-limits
score:
  band: thin
  composite: 38.6
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 56.5
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 38.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Deepnote Authentication
  slug: deepnote-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Deepnote Domain Security
  slug: deepnote-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Deepnote Vulnerability Disclosure
  slug: deepnote-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: deepnote
tags:
- Data Science
- Notebooks
- Analytics
- Collaboration
- Data Apps
website: https://deepnote.com
---
