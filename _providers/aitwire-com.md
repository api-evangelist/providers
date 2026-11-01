---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 7
  human_in_the_loop: 1
  name: Aitwire Com Agentic Access
  operation_count: 17
  slug: aitwire-com-agentic-access
  summary_line: 17 operations · 7 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.aitwire.com/v1
  baseurl_source: declared
  description: The API Keys API from aitwire-com — 2 operation(s) for api keys.
  name: aitwire-com API Keys API
  slug: aitwire-com-api-keys-api
- baseURL: https://api.aitwire.com/v1
  baseurl_source: declared
  description: The Attribution API from aitwire-com — 1 operation(s) for attribution.
  name: aitwire-com Attribution API
  slug: aitwire-com-attribution-api
- baseURL: https://api.aitwire.com/v1
  baseurl_source: declared
  description: The Authority API from aitwire-com — 1 operation(s) for authority.
  name: aitwire-com Authority API
  slug: aitwire-com-authority-api
- baseURL: https://api.aitwire.com/v1
  baseurl_source: declared
  description: The Billing API from aitwire-com — 1 operation(s) for billing.
  name: aitwire-com Billing API
  slug: aitwire-com-billing-api
- baseURL: https://api.aitwire.com/v1
  baseurl_source: declared
  description: The Drift API from aitwire-com — 1 operation(s) for drift.
  name: aitwire-com Drift API
  slug: aitwire-com-drift-api
- baseURL: https://api.aitwire.com/v1
  baseurl_source: declared
  description: The Entities API from aitwire-com — 2 operation(s) for entities.
  name: aitwire-com Entities API
  slug: aitwire-com-entities-api
- baseURL: https://api.aitwire.com/v1
  baseurl_source: declared
  description: The Scans API from aitwire-com — 2 operation(s) for scans.
  name: aitwire-com Scans API
  slug: aitwire-com-scans-api
- baseURL: https://api.aitwire.com/v1
  baseurl_source: declared
  description: The Webhooks API from aitwire-com — 3 operation(s) for webhooks.
  name: aitwire-com Webhooks API
  slug: aitwire-com-webhooks-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/aitwire-com/agentic-access/aitwire-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aitwire-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/aitwire-com/rules/aitwire-com-rules.yml
  title: ''
  type: Spectral
  url: rules/aitwire-com-rules.yml
- group: design
  href: https://artifacts.apis.io/aitwire-com/json-ld/aitwire-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aitwire-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/aitwire-com/vocabulary/aitwire-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aitwire-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/aitwire-com/data-model/aitwire-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aitwire-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/aitwire-com/errors/aitwire-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aitwire-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aitwire-com/conformance/aitwire-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aitwire-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aitwire-com/llms/aitwire-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aitwire-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/aitwire-com/mcp/aitwire-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aitwire-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/aitwire-com/well-known/aitwire-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aitwire-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aitwire-com/hosts/aitwire-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aitwire-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aitwire-com/vendors/aitwire-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aitwire-com-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.aitwire.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aitwire.com/
- group: auth
  title: ''
  type: Security
  url: https://aitwire.com/security
- group: start
  title: ''
  type: Login
  url: https://aitwire.com/auth/login
- group: auth
  href: https://artifacts.apis.io/aitwire-com/authentication/aitwire-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aitwire-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/aitwire-com/security/aitwire-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aitwire-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aitwire.com/
- group: docs
  title: ''
  type: Documentation
  url: https://aitwire.com/docs/developer-portal
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aitwire.com/docs/developer-portal
- group: company
  title: ''
  type: Blog
  url: https://aitwire.com/blog
- group: operate
  title: ''
  type: Changelog
  url: https://aitwire.com/changelog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aitwire.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aitwire.com/privacy
created: '2026-10-29'
description: aitwire-com is a technology company that provides IoT connectivity solutions for industrial devices, enabling remote monitoring, data collection, and device management across various sectors such as manufacturing, energy, and logistics. Their platform offers secure, scalable APIs for device provisioning, telemetry ingestion, and command execution, supporting multiple protocols and integration with cloud services. The company focuses on delivering reliable, low-latency communication and robust analytics to help businesses optimize operations and improve asset utilization.
image: https://aitwire.com/og-image.png
json_schemas:
- name: Entity
  property_count: 10
  slug: aitwire-com-entity
- name: ScanRun
  property_count: 6
  slug: aitwire-com-scan-run
- name: UsageStats
  property_count: 7
  slug: aitwire-com-usage-stats
jsonld:
- class_count: 6
  name: Aitwire Com Context
  property_count: 29
  slug: aitwire-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.aitwire.com.
  name: aitwire-com MCP Server
  slug: aitwire-com-mcp-yml
modified: '2026-10-29'
name: aitwire-com
nav: Providers
network: true
overview: 'aitwire-com publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including API Keys API, Attribution API, Authority API, and 5 more. Tagged areas include Company, IoT, Connectivity, API, and Industrial.


  The aitwire-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  aitwire-com''s developer surface includes support, authentication, documentation, engineering blog, changelog, and 20 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: aitwire-com API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: aitwire-com-rules
score:
  band: developing
  composite: 43.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 59.2
    developer_ergonomics: 38.1
    discoverability: 65.0
    operational_transparency: 26.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aitwire Com Authentication
  slug: aitwire-com-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Aitwire Com Domain Security
  slug: aitwire-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aitwire-com
tags:
- Company
- IoT
- Connectivity
- API
- Industrial
website: https://aitwire.com/
---
