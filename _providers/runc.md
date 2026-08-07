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
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: runc is a CLI tool for spawning and running containers on Linux according to the OCI (Open Container Initiative) specification. It is the reference implementation of the OCI runtime specification, pro
  name: Runc
  slug: runc
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/runc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://opencontainers.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/opencontainers
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/opencontainers/runc
- group: company
  title: ''
  type: Blog
  url: https://opencontainers.org/posts/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/opencontainers/runc/blob/main/README.md
- group: docs
  title: ''
  type: Specification
  url: https://github.com/opencontainers/runtime-spec
- group: auth
  title: ''
  type: Security
  url: https://github.com/opencontainers/runc/blob/main/SECURITY.md
created: '2026-03-26'
description: runc is a CLI tool for spawning and running containers on Linux according to the OCI (Open Container Initiative) specification. It is the reference implementation of the OCI runtime specification and is used as the default low-level container runtime by Docker, containerd, Podman, and other container platforms. runc manages container lifecycle operations including creating, starting, pausing, resuming, killing, and deleting containers. It implements the OCI Runtime Specification and exposes a command-line interface that higher-level runtimes use to manage individual container instances. runc also supports checkpoint/restore via CRIU, rootless containers (no root privileges needed via user namespaces), cgroup v2, seccomp syscall filtering, AppArmor, SELinux, and Intel Memory Protection Extensions. The current stable release line is 1.3.x (runc 1.5.0 expected late April 2026).
examples:
- key_count: 7
  name: Runc Container Config Example
  slug: runc-container-config-example
finops:
- name: Runc Finops
  service_category: API
  slug: runc-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/runc.png
json_schemas:
- name: OCI Runtime Container Configuration
  property_count: 8
  slug: runc-container-config
json_structures:
- name: Runc Container Config Structure
  property_count: 0
  slug: runc-container-config-structure
jsonld:
- class_count: 43
  name: Runc Context
  property_count: 5
  slug: runc-context
layout: provider
modified: '2026-05-02'
name: Runc
nav: Providers
network: true
overview: 'Runc publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Container Runtime, Containers, Linux, OCI, and Open Source.


  The Runc catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Runc''s developer surface includes engineering blog, documentation, and 6 more developer resources.'
plans:
- name: Runc Plans Pricing
  plan_count: 3
  slug: runc-plans-pricing
random_paper: 101
rate_limits:
- limit_count: 5
  name: Runc Rate Limits
  slug: runc-rate-limits
rules:
- name: Runc API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: runc-jsonschema-spectral-rules
score:
  band: thin
  composite: 34.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 22.6
    developer_ergonomics: 10.9
    discoverability: 59.3
    governance: 58.3
    operational_transparency: 47.4
  previous_composite: 34.8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/runc/refs/heads/main/screenshots/runc-2026-06-20T193250.png
security:
- kind: domain-security
  name: Runc Domain Security
  slug: runc-domain-security
  summary_line: TLSv1.3 · HSTS
slug: runc
tags:
- Container Runtime
- Containers
- Linux
- OCI
- Open Source
- CNCF
- Open Container Initiative
- Cloud Native
website: https://opencontainers.org/
---
