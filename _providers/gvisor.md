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
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: gVisor is an open-source application kernel written in Go that provides an additional layer of isolation between containerized applications and the host operating system. It implements a substantial p
  name: gVisor
  slug: gvisor
artifact_total: 6
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/gvisor/refs/heads/main/plans/gvisor-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gvisor-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/gvisor/refs/heads/main/rate-limits/gvisor-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gvisor-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/gvisor/refs/heads/main/finops/gvisor-finops.yml
  title: ''
  type: FinOps
  url: finops/gvisor-finops.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/google/gvisor/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/google/gvisor/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/google/gvisor/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/google/gvisor/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/google/gvisor/blob/master/LICENSE
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gvisor/refs/heads/main/security/gvisor-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/gvisor-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gvisor/refs/heads/main/security/gvisor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gvisor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gvisor.dev/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/google
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/google/gvisor
- group: docs
  title: ''
  type: Documentation
  url: https://gvisor.dev/docs/
- group: company
  title: ''
  type: Blog
  url: https://gvisor.dev/blog/
created: '2026-03-26'
description: gVisor is an application kernel written in Go that implements a substantial portion of the Linux system surface. It provides an additional layer of isolation between running applications and the host operating system, intercepting and handling application system calls in user space to reduce the attack surface of the host kernel.
finops:
- has_sources: false
  method: generated
  name: Gvisor Finops
  primary_unit: ''
  service_category: API
  slug: gvisor-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gvisor.png
layout: provider
modified: '2026-04-28'
name: gVisor
nav: Providers
network: true
overview: 'gVisor is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Containers, Kernel, Linux, Open Source, and Sandboxing.


  gVisor''s developer surface includes documentation, engineering blog, and 13 more developer resources.'
plans:
- name: Gvisor Plans Pricing
  plan_count: 3
  slug: gvisor-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Gvisor Rate Limits
  slug: gvisor-rate-limits
score:
  band: emerging
  composite: 22.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.4
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 21.1
  open_source:
    applies: true
    score: 100.0
  previous_composite: 24.2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/gvisor/refs/heads/main/screenshots/gvisor-2026-06-20T182445.png
security:
- kind: domain-security
  name: Gvisor Domain Security
  slug: gvisor-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Gvisor Vulnerability Disclosure
  slug: gvisor-vulnerability-disclosure
  summary_line: no policy recorded
slug: gvisor
tags:
- Containers
- Kernel
- Linux
- Open Source
- Sandboxing
- Security
website: https://gvisor.dev/
---
