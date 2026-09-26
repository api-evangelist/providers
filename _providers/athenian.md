---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - '{''url'': ''https://athenian.com'', ''status'': 301, ''note'': ''declared website redirects to https://github.com/athenianco — a different registrable domain (athenian.com -> github.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 41
  human_in_the_loop: 2
  name: Athenian Agentic Access
  operation_count: 79
  slug: athenian-agentic-access
  summary_line: 79 operations · 41 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.athenian.co/v1
  baseurl_source: declared
  description: The align API from Athenian — 3 operation(s) for align.
  name: Athenian Align API
  slug: athenian-align-api
- baseURL: https://api.athenian.co/v1
  baseurl_source: declared
  description: The events API from Athenian — 4 operation(s) for events.
  name: Athenian Events API
  slug: athenian-events-api
- baseURL: https://api.athenian.co/v1
  baseurl_source: declared
  description: The filter API from Athenian — 11 operation(s) for filter.
  name: Athenian Filter API
  slug: athenian-filter-api
- baseURL: https://api.athenian.co/v1
  baseurl_source: declared
  description: The get API from Athenian — 4 operation(s) for get.
  name: Athenian Get API
  slug: athenian-get-api
- baseURL: https://api.athenian.co/v1
  baseurl_source: declared
  description: The histograms API from Athenian — 3 operation(s) for histograms.
  name: Athenian Histograms API
  slug: athenian-histograms-api
- baseURL: https://api.athenian.co/v1
  baseurl_source: declared
  description: The integrations API from Athenian — 2 operation(s) for integrations.
  name: Athenian Integrations API
  slug: athenian-integrations-api
- baseURL: https://api.athenian.co/v1
  baseurl_source: declared
  description: The metrics API from Athenian — 7 operation(s) for metrics.
  name: Athenian Metrics API
  slug: athenian-metrics-api
- baseURL: https://api.athenian.co/v1
  baseurl_source: declared
  description: The pagination API from Athenian — 1 operation(s) for pagination.
  name: Athenian Pagination API
  slug: athenian-pagination-api
- baseURL: https://api.athenian.co/v1
  baseurl_source: declared
  description: The registration API from Athenian — 6 operation(s) for registration.
  name: Athenian Registration API
  slug: athenian-registration-api
- baseURL: https://api.athenian.co/v1
  baseurl_source: declared
  description: The reposet API from Athenian — 3 operation(s) for reposet.
  name: Athenian Reposet API
  slug: athenian-reposet-api
- baseURL: https://api.athenian.co/v1
  baseurl_source: declared
  description: The security API from Athenian — 3 operation(s) for security.
  name: Athenian Security API
  slug: athenian-security-api
- baseURL: https://api.athenian.co/v1
  baseurl_source: declared
  description: The settings API from Athenian — 13 operation(s) for settings.
  name: Athenian Settings API
  slug: athenian-settings-api
- baseURL: https://api.athenian.co/v1
  baseurl_source: declared
  description: The team API from Athenian — 3 operation(s) for team.
  name: Athenian Team API
  slug: athenian-team-api
- baseURL: https://api.athenian.co/v1
  baseurl_source: declared
  description: The user API from Athenian — 6 operation(s) for user.
  name: Athenian User API
  slug: athenian-user-api
- baseURL: https://api.athenian.co/v1
  baseurl_source: declared
  description: The version API from Athenian — 1 operation(s) for version.
  name: Athenian Version API
  slug: athenian-version-api
artifact_total: 35
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
  href: https://raw.githubusercontent.com/api-evangelist/athenian/refs/heads/main/overlays/athenian-openapi-overlay.yaml
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
  href: https://raw.githubusercontent.com/api-evangelist/athenian/refs/heads/main/agentic-access/athenian-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/athenian-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/athenian/refs/heads/main/security/athenian-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/athenian-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/athenian/refs/heads/main/authentication/athenian-authentication.yml
  title: ''
  type: Authentication
  url: authentication/athenian-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/athenian/refs/heads/main/mcp/athenian-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/athenian-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/athenian/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/athenian/refs/heads/main/lifecycle/athenian-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/athenian-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/athenian/refs/heads/main/llms/athenian-llms.txt
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
modified: '2026-07-18'
name: Athenian
nav: Providers
network: true
overview: 'Athenian publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Align API, Events API, Filter API, and 12 more. Tagged areas include Company, Engineering Intelligence, Software Development Analytics, Developer Productivity, and DevOps.


  Athenian''s developer surface includes authentication and 12 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -30.2
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  lifecycle: defunct
  previous_composite: 30.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: falling
  upsert:
    applies: true
    score: 72.2
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
- Jira
- CI/CD
- Analytics
website: https://athenian.com
---
