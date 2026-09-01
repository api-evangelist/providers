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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/weaveworks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.weave.works
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/weaveworks
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gitops.weaveworks.org
- group: build
  title: ''
  type: Packages
  url: packages/weaveworks-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/weaveworks-cli.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/weaveworks-lifecycle.yml
created: '2026-07-17'
description: Weaveworks was the cloud-native company that coined the term "GitOps" and built the Weave family of open-source infrastructure tooling — Weave Net (multi-host container networking), Weave Scope (Docker/Kubernetes visualization and monitoring), Weave GitOps, and the widely used eksctl CLI for Amazon EKS. Backed by Accel and GV, the company ceased commercial operations in February 2024 after a planned acquisition fell through. It shipped no hosted REST API or client SDKs; its public surface was open-source Go tooling. Following the shutdown, Flux CD moved to the CNCF (graduated), eksctl transferred to the eksctl-io org jointly maintained with AWS, and the remaining Weave repositories became community-driven under the github.com/weaveworks organization. The former company website (weave.works) has lapsed and now redirects to a parked page.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/weaveworks.png
layout: provider
modified: '2026-07-21'
name: Weaveworks
nav: Providers
network: true
overview: 'Weaveworks is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Developer Tools, GitOps, Kubernetes, and Container Networking.


  Weaveworks'' developer surface includes documentation, CLI, and 5 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 8.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Weaveworks Domain Security
  slug: weaveworks-domain-security
  summary_line: TLSv1.3
slug: weaveworks
tags:
- Company
- Developer Tools
- GitOps
- Kubernetes
- Container Networking
- Cloud-Native
- Open-Source
- DevOps
website: http://www.weave.works
---
