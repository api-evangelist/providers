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
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-12'
api_count: 4
apis:
- description: Indicator of compromise detail lookups and submission
  name: AlienVault Indicators API
  slug: alienvault-indicators-api
- description: Threat pulses (curated indicator collections)
  name: AlienVault Pulses API
  slug: alienvault-pulses-api
- description: Search across pulses and users
  name: AlienVault Search API
  slug: alienvault-search-api
- description: OTX community users
  name: AlienVault Users API
  slug: alienvault-users-api
artifact_total: 7
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/alienvault-otx-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://otx.alienvault.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://otx.alienvault.com/api
- group: docs
  title: ''
  type: APIReference
  url: https://otx.alienvault.com/api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AlienVault-Labs
- group: start
  title: ''
  type: SignUp
  url: https://otx.alienvault.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://otx.alienvault.com/terms/
- group: build
  title: ''
  type: Packages
  url: packages/alienvault-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/alienvault-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/alienvault-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alienvault-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/alienvault-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alienvault-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/alienvault-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/alienvault-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/alienvault-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/alienvault-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: AlienVault is the security company behind the Open Threat Exchange (OTX), one of the largest open threat-intelligence communities in the world. OTX lets security practitioners and researchers create and share "pulses" — curated collections of indicators of compromise (IOCs) such as malicious IPs, domains, hostnames, URLs, file hashes, and CVEs — and consume that shared intelligence to automatically update their defensive infrastructure. The OTX DirectConnect API provides programmatic access to subscribed pulses, indicator detail lookups across multiple facets (general, geo, malware, passive DNS, reputation, URL lists), pulse and user search, and indicator submission for analysis. Authentication is via an X-OTX-API-KEY header. AlienVault was acquired by AT&T in 2018, becoming AT&T Cybersecurity, and OTX now operates under the LevelBlue brand. An official Python SDK (OTXv2) is published on PyPI and GitHub.
image: https://otx.alienvault.com/static/otx/img/otx_logo.png
layout: provider
mcp_servers:
- description: ''
  name: alienvault-mcp.yml
  slug: alienvault-mcpyml
modified: '2026-07-17'
name: AlienVault
nav: Providers
network: true
overview: 'AlienVault publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Indicators API, Pulses API, Search API, and 1 more. Tagged areas include Company, Security, Threat Intelligence, Cybersecurity, and Open Threat Exchange.


  AlienVault''s developer surface includes documentation, API reference, signup flow, authentication, and 14 more developer resources.'
random_paper: 117
score:
  band: thin
  composite: 37.6
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 54.5
    developer_ergonomics: 45.1
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 37.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alienvault/refs/heads/main/screenshots/alienvault-2026-07-25T195617.png
security:
- kind: authentication
  name: Alienvault Authentication
  slug: alienvault-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Alienvault Domain Security
  slug: alienvault-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alienvault
tags:
- Company
- Security
- Threat Intelligence
- Cybersecurity
- Open Threat Exchange
- Indicators of Compromise
- Threat Feeds
- API
website: https://otx.alienvault.com/api
---
