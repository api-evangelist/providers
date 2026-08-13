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
api_count: 11
apis:
- description: The Agents API from Unitrends — 1 operation(s) for agents.
  name: Unitrends Agents API
  slug: unitrends-agents-api
- description: The Appliances API from Unitrends — 1 operation(s) for appliances.
  name: Unitrends Appliances API
  slug: unitrends-appliances-api
- description: The Assets API from Unitrends — 2 operation(s) for assets.
  name: Unitrends Assets API
  slug: unitrends-assets-api
- description: The BackupIqAlerts API from Unitrends — 1 operation(s) for backupiqalerts.
  name: Unitrends BackupIqAlerts API
  slug: unitrends-backupiqalerts-api
- description: The Backups API from Unitrends — 1 operation(s) for backups.
  name: Unitrends Backups API
  slug: unitrends-backups-api
- description: The Customers API from Unitrends — 1 operation(s) for customers.
  name: Unitrends Customers API
  slug: unitrends-customers-api
- description: The Domains API from Unitrends — 1 operation(s) for domains.
  name: Unitrends Domains API
  slug: unitrends-domains-api
- description: The DomainsEntra API from Unitrends — 1 operation(s) for domainsentra.
  name: Unitrends DomainsEntra API
  slug: unitrends-domainsentra-api
- description: The DomainsV2 API from Unitrends — 1 operation(s) for domainsv2.
  name: Unitrends DomainsV2 API
  slug: unitrends-domainsv2-api
- description: The DomainUsers API from Unitrends — 1 operation(s) for domainusers.
  name: Unitrends DomainUsers API
  slug: unitrends-domainusers-api
- description: The DomainUsersV2 API from Unitrends — 1 operation(s) for domainusersv2.
  name: Unitrends DomainUsersV2 API
  slug: unitrends-domainusersv2-api
artifact_total: 15
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unitrends-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/unitrends-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.unitrends.com/
- group: company
  title: ''
  type: Blog
  url: https://www.unitrends.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://helpdesk.kaseya.com/hc/en-gb
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Unitrends
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/Unitrends/unitrends-api-doc/wiki
- group: commercial
  title: ''
  type: Pricing
  url: https://www.unitrends.com/request/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kaseya.com/legal/website-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kaseya.com/legal/kaseya-privacy-statement/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kaseya.com/
- group: other
  title: ''
  type: CaseStudies
  url: https://www.unitrends.com/case-studies/
- group: start
  title: ''
  type: Login
  url: https://portal.backup.net/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/unitrends-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/unitrends-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/unitrends-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/unitrends-public-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/unitrends-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/unitrends-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/unitrends-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/unitrends-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/unitrends-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/unitrends-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Unitrends, a Kaseya company, provides all-in-one backup and disaster recovery (BCDR) solutions that secure, defend, and recover data across on-prem data centers, cloud, SaaS, and endpoints. The platform spans Recovery Series backup appliances, Unitrends Backup software, endpoint backup, and the UniView / Unitrends MSP portal, with ransomware detection, automated recovery assurance testing, and BackupIQ intelligence. Developers get a UniView Portal Public API (OAuth 2.0 client credentials via login.backup.net) for customers, appliances, assets, backups, and BackupIQ alerts, plus a documented per-appliance REST API and a community PowerShell toolkit.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unitrends.png
layout: provider
mcp_servers:
- description: ''
  name: unitrends-mcp.yml
  slug: unitrends-mcpyml
modified: '2026-07-21'
name: Unitrends
nav: Providers
network: true
overview: 'Unitrends publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Appliances API, Assets API, and 8 more. Tagged areas include Company, Backup, Disaster Recovery, Data Protection, and BCDR.


  Unitrends'' developer surface includes authentication, engineering blog, support, documentation, pricing, and 19 more developer resources.'
random_paper: 28
scopes:
- name: Unitrends Scopes
  scope_count: 3
  slug: unitrends-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: thin
  composite: 41.3
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 51.8
    developer_ergonomics: 29.9
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 41.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Unitrends Authentication
  slug: unitrends-authentication
  summary_line: oauth2/http-bearer/session-token · 3 schemes
- kind: domain-security
  name: Unitrends Domain Security
  slug: unitrends-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: unitrends
tags:
- Company
- Backup
- Disaster Recovery
- Data Protection
- BCDR
- Ransomware Protection
- MSP
- Endpoint Backup
website: https://www.unitrends.com/
---
