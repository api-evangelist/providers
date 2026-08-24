---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: Open-source cloud cost inspector providing cost visibility, optimization recommendations, security checks, and governance across multi-cloud environments. Distributed as a self-hosted dashboard with G
  name: Komiser
  slug: komiser
artifact_total: 5
common:
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/mlabouardy/komiser/blob/develop/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/mlabouardy/komiser/blob/develop/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/mlabouardy/komiser/blob/develop/CONTRIBUTING.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/komiser-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/komiser
- group: company
  title: ''
  type: Website
  url: https://www.komiser.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.komiser.io/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/tailwarden/komiser
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/tailwarden/komiser/releases
- group: operate
  title: ''
  type: Issues
  url: https://github.com/tailwarden/komiser/issues
created: '2026-03-27'
description: Komiser is an open-source, cloud-agnostic resource manager for analyzing and managing cloud cost, usage, security, and governance across multi-cloud environments including AWS, Azure, GCP, DigitalOcean, OCI, Linode, Scaleway, Tencent, MongoDB Atlas, and Kubernetes.
finops:
- name: Komiser Finops
  service_category: API
  slug: komiser-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/komiser.png
layout: provider
modified: '2026-04-28'
name: Komiser
nav: Providers
network: true
overview: 'Komiser publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Cost, FinOps, Governance, Multi-Cloud, and Open-Source.


  Komiser''s developer surface includes documentation, release notes, and 8 more developer resources.'
plans:
- name: Komiser Plans Pricing
  plan_count: 3
  slug: komiser-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Komiser Rate Limits
  slug: komiser-rate-limits
score:
  band: emerging
  composite: 14.5
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 14.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/komiser/refs/heads/main/screenshots/komiser-2026-06-20T184121.png
security:
- kind: domain-security
  name: Komiser Domain Security
  slug: komiser-domain-security
  summary_line: no transport/DNS hardening detected
slug: komiser
tags:
- Cloud Cost
- FinOps
- Governance
- Multi-Cloud
- Open-Source
website: https://www.komiser.io/
---
