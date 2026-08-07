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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: Distroless images by Google contain only the application and its runtime dependencies, stripping out package managers, shells, and other OS-level utilities to minimize attack surface and image size.
  name: Distroless
  slug: distroless
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://github.com/GoogleContainerTools/distroless
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleContainerTools
- group: start
  title: ''
  type: Container Registry
  url: https://gcr.io/distroless
- group: operate
  title: ''
  type: Issues
  url: https://github.com/GoogleContainerTools/distroless/issues
created: '2026-03-26'
description: Distroless images by Google contain only the application and its runtime dependencies, stripping out package managers, shells, and other OS-level utilities to minimize attack surface and image size. The smallest variant (gcr.io/distroless/static-debian12) is roughly 2 MB. Distroless ships base images for static binaries, glibc-based binaries, C/C++, Java (17, 21, 25), Node.js (22, 24), and Python 3, with multi-architecture support including amd64, arm64, arm, s390x, ppc64le, and riscv64. Adopters include Kubernetes, Knative, Tekton, and Teleport.
finops:
- name: Distroless Finops
  service_category: API
  slug: distroless-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/distroless.png
layout: provider
modified: '2026-04-28'
name: Distroless
nav: Providers
network: true
overview: Distroless publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Native, Container Images, Containers, Google, and Security.
plans:
- name: Distroless Plans Pricing
  plan_count: 3
  slug: distroless-plans-pricing
random_paper: 83
rate_limits:
- limit_count: 5
  name: Distroless Rate Limits
  slug: distroless-rate-limits
score:
  band: emerging
  composite: 18.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 18.6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/distroless/refs/heads/main/screenshots/distroless-2026-06-20T180057.png
slug: distroless
tags:
- Cloud Native
- Container Images
- Containers
- Google
- Security
---
