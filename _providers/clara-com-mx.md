---
agent_readiness:
  band: agent-ready
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.5
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Clara provides financial management services for businesses in Mexico.
  name: Clara API
  slug: clara-api
- baseURL: https://public-api.mx.clara.com
  baseurl_source: declared
  description: 'Clara API as documented publicly: 28 operations. Contract generated from the documentation by API Evangelist (2026-10-24); not the provider''s own document.'
  name: Clara API
  slug: clara-com-mx-api
artifact_total: 15
common:
- group: commercial
  href: https://artifacts.apis.io/clara-com-mx/plans/clara-com-mx-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/clara-com-mx-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/clara-com-mx/rules/clara-com-mx-rules.yml
  title: ''
  type: Spectral
  url: rules/clara-com-mx-rules.yml
- group: design
  href: https://artifacts.apis.io/clara-com-mx/json-ld/clara-com-mx-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/clara-com-mx-context.jsonld
- group: design
  href: https://artifacts.apis.io/clara-com-mx/vocabulary/clara-com-mx-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/clara-com-mx-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/clara-com-mx/data-model/clara-com-mx-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clara-com-mx-data-model.yml
- group: start
  href: https://artifacts.apis.io/clara-com-mx/sandbox/clara-com-mx-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/clara-com-mx-sandbox.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.clara.com/es-mx
- group: auth
  href: https://artifacts.apis.io/clara-com-mx/authentication/clara-com-mx-authentication.yml
  title: ''
  type: Authentication
  url: authentication/clara-com-mx-authentication.yml
- group: design
  href: https://artifacts.apis.io/clara-com-mx/conformance/clara-com-mx-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clara-com-mx-conformance.yml
- group: agent
  href: https://artifacts.apis.io/clara-com-mx/llms/clara-com-mx-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clara-com-mx-llms.txt
- group: other
  href: https://artifacts.apis.io/clara-com-mx/a2a/clara-com-mx-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/clara-com-mx-a2a.yml
- group: agent
  href: https://artifacts.apis.io/clara-com-mx/mcp/clara-com-mx-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/clara-com-mx-mcp.yml
- group: agent
  href: https://artifacts.apis.io/clara-com-mx/well-known/clara-com-mx-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clara-com-mx-well-known.yml
- group: other
  href: https://artifacts.apis.io/clara-com-mx/hosts/clara-com-mx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clara-com-mx-hosts.yml
- group: other
  href: https://artifacts.apis.io/clara-com-mx/vendors/clara-com-mx-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clara-com-mx-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.clara.com/platform/security
- group: commercial
  title: ''
  type: Pricing
  url: https://www.clara.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.clara.com/resources/newsroom
- group: company
  title: ''
  type: Blog
  url: https://www.clara.com/blog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.clara.team/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developers.clara.team/introduction
- group: auth
  href: https://artifacts.apis.io/clara-com-mx/security/clara-com-mx-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/clara-com-mx-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/clara-com-mx/security/clara-com-mx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clara-com-mx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.clara.com.mx/
created: '2026-10-24'
description: 'Clara is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by general-catalyst) and added to the network as a stub for full-pipeline profiling.'
image: https://cdn.prod.website-files.com/68ffa900bd486e7d9f3183da/6a29c37512926811b4015b7c_Share_ESP%20Clara%20com-1%201200.webp
json_schemas:
- name: PostApiTestV3WebhooksEventsRequest
  property_count: 4
  slug: clara-com-mx-post-api-test-v3-webhooks-events-request
- name: PostApiTestV3WebhooksEventsResponse
  property_count: 5
  slug: clara-com-mx-post-api-test-v3-webhooks-events-response
- name: PostApiTestV3WebhooksSubscriptionsRequest
  property_count: 3
  slug: clara-com-mx-post-api-test-v3-webhooks-subscriptions-request
- name: PostApiV1VcnCardRequest
  property_count: 6
  slug: clara-com-mx-post-api-v1-vcn-card-request
- name: PostApiV2CardsUuidConfigurationsRequest
  property_count: 4
  slug: clara-com-mx-post-api-v2-cards-uuid-configurations-request
- name: PostApiV3CardsRequest
  property_count: 6
  slug: clara-com-mx-post-api-v3-cards-request
jsonld:
- class_count: 27
  name: Clara Com Mx Context
  property_count: 61
  slug: clara-com-mx-context
layout: provider
mcp_servers:
- description: Remote MCP server at developers.clara.team.
  name: Clara MCP Server
  slug: clara-com-mx-mcp-yml
modified: '2026-10-24'
name: Clara
nav: Providers
network: true
overview: 'Clara is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Corporate Cards, Expense Management, Accounts Payable, Travel Pay, and AI Finance.


  The Clara catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Clara''s developer surface includes sandbox, authentication, pricing, engineering blog, API reference, and 19 more developer resources.'
plans:
- name: Clara Com Mx Plans Pricing
  plan_count: 2
  slug: clara-com-mx-plans-pricing
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Clara API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: clara-com-mx-rules
score:
  band: thin
  composite: 35.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 60.8
    catalog_earned_first_party: 8.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 35.6
    contract_quality: 26.0
    developer_ergonomics: 38.1
    discoverability: 50.0
    operational_transparency: 10.5
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
    score: 26.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Clara Com Mx Authentication
  slug: clara-com-mx-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Clara Com Mx Domain Security
  slug: clara-com-mx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Clara Com Mx Trust Center
  slug: clara-com-mx-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: clara-com-mx
tags:
- Corporate Cards
- Expense Management
- Accounts Payable
- Travel Pay
- AI Finance
- Latin America
- ERP Integration
website: https://www.clara.com.mx/
---
