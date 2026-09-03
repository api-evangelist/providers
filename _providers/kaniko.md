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
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Kaniko is a command-line tool distributed as the container image gcr.io/kaniko-project/executor that builds container images from a Dockerfile. It supports multiple build context sources (GCS, S3, Azu
  name: Kaniko CLI
  slug: kaniko-cli
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://github.com/GoogleContainerTools/kaniko
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/GoogleContainerTools/kaniko/blob/main/README.md
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/GoogleContainerTools/kaniko/blob/main/docs/tutorial.md
- group: other
  title: ''
  type: Development
  url: https://github.com/GoogleContainerTools/kaniko/blob/main/DEVELOPMENT.md
- group: other
  title: ''
  type: Contributing
  url: https://github.com/GoogleContainerTools/kaniko/blob/main/CONTRIBUTING.md
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/GoogleContainerTools/kaniko/releases
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleContainerTools
created: '2026-03-26'
description: Kaniko is an open-source tool from Google that builds container images from a Dockerfile inside a container or Kubernetes cluster without requiring a Docker daemon. It executes each command within a Dockerfile in userspace, enabling secure container builds in environments where running a Docker daemon is impractical or insecure. The project was archived on June 3, 2025, and is now read-only.
finops:
- name: Kaniko Finops
  service_category: API
  slug: kaniko-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kaniko.png
layout: provider
modified: '2026-04-28'
name: Kaniko
nav: Providers
network: true
overview: 'Kaniko publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Archived, Build Tools, CLI, Container Images, and Containers.


  Kaniko''s developer surface includes documentation, getting-started guide, release notes, and 4 more developer resources.'
plans:
- name: Kaniko Plans Pricing
  plan_count: 3
  slug: kaniko-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Kaniko Rate Limits
  slug: kaniko-rate-limits
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 5
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 16.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kaniko/refs/heads/main/screenshots/kaniko-2026-06-20T183915.png
slug: kaniko
tags:
- Archived
- Build Tools
- CLI
- Container Images
- Containers
- Daemonless
- Google
- Kubernetes
- Open-Source
---
