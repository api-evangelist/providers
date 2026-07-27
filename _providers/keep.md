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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 41.3
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 81
  human_in_the_loop: 5
  name: Keep Agentic Access
  operation_count: 136
  slug: keep-agentic-access
  summary_line: 136 operations · 81 acting · 5 human-in-the-loop
api_count: 27
apis:
- description: The actions API from Keep — 2 operation(s) for actions.
  name: Keep actions API
  slug: keep-actions-api
- description: The alerts API from Keep — 24 operation(s) for alerts.
  name: Keep alerts API
  slug: keep-alerts-api
- description: The auth API from Keep — 8 operation(s) for auth.
  name: Keep auth API
  slug: keep-auth-api
- description: The dashboard API from Keep — 3 operation(s) for dashboard.
  name: Keep dashboard API
  slug: keep-dashboard-api
- description: The deduplications API from Keep — 3 operation(s) for deduplications.
  name: Keep deduplications API
  slug: keep-deduplications-api
- description: The enrichment API from Keep — 4 operation(s) for enrichment.
  name: Keep enrichment API
  slug: keep-enrichment-api
- description: The extraction API from Keep — 2 operation(s) for extraction.
  name: Keep extraction API
  slug: keep-extraction-api
- description: The groups API from Keep — 2 operation(s) for groups.
  name: Keep groups API
  slug: keep-groups-api
- description: The healthcheck API from Keep — 1 operation(s) for healthcheck.
  name: Keep healthcheck API
  slug: keep-healthcheck-api
- description: The incidents API from Keep — 13 operation(s) for incidents.
  name: Keep incidents API
  slug: keep-incidents-api
- description: The Keep API API from Keep — 1 operation(s) for keep api.
  name: Keep Keep API API
  slug: keep-keep-api-api
- description: The maintenance API from Keep — 2 operation(s) for maintenance.
  name: Keep maintenance API
  slug: keep-maintenance-api
- description: The mapping API from Keep — 2 operation(s) for mapping.
  name: Keep mapping API
  slug: keep-mapping-api
- description: The metrics API from Keep — 1 operation(s) for metrics.
  name: Keep metrics API
  slug: keep-metrics-api
- description: The permissions API from Keep — 2 operation(s) for permissions.
  name: Keep permissions API
  slug: keep-permissions-api
- description: The preset API from Keep — 5 operation(s) for preset.
  name: Keep preset API
  slug: keep-preset-api
- description: The providers API from Keep — 16 operation(s) for providers.
  name: Keep providers API
  slug: keep-providers-api
- description: The pusher API from Keep — 1 operation(s) for pusher.
  name: Keep pusher API
  slug: keep-pusher-api
- description: The roles API from Keep — 2 operation(s) for roles.
  name: Keep roles API
  slug: keep-roles-api
- description: The rules API from Keep — 2 operation(s) for rules.
  name: Keep rules API
  slug: keep-rules-api
- description: The settings API from Keep — 7 operation(s) for settings.
  name: Keep settings API
  slug: keep-settings-api
- description: The status API from Keep — 1 operation(s) for status.
  name: Keep status API
  slug: keep-status-api
- description: The tags API from Keep — 1 operation(s) for tags.
  name: Keep tags API
  slug: keep-tags-api
- description: The topology API from Keep — 3 operation(s) for topology.
  name: Keep topology API
  slug: keep-topology-api
- description: The users API from Keep — 2 operation(s) for users.
  name: Keep users API
  slug: keep-users-api
- description: The whoami API from Keep — 1 operation(s) for whoami.
  name: Keep whoami API
  slug: keep-whoami-api
- description: The workflows API from Keep — 11 operation(s) for workflows.
  name: Keep workflows API
  slug: keep-workflows-api
artifact_total: 32
collections:
- collection_type: open
  name: Keep API
  slug: open-keep
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/keep-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/keep-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/keep-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/keep-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/keepalerting
- group: company
  title: ''
  type: Website
  url: https://www.keephq.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.keephq.dev
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/keephq
- group: build
  title: ''
  type: GitHubRepo
  url: https://github.com/keephq/keep
- group: start
  title: ''
  type: Signup
  url: https://platform.keephq.dev
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.keephq.dev/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.keephq.dev/blog
created: '2026-05-11'
description: Keep is an open-source AIOps and alert management platform that unifies alerts from any monitoring tool, providing deduplication, correlation, enrichment, and workflow automation across observability, incident response, ticketing, and CMDB systems. The Keep REST API enables programmatic access to alerts, incidents, workflows, providers, and integrations with FastAPI-generated OpenAPI documentation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/keep.png
layout: provider
modified: '2026-05-11'
name: Keep
nav: Providers
network: true
overview: 'Keep publishes 27 APIs on the [APIs.io](https://apis.io/) network, including actions API, alerts API, auth API, and 24 more. Tagged areas include AIOps, Alerting, Incident Management, Observability, and Open Source.


  Keep''s developer surface includes authentication, documentation, signup flow, engineering blog, and 8 more developer resources.'
random_paper: 13
scopes:
- name: Keep Scopes
  scope_count: 0
  slug: keep-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 27.7
  delta: 3.2
  facets:
    commercial_clarity: 0.0
    contract_quality: 50.7
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 24.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/keep/refs/heads/main/screenshots/keep-2026-06-20T183935.png
security:
- kind: authentication
  name: Keep Authentication
  slug: keep-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Keep Domain Security
  slug: keep-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: keep
tags:
- AIOps
- Alerting
- Incident Management
- Observability
- Open Source
- SRE
- Workflow Automation
website: https://www.keephq.dev
---
