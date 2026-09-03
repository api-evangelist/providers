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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.5
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://public-api.backup.net
  baseurl_source: declared
  description: The Agents API from Unitrends — 1 operation(s) for agents.
  name: Unitrends Agents API
  slug: unitrends-agents-api
- baseURL: https://public-api.backup.net
  baseurl_source: declared
  description: The Appliances API from Unitrends — 1 operation(s) for appliances.
  name: Unitrends Appliances API
  slug: unitrends-appliances-api
- baseURL: https://public-api.backup.net
  baseurl_source: declared
  description: The Assets API from Unitrends — 2 operation(s) for assets.
  name: Unitrends Assets API
  slug: unitrends-assets-api
- baseURL: https://public-api.backup.net
  baseurl_source: declared
  description: The BackupIqAlerts API from Unitrends — 1 operation(s) for backupiqalerts.
  name: Unitrends BackupIqAlerts API
  slug: unitrends-backupiqalerts-api
- baseURL: https://public-api.backup.net
  baseurl_source: declared
  description: The Backups API from Unitrends — 1 operation(s) for backups.
  name: Unitrends Backups API
  slug: unitrends-backups-api
- baseURL: https://public-api.backup.net
  baseurl_source: declared
  description: The Customers API from Unitrends — 1 operation(s) for customers.
  name: Unitrends Customers API
  slug: unitrends-customers-api
- baseURL: https://public-api.backup.net
  baseurl_source: declared
  description: The Domains API from Unitrends — 1 operation(s) for domains.
  name: Unitrends Domains API
  slug: unitrends-domains-api
- baseURL: https://public-api.backup.net
  baseurl_source: declared
  description: The DomainsEntra API from Unitrends — 1 operation(s) for domainsentra.
  name: Unitrends DomainsEntra API
  slug: unitrends-domainsentra-api
- baseURL: https://public-api.backup.net
  baseurl_source: declared
  description: The DomainsV2 API from Unitrends — 1 operation(s) for domainsv2.
  name: Unitrends DomainsV2 API
  slug: unitrends-domainsv2-api
- baseURL: https://public-api.backup.net
  baseurl_source: declared
  description: The DomainUsers API from Unitrends — 1 operation(s) for domainusers.
  name: Unitrends DomainUsers API
  slug: unitrends-domainusers-api
- baseURL: https://public-api.backup.net
  baseurl_source: declared
  description: The DomainUsersV2 API from Unitrends — 1 operation(s) for domainusersv2.
  name: Unitrends DomainUsersV2 API
  slug: unitrends-domainusersv2-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Public Agents API
  slug: open-unitrends-agents-api
- collection_type: open
  name: Public Agents Appliances API
  slug: open-unitrends-appliances-api
- collection_type: open
  name: Public Agents Assets API
  slug: open-unitrends-assets-api
- collection_type: open
  name: Public Agents BackupIqAlerts API
  slug: open-unitrends-backupiqalerts-api
- collection_type: open
  name: Public Agents Backups API
  slug: open-unitrends-backups-api
- collection_type: open
  name: Public Agents Customers API
  slug: open-unitrends-customers-api
- collection_type: open
  name: Public Agents Domains API
  slug: open-unitrends-domains-api
- collection_type: open
  name: Public Agents DomainsEntra API
  slug: open-unitrends-domainsentra-api
- collection_type: open
  name: Public Agents DomainsV2 API
  slug: open-unitrends-domainsv2-api
- collection_type: open
  name: Public Agents DomainUsers API
  slug: open-unitrends-domainusers-api
- collection_type: open
  name: Public Agents DomainUsersV2 API
  slug: open-unitrends-domainusersv2-api
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
  name: Unitrends MCP Server
  slug: unitrends-mcp-server
modified: '2026-07-21'
name: Unitrends
nav: Providers
network: true
overview: 'Unitrends publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Appliances API, Assets API, and 8 more. Tagged areas include Company, Backup, Disaster Recovery, Data Protection, and BCDR.


  Unitrends'' developer surface includes authentication, engineering blog, support, documentation, pricing, and 19 more developer resources.'
random_paper: 1
scopes:
- name: Unitrends Scopes
  scope_count: 3
  slug: unitrends-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 39.4
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 4.5
    contract_quality: 48.4
    developer_ergonomics: 49.4
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 39.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/unitrends/refs/heads/main/screenshots/unitrends-2026-09-02T164925.png
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
