---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://interlink-hq.github.io/interLink/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/interlink-hq/interLink
- group: docs
  title: ''
  type: Documentation
  url: https://interlink-hq.github.io/interLink/docs/intro
created: '2025-01-01'
description: interLink is an abstraction layer that extends the Kubernetes Virtual Kubelet interface, enabling pods to execute on remote resources such as HPC batch systems (SLURM, HTCondor), virtual machines, remote Kubernetes clusters, and serverless platforms. It comprises a Virtual Kubelet that converts pod execution requests into remote API calls and a modular interLink API Server with provider-specific sidecar plugins, with built-in OpenTelemetry observability, TLS/mTLS, and OAuth2 authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/interlink.png
layout: provider
modified: '2026-04-28'
name: Interlink
nav: Providers
network: true
overview: 'Interlink is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include HPC, Kubernetes, Multi-Cluster, Networking, and Virtual Kubelet.


  Interlink''s developer surface includes GitHub presence, documentation, and 1 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 7.6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/interlink/refs/heads/main/screenshots/interlink-2026-06-20T183447.png
slug: interlink
tags:
- HPC
- Kubernetes
- Multi-Cluster
- Networking
- Virtual Kubelet
website: https://interlink-hq.github.io/interLink/
---
