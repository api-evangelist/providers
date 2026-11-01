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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.7
  scored_at: '2026-10-31'
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
artifact_total: 29
collections:
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
- group: commercial
  href: https://artifacts.apis.io/unitrends/plans/unitrends-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/unitrends-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/unitrends/capabilities/unitrends-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/unitrends-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/unitrends/security/unitrends-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/unitrends-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/unitrends/authentication/unitrends-authentication.yml
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
  href: https://artifacts.apis.io/unitrends/well-known/unitrends-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/unitrends-well-known.yml
- group: agent
  href: https://artifacts.apis.io/unitrends/mcp/unitrends-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/unitrends-mcp.yml
- group: agent
  href: https://artifacts.apis.io/unitrends/llms/unitrends-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/unitrends-llms.txt
- group: other
  href: https://artifacts.apis.io/unitrends/overlays/unitrends-public-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/unitrends-public-api-overlay.yaml
- group: design
  href: https://artifacts.apis.io/unitrends/conformance/unitrends-conformance.yml
  title: ''
  type: Conformance
  url: conformance/unitrends-conformance.yml
- group: design
  href: https://artifacts.apis.io/unitrends/lifecycle/unitrends-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/unitrends-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/unitrends/scopes/unitrends-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/unitrends-scopes.yml
- group: build
  href: https://artifacts.apis.io/unitrends/packages/unitrends-packages.yml
  title: ''
  type: Packages
  url: packages/unitrends-packages.yml
- group: design
  href: https://artifacts.apis.io/unitrends/conventions/unitrends-conventions.yml
  title: ''
  type: Conventions
  url: conventions/unitrends-conventions.yml
- group: design
  href: https://artifacts.apis.io/unitrends/data-model/unitrends-data-model.yml
  title: ''
  type: DataModel
  url: data-model/unitrends-data-model.yml
- group: agent
  href: https://artifacts.apis.io/unitrends/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Unitrends, a Kaseya company, provides all-in-one backup and disaster recovery (BCDR) solutions that secure, defend, and recover data across on-prem data centers, cloud, SaaS, and endpoints. The platform spans Recovery Series backup appliances, Unitrends Backup software, endpoint backup, and the UniView / Unitrends MSP portal, with ransomware detection, automated recovery assurance testing, and BackupIQ intelligence. Developers get a UniView Portal Public API (OAuth 2.0 client credentials via login.backup.net) for customers, appliances, assets, backups, and BackupIQ alerts, plus a documented per-appliance REST API and a community PowerShell toolkit.
finops:
- has_sources: true
  method: derived
  name: Unitrends Finops
  primary_unit: ''
  service_category: ''
  slug: unitrends-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unitrends.png
layout: provider
modified: '2026-07-21'
name: Unitrends
nav: Providers
network: true
overview: 'Unitrends publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, Appliances API, Assets API, and 8 more. Tagged areas include Company, Backup, Disaster Recovery, Data Protection, and BCDR.


  Unitrends'' developer surface includes authentication, engineering blog, support, documentation, pricing, and 21 more developer resources.'
plans:
- name: Unitrends Plans Pricing
  plan_count: 0
  slug: unitrends-plans-pricing
random_paper: 4
scopes:
- name: Unitrends Scopes
  scope_count: 3
  slug: unitrends-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 43.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 46.0
    developer_ergonomics: 49.4
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 43.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/unitrends/unitrends-2026-09-02T164925.png
security:
- kind: authentication
  name: Unitrends Authentication
  slug: unitrends-authentication
  summary_line: oauth2/http-bearer/session-token · 3 schemes
- kind: domain-security
  name: Unitrends Domain Security
  slug: unitrends-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Monitor a Unitrends backup estate
  slug: unitrends-monitor-backup-estate
- name: Inventory SaaS backup tenants and users
  slug: unitrends-saas-tenant-inventory
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
