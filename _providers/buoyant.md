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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.0
  scored_at: '2026-09-05'
api_count: 3
apis:
- description: Linkerd is a CNCF-graduated service mesh for Kubernetes that transparently adds mutual TLS encryption, latency-aware load balancing, retries, timeouts, circuit breaking, and observability to any Kuber
  name: Linkerd Service Mesh
  slug: linkerd
- description: Buoyant Enterprise Linkerd is the enterprise-supported distribution of Linkerd with additional features including FIPS-validated cryptography, lifecycle automation, multi-cluster networking, and enter
  name: Buoyant Enterprise Linkerd (BEL)
  slug: buoyant-enterprise-linkerd
- description: Buoyant Cloud is the hosted control surface for Linkerd fleets — health checks, golden metrics, multi-cluster link management and automated Linkerd upgrades. Clusters connect through the Buoyant Cloud
  name: Buoyant Cloud
  slug: buoyant-cloud
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://buoyant.io/
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/linkerd/linkerd2/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/linkerd/linkerd2/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/linkerd/linkerd2/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/linkerd/linkerd2/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/linkerd/linkerd2/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/linkerd/linkerd2/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/buoyant-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/buoyantio
- group: start
  title: ''
  type: Portal
  url: https://buoyant.io/
- group: docs
  title: ''
  type: Documentation
  url: https://linkerd.io/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/linkerd
- group: company
  title: ''
  type: Blog
  url: https://buoyant.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://buoyant.io/pricing/
- group: operate
  title: ''
  type: Slack
  url: https://slack.linkerd.io/
- group: operate
  title: ''
  type: Community
  url: https://linkerd.io/community/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.buoyant.io/buoyant-enterprise-linkerd/latest/overview/
- group: docs
  title: ''
  type: APIReference
  url: https://linkerd.io/docs/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://linkerd.io/2/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://www.buoyant.io/linkerd-support
- group: operate
  title: ''
  type: HelpCenter
  url: https://linkerd.buoyant.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.buoyant.io/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://buoyant.cloud/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BuoyantIO
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/buoyant-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/buoyant-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/buoyant-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/buoyant-cli.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/buoyant-grpc.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/buoyant-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/buoyant-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/buoyant-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/buoyant-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/buoyant-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/buoyant-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/buoyant-changelog.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/buoyant-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/buoyant-vulnerability-disclosure.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/buoyant-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/buoyant-rate-limits.yml
created: '2026-01-02'
description: Buoyant is the creator of Linkerd, the CNCF-graduated service mesh for Kubernetes. Linkerd provides zero-trust security via mutual TLS, ultra-high availability with automated failover, and observability for microservices including AI/LLM workloads. Buoyant Enterprise Linkerd adds enterprise features including FIPS 140-2/140-3 validated encryption and multi-cluster support.
finops:
- name: Buoyant Finops
  service_category: API
  slug: buoyant-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/buoyant.png
layout: provider
modified: '2026-09-04'
name: Buoyant
nav: Providers
network: true
overview: 'Buoyant publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI Observability, Kubernetes, Linkerd, mTLS, and Observability.


  Buoyant''s developer surface includes developer portal, documentation, engineering blog, pricing, API reference, getting-started guide, support, and 33 more developer resources.'
plans:
- name: Buoyant Plans Pricing
  plan_count: 3
  slug: buoyant-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Buoyant Rate Limits
  slug: buoyant-rate-limits
score:
  band: developing
  composite: 52.5
  coverage:
    artifact_dirs: 16
    catalog_earned: 50.0
    catalog_earned_first_party: 12.0
    catalog_gap: 65.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.8
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 4.5
    contract_quality: 26.7
    developer_ergonomics: 71.4
    discoverability: 72.2
    governance: 4.5
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 100.0
  previous_composite: 47.7
  provenance:
    conformance: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/buoyant/refs/heads/main/screenshots/buoyant-2026-06-20T173802.png
security:
- kind: authentication
  name: Buoyant Authentication
  slug: buoyant-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Buoyant Domain Security
  slug: buoyant-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Buoyant Vulnerability Disclosure
  slug: buoyant-vulnerability-disclosure
  summary_line: Hackerone
slug: buoyant
tags:
- AI Observability
- Kubernetes
- Linkerd
- mTLS
- Observability
- Service Mesh
- Zero Trust
website: https://buoyant.io/
---
