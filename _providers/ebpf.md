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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ebpf-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ebpf.io/
- group: other
  title: ''
  type: What is eBPF
  url: https://ebpf.io/what-is-ebpf/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ebpf.io/
- group: other
  title: ''
  type: Applications
  url: https://ebpf.io/applications/
- group: other
  title: ''
  type: Infrastructure
  url: https://ebpf.io/infrastructure/
- group: operate
  title: ''
  type: Community
  url: https://ebpf.io/get-started/
- group: company
  title: ''
  type: Blog
  url: https://ebpf.io/blog/
- group: other
  title: ''
  type: Foundation
  url: https://ebpf.foundation/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/ebpffoundation
created: '2025-01-01'
description: eBPF (extended Berkeley Packet Filter) is a technology that allows programs to run in a sandboxed virtual machine within the Linux kernel without changing kernel source code or loading kernel modules. It enables high-performance networking, security monitoring, observability, and tracing capabilities at the operating system level with minimal overhead. eBPF is governed as a standard by the eBPF Foundation under the Linux Foundation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ebpf.png
layout: provider
modified: '2026-04-28'
name: eBPF
nav: Providers
network: true
overview: 'eBPF is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include eBPF, Kernel, Linux, Networking, and Observability.


  eBPF''s developer surface includes documentation, engineering blog, and 8 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 8.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ebpf/refs/heads/main/screenshots/ebpf-2026-06-20T180414.png
security:
- kind: domain-security
  name: Ebpf Domain Security
  slug: ebpf-domain-security
  summary_line: TLSv1.3 · HSTS
slug: ebpf
tags:
- eBPF
- Kernel
- Linux
- Networking
- Observability
- Security
- Tracing
website: https://ebpf.io/
---
