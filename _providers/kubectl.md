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
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: kubectl is the official command-line tool for Kubernetes, used to deploy applications, inspect resources, and manage clusters via the Kubernetes API.
  name: Kubectl
  slug: kubectl
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kubectl-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kubectl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kubernetes.io/docs/reference/kubectl/
- group: docs
  title: ''
  type: Documentation
  url: https://kubernetes.io/docs/reference/kubectl/overview/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kubernetes/kubectl
- group: company
  title: ''
  type: Blog
  url: https://kubernetes.io/feed.xml
created: '2026-03-25'
description: kubectl is the official command-line tool for Kubernetes, used to deploy applications, inspect resources, and manage clusters via the Kubernetes API.
finops:
- name: Kubectl Finops
  service_category: API
  slug: kubectl-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kubectl.png
layout: provider
modified: '2026-04-28'
name: Kubectl
nav: Providers
network: true
overview: 'Kubectl publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Command Line Interface and Infrastructure CLI.


  Kubectl''s developer surface includes documentation, engineering blog, and 4 more developer resources.'
plans:
- name: Kubectl Plans Pricing
  plan_count: 3
  slug: kubectl-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 5
  name: Kubectl Rate Limits
  slug: kubectl-rate-limits
score:
  band: emerging
  composite: 18.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 18.9
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kubectl/refs/heads/main/screenshots/kubectl-2026-06-20T184201.png
security:
- kind: domain-security
  name: Kubectl Domain Security
  slug: kubectl-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Kubectl Vulnerability Disclosure
  slug: kubectl-vulnerability-disclosure
  summary_line: disclosure policy published
slug: kubectl
tags:
- Command Line Interface
- Infrastructure CLI
website: https://kubernetes.io/docs/reference/kubectl/
---
