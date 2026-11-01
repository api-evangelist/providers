---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Filingfirehose Com Agentic Access
  operation_count: 8
  slug: filingfirehose-com-agentic-access
  summary_line: 8 operations · 1 acting
api_count: 1
apis:
- description: The billing API from filingfirehose-com — 1 operation(s) for billing.
  name: filingfirehose-com Billing API
  slug: filingfirehose-com-billing-api
- description: The filings API from filingfirehose-com — 3 operation(s) for filings.
  name: filingfirehose-com Filings API
  slug: filingfirehose-com-filings-api
- description: The meta API from filingfirehose-com — 1 operation(s) for meta.
  name: filingfirehose-com Meta API
  slug: filingfirehose-com-meta-api
- description: The public API from filingfirehose-com — 3 operation(s) for public.
  name: filingfirehose-com Public API
  slug: filingfirehose-com-public-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/filingfirehose-com/agentic-access/filingfirehose-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/filingfirehose-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/filingfirehose-com/plans/filingfirehose-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/filingfirehose-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/filingfirehose-com/rules/filingfirehose-com-rules.yml
  title: ''
  type: Spectral
  url: rules/filingfirehose-com-rules.yml
- group: design
  href: https://artifacts.apis.io/filingfirehose-com/json-ld/filingfirehose-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/filingfirehose-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/filingfirehose-com/vocabulary/filingfirehose-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/filingfirehose-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/filingfirehose-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/filingfirehose-com/data-model/filingfirehose-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/filingfirehose-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/filingfirehose-com/errors/filingfirehose-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/filingfirehose-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/filingfirehose-com/conformance/filingfirehose-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/filingfirehose-com-conformance.yml
- group: build
  href: https://artifacts.apis.io/filingfirehose-com/mcp/filingfirehose-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/filingfirehose-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/filingfirehose-com/mcp/filingfirehose-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/filingfirehose-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/filingfirehose-com/hosts/filingfirehose-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/filingfirehose-com-hosts.yml
- group: other
  title: ''
  type: Leadership
  url: https://filingfirehose.com/whales/holdings/TEAM
- group: company
  title: ''
  type: Blog
  url: https://filingfirehose.com/blog
- group: auth
  href: https://artifacts.apis.io/filingfirehose-com/security/filingfirehose-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/filingfirehose-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://filingfirehose.com/
- group: docs
  title: ''
  type: Documentation
  url: https://filingfirehose.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://filingfirehose.com/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://filingfirehose.com/#pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://filingfirehose.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://filingfirehose.com/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:info@filingfirehose.com
- group: start
  title: ''
  type: SignUp
  url: https://filingfirehose.com/trial
created: '2026-10-30'
description: FilingFirehose provides a JSON API that delivers structured, normalized SEC EDGAR filings, including detailed 8‑K body‑text parsing, activist 13D tagging, and ATM offering detection. The service offers a free tier and paid plans starting at $29 per month, targeting retail traders, small funds, and fintech analysts. It also supplies CSV exports, webhooks for new filings, and email support, with higher‑tier plans offering full historical archives and priority SLA.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/default.png
json_schemas:
- name: FilingsResponse
  property_count: 2
  slug: filingfirehose-com-filings-response
jsonld:
- class_count: 6
  name: Filingfirehose Com Context
  property_count: 28
  slug: filingfirehose-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at filingfirehose.com.
  name: filingfirehose-com MCP Server
  slug: filingfirehose-com-mcp-yml
modified: '2026-10-30'
name: filingfirehose-com
nav: Providers
network: true
overview: 'filingfirehose-com publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Billing API, Filings API, Meta API, and 1 more. Tagged areas include SEC, EDGAR, Finance, Data-API, and JSON.


  The filingfirehose-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  filingfirehose-com''s developer surface includes engineering blog, documentation, API reference, pricing, support, signup flow, and 17 more developer resources.'
plans:
- name: Filingfirehose Com Plans Pricing
  plan_count: 3
  slug: filingfirehose-com-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Filingfirehose Com Rate Limits
  slug: filingfirehose-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: filingfirehose-com API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: filingfirehose-com-rules
score:
  band: developing
  composite: 48.6
  coverage:
    artifact_dirs: 23
    catalog_earned: 79.9
    catalog_earned_first_party: 0.0
    catalog_gap: 35.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 49.0
    developer_ergonomics: 30.2
    discoverability: 58.3
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 23.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Filingfirehose Com Authentication
  slug: filingfirehose-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Filingfirehose Com Domain Security
  slug: filingfirehose-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: search-13d-filings
  slug: filingfirehose-com-search-13d
- name: search-8k-filings
  slug: filingfirehose-com-search-8k
slug: filingfirehose-com
tags:
- SEC
- EDGAR
- Finance
- Data-API
- JSON
website: https://filingfirehose.com/
---
