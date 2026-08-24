---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Uptime Com Agentic Access
  operation_count: 39
  slug: uptime-com-agentic-access
  summary_line: 39 operations · 22 acting
api_count: 7
apis:
- description: Create, list, update, pause, resume, and delete monitoring checks.
  name: Uptime.com Checks API
  slug: uptime-com-checks-api
- description: Manage contact groups used for alert notifications.
  name: Uptime.com Contacts API
  slug: uptime-com-contacts-api
- description: Manage notification integrations.
  name: Uptime.com Integrations API
  slug: uptime-com-integrations-api
- description: List and retrieve detected outage records.
  name: Uptime.com Outages API
  slug: uptime-com-outages-api
- description: Create, list, update, and delete SLA reports.
  name: Uptime.com SLA Reports API
  slug: uptime-com-sla-reports-api
- description: Manage status pages, components, and incidents.
  name: Uptime.com Status Pages API
  slug: uptime-com-status-pages-api
- description: Manage color-coded check tags.
  name: Uptime.com Tags API
  slug: uptime-com-tags-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Uptime.com REST Checks API
  slug: open-uptime-com-checks-api
- collection_type: open
  name: Uptime.com REST Checks Contacts API
  slug: open-uptime-com-contacts-api
- collection_type: open
  name: Uptime.com REST Checks Integrations API
  slug: open-uptime-com-integrations-api
- collection_type: open
  name: Uptime.com REST Checks Outages API
  slug: open-uptime-com-outages-api
- collection_type: open
  name: Uptime.com REST Checks SLA Reports API
  slug: open-uptime-com-sla-reports-api
- collection_type: open
  name: Uptime.com REST Checks Status Pages API
  slug: open-uptime-com-status-pages-api
- collection_type: open
  name: Uptime.com REST Checks Tags API
  slug: open-uptime-com-tags-api
- collection_type: open
  name: Uptime.com REST API
  slug: open-uptime-com
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/uptime-com-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uptime-com-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uptime-com-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/uptime-com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/uptime-com
- group: company
  title: ''
  type: Website
  url: https://uptime.com/
- group: docs
  title: ''
  type: Documentation
  url: https://uptime.com/api/v1/docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/uptime-com-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/uptime-com-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/uptime-com-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://uptime.com/blog/feed/
created: '2026-06-21'
description: Uptime.com is a website, application, and infrastructure monitoring platform providing uptime checks, transaction and API monitoring, page speed checks, SLA reporting, status pages, and alerting from a global network of probe servers. Its REST API at https://uptime.com/api/v1 (Token authentication) lets customers programmatically manage checks, outages, SLA reports, status pages, contacts, integrations, and tags.
finops:
- name: Uptime Com Finops
  service_category: Monitoring and Observability
  slug: uptime-com-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uptime-com.png
layout: provider
modified: '2026-06-21'
name: Uptime.com
nav: Providers
network: true
overview: 'Uptime.com publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Checks API, Contacts API, Integrations API, and 4 more. Tagged areas include Monitoring, Uptime, Website Monitoring, Status Pages, and SLA.


  Uptime.com''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Uptime Com Plans Pricing
  plan_count: 4
  slug: uptime-com-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 4
  name: Uptime Com Rate Limits
  slug: uptime-com-rate-limits
score:
  band: thin
  composite: 38.0
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 54.1
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 38.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Uptime Com Authentication
  slug: uptime-com-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Uptime Com Domain Security
  slug: uptime-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: uptime-com
tags:
- Monitoring
- Uptime
- Website Monitoring
- Status Pages
- SLA
website: https://uptime.com/
---
