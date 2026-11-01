---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://public-api.mx.clara.com
  baseurl_source: declared
  description: 'Clara API as documented publicly: 28 operations. Contract generated from the documentation by API Evangelist (2026-10-22); not the provider''s own document.'
  name: Clara API
  slug: clara-cc-api
artifact_total: 14
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clara.com/global/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clara.com/global/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://www.clara.com/global/guides
- group: commercial
  href: https://artifacts.apis.io/clara-cc/plans/clara-cc-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/clara-cc-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/clara-cc/rules/clara-cc-rules.yml
  title: ''
  type: Spectral
  url: rules/clara-cc-rules.yml
- group: design
  href: https://artifacts.apis.io/clara-cc/json-ld/clara-cc-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/clara-cc-context.jsonld
- group: design
  href: https://artifacts.apis.io/clara-cc/vocabulary/clara-cc-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/clara-cc-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/clara-cc/data-model/clara-cc-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clara-cc-data-model.yml
- group: start
  href: https://artifacts.apis.io/clara-cc/sandbox/clara-cc-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/clara-cc-sandbox.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.clara.com/
- group: auth
  href: https://artifacts.apis.io/clara-cc/authentication/clara-cc-authentication.yml
  title: ''
  type: Authentication
  url: authentication/clara-cc-authentication.yml
- group: design
  href: https://artifacts.apis.io/clara-cc/conformance/clara-cc-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clara-cc-conformance.yml
- group: agent
  href: https://artifacts.apis.io/clara-cc/llms/clara-cc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clara-cc-llms.txt
- group: other
  href: https://artifacts.apis.io/clara-cc/a2a/clara-cc-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/clara-cc-a2a.yml
- group: agent
  href: https://artifacts.apis.io/clara-cc/mcp/clara-cc-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/clara-cc-mcp.yml
- group: agent
  href: https://artifacts.apis.io/clara-cc/well-known/clara-cc-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clara-cc-well-known.yml
- group: other
  href: https://artifacts.apis.io/clara-cc/hosts/clara-cc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clara-cc-hosts.yml
- group: other
  href: https://artifacts.apis.io/clara-cc/vendors/clara-cc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clara-cc-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.clara.com/
- group: auth
  title: ''
  type: Security
  url: https://www.clara.com/platform/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.clara.com/resources/newsroom
- group: auth
  href: https://artifacts.apis.io/clara-cc/security/clara-cc-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/clara-cc-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/clara-cc/security/clara-cc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clara-cc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.clara.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.clara.team
- group: docs
  title: ''
  type: APIReference
  url: https://developers.clara.team/introduction
- group: operate
  title: ''
  type: Support
  url: https://ayuda.clara.com.mx/hc/
- group: company
  title: ''
  type: Blog
  url: https://www.clara.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.clara.com/pricing
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://developers.clara.team/openapi.json
  - status: null
    url: https://developers.clara.team/mcp
  - status: 401
    url: https://api.clara.team/mcp
  - status: 200
    url: https://www.clara.com
  reason: partner-login
  state: gated
created: '2026-10-22'
description: Clara is a Latin American spend management fintech offering corporate cards, vendor payments, travel pay, and AI‑driven expense automation. Backed by Coatue, it serves Brazil, Colombia, Mexico and other markets, helping finance teams reduce manual work, increase tax savings, and gain real‑time spend insights.
image: https://cdn.prod.website-files.com/68ffa900bd486e7d9f3183da/6a29c454934463f06d822c93_Share_Clara%20Global%201200.png
json_schemas:
- name: GetApiV3AccountsPayableResponse
  property_count: 5
  slug: clara-cc-get-api-v3-accounts-payable-response
- name: PostApiTestV3WebhooksEventsRequest
  property_count: 4
  slug: clara-cc-post-api-test-v3-webhooks-events-request
- name: PostApiTestV3WebhooksEventsResponse
  property_count: 5
  slug: clara-cc-post-api-test-v3-webhooks-events-response
- name: PostApiV1VcnCardRequest
  property_count: 6
  slug: clara-cc-post-api-v1-vcn-card-request
- name: PostApiV2CardsUuidConfigurationsRequest
  property_count: 4
  slug: clara-cc-post-api-v2-cards-uuid-configurations-request
- name: PostApiV3CardsRequest
  property_count: 6
  slug: clara-cc-post-api-v3-cards-request
jsonld:
- class_count: 35
  name: Clara Cc Context
  property_count: 64
  slug: clara-cc-context
layout: provider
mcp_servers:
- description: Remote MCP server at developers.clara.team.
  name: Clara MCP Server
  slug: clara-cc-mcp-yml
modified: '2026-10-22'
name: Clara
nav: Providers
network: true
overview: 'Clara is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Spend Management, Corporate Cards, Latin America, and AI.


  The Clara catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Clara''s developer surface includes documentation, sandbox, authentication, API reference, support, engineering blog, pricing, and 22 more developer resources.'
plans:
- name: Clara Cc Plans Pricing
  plan_count: 2
  slug: clara-cc-plans-pricing
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Clara API Rules
  rule_count: 14
  severity_counts:
    error: 10
    hint: 0
    info: 3
    warn: 1
  slug: clara-cc-rules
score:
  band: developing
  composite: 46.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 68.4
    contract_governance: 35.6
    contract_quality: 26.3
    developer_ergonomics: 52.4
    discoverability: 66.7
    operational_transparency: 26.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 13
      marker_coverage: 100.0
      total: 13
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Clara Cc Authentication
  slug: clara-cc-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Clara Cc Domain Security
  slug: clara-cc-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Clara Cc Trust Center
  slug: clara-cc-trust-center
  summary_line: ISO 27001, PCI DSS
slug: clara-cc
tags:
- Fintech
- Spend Management
- Corporate Cards
- Latin America
- AI
website: https://www.clara.com
---
