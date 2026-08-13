---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: DVC ships as a CLI plus a Python API (`dvc.api`). It tracks data and model files via pointers stored in Git and pushes payloads to remote storage backends (S3, Azure, GCS, SSH, HDFS, HTTP, etc.). Ther
  name: DVC CLI and Python API
  slug: dvc-cli
artifact_total: 5
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/iterative/dvc/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/iterative/dvc/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/treeverse/dvc/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/treeverse/dvc/blob/main/CONTRIBUTING.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dvc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dvc.org/
- group: start
  title: ''
  type: Portal
  url: https://doc.dvc.org/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/iterative/dvc
- group: other
  title: Iterative.ai
  type: ParentOrg
  url: https://iterative.ai/
- group: build
  title: ''
  type: VSCodeExtension
  url: https://marketplace.visualstudio.com/items?itemName=Iterative.dvc
- group: commercial
  title: ''
  type: Plans
  url: plans/dvc-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dvc-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dvc-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://dvc.org/feed/
created: '2026-05-08'
description: DVC (Data Version Control) is an Apache 2.0 open-source CLI and Python library for versioning datasets, models, pipelines, and ML experiments on top of Git. It is not a network service — there is no DVC REST API.
finops:
- name: Dvc Finops
  service_category: ML
  slug: dvc-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dvc.png
layout: provider
modified: '2026-05-08'
name: DVC
nav: Providers
network: true
overview: 'DVC publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include ML, MLOps, Versioning, CLI, and Open Source.


  DVC''s developer surface includes developer portal, engineering blog, and 12 more developer resources.'
plans:
- name: Dvc Plans Pricing
  plan_count: 1
  slug: dvc-plans-pricing
random_paper: 77
rate_limits:
- limit_count: 1
  name: Dvc Rate Limits
  slug: dvc-rate-limits
score:
  band: emerging
  composite: 14.4
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 14.4
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dvc/refs/heads/main/screenshots/dvc-2026-06-20T180328.png
security:
- kind: domain-security
  name: Dvc Domain Security
  slug: dvc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dvc
tags:
- ML
- MLOps
- Versioning
- CLI
- Open Source
website: https://dvc.org/
---
