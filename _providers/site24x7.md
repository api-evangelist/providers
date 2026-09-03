---
access_model:
  confidence: high
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 36
  human_in_the_loop: 0
  name: Site24X7 Agentic Access
  operation_count: 74
  slug: site24x7-agentic-access
  summary_line: 74 operations · 36 acting
api_count: 1
apis:
- baseURL: https://api.site24x7.com/api
  baseurl_source: declared
  description: Alert and alarm management
  name: Site24x7 Alarms API
  slug: site24x7-alarms-api
- baseURL: https://api.site24x7.com/api
  baseurl_source: declared
  description: Real-time status and health information
  name: Site24x7 Current Status API
  slug: site24x7-current-status-api
- baseURL: https://api.site24x7.com/api
  baseurl_source: declared
  description: Scheduled maintenance management
  name: Site24x7 Maintenance Windows API
  slug: site24x7-maintenance-windows-api
- baseURL: https://api.site24x7.com/api
  baseurl_source: declared
  description: Organize monitors into logical groups
  name: Site24x7 Monitor Groups API
  slug: site24x7-monitor-groups-api
- baseURL: https://api.site24x7.com/api
  baseurl_source: declared
  description: Create, retrieve, update, and delete monitors of all types
  name: Site24x7 Monitors API
  slug: site24x7-monitors-api
- baseURL: https://api.site24x7.com/api
  baseurl_source: declared
  description: Alert notification configuration
  name: Site24x7 Notification Profiles API
  slug: site24x7-notification-profiles-api
- baseURL: https://api.site24x7.com/api
  baseurl_source: declared
  description: Outage records and incident management
  name: Site24x7 Outages API
  slug: site24x7-outages-api
- baseURL: https://api.site24x7.com/api
  baseurl_source: declared
  description: Availability, performance, SLA, and custom reports
  name: Site24x7 Reports API
  slug: site24x7-reports-api
- baseURL: https://api.site24x7.com/api
  baseurl_source: declared
  description: Tag-based monitor organization
  name: Site24x7 Tags API
  slug: site24x7-tags-api
- baseURL: https://api.site24x7.com/api
  baseurl_source: declared
  description: Performance threshold configuration
  name: Site24x7 Threshold Profiles API
  slug: site24x7-threshold-profiles-api
- baseURL: https://api.site24x7.com/api
  baseurl_source: declared
  description: User account administration
  name: Site24x7 Users API
  slug: site24x7-users-api
artifact_total: 39
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Site24x7 REST Alarms API
  slug: open-site24x7-alarms-api
- collection_type: open
  name: Site24x7 REST Alarms Current Status API
  slug: open-site24x7-current-status-api
- collection_type: open
  name: Site24x7 REST Alarms Maintenance Windows API
  slug: open-site24x7-maintenance-windows-api
- collection_type: open
  name: Site24x7 REST Alarms Monitor Groups API
  slug: open-site24x7-monitor-groups-api
- collection_type: open
  name: Site24x7 REST Alarms Monitors API
  slug: open-site24x7-monitors-api
- collection_type: open
  name: Site24x7 REST Alarms Notification Profiles API
  slug: open-site24x7-notification-profiles-api
- collection_type: open
  name: Site24x7 REST Alarms Outages API
  slug: open-site24x7-outages-api
- collection_type: open
  name: Site24x7 REST Alarms Reports API
  slug: open-site24x7-reports-api
- collection_type: open
  name: Site24x7 REST Alarms Tags API
  slug: open-site24x7-tags-api
- collection_type: open
  name: Site24x7 REST Alarms Threshold Profiles API
  slug: open-site24x7-threshold-profiles-api
- collection_type: open
  name: Site24x7 REST Alarms Users API
  slug: open-site24x7-users-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/site24x7-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/site24x7-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/site24x7-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/site24x7-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/site24x7-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.site24x7.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.site24x7.com/help/api/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/site24x7
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/site24x7
- group: company
  title: ''
  type: Blog
  url: https://www.site24x7.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.site24x7.com/site24x7-pricing.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.site24x7.com/
- group: other
  title: ''
  type: X
  url: https://x.com/Site24x7
- group: commercial
  title: ''
  type: Plans
  url: plans/site24x7-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/site24x7-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/site24x7-finops.yml
created: '2026-06-13'
description: Site24x7 is a full-stack cloud monitoring platform with a REST API for managing monitors, on-call schedules, alerts, SLAs, and accessing availability and performance metrics. The platform covers website uptime, server infrastructure, cloud services (AWS, Azure, GCP), application performance (APM), real user monitoring (RUM), network devices, databases, and synthetic transactions. The API uses OAuth 2.0 via the Zoho Developer Console and supports multiple regional data centers across the US, EU, India, Australia, Japan, Canada, UK, UAE, and Saudi Arabia.
examples:
- key_count: 15
  name: Create Monitor
  slug: create-monitor
- key_count: 3
  name: Monitor Response
  slug: monitor-response
- key_count: 3
  name: Status Count Response
  slug: status-count-response
finops:
- name: Site24X7 Finops
  service_category: ''
  slug: site24x7-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/site24x7.png
json_schemas:
- name: Monitor
  property_count: 14
  slug: monitor
- name: Outage
  property_count: 10
  slug: outage
- name: User
  property_count: 9
  slug: user
jsonld:
- class_count: 10
  name: Site24X7 Context
  property_count: 34
  slug: site24x7-context
layout: provider
modified: '2026-06-13'
name: Site24x7
nav: Providers
network: true
overview: 'Site24x7 publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Alarms API, Current Status API, Maintenance Windows API, and 8 more. Tagged areas include Monitoring, Observability, Uptime, Infrastructure, and Cloud.


  The Site24x7 catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Site24x7''s developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Site24X7 Plans Pricing
  plan_count: 8
  slug: site24x7-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 3
  name: Site24X7 Rate Limits
  slug: site24x7-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Site24x7 API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: site24x7-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.3
  coverage:
    artifact_dirs: 15
    catalog_gap: 36.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 9.8
    contract_quality: 68.3
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 52.6
  previous_composite: 48.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/site24x7/refs/heads/main/screenshots/site24x7-2026-06-20T193955.png
security:
- kind: authentication
  name: Site24X7 Authentication
  slug: site24x7-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Site24X7 Domain Security
  slug: site24x7-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Site24X7 Vulnerability Disclosure
  slug: site24x7-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Site24X7 Trust Center
  slug: site24x7-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, GDPR, CSA STAR
slug: site24x7
tags:
- Monitoring
- Observability
- Uptime
- Infrastructure
- Cloud
- APM
- SLA
- Alerts
- Synthetic Monitoring
- Real User Monitoring
- Network Monitoring
- Server Monitoring
- Website Monitoring
- On-Call
- Status Pages
website: https://www.site24x7.com/
---
