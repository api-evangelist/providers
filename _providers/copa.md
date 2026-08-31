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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
api_count: 3
apis:
- description: The copa command line interface used to patch container images. The core subcommand `copa patch` accepts an image reference and an optional vulnerability report and produces a new tagged image with OS
  name: Copa CLI
  slug: cli
- description: 'Copa exposes a plugin interface that allows third-party vulnerability scanners to feed reports into the patcher. Out of the box, Copa supports Trivy JSON reports and provides documentation for adding '
  name: Copa Scanner Plugin Interface
  slug: scanner-plugins
- description: 'Copa can emit a Vulnerability Exchange (VEX) document describing which CVEs were patched. VEX documents help security teams and downstream consumers verify that an image has been remediated and track '
  name: Copa VEX Output
  slug: vex
artifact_total: 6
common:
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/project-copacetic/copacetic/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/project-copacetic/copacetic/blob/main/CODE_OF_CONDUCT.md
- group: company
  title: ''
  type: Website
  url: https://project-copacetic.github.io/copacetic/website/
- group: docs
  title: ''
  type: Documentation
  url: https://project-copacetic.github.io/copacetic/website/quick-start/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/project-copacetic/copacetic
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/project-copacetic
- group: operate
  title: ''
  type: Issue Tracker
  url: https://github.com/project-copacetic/copacetic/issues
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/project-copacetic/copacetic/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/project-copacetic/copacetic/blob/main/LICENSE
- group: operate
  title: ''
  type: Community
  url: https://github.com/project-copacetic/copacetic/blob/main/CONTRIBUTING.md
created: '2025-01-01'
description: Project Copacetic (Copa) is an open source command line tool that patches container images directly using BuildKit, without requiring a full image rebuild. Copa parses vulnerability scan reports from Trivy and other scanners, applies the corresponding OS package updates via the appropriate package manager (apt, apk, dnf, tdnf, yum, zypper), and produces a new container image with a patched layer. Copa supports multi-platform images, distroless images, and custom scanner plugins through the Vulnerability Exchange (VEX) and pluggable scanner interface.
finops:
- name: Copa Finops
  service_category: API
  slug: copa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/copa.png
layout: provider
modified: '2026-04-28'
name: Copa (Project Copacetic)
nav: Providers
network: true
overview: 'Copa (Project Copacetic) publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include BuildKit, CLI, CNCF Sandbox, Container Patching, and Containers.


  Copa (Project Copacetic)''s developer surface includes documentation, changelog, and 8 more developer resources.'
plans:
- name: Copa Plans Pricing
  plan_count: 3
  slug: copa-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Copa Rate Limits
  slug: copa-rate-limits
score:
  band: thin
  composite: 27.2
  coverage:
    artifact_dirs: 4
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 8.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 100.0
  previous_composite: 19.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/copa/refs/heads/main/screenshots/copa-2026-06-20T175009.png
slug: copa
tags:
- BuildKit
- CLI
- CNCF Sandbox
- Container Patching
- Containers
- Open-Source
- Security
- Trivy
- Vulnerability Management
website: https://project-copacetic.github.io/copacetic/website/
---
