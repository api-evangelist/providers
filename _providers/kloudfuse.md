---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: templated
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.3
  scored_at: '2026-10-17'
api_count: 10
apis:
- baseURL: https://{instance}
  baseurl_source: declared
  description: The Cardinality Explorer API from Kloudfuse — 3 operation(s) for cardinality explorer.
  name: Kloudfuse Cardinality Explorer API
  slug: kloudfuse-cardinality-explorer-api
- baseURL: https://{instance}
  baseurl_source: declared
  description: The Events API from Kloudfuse — 1 operation(s) for events.
  name: Kloudfuse Events API
  slug: kloudfuse-events-api
- baseURL: https://{instance}
  baseurl_source: declared
  description: The Folders API from Kloudfuse — 9 operation(s) for folders.
  name: Kloudfuse Folders API
  slug: kloudfuse-folders-api
- baseURL: https://{instance}
  baseurl_source: declared
  description: The Hydration API from Kloudfuse — 7 operation(s) for hydration.
  name: Kloudfuse Hydration API
  slug: kloudfuse-hydration-api
- baseURL: https://{instance}
  baseurl_source: declared
  description: The Ingester API from Kloudfuse — 5 operation(s) for ingester.
  name: Kloudfuse Ingester API
  slug: kloudfuse-ingester-api
- baseURL: https://{instance}
  baseurl_source: declared
  description: The Metrics API from Kloudfuse — 5 operation(s) for metrics.
  name: Kloudfuse Metrics API
  slug: kloudfuse-metrics-api
- baseURL: https://{instance}
  baseurl_source: declared
  description: The Policies API from Kloudfuse — 7 operation(s) for policies.
  name: Kloudfuse Policies API
  slug: kloudfuse-policies-api
- baseURL: https://{instance}
  baseurl_source: declared
  description: The Teams API from Kloudfuse — 6 operation(s) for teams.
  name: Kloudfuse Teams API
  slug: kloudfuse-teams-api
- baseURL: https://{instance}
  baseurl_source: declared
  description: The Traces API from Kloudfuse — 5 operation(s) for traces.
  name: Kloudfuse Traces API
  slug: kloudfuse-traces-api
- baseURL: https://{instance}
  baseurl_source: declared
  description: The Graph QL API from Kloudfuse — 1 operation(s) for graph ql.
  name: Kloudfuse Graph QL API
  slug: kloudfuse-graph-ql-api
artifact_total: 15
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kloudfuse/refs/heads/main/rules/kloudfuse-rules.yml
  title: ''
  type: Spectral
  url: rules/kloudfuse-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kloudfuse/refs/heads/main/json-ld/kloudfuse-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/kloudfuse-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kloudfuse/refs/heads/main/vocabulary/kloudfuse-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/kloudfuse-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kloudfuse/refs/heads/main/data-model/kloudfuse-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kloudfuse-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.kloudfuse.com/security
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kloudfuse/refs/heads/main/conformance/kloudfuse-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kloudfuse-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kloudfuse/refs/heads/main/llms/kloudfuse-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kloudfuse-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kloudfuse/refs/heads/main/hosts/kloudfuse-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kloudfuse-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kloudfuse/refs/heads/main/vendors/kloudfuse-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kloudfuse-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.kloudfuse.com/platform/latest/setup/install/prequisites/index
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kloudfuse/refs/heads/main/security/kloudfuse-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/kloudfuse-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kloudfuse/refs/heads/main/security/kloudfuse-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kloudfuse-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kloudfuse.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kloudfuse.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.kloudfuse.com/platform/latest/reference/api/metrics/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.kloudfuse.com/platform/latest/administration/authentication/ingestion-api-key/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kloudfuse/refs/heads/main/errors/kloudfuse-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/kloudfuse-problem-types.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kloudfuse/refs/heads/main/mcp/kloudfuse-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/kloudfuse-mcp.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.kloudfuse.com/platform/latest/release-notes/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.kloudfuse.com/platform/latest/whats-new/deprecations/
- group: company
  title: ''
  type: Blog
  url: https://www.kloudfuse.com/blog
- group: company
  title: ''
  type: Newsroom
  url: https://www.kloudfuse.com/news
- group: commercial
  title: ''
  type: Pricing
  url: https://www.kloudfuse.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kloudfuse.com/legal/privacy
- group: start
  title: ''
  type: Sandbox
  url: https://www.kloudfuse.com/playground
- group: auth
  title: ''
  type: Security
  url: https://www.kloudfuse.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.kloudfuse.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kloudfuse
- group: other
  title: ''
  type: Leadership
  url: https://www.kloudfuse.com/company
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.kloudfuse.com/llms.txt
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.kloudfuse.com
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: Kloudfuse is a unified observability platform that consolidates metrics, logs, traces, events, real user monitoring and continuous profiling into a single data lake deployed in the customer's own cloud (VPC). It exposes Prometheus-, Loki- and Tempo-compatible query APIs, a GraphQL query transport, RBAC policy and team REST APIs, an OTLP/Prometheus remote-write ingester, a hydration API for archived data, and an MCP server for AI assistants.
image: https://www.kloudfuse.com/assets/og-default.png
jsonld:
- class_count: 1
  name: Kloudfuse Context
  property_count: 4
  slug: kloudfuse-context
layout: provider
mcp_servers:
- description: Remote MCP server at {kloudfuse-instance} requiring OAuth.
  name: Kloudfuse MCP Server
  slug: kloudfuse-mcp-yml
modified: '2026-10-13'
name: Kloudfuse
nav: Providers
network: true
overview: 'Kloudfuse is listed with 10 APIs on the [APIs.io](https://apis.io/) network, including Cardinality Explorer API, Events API, Folders API, and 7 more. Tagged areas include Company, Observability, Monitoring, Logs, and Metrics.


  The Kloudfuse catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Kloudfuse''s developer surface includes getting-started guide, documentation, API reference, authentication, changelog, engineering blog, pricing, and 23 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Kloudfuse API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: kloudfuse-rules
score:
  band: thin
  composite: 37.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 50.8
    catalog_earned_first_party: 0.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 16.6
    developer_ergonomics: 50.0
    discoverability: 76.7
    operational_transparency: 39.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 11
      marker_coverage: 100.0
      total: 11
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Kloudfuse Domain Security
  slug: kloudfuse-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Kloudfuse Trust Center
  slug: kloudfuse-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: kloudfuse
tags:
- Company
- Observability
- Monitoring
- Logs
- Metrics
- Tracing
- OpenTelemetry
- MCP
website: https://www.kloudfuse.com
---
