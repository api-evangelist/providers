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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Drop-in faster GitHub-hosted runner replacement selected by changing the runs-on tag (e.g. blacksmith-2vcpu-ubuntu-2404). Linux/Windows jobs run in ephemeral Firecracker microVMs; x64, ARM64, and macO
  name: Blacksmith GitHub Actions Runners
  slug: github-actions-runners
- description: Accelerated Docker image builds via Blacksmith's BuildKit and the useblacksmith/build-push-action and useblacksmith/setup-docker-builder GitHub Actions, reusing cached layers on sticky disks to rebuil
  name: Blacksmith Docker Builds
  slug: docker-builds
- description: Co-located CI cache that transparently backs official GitHub and popular third-party cache actions (e.g. actions/cache, useblacksmith/cache) at roughly 400MB/s, plus Sticky Disks, container init pre-h
  name: Blacksmith Cache
  slug: cache
- description: Command-line interface (beta) that lets coding agents run CI against local changes instantly - blacksmith testbox warmup/run/status dispatch a workflow to a warm microVM, rsync local changes, and exec
  name: Blacksmith Testbox CLI
  slug: testbox-cli
- description: 'Web dashboard at app.blacksmith.sh for organization setup, runner and cache management, and observability - CI analytics, run history, logs, machine metrics, monitors, SSH access, and test analytics. '
  name: Blacksmith Dashboard and Observability
  slug: dashboard
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Blacksmith
  slug: open-blacksmith-sh
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/blacksmith-sh-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blacksmith-sh-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/blacksmith-sh-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/blacksmith-sh-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/useblacksmith
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/useblacksmith
- group: company
  title: ''
  type: Website
  url: https://www.blacksmith.sh/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blacksmith.sh
- group: start
  title: ''
  type: Console
  url: https://app.blacksmith.sh
- group: operate
  title: ''
  type: Status
  url: https://status.blacksmith.sh
- group: commercial
  title: ''
  type: Plans
  url: plans/blacksmith-sh-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/blacksmith-sh-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/blacksmith-sh-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.blacksmith.sh/blog
created: '2026-06-20'
description: Blacksmith runs your GitHub Actions up to 2x faster at half the cost on a fleet of modern gaming-CPU bare metal, booting ephemeral Firecracker microVMs in under three seconds. It is a drop-in replacement integrated as a GitHub App and selected via runs-on runner tags, with a co-located CI cache, 40x faster Docker layer caching, sticky disks, an observability dashboard, and a Testbox CLI. Blacksmith does not publish a general-purpose public REST API - integration is GitHub-App, YAML runner-tag, and GitHub Actions based.
finops:
- name: Blacksmith Sh Finops
  service_category: Developer Tools
  slug: blacksmith-sh-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/blacksmith-sh.png
layout: provider
modified: '2026-06-20'
name: Blacksmith
nav: Providers
network: true
overview: 'Blacksmith publishes 3 APIs on the [APIs.io](https://apis.io/) network: GitHub Actions Runners, Docker Builds, and Cache. Tagged areas include CI/CD, GitHub Actions, Runners, Caching, and Docker.


  Blacksmith''s developer surface includes authentication, documentation, developer console, status page, engineering blog, and 9 more developer resources.'
plans:
- name: Blacksmith Sh Plans Pricing
  plan_count: 4
  slug: blacksmith-sh-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 4
  name: Blacksmith Sh Rate Limits
  slug: blacksmith-sh-rate-limits
scopes:
- name: Blacksmith Sh Scopes
  scope_count: 0
  slug: blacksmith-sh-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 34.0
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 27.9
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 34.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blacksmith-sh/refs/heads/main/screenshots/blacksmith-sh-2026-06-20T173338.png
security:
- kind: authentication
  name: Blacksmith Sh Authentication
  slug: blacksmith-sh-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Blacksmith Sh Domain Security
  slug: blacksmith-sh-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Blacksmith Sh Trust Center
  slug: blacksmith-sh-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: blacksmith-sh
tags:
- CI/CD
- GitHub Actions
- Runners
- Caching
- Docker
website: https://www.blacksmith.sh/
---
