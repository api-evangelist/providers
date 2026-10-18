---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 49.8
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 34
  human_in_the_loop: 34
  name: Uptimerobot Agentic Access
  operation_count: 64
  slug: uptimerobot-agentic-access
  summary_line: 64 operations · 34 acting · 34 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.uptimerobot.com/v3
  baseurl_source: declared
  description: The Alert Contacts API from UptimeRobot — 2 operation(s) for alert contacts.
  name: UptimeRobot Alert Contacts API
  slug: uptimerobot-alert-contacts-api
- baseURL: https://api.uptimerobot.com/v3
  baseurl_source: declared
  description: The Incidents API from UptimeRobot — 6 operation(s) for incidents.
  name: UptimeRobot Incidents API
  slug: uptimerobot-incidents-api
- baseURL: https://api.uptimerobot.com/v3
  baseurl_source: declared
  description: The Integrations API from UptimeRobot — 2 operation(s) for integrations.
  name: UptimeRobot Integrations API
  slug: uptimerobot-integrations-api
- baseURL: https://api.uptimerobot.com/v3
  baseurl_source: declared
  description: The Maintenance Windows API from UptimeRobot — 2 operation(s) for maintenance windows.
  name: UptimeRobot Maintenance Windows API
  slug: uptimerobot-maintenance-windows-api
- baseURL: https://api.uptimerobot.com/v3
  baseurl_source: declared
  description: The Monitor Groups API from UptimeRobot — 2 operation(s) for monitor groups.
  name: UptimeRobot Monitor Groups API
  slug: uptimerobot-monitor-groups-api
- baseURL: https://api.uptimerobot.com/v3
  baseurl_source: declared
  description: The Monitors API from UptimeRobot — 11 operation(s) for monitors.
  name: UptimeRobot Monitors API
  slug: uptimerobot-monitors-api
- baseURL: https://api.uptimerobot.com/v3
  baseurl_source: declared
  description: The Monitors - Bulk Operations API from UptimeRobot — 3 operation(s) for monitors - bulk operations.
  name: UptimeRobot Monitors - Bulk Operations API
  slug: uptimerobot-monitors-bulk-operations-api
- baseURL: https://api.uptimerobot.com/v3
  baseurl_source: declared
  description: The PSP Announcements API from UptimeRobot — 4 operation(s) for psp announcements.
  name: UptimeRobot PSP Announcements API
  slug: uptimerobot-psp-announcements-api
- baseURL: https://api.uptimerobot.com/v3
  baseurl_source: declared
  description: The Public Status Pages API from UptimeRobot — 2 operation(s) for public status pages.
  name: UptimeRobot Public Status Pages API
  slug: uptimerobot-public-status-pages-api
- baseURL: https://api.uptimerobot.com/v3
  baseurl_source: declared
  description: The Storm Protection API from UptimeRobot — 1 operation(s) for storm protection.
  name: UptimeRobot Storm Protection API
  slug: uptimerobot-storm-protection-api
- baseURL: https://api.uptimerobot.com/v3
  baseurl_source: declared
  description: The Tags API from UptimeRobot — 2 operation(s) for tags.
  name: UptimeRobot Tags API
  slug: uptimerobot-tags-api
- baseURL: https://api.uptimerobot.com/v3
  baseurl_source: declared
  description: The User API from UptimeRobot — 3 operation(s) for user.
  name: UptimeRobot User API
  slug: uptimerobot-user-api
artifact_total: 25
asyncapis:
- description: ''
  name: Uptimerobot Webhooks
  slug: uptimerobot-webhooks
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://uptimerobot.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://uptimerobot.com/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://uptimerobot.com/quick-monitor-setup
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/uptimerobot/refs/heads/main/agentic-access/uptimerobot-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/uptimerobot-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/uptimerobot/refs/heads/main/plans/uptimerobot-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/uptimerobot-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/uptimerobot/refs/heads/main/rules/uptimerobot-rules.yml
  title: ''
  type: Spectral
  url: rules/uptimerobot-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/uptimerobot/refs/heads/main/json-ld/uptimerobot-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/uptimerobot-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/uptimerobot/refs/heads/main/vocabulary/uptimerobot-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/uptimerobot-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/uptimerobot/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/uptimerobot/refs/heads/main/asyncapi/uptimerobot-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/uptimerobot-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/uptimerobot/refs/heads/main/data-model/uptimerobot-data-model.yml
  title: ''
  type: DataModel
  url: data-model/uptimerobot-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/uptimerobot/refs/heads/main/errors/uptimerobot-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/uptimerobot-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/uptimerobot/refs/heads/main/conformance/uptimerobot-conformance.yml
  title: ''
  type: Conformance
  url: conformance/uptimerobot-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/uptimerobot/refs/heads/main/llms/uptimerobot-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/uptimerobot-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/uptimerobot/refs/heads/main/well-known/uptimerobot-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/uptimerobot-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/uptimerobot/refs/heads/main/well-known/uptimerobot-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/uptimerobot-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/uptimerobot/refs/heads/main/hosts/uptimerobot-hosts.yml
  title: ''
  type: Hosts
  url: hosts/uptimerobot-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/uptimerobot/refs/heads/main/vendors/uptimerobot-vendors.yml
  title: ''
  type: Vendors
  url: vendors/uptimerobot-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/uptimerobot/refs/heads/main/packages/uptimerobot-packages.yml
  title: ''
  type: SDKs
  url: packages/uptimerobot-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/uptimerobot/refs/heads/main/packages/uptimerobot-packages.yml
  title: ''
  type: Packages
  url: packages/uptimerobot-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.uptimerobot.com/
- group: auth
  title: ''
  type: Security
  url: https://uptimerobot.com/security/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/uptimerobot
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/uptimerobot/refs/heads/main/authentication/uptimerobot-authentication.yml
  title: ''
  type: Authentication
  url: authentication/uptimerobot-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/uptimerobot/refs/heads/main/security/uptimerobot-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/uptimerobot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://uptimerobot.com
- group: docs
  title: ''
  type: Documentation
  url: https://uptimerobot.com/api/
- group: docs
  title: ''
  type: APIReference
  url: https://uptimerobot.com/api/
- group: operate
  title: ''
  type: Support
  url: https://uptimerobot.com/help/
- group: company
  title: ''
  type: Blog
  url: https://uptimerobot.com/blog/
- group: operate
  title: ''
  type: Roadmap
  url: https://uptimerobot.com/roadmap/
- group: commercial
  title: ''
  type: Pricing
  url: https://uptimerobot.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.uptimerobot.com/sign-up
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/uptimerobot/workspace/uptimerobot-api
created: '2026-10-13'
description: UptimeRobot provides free and paid website monitoring services, offering uptime, SSL, DNS, and keyword monitoring, as well as a robust API for developers to integrate monitoring into their applications. With over 3.4 million users, it supports multi-location checks, real‑time alerts, status pages, and extensive integrations, catering to developers, DevOps teams, marketers, and businesses.
image: https://uptimerobot.com/_astro/ogimage.VdCGQqWN.png
json_schemas:
- name: CreateApiMonitorDto
  property_count: 26
  slug: uptimerobot-create-api-monitor-dto
- name: CreateKeywordMonitorDto
  property_count: 29
  slug: uptimerobot-create-keyword-monitor-dto
- name: MonitorDto
  property_count: 45
  slug: uptimerobot-monitor-dto
- name: MonitorPaginationDto
  property_count: 2
  slug: uptimerobot-monitor-pagination-dto
- name: MonitorResponseTimeStatsByRegionDto
  property_count: 7
  slug: uptimerobot-monitor-response-time-stats-by-region-dto
- name: UpdateMonitorDto
  property_count: 32
  slug: uptimerobot-update-monitor-dto
jsonld:
- class_count: 120
  name: Uptimerobot Context
  property_count: 227
  slug: uptimerobot-context
layout: provider
modified: '2026-10-13'
name: UptimeRobot
nav: Providers
network: true
overview: 'UptimeRobot publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Alert Contacts API, Incidents API, Integrations API, and 9 more. Tagged areas include Uptime Monitoring, Status Pages, Incident Management, DevOps, and Monitoring Integrations.


  The UptimeRobot catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  UptimeRobot''s developer surface includes getting-started guide, authentication, documentation, API reference, support, engineering blog, pricing, and 27 more developer resources.'
plans:
- name: Uptimerobot Plans Pricing
  plan_count: 2
  slug: uptimerobot-plans-pricing
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: UptimeRobot API Rules
  rule_count: 13
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 2
  slug: uptimerobot-rules
score:
  band: strong
  composite: 61.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 35.6
    contract_quality: 69.9
    developer_ergonomics: 61.3
    discoverability: 73.2
    operational_transparency: 44.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Uptimerobot Authentication
  slug: uptimerobot-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Uptimerobot Domain Security
  slug: uptimerobot-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: uptimerobot
tags:
- Uptime Monitoring
- Status Pages
- Incident Management
- DevOps
- Monitoring Integrations
website: https://uptimerobot.com
---
