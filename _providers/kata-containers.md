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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Kata Containers is an open source container runtime that uses lightweight virtual machines to provide the speed of containers with the security of traditional VMs. It is compatible with the OCI runtim
  name: Kata Containers
  slug: kata-containers
artifact_total: 5
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/kata-containers/kata-containers/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/kata-containers/kata-containers/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/kata-containers/kata-containers/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/kata-containers/kata-containers/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/kata-containers/kata-containers/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/kata-containers/kata-containers/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kata-containers-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/katacontainers
- group: company
  title: ''
  type: Website
  url: https://katacontainers.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kata-containers
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/kata-containers/kata-containers
- group: docs
  title: ''
  type: Documentation
  url: https://katacontainers.io/docs/
- group: company
  title: ''
  type: Blog
  url: https://katacontainers.io/blog/
- group: operate
  title: ''
  type: Slack
  url: https://katacontainers.slack.com/
created: '2026-03-26'
description: Kata Containers is an open source project that builds lightweight virtual machines that seamlessly plug into the container ecosystem. It combines the speed of containers with the security isolation of virtual machines, providing a hardware-level isolation boundary for each container or pod.
finops:
- name: Kata Containers Finops
  service_category: API
  slug: kata-containers-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kata-containers.png
layout: provider
modified: '2026-04-28'
name: Kata Containers
nav: Providers
network: true
overview: 'Kata Containers publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Containers, Isolation, Kubernetes, Open-Source, and Security.


  Kata Containers'' developer surface includes documentation, engineering blog, and 12 more developer resources.'
plans:
- name: Kata Containers Plans Pricing
  plan_count: 3
  slug: kata-containers-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Kata Containers Rate Limits
  slug: kata-containers-rate-limits
score:
  band: emerging
  composite: 25.9
  coverage:
    artifact_dirs: 6
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 100.0
  previous_composite: 25.9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kata-containers/refs/heads/main/screenshots/kata-containers-2026-06-20T183924.png
security:
- kind: domain-security
  name: Kata Containers Domain Security
  slug: kata-containers-domain-security
  summary_line: TLSv1.3 · HSTS
slug: kata-containers
tags:
- Containers
- Isolation
- Kubernetes
- Open-Source
- Security
- Virtual Machines
website: https://katacontainers.io/
---
