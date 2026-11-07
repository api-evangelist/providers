---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: operate
  href: https://artifacts.apis.io/metric-insights/changelog/metric-insights-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/metric-insights-changelog.yml
- group: agent
  href: https://artifacts.apis.io/metric-insights/llms/metric-insights-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/metric-insights-llms.txt
- group: agent
  href: https://artifacts.apis.io/metric-insights/mcp/metric-insights-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/metric-insights-mcp.yml
- group: other
  href: https://artifacts.apis.io/metric-insights/hosts/metric-insights-hosts.yml
  title: ''
  type: Hosts
  url: hosts/metric-insights-hosts.yml
- group: other
  href: https://artifacts.apis.io/metric-insights/vendors/metric-insights-vendors.yml
  title: ''
  type: Vendors
  url: vendors/metric-insights-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.metricinsights.com/
- group: auth
  href: https://artifacts.apis.io/metric-insights/security/metric-insights-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/metric-insights-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.metricinsights.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.metricinsights.com/
- group: docs
  title: ''
  type: APIReference
  url: https://www.metricinsights.com/platform/concierge/documentation-faqs/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.metricinsights.com/schedule-a-demo/
- group: operate
  title: ''
  type: Support
  url: https://help.metricinsights.com/
- group: company
  title: ''
  type: Blog
  url: https://www.metricinsights.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/metricinsights
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on discovered hosts.
  evidence:
  - status: 0
    url: https://api.metricinsights.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Metric Insights provides a governed business intelligence (BI) platform that enables organizations to discover, govern, and operationalize data across BI tools, analytics, and AI. Their cloud SaaS and self‑hosted solutions offer data catalog, metadata management, security, alerting, and a conversational AI concierge to help users explore insights. The platform integrates with Tableau, Power BI, Qlik, Sigma and many others, delivering a unified data governance experience for modern enterprises.
layout: provider
mcp_servers:
- description: Remote MCP server at support.metricinsights.com.
  name: Metric Insights MCP Server
  slug: metric-insights-mcp-yml
modified: '2026-10-29'
name: Metric Insights
nav: Providers
network: true
overview: 'Metric Insights is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Business Intelligence, Data Governance, Analytics, Artificial Intelligence, and Software-as-a-Service.


  Metric Insights'' developer surface includes changelog, documentation, API reference, getting-started guide, support, engineering blog, and 8 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.9
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 55.0
    operational_transparency: 26.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 16.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/metric-insights/metric-insights-2026-11-03T135543.png
security:
- kind: domain-security
  name: Metric Insights Domain Security
  slug: metric-insights-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: metric-insights
tags:
- Business Intelligence
- Data Governance
- Analytics
- Artificial Intelligence
- Software-as-a-Service
website: https://www.metricinsights.com/
---
