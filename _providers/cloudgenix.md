---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: REST API for the CloudGenix AppFabric / Cloud Controller — manage sites, elements (ION devices), WAN networks, application policies, and telemetry. Token-authenticated via the X-Auth-Token header.
  name: CloudGenix Cloud Controller API
  slug: cloudgenix-cloud-controller-api
artifact_total: 2
common:
- group: docs
  title: ''
  type: Documentation
  url: https://developers.cloudgenix.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CloudGenix
- group: build
  title: ''
  type: Packages
  url: packages/cloudgenix-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cloudgenix-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/cloudgenix-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloudgenix-authentication.yml
created: '2026-07-17'
description: CloudGenix was a cloud-native SD-WAN (software-defined wide area network) company founded in 2013 and backed by Mayfield. Its AppFabric platform let enterprises build application-defined, policy-driven WANs managed from a cloud controller, with a full REST API (the CloudGenix Cloud Controller / AppFabric API) and first-party SDKs in Python, C#, Java, and JavaScript plus a CI-capable configuration CLI. Palo Alto Networks acquired CloudGenix in April 2020 for more than $420M and rebranded the product as Prisma SD-WAN, now part of the Prisma SASE portfolio. The public developer tooling remains published under the official CloudGenix GitHub organization.
image: https://avatars.githubusercontent.com/CloudGenix
layout: provider
modified: '2026-07-18'
name: Cloudgenix
nav: Providers
network: true
overview: 'Cloudgenix publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, SD-WAN, Networking, Cloud, and Software Defined Networking.


  Cloudgenix''s developer surface includes documentation, CLI, authentication, and 3 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 13.4
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 13.4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudgenix/refs/heads/main/screenshots/cloudgenix-2026-07-25T205705.png
security:
- kind: authentication
  name: Cloudgenix Authentication
  slug: cloudgenix-authentication
  summary_line: apiKey · 1 scheme
slug: cloudgenix
tags:
- Company
- SD-WAN
- Networking
- Cloud
- Software Defined Networking
- Network Automation
- SASE
- Infrastructure
---
