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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Mage Ai Agentic Access
  operation_count: 15
  slug: mage-ai-agentic-access
  summary_line: 15 operations · 9 acting
api_count: 4
apis:
- description: Manage data loader, transformer, and data exporter blocks.
  name: Mage Blocks API
  slug: mage-ai-blocks-api
- description: Trigger pipeline runs and read run status.
  name: Mage Pipeline Runs API
  slug: mage-ai-pipeline-runs-api
- description: Manage triggers (schedule, event, and API triggers).
  name: Mage Pipeline Schedules API
  slug: mage-ai-pipeline-schedules-api
- description: Manage pipelines.
  name: Mage Pipelines API
  slug: mage-ai-pipelines-api
artifact_total: 12
collections:
- collection_type: open
  name: Mage API
  slug: open-mage-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mage-ai-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mage-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mage-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mage-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mage-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/magetech
- group: company
  title: ''
  type: Website
  url: https://www.mage.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mage.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/mage-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mage-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mage-ai-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.mage.ai/blog
created: '2026-06-20'
description: Mage is an open-source data pipeline tool for building, running, and managing data pipelines from transformer, data loader, and data exporter blocks. The self-hosted Mage app exposes a REST API for triggering pipeline runs and managing pipelines, blocks, pipeline runs, and schedules; Mage Pro is the managed cloud edition.
finops:
- name: Mage Ai Finops
  service_category: Analytics
  slug: mage-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mage-ai.png
layout: provider
modified: '2026-06-20'
name: Mage
nav: Providers
network: true
overview: 'Mage publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Blocks API, Pipeline Runs API, Pipeline Schedules API, and 1 more. Tagged areas include Data Pipelines, Orchestration, ETL, Data Engineering, and Open Source.


  Mage''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Mage Ai Plans Pricing
  plan_count: 5
  slug: mage-ai-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 4
  name: Mage Ai Rate Limits
  slug: mage-ai-rate-limits
score:
  band: thin
  composite: 34.9
  delta: -3.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 45.4
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 37.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mage-ai/refs/heads/main/screenshots/mage-ai-2026-06-20T184836.png
security:
- kind: authentication
  name: Mage Ai Authentication
  slug: mage-ai-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Mage Ai Domain Security
  slug: mage-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mage Ai Vulnerability Disclosure
  slug: mage-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: mage-ai
tags:
- Data Pipelines
- Orchestration
- ETL
- Data Engineering
- Open Source
website: https://www.mage.ai
---
