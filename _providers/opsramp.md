---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
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
  score: 17.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Opsramp Agentic Access
  operation_count: 16
  slug: opsramp-agentic-access
  summary_line: 16 operations · 9 acting
api_count: 10
apis:
- description: The Alerts API from OpsRamp — 3 operation(s) for alerts.
  name: OpsRamp Alerts API
  slug: opsramp-alerts-api
- description: The Alerts Search API from OpsRamp — 1 operation(s) for alerts search.
  name: OpsRamp Alerts Search API
  slug: opsramp-alerts-search-api
- description: The Jobs API from OpsRamp — 2 operation(s) for jobs.
  name: OpsRamp Jobs API
  slug: opsramp-jobs-api
- description: The Monitoring API from OpsRamp — 1 operation(s) for monitoring.
  name: OpsRamp Monitoring API
  slug: opsramp-monitoring-api
- description: The Resourcemonitors API from OpsRamp — 1 operation(s) for resourcemonitors.
  name: OpsRamp Resourcemonitors API
  slug: opsramp-resourcemonitors-api
- description: The Resources API from OpsRamp — 3 operation(s) for resources.
  name: OpsRamp Resources API
  slug: opsramp-resources-api
- description: The Resources Search API from OpsRamp — 1 operation(s) for resources search.
  name: OpsRamp Resources Search API
  slug: opsramp-resources-search-api
- description: The Tenancy API from OpsRamp — 1 operation(s) for tenancy.
  name: OpsRamp Tenancy API
  slug: opsramp-tenancy-api
- description: The Ticketentity API from OpsRamp — 2 operation(s) for ticketentity.
  name: OpsRamp Ticketentity API
  slug: opsramp-ticketentity-api
- description: The Ticketentity Search API from OpsRamp — 1 operation(s) for ticketentity search.
  name: OpsRamp Ticketentity Search API
  slug: opsramp-ticketentity-search-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OpsRamp Alerts API
  slug: open-opsramp-alerts-api
- collection_type: open
  name: OpsRamp Alerts Alerts Search API
  slug: open-opsramp-alerts-search-api
- collection_type: open
  name: OpsRamp Alerts Jobs API
  slug: open-opsramp-jobs-api
- collection_type: open
  name: OpsRamp Alerts Monitoring API
  slug: open-opsramp-monitoring-api
- collection_type: open
  name: OpsRamp Alerts Resourcemonitors API
  slug: open-opsramp-resourcemonitors-api
- collection_type: open
  name: OpsRamp Alerts Resources API
  slug: open-opsramp-resources-api
- collection_type: open
  name: OpsRamp Alerts Resources Search API
  slug: open-opsramp-resources-search-api
- collection_type: open
  name: OpsRamp Alerts Tenancy API
  slug: open-opsramp-tenancy-api
- collection_type: open
  name: OpsRamp Alerts Ticketentity API
  slug: open-opsramp-ticketentity-api
- collection_type: open
  name: OpsRamp Alerts Ticketentity Search API
  slug: open-opsramp-ticketentity-search-api
- collection_type: open
  name: OpsRamp API
  slug: open-opsramp
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/opsramp-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opsramp-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/opsramp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/opsramp
- group: company
  title: ''
  type: Website
  url: https://www.opsramp.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.opsramp.com
- group: company
  title: ''
  type: Blog
  url: https://blog.opsramp.com/rss.xml
created: '2026-03-27'
description: OpsRamp is an AIOps and IT operations management platform for hybrid infrastructure monitoring and management.
finops:
- name: Opsramp Finops
  service_category: API
  slug: opsramp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opsramp.png
layout: provider
modified: '2026-05-19'
name: OpsRamp
nav: Providers
network: true
overview: 'OpsRamp publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Alerts Search API, Jobs API, and 7 more. Tagged areas include AIOps and IT Operations.


  OpsRamp''s developer surface includes documentation, engineering blog, and 5 more developer resources.'
plans:
- name: Opsramp Plans Pricing
  plan_count: 3
  slug: opsramp-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Opsramp Rate Limits
  slug: opsramp-rate-limits
score:
  band: emerging
  composite: 22.3
  coverage:
    artifact_dirs: 9
    catalog_gap: 81.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 42.9
    developer_ergonomics: 11.9
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 22.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opsramp/refs/heads/main/screenshots/opsramp-2026-06-20T191106.png
security:
- kind: domain-security
  name: Opsramp Domain Security
  slug: opsramp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: opsramp
tags:
- AIOps
- IT Operations
website: https://www.opsramp.com
---
