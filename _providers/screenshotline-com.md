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
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.6
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Screenshot API that captures web pages as images or markdown.
  name: Screenshot API
  slug: screenshot-api
- description: 'screenshotline-com API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: screenshotline-com API
  slug: screenshotline-com-api
artifact_total: 11
common:
- group: other
  href: https://artifacts.apis.io/screenshotline-com/vendors/screenshotline-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/screenshotline-com-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/screenshotline-com/plans/screenshotline-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/screenshotline-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/screenshotline-com/rules/screenshotline-com-rules.yml
  title: ''
  type: Spectral
  url: rules/screenshotline-com-rules.yml
- group: design
  href: https://artifacts.apis.io/screenshotline-com/json-ld/screenshotline-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/screenshotline-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/screenshotline-com/vocabulary/screenshotline-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/screenshotline-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/screenshotline-com/data-model/screenshotline-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/screenshotline-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/screenshotline-com/changelog/screenshotline-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/screenshotline-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/screenshotline-com/authentication/screenshotline-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/screenshotline-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/screenshotline-com/errors/screenshotline-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/screenshotline-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/screenshotline-com/conformance/screenshotline-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/screenshotline-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/screenshotline-com/mcp/screenshotline-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/screenshotline-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/screenshotline-com/hosts/screenshotline-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/screenshotline-com-hosts.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.screenshotline.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://screenshotline.com/changelog
- group: auth
  href: https://artifacts.apis.io/screenshotline-com/security/screenshotline-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/screenshotline-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://screenshotline.com/
- group: docs
  title: ''
  type: Documentation
  url: https://screenshotline.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://screenshotline.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://screenshotline.com/docs
- group: company
  title: ''
  type: Blog
  url: https://screenshotline.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://screenshotline.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://screenshotline.com/terms
coverage:
  checked: '2026-10-31'
  detail: Public documentation exists but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec is published.
  evidence:
  - status: 404
    url: https://api.screenshotline.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Screenshotline — a screenshot API that survives production. URL in, image out. A screenshot API that handles consent walls, lazy images and late-rendering SPAs. Free tier, no card. Also returns pages as Markdown for LLMs.
image: data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%2032%2032%22%3E%3Crect%20width%3D%2232%22%20height%3D%2232%22%20rx%3D%227%22%20fill%3D%22%230c6b75%22%2F%3E%3Crect%20x%3D%227%22%20y%3D%229%22%20width%3D%2218%22%20height%3D%223%22%20rx%3D%221.5%22%20fill%3D%22%23fff%22%20opacity%3D%22.92%22%2F%3E%3Crect%20x%3D%227%22%20y%3D%2215.5%22%20width%3D%2218%22%20height%3D%228%22%20rx%3D%222%22%20fill%3D%22%23fff%22%20opacity%3D%22.62%22%2F%3E%3C%2Fsvg%3E'
json_schemas:
- name: GetExtractResponse
  property_count: 1
  slug: screenshotline-com-get-extract-response
- name: GetResponse
  property_count: 1
  slug: screenshotline-com-get-response
jsonld:
- class_count: 2
  name: Screenshotline Com Context
  property_count: 2
  slug: screenshotline-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.screenshotline.com requiring an API key.
  name: screenshotline-com MCP Server
  slug: screenshotline-com-mcp-yml
modified: '2026-10-31'
name: screenshotline-com
nav: Providers
network: true
overview: 'screenshotline-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Screenshot API, Web Capture, Image Generation, Developer Tools, and Free Tier.


  The screenshotline-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  screenshotline-com''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, engineering blog, pricing, and 15 more developer resources.'
plans:
- name: Screenshotline Com Plans Pricing
  plan_count: 4
  slug: screenshotline-com-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: screenshotline-com API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: screenshotline-com-rules
scopes:
- name: Screenshotline Com Scopes
  scope_count: 0
  slug: screenshotline-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 51.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 77.5
    catalog_earned_first_party: 0.0
    catalog_gap: 37.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 49.5
    contract_governance: 79.1
    contract_quality: 48.3
    developer_ergonomics: 42.9
    discoverability: 56.7
    operational_transparency: 31.6
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Screenshotline Com Authentication
  slug: screenshotline-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Screenshotline Com Domain Security
  slug: screenshotline-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: screenshotline-com
tags:
- Screenshot API
- Web Capture
- Image Generation
- Developer Tools
- Free Tier
website: https://screenshotline.com/
---
