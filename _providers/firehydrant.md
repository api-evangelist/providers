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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Firehydrant Agentic Access
  operation_count: 38
  slug: firehydrant-agentic-access
  summary_line: 38 operations · 21 acting
api_count: 16
apis:
- description: FireHydrant is an incident management platform providing automated runbooks, status pages, and retrospective workflows.
  name: FireHydrant
  slug: firehydrant
- description: The Audits API from FireHydrant — 1 operation(s) for audits.
  name: FireHydrant Audits API
  slug: firehydrant-audits-api
- description: The Change Events API from FireHydrant — 2 operation(s) for change events.
  name: FireHydrant Change Events API
  slug: firehydrant-change-events-api
- description: The Changes API from FireHydrant — 1 operation(s) for changes.
  name: FireHydrant Changes API
  slug: firehydrant-changes-api
- description: The Conversations API from FireHydrant — 1 operation(s) for conversations.
  name: FireHydrant Conversations API
  slug: firehydrant-conversations-api
- description: The Environments API from FireHydrant — 2 operation(s) for environments.
  name: FireHydrant Environments API
  slug: firehydrant-environments-api
- description: The Functionalities API from FireHydrant — 1 operation(s) for functionalities.
  name: FireHydrant Functionalities API
  slug: firehydrant-functionalities-api
- description: The Incidents API from FireHydrant — 5 operation(s) for incidents.
  name: FireHydrant Incidents API
  slug: firehydrant-incidents-api
- description: The Ping API from FireHydrant — 1 operation(s) for ping.
  name: FireHydrant Ping API
  slug: firehydrant-ping-api
- description: The Priorities API from FireHydrant — 1 operation(s) for priorities.
  name: FireHydrant Priorities API
  slug: firehydrant-priorities-api
- description: The Runbooks API from FireHydrant — 2 operation(s) for runbooks.
  name: FireHydrant Runbooks API
  slug: firehydrant-runbooks-api
- description: The Scheduled Maintenances API from FireHydrant — 1 operation(s) for scheduled maintenances.
  name: FireHydrant Scheduled Maintenances API
  slug: firehydrant-scheduled-maintenances-api
- description: The Services API from FireHydrant — 2 operation(s) for services.
  name: FireHydrant Services API
  slug: firehydrant-services-api
- description: The Severities API from FireHydrant — 1 operation(s) for severities.
  name: FireHydrant Severities API
  slug: firehydrant-severities-api
- description: The Signals API from FireHydrant — 1 operation(s) for signals.
  name: FireHydrant Signals API
  slug: firehydrant-signals-api
- description: The Teams API from FireHydrant — 2 operation(s) for teams.
  name: FireHydrant Teams API
  slug: firehydrant-teams-api
artifact_total: 25
collections:
- collection_type: open
  name: FireHydrant REST API
  slug: open-firehydrant
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/firehydrant-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/firehydrant-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/firehydrant-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/firehydrant-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/firehydrant
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/firehydrant
- group: company
  title: ''
  type: Website
  url: https://firehydrant.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.firehydrant.io
- group: company
  title: ''
  type: Blog
  url: https://firehydrant.com/rss.xml
created: '2026-03-27'
description: FireHydrant is an incident management platform providing automated runbooks, status pages, and retrospective workflows.
finops:
- name: Firehydrant Finops
  service_category: API
  slug: firehydrant-finops
graphqls:
- description: FireHydrant is a reliability operations and incident management platform. This conceptual GraphQL schema models the core resources available through the FireHydrant REST API at https://developers.fire
  name: FireHydrant GraphQL Schema
  slug: firehydrant-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/firehydrant.png
layout: provider
modified: '2026-03-27'
name: FireHydrant
nav: Providers
network: true
overview: 'FireHydrant publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Audits API, Change Events API, Changes API, and 12 more. Tagged areas include AIOps and Incident Management.


  FireHydrant''s developer surface includes authentication, documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Firehydrant Plans Pricing
  plan_count: 3
  slug: firehydrant-plans-pricing
random_paper: 54
rate_limits:
- limit_count: 5
  name: Firehydrant Rate Limits
  slug: firehydrant-rate-limits
score:
  band: thin
  composite: 38.9
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 62.8
    developer_ergonomics: 21.7
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/firehydrant/refs/heads/main/screenshots/firehydrant-2026-06-20T181235.png
security:
- kind: authentication
  name: Firehydrant Authentication
  slug: firehydrant-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Firehydrant Domain Security
  slug: firehydrant-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Firehydrant Trust Center
  slug: firehydrant-trust-center
  summary_line: SOC 2, ISO 27001, CSA STAR
slug: firehydrant
tags:
- AIOps
- Incident Management
website: https://firehydrant.com
---
