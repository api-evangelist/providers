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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Swarmia Agentic Access
  operation_count: 12
  slug: swarmia-agentic-access
  summary_line: 12 operations · 6 acting
api_count: 6
apis:
- description: Ingestion of usage data from external AI assistant tools.
  name: Swarmia Additional AI integrations API
  slug: swarmia-additional-ai-integrations-api
- description: Machine-readable versions of major reports found in the Swarmia app.
  name: Swarmia Built-in reports API
  slug: swarmia-built-in-reports-api
- description: Saved custom reports created in the Swarmia explore view.
  name: Swarmia Custom reports API
  slug: swarmia-custom-reports-api
- description: Deployment and fix-deployment event ingestion for delivery and DORA metrics.
  name: Swarmia Deployments API
  slug: swarmia-deployments-api
- description: Programmatic management of teams and memberships.
  name: Swarmia Team management API
  slug: swarmia-team-management-api
- description: Create, read, update, and delete employee time-off periods.
  name: Swarmia Time off API
  slug: swarmia-time-off-api
artifact_total: 14
collections:
- collection_type: open
  name: Swarmia API
  slug: open-swarmia
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/swarmia-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/swarmia-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/swarmia-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/swarmia-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/swarmia
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/swarmia
- group: company
  title: ''
  type: Website
  url: https://www.swarmia.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.swarmia.com
- group: commercial
  title: ''
  type: Plans
  url: plans/swarmia-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/swarmia-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/swarmia-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.swarmia.com/rss.xml
created: '2026-06-21'
description: Swarmia is an engineering-effectiveness analytics platform that combines software delivery metrics (DORA), developer experience, investment balance, and AI adoption insights. Its REST API lets teams export built-in and custom reports, ingest deployment and events data, manage teams and memberships, and record time off, authenticated with Bearer API tokens.
finops:
- name: Swarmia Finops
  service_category: Developer Tools
  slug: swarmia-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/swarmia.png
layout: provider
modified: '2026-06-21'
name: Swarmia
nav: Providers
network: true
overview: 'Swarmia publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Additional AI integrations API, Built-in reports API, Custom reports API, and 3 more. Tagged areas include Engineering Effectiveness, Developer Productivity, DORA, Software Delivery, and Analytics.


  Swarmia''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Swarmia Plans Pricing
  plan_count: 4
  slug: swarmia-plans-pricing
random_paper: 63
rate_limits:
- limit_count: 3
  name: Swarmia Rate Limits
  slug: swarmia-rate-limits
score:
  band: thin
  composite: 38.6
  delta: -2.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 56.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Swarmia Authentication
  slug: swarmia-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Swarmia Domain Security
  slug: swarmia-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Swarmia Vulnerability Disclosure
  slug: swarmia-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: swarmia
tags:
- Engineering Effectiveness
- Developer Productivity
- DORA
- Software Delivery
- Analytics
website: https://www.swarmia.com
---
