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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.8
  scored_at: '2026-07-28'
api_count: 14
apis:
- description: Everything about [accounts](#model/account)
  name: Slide Accounts API
  slug: slide-accounts-api
- description: Everything about [agents](#model/agent)
  name: Slide Agents API
  slug: slide-agents-api
- description: Everything about [alerts](#model/alert)
  name: Slide Alerts API
  slug: slide-alerts-api
- description: The Audits API from Slide — 4 operation(s) for audits.
  name: Slide Audits API
  slug: slide-audits-api
- description: Everything about [backups](#model/backup)
  name: Slide Backups API
  slug: slide-backups-api
- description: Everything about [clients](#model/client)
  name: Slide Clients API
  slug: slide-clients-api
- description: Everything about [devices](#model/device)
  name: Slide Devices API
  slug: slide-devices-api
- description: Everything about [networks](#model/network)
  name: Slide Networks API
  slug: slide-networks-api
- description: Everything about [file restores](#model/filerestore)
  name: Slide Restores (File) API
  slug: slide-restores-file-api
- description: Everything about [image exports](#model/imageexport)
  name: Slide Restores (Image) API
  slug: slide-restores-image-api
- description: Everything about [push file restores](#model/filerestorepush)
  name: Slide Restores (Push) API
  slug: slide-restores-push-api
- description: Everything about [virtual machines](#model/virtualmachine)
  name: Slide Restores (Virtual Machine) API
  slug: slide-restores-virtual-machine-api
- description: Everything about [snapshots](#model/snapshot)
  name: Slide Snapshots API
  slug: slide-snapshots-api
- description: Everything about [users](#model/user)
  name: Slide Users API
  slug: slide-users-api
artifact_total: 18
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/slide-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/slide-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://slide.tech
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.slide.tech
- group: docs
  title: ''
  type: Documentation
  url: https://docs.slide.tech
- group: docs
  title: ''
  type: APIReference
  url: https://docs.slide.tech/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.slide.tech/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/Ggb3xv3kWG
- group: operate
  title: ''
  type: StatusPage
  url: https://status.slide.tech
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.slide.tech/releases/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.slide.tech/deprecations/
- group: start
  title: ''
  type: Login
  url: https://console.slide.tech/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://slide.tech/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://slide.tech/legal/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://docs.slide.tech/security-and-trust/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/slide-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/slide-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/slide-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/slide-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/slide-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/slide-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/slide-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/slide-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/slide-trust-center.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/slide-llms.txt
created: '2026-07-17'
description: Slide is a modern, security-first Business Continuity and Disaster Recovery (BCDR) platform built exclusively for Managed Service Providers (MSPs). Founded by Datto creator Austin McChord, Slide pairs on-premise Slide Box appliances with the Slide Cloud to deliver always-encrypted, block-level backup, snapshot management, file and image restores, and virtualization. Its open REST API (api.slide.tech) gives MSPs full programmatic control to integrate, extend, and automate agents, devices, backups, snapshots, restores, networks, clients, users, alerts, and audit logs within their existing tooling. The platform uses AES-256 and ZFS native encryption, offers month-to-month subscriptions, and is SOC 2 Type 1 certified.
image: https://images.prismic.io/slide/aiG5lQeQX7-eWv32_image-3-.png
layout: provider
mcp_servers:
- description: ''
  name: slide-mcp.yml
  slug: slide-mcpyml
modified: '2026-07-21'
name: Slide
nav: Providers
network: true
overview: 'Slide publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Agents API, Alerts API, and 11 more. Tagged areas include Company, Backup, Disaster Recovery, Business Continuity, and BCDR.


  Slide''s developer surface includes authentication, documentation, API reference, getting-started guide, support, changelog, and 20 more developer resources.'
random_paper: 37
score:
  band: developing
  composite: 49.4
  delta: -2.9
  facets:
    commercial_clarity: 50.0
    contract_quality: 55.9
    developer_ergonomics: 53.8
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 39.5
  previous_composite: 52.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Slide Authentication
  slug: slide-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Slide Domain Security
  slug: slide-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Slide Trust Center
  slug: slide-trust-center
  summary_line: SOC 2 Type 1 (Security and Availability Trust Services Criteria)
slug: slide
tags:
- Company
- Backup
- Disaster Recovery
- Business Continuity
- BCDR
- Managed Service Providers
- MSP
- Data Protection
- Cloud Storage
- Virtualization
website: https://slide.tech
---
