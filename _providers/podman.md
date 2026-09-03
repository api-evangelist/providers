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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 115
  human_in_the_loop: 8
  name: Podman Agentic Access
  operation_count: 193
  slug: podman-agentic-access
  summary_line: 193 operations · 115 acting · 8 human-in-the-loop
api_count: 1
apis:
- baseURL: http://d/v6.0.0/libpod
  baseurl_source: declared
  description: Actions related to artifacts
  name: Podman artifacts API
  slug: podman-artifacts-api
- baseURL: http://d/v6.0.0/libpod
  baseurl_source: declared
  description: Actions related to containers
  name: Podman containers API
  slug: podman-containers-api
- baseURL: http://d/v6.0.0/libpod
  baseurl_source: declared
  description: Actions related to containers for the compatibility endpoints
  name: Podman containers (compat) API
  slug: podman-containers-compat-api
- baseURL: http://d/v6.0.0/libpod
  baseurl_source: declared
  description: Actions related to exec
  name: Podman exec API
  slug: podman-exec-api
- baseURL: http://d/v6.0.0/libpod
  baseurl_source: declared
  description: Actions related to exec for the compatibility endpoints
  name: Podman exec (compat) API
  slug: podman-exec-compat-api
- baseURL: http://d/v6.0.0/libpod
  baseurl_source: declared
  description: Actions related to images
  name: Podman images API
  slug: podman-images-api
- baseURL: http://d/v6.0.0/libpod
  baseurl_source: declared
  description: Actions related to images for the compatibility endpoints
  name: Podman images (compat) API
  slug: podman-images-compat-api
- baseURL: http://d/v6.0.0/libpod
  baseurl_source: declared
  description: Actions related to manifests
  name: Podman manifests API
  slug: podman-manifests-api
- baseURL: http://d/v6.0.0/libpod
  baseurl_source: declared
  description: Actions related to networks
  name: Podman networks API
  slug: podman-networks-api
- baseURL: http://d/v6.0.0/libpod
  baseurl_source: declared
  description: Actions related to networks for the compatibility endpoints
  name: Podman networks (compat) API
  slug: podman-networks-compat-api
- baseURL: http://d/v6.0.0/libpod
  baseurl_source: declared
  description: Actions related to pods
  name: Podman pods API
  slug: podman-pods-api
- baseURL: http://d/v6.0.0/libpod
  baseurl_source: declared
  description: The quadlets API from Podman — 5 operation(s) for quadlets.
  name: Podman quadlets API
  slug: podman-quadlets-api
- baseURL: http://d/v6.0.0/libpod
  baseurl_source: declared
  description: Actions related to secrets
  name: Podman secrets API
  slug: podman-secrets-api
- baseURL: http://d/v6.0.0/libpod
  baseurl_source: declared
  description: Actions related to secrets for the compatibility endpoints
  name: Podman secrets (compat) API
  slug: podman-secrets-compat-api
- baseURL: http://d/v6.0.0/libpod
  baseurl_source: declared
  description: Actions related to Podman engine
  name: Podman system API
  slug: podman-system-api
- baseURL: http://d/v6.0.0/libpod
  baseurl_source: declared
  description: Actions related to Podman and compatibility engines
  name: Podman system (compat) API
  slug: podman-system-compat-api
- baseURL: http://d/v6.0.0/libpod
  baseurl_source: declared
  description: Actions related to volumes
  name: Podman volumes API
  slug: podman-volumes-api
- baseURL: http://d/v6.0.0/libpod
  baseurl_source: declared
  description: Actions related to volumes for the compatibility endpoints
  name: Podman volumes (compat) API
  slug: podman-volumes-compat-api
artifact_total: 43
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: supports a RESTful API for the Libpod library artifacts API
  slug: open-podman-artifacts-api
- collection_type: open
  name: supports a RESTful API for the Libpod library artifacts containers API
  slug: open-podman-containers-api
- collection_type: open
  name: supports a RESTful API for the Libpod library artifacts containers (compat) API
  slug: open-podman-containers-compat-api
- collection_type: open
  name: supports a RESTful API for the Libpod library artifacts exec API
  slug: open-podman-exec-api
- collection_type: open
  name: supports a RESTful API for the Libpod library artifacts exec (compat) API
  slug: open-podman-exec-compat-api
- collection_type: open
  name: supports a RESTful API for the Libpod library artifacts images API
  slug: open-podman-images-api
- collection_type: open
  name: supports a RESTful API for the Libpod library artifacts images (compat) API
  slug: open-podman-images-compat-api
- collection_type: open
  name: supports a RESTful API for the Libpod library artifacts manifests API
  slug: open-podman-manifests-api
- collection_type: open
  name: supports a RESTful API for the Libpod library artifacts networks API
  slug: open-podman-networks-api
- collection_type: open
  name: supports a RESTful API for the Libpod library artifacts networks (compat) API
  slug: open-podman-networks-compat-api
- collection_type: open
  name: supports a RESTful API for the Libpod library artifacts pods API
  slug: open-podman-pods-api
- collection_type: open
  name: supports a RESTful API for the Libpod library artifacts quadlets API
  slug: open-podman-quadlets-api
- collection_type: open
  name: supports a RESTful API for the Libpod library artifacts secrets API
  slug: open-podman-secrets-api
- collection_type: open
  name: supports a RESTful API for the Libpod library artifacts secrets (compat) API
  slug: open-podman-secrets-compat-api
- collection_type: open
  name: supports a RESTful API for the Libpod library artifacts system API
  slug: open-podman-system-api
- collection_type: open
  name: supports a RESTful API for the Libpod library artifacts system (compat) API
  slug: open-podman-system-compat-api
- collection_type: open
  name: supports a RESTful API for the Libpod library artifacts volumes API
  slug: open-podman-volumes-api
- collection_type: open
  name: supports a RESTful API for the Libpod library artifacts volumes (compat) API
  slug: open-podman-volumes-compat-api
- collection_type: open
  name: supports a RESTful API for the Libpod library
  slug: open-podman
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/containers/podman/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/containers/podman/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/podman-container-tools/podman/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/podman-container-tools/podman/blob/main/CODE-OF-CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/podman-container-tools/podman/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/containers/podman/blob/main/LICENSE
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
overview: 'Podman publishes 18 APIs on the [APIs.io](https://apis.io/) network, including artifacts API, containers API, containers (compat) API, and 15 more. Tagged areas include Cloud-Native, Containers, DevOps, OCI, and Open-Source.


  Podman''s developer surface includes documentation, engineering blog, getting-started guide, and 12 more developer resources.'
plans:
- name: Podman Plans Pricing
  plan_count: 3
  slug: podman-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Podman Rate Limits
  slug: podman-rate-limits
score:
  band: thin
  composite: 39.2
  coverage:
    artifact_dirs: 9
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 51.5
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 100.0
  previous_composite: 39.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/podman/refs/heads/main/screenshots/podman-2026-06-20T191837.png
security:
- kind: domain-security
  name: Podman Domain Security
  slug: podman-domain-security
  summary_line: TLSv1.3 · DMARC
slug: podman
tags:
- Cloud-Native
- Containers
- DevOps
- OCI
- Open-Source
website: https://podman.io/
---
