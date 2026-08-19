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
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 18
  human_in_the_loop: 4
  name: Kubescape Agentic Access
  operation_count: 23
  slug: kubescape-agentic-access
  summary_line: 23 operations · 18 acting · 4 human-in-the-loop
api_count: 7
apis:
- description: The open-source Kubescape Operator's in-cluster components (storage, kubevuln, gateway, operator, node-agent) each expose an OpenAPI/Swagger-documented HTTP API reachable inside the cluster at /openap
  name: Kubescape In-Cluster Component API (Open Source)
  slug: kubescape-in-cluster-component-api
- description: Agent access keys and exception policies.
  name: Kubescape Access Keys API
  slug: kubescape-access-keys-api
- description: Generated NetworkPolicies and seccomp profiles.
  name: Kubescape Network Policies API
  slug: kubescape-network-policies-api
- description: Framework, control, and resource posture results.
  name: Kubescape Posture & Compliance API
  slug: kubescape-posture-compliance-api
- description: Registry scans and Git repository posture.
  name: Kubescape Registry & Repository API
  slug: kubescape-registry-repository-api
- description: Runtime incidents, attack chains, and security risks.
  name: Kubescape Runtime Security API
  slug: kubescape-runtime-security-api
- description: Image and workload vulnerability scanning and results.
  name: Kubescape Vulnerabilities API
  slug: kubescape-vulnerabilities-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ARMO Platform Customer API (Kubescape) Access Keys API
  slug: open-kubescape-access-keys-api
- collection_type: open
  name: ARMO Platform Customer API (Kubescape) Access Keys Network Policies API
  slug: open-kubescape-network-policies-api
- collection_type: open
  name: ARMO Platform Customer API (Kubescape) Access Keys Posture & Compliance API
  slug: open-kubescape-posture-compliance-api
- collection_type: open
  name: ARMO Platform Customer API (Kubescape) Access Keys Registry & Repository API
  slug: open-kubescape-registry-repository-api
- collection_type: open
  name: ARMO Platform Customer API (Kubescape) Access Keys Runtime Security API
  slug: open-kubescape-runtime-security-api
- collection_type: open
  name: ARMO Platform Customer API (Kubescape) Access Keys Vulnerabilities API
  slug: open-kubescape-vulnerabilities-api
- collection_type: open
  name: ARMO Platform Customer API (Kubescape)
  slug: open-kubescape
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kubescape-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kubescape-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kubescape-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kubescape
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/armosec
- group: company
  title: ''
  type: Website
  url: https://kubescape.io
- group: docs
  title: ''
  type: Documentation
  url: https://kubescape.io/docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/kubescape-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kubescape-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/kubescape-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://kubescape.io/blog/
created: '2026-07-11'
description: Kubescape is an open-source (Apache 2.0) Kubernetes security platform and CNCF incubating project, originally contributed by ARMO. It provides risk analysis, security and compliance posture scanning, misconfiguration detection, image and runtime vulnerability scanning, and eBPF-based runtime threat detection across the IDE, CI/CD pipelines, and live clusters. The core Kubescape is a CLI and an in-cluster Operator whose components expose OpenAPI/Swagger-documented HTTP APIs in-cluster (there is no single hosted public REST endpoint for the open-source tool). ARMO Platform is the commercial multi-cluster, multi-cloud SaaS built on Kubescape and exposes a documented hosted Customer API (base https://api.armosec.io) for posture, compliance, vulnerabilities, runtime incidents, attack paths, network policies, and registry/repository scanning, authenticated with an X-API-KEY access key.
finops:
- name: Kubescape Finops
  service_category: Security and Compliance
  slug: kubescape-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kubescape.png
layout: provider
modified: '2026-07-11'
name: Kubescape
nav: Providers
network: true
overview: 'Kubescape publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Access Keys API, Network Policies API, Posture & Compliance API, and 3 more. Tagged areas include Kubernetes Security, Cloud Native Security, Container Security, DevSecOps, and Kubernetes.


  Kubescape''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Kubescape Plans Pricing
  plan_count: 4
  slug: kubescape-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 4
  name: Kubescape Rate Limits
  slug: kubescape-rate-limits
score:
  band: thin
  composite: 38.1
  delta: -0.7
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 54.5
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 38.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kubescape/refs/heads/main/screenshots/kubescape-2026-07-25T224314.png
security:
- kind: authentication
  name: Kubescape Authentication
  slug: kubescape-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Kubescape Domain Security
  slug: kubescape-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kubescape
tags:
- Kubernetes Security
- Cloud Native Security
- Container Security
- DevSecOps
- Kubernetes
- Vulnerability Scanning
- Compliance
- Runtime Security
- CNCF
- Open Source
website: https://kubescape.io
---
