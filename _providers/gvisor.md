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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: gVisor is an open-source application kernel written in Go that provides an additional layer of isolation between containerized applications and the host operating system. It implements a substantial p
  name: gVisor
  slug: gvisor
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gvisor-vulnerability-disclosure.yml
- group: auth
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
- name: Gvisor Finops
  service_category: API
  slug: gvisor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gvisor.png
layout: provider
modified: '2026-04-28'
name: gVisor
nav: Providers
network: true
overview: 'gVisor publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Containers, Kernel, Linux, Open Source, and Sandboxing.


  gVisor''s developer surface includes documentation, engineering blog, and 5 more developer resources.'
plans:
- name: Gvisor Plans Pricing
  plan_count: 3
  slug: gvisor-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Gvisor Rate Limits
  slug: gvisor-rate-limits
score:
  band: emerging
  composite: 22.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 22.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gvisor/refs/heads/main/screenshots/gvisor-2026-06-20T182445.png
security:
- kind: domain-security
  name: Gvisor Domain Security
  slug: gvisor-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Gvisor Vulnerability Disclosure
  slug: gvisor-vulnerability-disclosure
  summary_line: disclosure policy published
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
