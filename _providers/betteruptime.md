---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Betteruptime Agentic Access
  operation_count: 16
  slug: betteruptime-agentic-access
  summary_line: 16 operations · 9 acting
api_count: 1
apis:
- description: Manage heartbeat monitors for cron jobs and background workers
  name: Better Uptime Heartbeats API
  slug: betteruptime-heartbeats-api
- description: View and manage incidents triggered by monitors
  name: Better Uptime Incidents API
  slug: betteruptime-incidents-api
- description: Manage uptime monitors for websites and services
  name: Better Uptime Monitors API
  slug: betteruptime-monitors-api
- description: Manage public status pages for communicating service health
  name: Better Uptime Status Pages API
  slug: betteruptime-status-pages-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Better Stack Uptime Heartbeats API
  slug: open-betteruptime-heartbeats-api
- collection_type: open
  name: Better Stack Uptime Heartbeats Incidents API
  slug: open-betteruptime-incidents-api
- collection_type: open
  name: Better Stack Uptime Heartbeats Monitors API
  slug: open-betteruptime-monitors-api
- collection_type: open
  name: Better Stack Uptime Heartbeats Status Pages API
  slug: open-betteruptime-status-pages-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/betteruptime-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/betteruptime-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/betteruptime-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/betteruptime-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/betteruptime-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://betterstack.com/uptime
- group: docs
  title: ''
  type: Documentation
  url: https://betterstack.com/docs/uptime/api/getting-started-with-uptime-api/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BetterStackHQ
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/betterstack
- group: other
  title: ''
  type: X
  url: https://x.com/betteruptime
- group: company
  title: ''
  type: Blog
  url: https://betterstack.com/community/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://betterstack.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.betterstack.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/betteruptime-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/betteruptime-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/betteruptime-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/betteruptime-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/betteruptime-context.jsonld
- group: company
  title: ''
  type: BlogFeed
  url: blogs/blogs.json
created: '2026-06-12'
description: Better Uptime (now part of Better Stack) is an uptime monitoring and incident management platform that helps engineering teams detect outages, manage on-call schedules, and communicate incidents through status pages. The platform provides a REST API following the JSON:API specification for programmatic management of monitors, heartbeats, on-call schedules, status pages, and integrations. Better Stack supports Bearer token authentication with both global and team-scoped API tokens, and offers a Terraform provider for infrastructure-as-code workflows.
examples:
- key_count: 2
  name: Betteruptime Create Monitor Example
  slug: betteruptime-create-monitor-example
- key_count: 1
  name: Betteruptime Get Monitor Example
  slug: betteruptime-get-monitor-example
- key_count: 2
  name: Betteruptime List Incidents Example
  slug: betteruptime-list-incidents-example
- key_count: 2
  name: Betteruptime List Monitors Example
  slug: betteruptime-list-monitors-example
finops:
- name: Betteruptime Finops
  service_category: Monitoring
  slug: betteruptime-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/betteruptime.png
json_schemas:
- name: Better Stack Heartbeat
  property_count: 1
  slug: betteruptime-heartbeat
- name: Better Stack Incident
  property_count: 1
  slug: betteruptime-incident
- name: Better Stack Monitor
  property_count: 1
  slug: betteruptime-monitor
- name: Better Stack Status Page
  property_count: 1
  slug: betteruptime-status-page
jsonld:
- class_count: 2
  name: Betteruptime Context
  property_count: 48
  slug: betteruptime-context
layout: provider
modified: '2026-06-12'
name: Better Uptime
nav: Providers
network: true
overview: 'Better Uptime publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Heartbeats API, Incidents API, Monitors API, and 1 more. Tagged areas include Uptime Monitoring, Incident Management, Status Pages, On-Call Scheduling, and Observability.


  The Better Uptime catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Better Uptime''s developer surface includes authentication, documentation, engineering blog, pricing, and 15 more developer resources.'
plans:
- name: Betteruptime Plans Pricing
  plan_count: 3
  slug: betteruptime-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Betteruptime Rate Limits
  slug: betteruptime-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Better Uptime API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: betteruptime-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.6
  coverage:
    artifact_dirs: 15
    catalog_gap: 38.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 25.0
    contract_quality: 65.3
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 23.7
  previous_composite: 45.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/betteruptime/refs/heads/main/screenshots/betteruptime-2026-06-20T173208.png
security:
- kind: authentication
  name: Betteruptime Authentication
  slug: betteruptime-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Betteruptime Domain Security
  slug: betteruptime-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Betteruptime Vulnerability Disclosure
  slug: betteruptime-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Betteruptime Trust Center
  slug: betteruptime-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: betteruptime
tags:
- Uptime Monitoring
- Incident Management
- Status Pages
- On-Call Scheduling
- Observability
- DevOps
website: https://betterstack.com/uptime
---
