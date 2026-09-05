---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
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
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Openstatus Agentic Access
  operation_count: 22
  slug: openstatus-agentic-access
  summary_line: 22 operations · 12 acting
api_count: 1
apis:
- baseURL: https://api.openstatus.dev/v1
  baseurl_source: declared
  description: On-demand synthetic checks.
  name: OpenStatus Check API
  slug: openstatus-check-api
- baseURL: https://api.openstatus.dev/v1
  baseurl_source: declared
  description: Incidents automatically opened when a monitor fails.
  name: OpenStatus Incident API
  slug: openstatus-incident-api
- baseURL: https://api.openstatus.dev/v1
  baseurl_source: declared
  description: HTTP, TCP, and DNS uptime monitors.
  name: OpenStatus Monitor API
  slug: openstatus-monitor-api
- baseURL: https://api.openstatus.dev/v1
  baseurl_source: declared
  description: Public status pages and subscribers.
  name: OpenStatus Page API
  slug: openstatus-page-api
- baseURL: https://api.openstatus.dev/v1
  baseurl_source: declared
  description: Status reports and their updates.
  name: OpenStatus Status Report API
  slug: openstatus-status-report-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OpenStatus Check API
  slug: open-openstatus-check-api
- collection_type: open
  name: OpenStatus Check Incident API
  slug: open-openstatus-incident-api
- collection_type: open
  name: OpenStatus Check Monitor API
  slug: open-openstatus-monitor-api
- collection_type: open
  name: OpenStatus Check Page API
  slug: open-openstatus-page-api
- collection_type: open
  name: OpenStatus Check Status Report API
  slug: open-openstatus-status-report-api
- collection_type: open
  name: OpenStatus API
  slug: open-openstatus
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openstatus-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/openstatus-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/openstatus-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openstatus-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openstatus-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openstatusHQ
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/openstatushq
- group: company
  title: ''
  type: Website
  url: https://www.openstatus.dev
- group: docs
  title: ''
  type: Documentation
  url: https://www.openstatus.dev/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/openstatus-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/openstatus-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/openstatus-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.openstatus.dev/blog
created: '2026-06-21'
description: OpenStatus is an open-source synthetic monitoring and status-page platform. It runs HTTP, TCP, and DNS uptime checks from 28 global regions, publishes hosted and self-hostable status pages, and manages incidents and status reports. The OpenStatus REST API at https://api.openstatus.dev/v1 lets teams programmatically manage monitors, status pages, status reports, incidents, and on-demand checks. The platform is free to self-host (AGPL-3.0) and also available as a managed cloud service.
finops:
- name: Openstatus Finops
  service_category: Management and Governance
  slug: openstatus-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openstatus.png
layout: provider
modified: '2026-06-21'
name: OpenStatus
nav: Providers
network: true
overview: 'OpenStatus publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Check API, Incident API, Monitor API, and 2 more. Tagged areas include Monitoring, Synthetic Monitoring, Uptime, Status Pages, and Incidents.


  OpenStatus'' developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Openstatus Plans Pricing
  plan_count: 6
  slug: openstatus-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 6
  name: Openstatus Rate Limits
  slug: openstatus-rate-limits
score:
  band: developing
  composite: 40.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 59.1
    developer_ergonomics: 25.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 41.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openstatus/refs/heads/main/screenshots/openstatus-2026-08-07T190644.png
security:
- kind: authentication
  name: Openstatus Authentication
  slug: openstatus-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Openstatus Domain Security
  slug: openstatus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Openstatus Vulnerability Disclosure
  slug: openstatus-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Openstatus Trust Center
  slug: openstatus-trust-center
  summary_line: SOC 2
slug: openstatus
tags:
- Monitoring
- Synthetic Monitoring
- Uptime
- Status Pages
- Incidents
- Open-Source
- Observability
website: https://www.openstatus.dev
---
