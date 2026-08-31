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
api_count: 4
apis:
- description: The official Containerfile reference shipped with the containers/common project. Documents every Containerfile instruction, syntax, and the ways Containerfile differs from Dockerfile, including secret
  name: Containerfile Reference
  slug: reference
- description: The Dockerfile format reference maintained by Docker. Containerfile is a strict superset of Dockerfile, so the Dockerfile reference covers the same instruction set with Docker-specific extensions such
  name: Dockerfile Reference
  slug: dockerfile-reference
- description: 'Dockerfile and Containerfile parsing in modern Docker is performed by BuildKit''s Dockerfile frontend, distributed as a container image (docker/dockerfile). The frontend version is selected via the `# '
  name: BuildKit Dockerfile Frontend
  slug: buildkit-frontend
- description: The Open Container Initiative Image Specification defines the format of the image artifacts that Containerfile and Dockerfile builds produce. The spec covers manifests, configuration, layers, and inde
  name: OCI Image Specification
  slug: oci-image-spec
artifact_total: 9
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/containers/common/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/containers/common/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/containers/common/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/containers/common/blob/main/CODE-OF-CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/containers/common/blob/main/.github/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/containers/common/blob/main/LICENSE
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/containerfile-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/containerfile-domain-security.yml
- group: docs
  title: ''
  type: Specification
  url: https://github.com/containers/common/blob/main/docs/Containerfile.5.md
- group: docs
  title: ''
  type: Documentation
  url: https://docs.docker.com/reference/dockerfile/
- group: docs
  title: ''
  type: Reference
  url: https://github.com/moby/buildkit/blob/master/frontend/dockerfile/docs/reference.md
- group: docs
  title: ''
  type: Reference
  url: https://opencontainers.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/containers
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/containers/buildah
created: '2025-01-01'
description: A Containerfile is a plain text file that contains instructions for building container images. It is fully compatible with Docker's Dockerfile format and is the default file name used by Buildah and Podman. Containerfile instructions describe a base image (FROM), the steps to assemble the image (RUN, COPY, ADD, ARG, ENV), and runtime defaults (CMD, ENTRYPOINT, EXPOSE, USER, WORKDIR, VOLUME). Modern build engines extend the format with cache, secret, and SSH mounts and with platform-aware multi-stage builds.
finops:
- name: Containerfile Finops
  service_category: API
  slug: containerfile-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/containerfile.png
layout: provider
modified: '2026-04-28'
name: Containerfile
nav: Providers
network: true
overview: 'Containerfile publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include BuildKit, Buildah, Containers, DevOps, and Docker.


  Containerfile''s developer surface includes documentation and 13 more developer resources.'
plans:
- name: Containerfile Plans Pricing
  plan_count: 3
  slug: containerfile-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Containerfile Rate Limits
  slug: containerfile-rate-limits
score:
  band: thin
  composite: 26.8
  coverage:
    artifact_dirs: 5
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 8.1
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 100.0
  previous_composite: 18.7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/containerfile/refs/heads/main/screenshots/containerfile-2026-06-20T174922.png
security:
- kind: domain-security
  name: Containerfile Domain Security
  slug: containerfile-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Containerfile Vulnerability Disclosure
  slug: containerfile-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: containerfile
tags:
- BuildKit
- Buildah
- Containers
- DevOps
- Docker
- Dockerfile
- Image Build
- OCI
- Podman
- Standard
---
