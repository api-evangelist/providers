---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Withreach Agentic Access
  operation_count: 28
  slug: withreach-agentic-access
  summary_line: 28 operations · 15 acting
api_count: 4
apis:
- baseURL: https://api.withreach.com
  baseurl_source: declared
  description: The Transaction Details API lets partners submit comprehensive transaction data, including line-item tax breakdowns, to Reach.
  name: Transaction Details API
  slug: transaction-details-api
- baseURL: https://checkout.rch.how/v2.22
  baseurl_source: declared
  description: The GET API from Reach — 7 operation(s) for get.
  name: Reach GET API
  slug: withreach-get-api
- baseURL: https://api.withreach.com
  baseurl_source: declared
  description: Manage a Order within Reach.
  name: Reach Order API
  slug: withreach-order-api
- baseURL: https://checkout.rch.how/v2.22
  baseurl_source: declared
  description: The POST API from Reach — 8 operation(s) for post.
  name: Reach POST API
  slug: withreach-post-api
- baseURL: https://api.withreach.com
  baseurl_source: declared
  description: The Quote API from Reach — 1 operation(s) for quote.
  name: Reach Quote API
  slug: withreach-quote-api
- baseURL: https://api.withreach.com
  baseurl_source: declared
  description: Manage a Session within Reach.
  name: Reach Session API
  slug: withreach-session-api
artifact_total: 23
asyncapis:
- description: ''
  name: Withreach Webhooks
  slug: withreach-webhooks
common:
- group: other
  href: https://artifacts.apis.io/withreach/capabilities/withreach-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/withreach-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/withreach/agentic-access/withreach-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/withreach-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/withreach/rules/withreach-rules.yml
  title: ''
  type: Spectral
  url: rules/withreach-rules.yml
- group: design
  href: https://artifacts.apis.io/withreach/json-ld/withreach-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/withreach-context.jsonld
- group: design
  href: https://artifacts.apis.io/withreach/vocabulary/withreach-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/withreach-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/withreach/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/withreach/data-model/withreach-data-model.yml
  title: ''
  type: DataModel
  url: data-model/withreach-data-model.yml
- group: operate
  href: https://artifacts.apis.io/withreach/changelog/withreach-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/withreach-changelog.yml
- group: auth
  href: https://artifacts.apis.io/withreach/authentication/withreach-authentication.yml
  title: ''
  type: Authentication
  url: authentication/withreach-authentication.yml
- group: design
  href: https://artifacts.apis.io/withreach/errors/withreach-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/withreach-problem-types.yml
- group: design
  href: https://artifacts.apis.io/withreach/conformance/withreach-conformance.yml
  title: ''
  type: Conformance
  url: conformance/withreach-conformance.yml
- group: other
  href: https://artifacts.apis.io/withreach/overlays/withreach-reach-checkout-api-overlay.yml
  title: ''
  type: Overlay
  url: overlays/withreach-reach-checkout-api-overlay.yml
- group: agent
  href: https://artifacts.apis.io/withreach/llms/withreach-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/withreach-llms.txt
- group: agent
  href: https://artifacts.apis.io/withreach/mcp/withreach-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/withreach-mcp.yml
- group: auth
  href: https://artifacts.apis.io/withreach/well-known/withreach-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/withreach-status-security.txt
- group: agent
  href: https://artifacts.apis.io/withreach/well-known/withreach-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/withreach-well-known.yml
- group: other
  href: https://artifacts.apis.io/withreach/hosts/withreach-hosts.yml
  title: ''
  type: Hosts
  url: hosts/withreach-hosts.yml
- group: other
  href: https://artifacts.apis.io/withreach/vendors/withreach-vendors.yml
  title: ''
  type: Vendors
  url: vendors/withreach-vendors.yml
- group: build
  href: https://artifacts.apis.io/withreach/packages/withreach-packages.yml
  title: ''
  type: SDKs
  url: packages/withreach-packages.yml
- group: build
  href: https://artifacts.apis.io/withreach/packages/withreach-packages.yml
  title: ''
  type: Packages
  url: packages/withreach-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.withreach.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.withreach.com/privacy-center
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.withreach.com/docs/shopify-getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/withreach
- group: auth
  href: https://artifacts.apis.io/withreach/security/withreach-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/withreach-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.withreach.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.withreach.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.withreach.com/reference
- group: operate
  title: ''
  type: Support
  url: https://www.withreach.com/request-a-call
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.withreach.com/
created: '2026-10-28'
description: Reach is the premier partner for ambitious, forward‑thinking online brands that want to connect with consumers around the world. Using its unique, local service provider model, Reach helps retailers process global payment transactions wherever a merchant’s customer is based. The company brings consistency to cross‑border currency conversions with its Guaranteed FX solution, has relationships with banks worldwide to enable local credit‑card processing, offers consumers alternative payment methods where they are accustomed to using them, and provides best‑in‑class fraud detection and prevention services.
image: https://zncv0trv7vajq2xt.public.blob.vercel-storage.com/Reach-OG-Image-1200x630.png
json_schemas:
- name: CaptureResultResource
  property_count: 1
  slug: withreach-capture-result-resource
- name: Order
  property_count: 28
  slug: withreach-order
- name: Quote
  property_count: 9
  slug: withreach-quote
- name: Refund
  property_count: 5
  slug: withreach-refund
- name: Session
  property_count: 24
  slug: withreach-session
- name: Tax linking
  property_count: 13
  slug: withreach-transaction-details-mode-a
- name: Tax only
  property_count: 10
  slug: withreach-transaction-details-mode-b
jsonld:
- class_count: 22
  name: Withreach Context
  property_count: 83
  slug: withreach-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.withreach.com.
  name: Reach MCP Server
  slug: withreach-mcp-yml
modified: '2026-10-28'
name: Reach
nav: Providers
network: true
overview: 'Reach publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Transaction Details API, GET API, Order API, and 3 more. Tagged areas include Company, Payments, Tax, Compliance, and E-commerce.


  The Reach catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Reach''s developer surface includes changelog, authentication, getting-started guide, documentation, API reference, support, and 24 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Reach API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 2
  slug: withreach-rules
score:
  band: developing
  composite: 48.2
  coverage:
    artifact_dirs: 25
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 70.8
    developer_ergonomics: 63.7
    discoverability: 70.0
    operational_transparency: 47.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Withreach Authentication
  slug: withreach-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Withreach Domain Security
  slug: withreach-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: withreach-create-manage-session
  slug: withreach-create-manage-session
- name: reach-checkout-api
  slug: withreach-reach-checkout-api
- name: reach-drop-in-api
  slug: withreach-reach-s-drop-in-api
slug: withreach
tags:
- Company
- Payments
- Tax
- Compliance
- E-commerce
- Merchant of Record
website: https://www.withreach.com/
---
