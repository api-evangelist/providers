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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-10-04'
api_count: 6
apis:
- description: Mirantis enterprise Kubernetes and container platform overview, indexing product, documentation, and developer resources.
  name: Mirantis
  slug: mirantis
- description: Mirantis Kubernetes Engine (MKE) is an enterprise container orchestration platform that delivers production-ready Kubernetes for hybrid and multi-cloud environments.
  name: Mirantis Kubernetes Engine
  slug: mke
- description: k0rdent is a composable Kubernetes management platform for centrally provisioning, observing, and securing fleets of clusters across clouds and edge.
  name: Mirantis k0rdent
  slug: k0rdent
- description: k0s is a single-binary, lightweight, certified Kubernetes distribution that runs on any infrastructure from cloud to edge.
  name: k0s
  slug: k0s
- description: MOSK delivers OpenStack on top of Kubernetes for cloud and telco workloads.
  name: Mirantis OpenStack for Kubernetes
  slug: mosk
- description: Lens is a Kubernetes IDE for managing, observing, and troubleshooting clusters.
  name: Lens Desktop
  slug: lens
artifact_total: 11
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/mirantis/refs/heads/main/finops/mirantis-finops.yml
  title: ''
  type: FinOps
  url: finops/mirantis-finops.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/mirantis/refs/heads/main/rate-limits/mirantis-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/mirantis-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/mirantis/refs/heads/main/plans/mirantis-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mirantis-plans-pricing.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/Mirantis/security/blob/main/vulnerability-disclosure-policy.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mirantis/refs/heads/main/llms/mirantis-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mirantis-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mirantis/refs/heads/main/well-known/mirantis-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mirantis-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mirantis/refs/heads/main/well-known/mirantis-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mirantis-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mirantis/refs/heads/main/hosts/mirantis-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mirantis-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mirantis/refs/heads/main/vendors/mirantis-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mirantis-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/mirantis/refs/heads/main/packages/mirantis-packages.yml
  title: ''
  type: SDKs
  url: packages/mirantis-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/mirantis/refs/heads/main/packages/mirantis-packages.yml
  title: ''
  type: Packages
  url: packages/mirantis-packages.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.mirantis.com/company/leadership/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.mirantis.com/get-started/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mirantis/refs/heads/main/security/mirantis-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mirantis-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mirantis/refs/heads/main/security/mirantis-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mirantis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mirantis.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mirantis.com/
- group: company
  title: ''
  type: Blog
  url: https://www.mirantis.com/blog/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Mirantis
- group: operate
  title: ''
  type: Support
  url: https://www.mirantis.com/support/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mirantis.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://www.mirantis.com/company/careers/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/MirantisIT
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mirantis
coverage:
  checked: '2026-10-04'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on the provider's documented API hosts.
  evidence:
  - status: 0
    url: https://api.mirantis.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-03-26'
description: Mirantis provides enterprise Kubernetes and container platform solutions for multi-cloud, hybrid-cloud, and edge deployments. Its product line includes Mirantis Kubernetes Engine (MKE), k0rdent Enterprise, Mirantis OpenStack for Kubernetes (MOSK), Mirantis Container Runtime, Mirantis Secure Registry, Lens Desktop, and the open source k0s Kubernetes distribution and k0smotron orchestrator.
finops:
- name: Mirantis Finops
  service_category: API
  slug: mirantis-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mirantis.png
layout: provider
modified: '2026-04-28'
name: Mirantis
nav: Providers
network: true
overview: 'Mirantis publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Kubernetes, Containers, Cloud, DevOps, and OpenStack.


  Mirantis'' developer surface includes getting-started guide, documentation, engineering blog, GitHub presence, support, pricing, and 18 more developer resources.'
plans:
- name: Mirantis Plans Pricing
  plan_count: 3
  slug: mirantis-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Mirantis Rate Limits
  slug: mirantis-rate-limits
score:
  band: emerging
  composite: 22.1
  coverage:
    artifact_dirs: 13
    catalog_earned: 44.0
    catalog_earned_first_party: 0.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 5.3
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 71.4
    operational_transparency: 23.7
  previous_composite: 16.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/mirantis/refs/heads/main/screenshots/mirantis-2026-06-20T185609.png
security:
- kind: domain-security
  name: Mirantis Domain Security
  slug: mirantis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mirantis Vulnerability Disclosure
  slug: mirantis-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: mirantis
tags:
- Kubernetes
- Containers
- Cloud
- DevOps
- OpenStack
website: https://www.mirantis.com/
---
