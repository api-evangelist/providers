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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Github Container Registry Agentic Access
  operation_count: 18
  slug: github-container-registry-agentic-access
  summary_line: 18 operations · 7 acting
api_count: 3
apis:
- description: Manage container packages owned by an organization
  name: GitHub Container Registry Organization Packages API
  slug: github-container-registry-organization-packages-api
- description: View packages owned by a user
  name: GitHub Container Registry User Namespace Packages API
  slug: github-container-registry-user-namespace-packages-api
- description: Manage container packages owned by the authenticated user
  name: GitHub Container Registry User Packages API
  slug: github-container-registry-user-packages-api
artifact_total: 10
collections:
- collection_type: open
  name: GitHub Container Registry API
  slug: open-github-container-registry
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/github-container-registry-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/github-container-registry-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://github.com/features/packages
- group: docs
  title: ''
  type: Documentation
  url: https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/github
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.github.com/en/billing/managing-billing-for-github-packages/about-billing-for-github-packages
- group: company
  title: ''
  type: Blog
  url: https://github.blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.githubstatus.com/
- group: start
  title: ''
  type: Signup
  url: https://github.com/signup
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.github.com/llms.txt
created: '2026-03-26'
description: GitHub Container Registry stores container images within your GitHub organization or personal account, allows you to associate images with repositories, and provides fine-grained permissions for managing access. It supports Docker and OCI image formats and is integrated with GitHub Actions for automated workflows.
finops:
- name: Github Container Registry Finops
  service_category: API
  slug: github-container-registry-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/github-container-registry.png
layout: provider
modified: '2026-05-19'
name: GitHub Container Registry
nav: Providers
network: true
overview: 'GitHub Container Registry publishes 3 APIs on the [APIs.io](https://apis.io/) network: Organization Packages API, User Namespace Packages API, and User Packages API. Tagged areas include Container Images, Containers, GitHub, Packages, and Registry.


  The GitHub Container Registry catalog on APIs.io includes 1 Spectral governance ruleset.


  GitHub Container Registry''s developer surface includes authentication, documentation, getting-started guide, pricing, engineering blog, signup flow, and 5 more developer resources.'
plans:
- name: Github Container Registry Plans Pricing
  plan_count: 3
  slug: github-container-registry-plans-pricing
random_paper: 74
rate_limits:
- limit_count: 5
  name: Github Container Registry Rate Limits
  slug: github-container-registry-rate-limits
rules:
- name: GitHub Container Registry API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: github-container-registry-rules
score:
  band: developing
  composite: 44.9
  delta: -2.4
  facets:
    commercial_clarity: 50.0
    contract_quality: 51.7
    developer_ergonomics: 32.6
    discoverability: 74.1
    governance: 10.4
    operational_transparency: 52.6
  previous_composite: 47.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/github-container-registry/refs/heads/main/screenshots/github-container-registry-2026-06-20T181838.png
security:
- kind: authentication
  name: Github Container Registry Authentication
  slug: github-container-registry-authentication
  summary_line: http · 1 scheme
slug: github-container-registry
tags:
- Container Images
- Containers
- GitHub
- Packages
- Registry
---
