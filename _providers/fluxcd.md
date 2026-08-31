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
    agent_skills: true
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
  score: 6.1
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Flux is a set of continuous and progressive delivery solutions for Kubernetes that are open and extensible, enabling GitOps-based automation for keeping Kubernetes clusters in sync with sources of con
  name: Flux CD
  slug: fluxcd
artifact_total: 11
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fluxcd-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fluxcd-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fluxcd.io/
- group: docs
  title: ''
  type: Documentation
  url: https://fluxcd.io/flux/
- group: start
  title: ''
  type: GettingStarted
  url: https://fluxcd.io/flux/get-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fluxcd
- group: company
  title: ''
  type: Blog
  url: https://fluxcd.io/blog/
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/fluxcd/agent-skills
created: '2026-03-26'
description: Flux is a set of continuous and progressive delivery solutions for Kubernetes that are open and extensible, enabling GitOps-based automation for keeping Kubernetes clusters in sync with sources of configuration like Git repositories.
finops:
- name: Fluxcd Finops
  service_category: API
  slug: fluxcd-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fluxcd.png
layout: provider
modified: '2026-05-19'
name: Flux CD
nav: Providers
network: true
overview: 'Flux CD publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Containers, Continuous Delivery, Deployment, GitOps, and Kubernetes.


  Flux CD''s developer surface includes documentation, getting-started guide, engineering blog, and 5 more developer resources.'
plans:
- name: Fluxcd Plans Pricing
  plan_count: 3
  slug: fluxcd-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Fluxcd Rate Limits
  slug: fluxcd-rate-limits
score:
  band: emerging
  composite: 16.7
  coverage:
    artifact_dirs: 7
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 16.7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fluxcd/refs/heads/main/screenshots/fluxcd-2026-06-20T181348.png
security:
- kind: domain-security
  name: Fluxcd Domain Security
  slug: fluxcd-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Fluxcd Vulnerability Disclosure
  slug: fluxcd-vulnerability-disclosure
  summary_line: disclosure policy published
skill_count: 5
skills:
- name: commit-assisted-by
  slug: commit-assisted-by
- name: flux-controller-patch-releases
  slug: flux-controller-patch-releases
- name: gitops-cluster-debug
  slug: gitops-cluster-debug
- name: gitops-knowledge
  slug: gitops-knowledge
- name: gitops-repo-audit
  slug: gitops-repo-audit
slug: fluxcd
tags:
- Containers
- Continuous Delivery
- Deployment
- GitOps
- Kubernetes
website: https://fluxcd.io/
---
