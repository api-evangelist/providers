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
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 1
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/ratify-project/ratify/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ratify-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ratify.dev
- group: docs
  title: ''
  type: Documentation
  url: https://ratify.dev/docs/what-is-ratify
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ratify-project/ratify
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/ratify-project
- group: build
  title: ''
  type: PackageManager
  url: https://artifacthub.io/packages/helm/ratify/ratify
- group: company
  title: ''
  type: Blog
  url: https://ratify.dev/blog/rss.xml
created: '2025-01-01'
description: Ratify is a CNCF Sandbox open-source verification framework for container images and other supply chain artifacts in Kubernetes environments. It enables policy-driven artifact ratification by coordinating any number of pluggable verifiers (signatures, SBOMs, scan results, attestations) against a given policy, integrating with Kubernetes admission webhooks via the Gatekeeper policy engine. Ratify is developed by the ratify-project GitHub organization (originally a Microsoft open-source project), written in Go, and distributed as a CLI tool, Go library, and Kubernetes admission webhook server. It supports OCI-compliant artifact stores including Azure Container Registry, Amazon ECR, and Docker Hub. Ratify exposes an internal HTTP verification API (v2alpha1) consumed by its webhook server but does not publish a public-facing REST API or OpenAPI specification.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ratify.png
layout: provider
modified: '2026-05-02'
name: Ratify
nav: Providers
network: true
overview: 'Ratify is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artifact Verification, CNCF, Cloud-Native, Container Security, and Kubernetes.


  Ratify''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 5.4
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 5.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ratify/refs/heads/main/screenshots/ratify-2026-06-20T192607.png
security:
- kind: domain-security
  name: Ratify Domain Security
  slug: ratify-domain-security
  summary_line: TLSv1.3 · HSTS
slug: ratify
tags:
- Artifact Verification
- CNCF
- Cloud-Native
- Container Security
- Kubernetes
- Open-Source
- Policy Enforcement
- Security
- Supply Chain
website: https://ratify.dev
---
