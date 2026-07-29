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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: JSON-based "A-REST" API for SUSE Manager (SUMA), used to manage systems, channels, configuration, errata, and users across Linux infrastructure. Calls use GET for retrievals, POST for changes, and POS
  name: SUSE Manager API
  slug: suma-api
- description: REST API for SUSE Rancher Prime Kubernetes management platform, used to manage clusters, projects, workloads, users, and policies. Supports v3 API endpoints with bearer token authentication.
  name: SUSE Rancher API
  slug: rancher-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/suse-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/suse-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.suse.com/c/feed/
created: '2026-05-11'
description: SUSE is a global provider of open source enterprise solutions including SUSE Linux Enterprise Server (SLES), SUSE Rancher Prime for Kubernetes management, SUSE Manager (SUMA) for Linux systems management, and SUSE Edge and Security solutions. SUSE products expose REST and "A-REST" APIs for automation, configuration, and integration. The SUSE Manager API and Rancher API provide programmatic control over systems, clusters, and policies.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/suse.png
layout: provider
modified: '2026-05-11'
name: SUSE
nav: Providers
network: true
overview: 'SUSE publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Linux, Kubernetes, Enterprise Linux, Systems Management, and Open Source.


  SUSE''s developer surface includes engineering blog and 2 more developer resources.'
random_paper: 48
score:
  band: minimal
  composite: 7.3
  delta: -2.4
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/suse/refs/heads/main/screenshots/suse-2026-06-20T194741.png
security:
- kind: domain-security
  name: Suse Domain Security
  slug: suse-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Suse Vulnerability Disclosure
  slug: suse-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: suse
tags:
- Linux
- Kubernetes
- Enterprise Linux
- Systems Management
- Open Source
- Container Management
---
