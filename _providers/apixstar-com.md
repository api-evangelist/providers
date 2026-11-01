---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.6
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Reddit API documentation providing endpoints for communities, users, posts, comments, and search.
  name: Reddit API
  slug: reddit-api
- description: 'apixstar-com API as documented publicly: 14 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: apixstar-com API
  slug: apixstar-com-api
artifact_total: 11
common:
- group: operate
  href: https://artifacts.apis.io/apixstar-com/rate-limits/apixstar-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/apixstar-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/apixstar-com/plans/apixstar-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apixstar-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/apixstar-com/rules/apixstar-com-rules.yml
  title: ''
  type: Spectral
  url: rules/apixstar-com-rules.yml
- group: design
  href: https://artifacts.apis.io/apixstar-com/json-ld/apixstar-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/apixstar-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/apixstar-com/vocabulary/apixstar-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/apixstar-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/apixstar-com/data-model/apixstar-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/apixstar-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/apixstar-com/conventions/apixstar-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/apixstar-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/apixstar-com/authentication/apixstar-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apixstar-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/apixstar-com/conformance/apixstar-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apixstar-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/apixstar-com/llms/apixstar-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apixstar-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/apixstar-com/mcp/apixstar-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/apixstar-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/apixstar-com/well-known/apixstar-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apixstar-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/apixstar-com/hosts/apixstar-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apixstar-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/apixstar-com/vendors/apixstar-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apixstar-com-vendors.yml
- group: start
  title: ''
  type: Sandbox
  url: https://console.apixstar.com/playground
- group: operate
  title: ''
  type: ChangeLog
  url: https://dev.apixstar.com/changelog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.apixstar.com</code
- group: auth
  href: https://artifacts.apis.io/apixstar-com/security/apixstar-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apixstar-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apixstar.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apixstar.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://apixstar.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apixstar.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apixstar.com/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://apixstar.com/docs
coverage:
  checked: '2026-10-30'
  detail: Human‑readable API reference is available but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable spec is published.
  evidence:
  - status: 200
    url: https://apixstar.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Apixstar provides a read‑only Reddit data API that delivers public Reddit posts, comments, user profiles, and search results as JSON. Built by the team behind Bavior, the service offers a reliable pipeline for developers needing Reddit data without scraping, with free credit and pay‑per‑request pricing. The platform emphasizes uptime, compliance with Reddit’s terms, and offers clear documentation, pricing, and privacy policies.
image: https://apixstar.com/brand/icon-512.png
json_schemas:
- name: GetRedditV1RCommunityResponse
  property_count: 2
  slug: apixstar-com-get-reddit-v1-rcommunity-response
jsonld:
- class_count: 1
  name: Apixstar Com Context
  property_count: 2
  slug: apixstar-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at apixstar.com.
  name: apixstar-com MCP Server
  slug: apixstar-com-mcp-yml
modified: '2026-10-30'
name: apixstar-com
nav: Providers
network: true
overview: 'apixstar-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Reddit, Data, API, and Developer.


  The apixstar-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  apixstar-com''s developer surface includes authentication, sandbox, changelog, documentation, pricing, getting-started guide, and 18 more developer resources.'
plans:
- name: Apixstar Com Plans Pricing
  plan_count: 4
  slug: apixstar-com-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Apixstar Com Rate Limits
  slug: apixstar-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: apixstar-com API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: apixstar-com-rules
scopes:
- name: Apixstar Com Scopes
  scope_count: 0
  slug: apixstar-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 54.8
  coverage:
    artifact_dirs: 24
    catalog_earned: 78.4
    catalog_earned_first_party: 0.0
    catalog_gap: 36.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.0
    contract_governance: 70.9
    contract_quality: 45.0
    developer_ergonomics: 50.0
    discoverability: 56.7
    operational_transparency: 34.7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Apixstar Com Authentication
  slug: apixstar-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Apixstar Com Domain Security
  slug: apixstar-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: apixstar-com
tags:
- Company
- Reddit
- Data
- API
- Developer
- Analytics
website: https://apixstar.com/
---
