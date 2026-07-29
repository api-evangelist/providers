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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
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
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 115
  human_in_the_loop: 8
  name: Podman Agentic Access
  operation_count: 193
  slug: podman-agentic-access
  summary_line: 193 operations · 115 acting · 8 human-in-the-loop
api_count: 18
apis:
- description: Actions related to artifacts
  name: Podman artifacts API
  slug: podman-artifacts-api
- description: Actions related to containers
  name: Podman containers API
  slug: podman-containers-api
- description: Actions related to containers for the compatibility endpoints
  name: Podman containers (compat) API
  slug: podman-containers-compat-api
- description: Actions related to exec
  name: Podman exec API
  slug: podman-exec-api
- description: Actions related to exec for the compatibility endpoints
  name: Podman exec (compat) API
  slug: podman-exec-compat-api
- description: Actions related to images
  name: Podman images API
  slug: podman-images-api
- description: Actions related to images for the compatibility endpoints
  name: Podman images (compat) API
  slug: podman-images-compat-api
- description: Actions related to manifests
  name: Podman manifests API
  slug: podman-manifests-api
- description: Actions related to networks
  name: Podman networks API
  slug: podman-networks-api
- description: Actions related to networks for the compatibility endpoints
  name: Podman networks (compat) API
  slug: podman-networks-compat-api
- description: Actions related to pods
  name: Podman pods API
  slug: podman-pods-api
- description: The quadlets API from Podman — 5 operation(s) for quadlets.
  name: Podman quadlets API
  slug: podman-quadlets-api
- description: Actions related to secrets
  name: Podman secrets API
  slug: podman-secrets-api
- description: Actions related to secrets for the compatibility endpoints
  name: Podman secrets (compat) API
  slug: podman-secrets-compat-api
- description: Actions related to Podman engine
  name: Podman system API
  slug: podman-system-api
- description: Actions related to Podman and compatibility engines
  name: Podman system (compat) API
  slug: podman-system-compat-api
- description: Actions related to volumes
  name: Podman volumes API
  slug: podman-volumes-api
- description: Actions related to volumes for the compatibility endpoints
  name: Podman volumes (compat) API
  slug: podman-volumes-compat-api
artifact_total: 24
collections:
- collection_type: open
  name: supports a RESTful API for the Libpod library
  slug: open-podman
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/podman-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/podman-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://podman.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.podman.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/containers
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/containers/podman
- group: company
  title: ''
  type: Blog
  url: https://podman.io/blogs/
- group: operate
  title: ''
  type: Community
  url: https://podman.io/community/
- group: start
  title: ''
  type: GettingStarted
  url: https://podman.io/get-started
created: '2026-03-16'
description: Podman is a daemonless, open-source container engine for developing, managing, and running OCI containers on Linux, supporting both rootful and rootless operation as a drop-in replacement for Docker. The Podman REST API exposes a Docker-compatible surface alongside Libpod-specific endpoints for pods, volumes, networks, secrets, generators, and system management.
finops:
- name: Podman Finops
  service_category: API
  slug: podman-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/podman.png
layout: provider
modified: '2026-05-19'
name: Podman
nav: Providers
network: true
overview: 'Podman publishes 18 APIs on the [APIs.io](https://apis.io/) network, including artifacts API, containers API, containers (compat) API, and 15 more. Tagged areas include Cloud Native, Containers, DevOps, OCI, and Open Source.


  Podman''s developer surface includes documentation, engineering blog, getting-started guide, and 6 more developer resources.'
plans:
- name: Podman Plans Pricing
  plan_count: 3
  slug: podman-plans-pricing
random_paper: 72
rate_limits:
- limit_count: 5
  name: Podman Rate Limits
  slug: podman-rate-limits
score:
  band: thin
  composite: 33.4
  delta: -3.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 32.3
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 37.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 18
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/podman/refs/heads/main/screenshots/podman-2026-06-20T191837.png
security:
- kind: domain-security
  name: Podman Domain Security
  slug: podman-domain-security
  summary_line: TLSv1.3 · DMARC
slug: podman
tags:
- Cloud Native
- Containers
- DevOps
- OCI
- Open Source
website: https://podman.io/
---
