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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 55
  human_in_the_loop: 3
  name: Athenian Agentic Access
  operation_count: 79
  slug: athenian-agentic-access
  summary_line: 79 operations · 55 acting · 3 human-in-the-loop
api_count: 16
apis:
- description: The align API from Athenian — 3 operation(s) for align.
  name: Athenian align API
  slug: athenian-align-api
- description: The default API from Athenian — 70 operation(s) for default.
  name: Athenian default API
  slug: athenian-default-api
- description: The events API from Athenian — 4 operation(s) for events.
  name: Athenian events API
  slug: athenian-events-api
- description: The filter API from Athenian — 11 operation(s) for filter.
  name: Athenian filter API
  slug: athenian-filter-api
- description: The get API from Athenian — 4 operation(s) for get.
  name: Athenian get API
  slug: athenian-get-api
- description: The histograms API from Athenian — 3 operation(s) for histograms.
  name: Athenian histograms API
  slug: athenian-histograms-api
- description: The integrations API from Athenian — 2 operation(s) for integrations.
  name: Athenian integrations API
  slug: athenian-integrations-api
- description: The metrics API from Athenian — 7 operation(s) for metrics.
  name: Athenian metrics API
  slug: athenian-metrics-api
- description: The pagination API from Athenian — 1 operation(s) for pagination.
  name: Athenian pagination API
  slug: athenian-pagination-api
- description: The registration API from Athenian — 6 operation(s) for registration.
  name: Athenian registration API
  slug: athenian-registration-api
- description: The reposet API from Athenian — 3 operation(s) for reposet.
  name: Athenian reposet API
  slug: athenian-reposet-api
- description: The security API from Athenian — 3 operation(s) for security.
  name: Athenian security API
  slug: athenian-security-api
- description: The settings API from Athenian — 13 operation(s) for settings.
  name: Athenian settings API
  slug: athenian-settings-api
- description: The team API from Athenian — 3 operation(s) for team.
  name: Athenian team API
  slug: athenian-team-api
- description: The user API from Athenian — 6 operation(s) for user.
  name: Athenian user API
  slug: athenian-user-api
- description: The version API from Athenian — 1 operation(s) for version.
  name: Athenian version API
  slug: athenian-version-api
artifact_total: 37
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: '{{ title }} align API'
  slug: open-athenian-align-api
- collection_type: open
  name: '{{ title }} align default API'
  slug: open-athenian-default-api
- collection_type: open
  name: '{{ title }} align events API'
  slug: open-athenian-events-api
- collection_type: open
  name: '{{ title }} align filter API'
  slug: open-athenian-filter-api
- collection_type: open
  name: '{{ title }} align get API'
  slug: open-athenian-get-api
- collection_type: open
  name: '{{ title }} align histograms API'
  slug: open-athenian-histograms-api
- collection_type: open
  name: '{{ title }} align integrations API'
  slug: open-athenian-integrations-api
- collection_type: open
  name: '{{ title }} align metrics API'
  slug: open-athenian-metrics-api
- collection_type: open
  name: '{{ title }} align pagination API'
  slug: open-athenian-pagination-api
- collection_type: open
  name: '{{ title }} align registration API'
  slug: open-athenian-registration-api
- collection_type: open
  name: '{{ title }} align reposet API'
  slug: open-athenian-reposet-api
- collection_type: open
  name: '{{ title }} align security API'
  slug: open-athenian-security-api
- collection_type: open
  name: '{{ title }} align settings API'
  slug: open-athenian-settings-api
- collection_type: open
  name: '{{ title }} align team API'
  slug: open-athenian-team-api
- collection_type: open
  name: '{{ title }} align user API'
  slug: open-athenian-user-api
- collection_type: open
  name: '{{ title }} align version API'
  slug: open-athenian-version-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/athenian-openapi-overlay.yaml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/athenianco/athenian-api-open/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/athenianco/athenian-api-open/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/athenian-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/athenian-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/athenian-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/athenian-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/athenian-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/athenian-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/athenianco
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/athenianco/athenian-api-open
- group: company
  title: ''
  type: Website
  url: https://athenian.com
created: '2026-07-17'
description: 'Athenian was a full-cycle software-development analytics platform founded in 2019 by Eiso Kant, with a seed round led by Point Nine. It integrated GitHub, JIRA, and CI/CD tooling to give engineering leaders end-to-end visibility into their delivery pipeline — lead time, cycle time, deployment frequency, PR review dynamics, and goal alignment — deliberately measuring teams and events rather than ranking individuals. The company has since wound down: athenian.com and athenian.co now redirect to github.com/athenianco and the production API host api.athenian.co no longer resolves. However, the OpenAPI specification (athenianco/api-spec, 79 operations, 218 schemas) and the open-source API implementation (athenian-api-open, MIT) remain publicly published on GitHub, which is why this profile is enriched from the real, still-available API contract.'
image: https://avatars.githubusercontent.com/u/58329504?v=4
layout: provider
mcp_servers:
- description: ''
  name: athenian-mcp.yml
  slug: athenian-mcpyml
modified: '2026-07-18'
name: Athenian
nav: Providers
network: true
overview: 'Athenian publishes 16 APIs on the [APIs.io](https://apis.io/) network, including align API, default API, events API, and 13 more. Tagged areas include Company, Engineering Intelligence, Software Development Analytics, Developer Productivity, and DevOps.


  Athenian''s developer surface includes authentication and 12 more developer resources.'
random_paper: 95
score:
  band: emerging
  composite: 26.1
  delta: -0.2
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 16.7
    contract_quality: 51.3
    developer_ergonomics: 13.7
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 2.6
  previous_composite: 26.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/athenian/refs/heads/main/screenshots/athenian-2026-07-25T201535.png
security:
- kind: authentication
  name: Athenian Authentication
  slug: athenian-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Athenian Domain Security
  slug: athenian-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: athenian
tags:
- Company
- Engineering Intelligence
- Software Development Analytics
- Developer Productivity
- DevOps
- Metrics
- Git
- JIRA
- CI/CD
- Analytics
website: https://athenian.com
---
