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
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: 'IBM Cloud Kubernetes Service is a managed Kubernetes offering that delivers powerful tools, an intuitive user experience, and built-in security for rapid delivery of applications that can be bound to '
  name: IBM Cloud Kubernetes
  slug: ibm-cloud-kubernetes
artifact_total: 7
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/ibm/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ibm-cloud-kubernetes-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ibm-cloud-kubernetes-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cloud.ibm.com/
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.ibm.com/docs/containers
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.ibm.com/docs/containers?topic=containers-getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/IBM-Cloud
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.ibm.com/kubernetes/catalog/create
- group: company
  title: ''
  type: Blog
  url: https://www.ibm.com/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://cloud.ibm.com/status
- group: start
  title: ''
  type: Signup
  url: https://cloud.ibm.com/registration
- group: design
  title: ''
  type: Rules
  url: rules/ibm-cloud-kubernetes-rules.yml
created: '2026-03-26'
description: IBM Cloud Kubernetes Service is a managed Kubernetes offering that delivers powerful tools, an intuitive user experience, and built-in security for rapid delivery of applications that can be bound to cloud services related to IBM Watson, IoT, DevOps, and data analytics.
finops:
- name: Ibm Cloud Kubernetes Finops
  service_category: API
  slug: ibm-cloud-kubernetes-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ibm-cloud-kubernetes.png
layout: provider
modified: '2026-08-21'
name: IBM Cloud Kubernetes
nav: Providers
network: true
overview: 'IBM Cloud Kubernetes publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud, Containers, IBM, Kubernetes, and Orchestration.


  The IBM Cloud Kubernetes catalog on APIs.io includes 1 Spectral governance ruleset.


  IBM Cloud Kubernetes'' developer surface includes documentation, getting-started guide, pricing, engineering blog, signup flow, and 7 more developer resources.'
plans:
- name: Ibm Cloud Kubernetes Plans Pricing
  plan_count: 3
  slug: ibm-cloud-kubernetes-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Ibm Cloud Kubernetes Rate Limits
  slug: ibm-cloud-kubernetes-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: IBM Cloud Kubernetes API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: ibm-cloud-kubernetes-rules
score:
  band: emerging
  composite: 22.0
  coverage:
    artifact_dirs: 7
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 22.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ibm-cloud-kubernetes/refs/heads/main/screenshots/ibm-cloud-kubernetes-2026-06-20T183124.png
security:
- kind: domain-security
  name: Ibm Cloud Kubernetes Domain Security
  slug: ibm-cloud-kubernetes-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Ibm Cloud Kubernetes Vulnerability Disclosure
  slug: ibm-cloud-kubernetes-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: ibm-cloud-kubernetes
tags:
- Cloud
- Containers
- IBM
- Kubernetes
- Orchestration
website: https://cloud.ibm.com/
---
