---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.1
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: API for automating LinkedIn, email, and WhatsApp communications as described on the documentation site.
  name: LinkupAPI API
  slug: linkupapi-api-2
- baseURL: https://api.linkupapi.com
  baseurl_source: declared
  description: 'LinkupAPI API as documented publicly: 55 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: LinkupAPI API
  slug: linkupapi-api
artifact_total: 15
asyncapis:
- description: ''
  name: Linkupapi Webhooks
  slug: linkupapi-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/linkupapi/plans/linkupapi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/linkupapi-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/linkupapi/rules/linkupapi-rules.yml
  title: ''
  type: Spectral
  url: rules/linkupapi-rules.yml
- group: design
  href: https://artifacts.apis.io/linkupapi/json-ld/linkupapi-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/linkupapi-context.jsonld
- group: design
  href: https://artifacts.apis.io/linkupapi/vocabulary/linkupapi-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/linkupapi-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/linkupapi/asyncapi/linkupapi-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/linkupapi-webhooks.yml
- group: design
  href: https://artifacts.apis.io/linkupapi/data-model/linkupapi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/linkupapi-data-model.yml
- group: auth
  href: https://artifacts.apis.io/linkupapi/authentication/linkupapi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/linkupapi-authentication.yml
- group: design
  href: https://artifacts.apis.io/linkupapi/errors/linkupapi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/linkupapi-problem-types.yml
- group: design
  href: https://artifacts.apis.io/linkupapi/conformance/linkupapi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/linkupapi-conformance.yml
- group: agent
  href: https://artifacts.apis.io/linkupapi/llms/linkupapi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/linkupapi-llms.txt
- group: other
  href: https://artifacts.apis.io/linkupapi/a2a/linkupapi-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/linkupapi-a2a.yml
- group: agent
  href: https://artifacts.apis.io/linkupapi/mcp/linkupapi-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/linkupapi-mcp.yml
- group: agent
  href: https://artifacts.apis.io/linkupapi/well-known/linkupapi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/linkupapi-well-known.yml
- group: other
  href: https://artifacts.apis.io/linkupapi/hosts/linkupapi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/linkupapi-hosts.yml
- group: other
  href: https://artifacts.apis.io/linkupapi/vendors/linkupapi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/linkupapi-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://linkupapi.com/legal/legal-notice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://linkupapi.com/legal/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://linkupapi.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.linkupapi.com/api-reference/v2/mcp-setup
- group: docs
  title: ''
  type: Documentation
  url: https://docs.linkupapi.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.linkupapi.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/linkupapi/security/linkupapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/linkupapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://linkupapi.com/
coverage:
  checked: '2026-10-18'
  detail: The only OpenAPI document found (https://docs.linkupapi.com/openapi.json) describes a LinkedIn API, not LinkupAPI, so no valid contract belongs to this provider.
  evidence:
  - status: 200
    url: https://docs.linkupapi.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-18'
description: LinkupAPI provides an outreach API enabling AI agents and software to automate LinkedIn, email, and WhatsApp communications. It offers endpoints for prospect search, profile retrieval, email verification, messaging, and engagement tracking, supporting use cases like lead generation, candidate sourcing, and CRM enrichment. The platform includes a Managed Cloud Platform (MCP) for seamless integration with Claude, Cursor, and other AI tools, delivering real-time data and interaction capabilities across B2B channels.
image: https://media.linkupapi.com/hero/LinkupAPI_Hero_v2_poster.jpg
json_schemas:
- name: PostV1MessagesSendMessageRequest
  property_count: 4
  slug: linkupapi-post-v1-messages-send-message-request
- name: PostV1NetworkAcceptInvitationRequest
  property_count: 3
  slug: linkupapi-post-v1-network-accept-invitation-request
- name: PostV1NetworkAcceptInvitationResponse
  property_count: 3
  slug: linkupapi-post-v1-network-accept-invitation-response
- name: PostV1ProfileSearchRequest
  property_count: 5
  slug: linkupapi-post-v1-profile-search-request
- name: PostV1WebhooksAccountsRequest
  property_count: 4
  slug: linkupapi-post-v1-webhooks-accounts-request
- name: PostV2CategoryRequest
  property_count: 3
  slug: linkupapi-post-v2-category-request
jsonld:
- class_count: 35
  name: Linkupapi Context
  property_count: 18
  slug: linkupapi-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.linkupapi.com.
  name: LinkupAPI MCP Server
  slug: linkupapi-mcp-yml
modified: '2026-10-18'
name: LinkupAPI
nav: Providers
network: true
overview: 'LinkupAPI is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Outreach, Artificial Intelligence, and Automation.


  The LinkupAPI catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  LinkupAPI''s developer surface includes authentication, pricing, getting-started guide, documentation, API reference, and 18 more developer resources.'
plans:
- name: Linkupapi Plans Pricing
  plan_count: 3
  slug: linkupapi-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: LinkupAPI API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: linkupapi-rules
score:
  band: thin
  composite: 38.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 64.0
    catalog_earned_first_party: 12.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.7
  facets:
    access_clarity: 63.2
    contract_governance: 19.7
    contract_quality: 32.6
    developer_ergonomics: 40.5
    discoverability: 48.3
    operational_transparency: 7.9
  previous_composite: 40.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 12
      marker_coverage: 100.0
      total: 12
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Linkupapi Authentication
  slug: linkupapi-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Linkupapi Domain Security
  slug: linkupapi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: linkupapi
tags:
- Company
- Outreach
- Artificial Intelligence
- Automation
website: https://linkupapi.com/
---
