---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 48.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://platform.chamelio.ai
  baseurl_source: declared
  description: 'Chamelio API as documented publicly: 14 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Chamelio API
  slug: chamelio-api
artifact_total: 14
asyncapis:
- description: ''
  name: Chamelio Webhooks
  slug: chamelio-webhooks
common:
- group: design
  href: https://artifacts.apis.io/chamelio/rules/chamelio-rules.yml
  title: ''
  type: Spectral
  url: rules/chamelio-rules.yml
- group: design
  href: https://artifacts.apis.io/chamelio/json-ld/chamelio-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/chamelio-context.jsonld
- group: design
  href: https://artifacts.apis.io/chamelio/vocabulary/chamelio-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/chamelio-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/chamelio/asyncapi/chamelio-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/chamelio-webhooks.yml
- group: design
  href: https://artifacts.apis.io/chamelio/data-model/chamelio-data-model.yml
  title: ''
  type: DataModel
  url: data-model/chamelio-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.chamelio.ai/security
- group: auth
  href: https://artifacts.apis.io/chamelio/authentication/chamelio-authentication.yml
  title: ''
  type: Authentication
  url: authentication/chamelio-authentication.yml
- group: design
  href: https://artifacts.apis.io/chamelio/conformance/chamelio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chamelio-conformance.yml
- group: agent
  href: https://artifacts.apis.io/chamelio/llms/chamelio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chamelio-llms.txt
- group: agent
  href: https://artifacts.apis.io/chamelio/mcp/chamelio-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/chamelio-mcp.yml
- group: agent
  href: https://artifacts.apis.io/chamelio/well-known/chamelio-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chamelio-well-known.yml
- group: other
  href: https://artifacts.apis.io/chamelio/hosts/chamelio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chamelio-hosts.yml
- group: other
  href: https://artifacts.apis.io/chamelio/vendors/chamelio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chamelio-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.chamelio.ai/security
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.chamelio.ai/guides/sso-setup
- group: auth
  href: https://artifacts.apis.io/chamelio/security/chamelio-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/chamelio-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/chamelio/security/chamelio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chamelio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chamelio.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.chamelio.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.chamelio.ai/api-reference/introduction
- group: company
  title: ''
  type: Blog
  url: https://www.chamelio.ai/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.chamelio.ai/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.chamelio.ai/
- group: design
  title: ''
  type: Webhooks
  url: https://www.chamelio.ai/integrations/webhooks
created: '2026-10-29'
description: Chamelio provides a legal intelligence platform that helps organizations manage contracts, track obligations, and automate compliance workflows. The service offers document classification, risk analysis, and integration with popular collaboration tools. Founded to simplify legal operations, Chamelio serves enterprises seeking to centralize legal data and improve decision‑making across contracts and regulatory requirements.
image: https://cdn.prod.website-files.com/69fa3fd4f38569f68c317bd1/6a01f73240f12d12d909dfda_og_share.jpg
json_schemas:
- name: GetServerClickwrapSlugResponse
  property_count: 7
  slug: chamelio-get-server-clickwrap-slug-response
- name: PostCoreDocumentsSearchRequest
  property_count: 2
  slug: chamelio-post-core-documents-search-request
- name: PostCoreUploadRequest
  property_count: 6
  slug: chamelio-post-core-upload-request
- name: PostTasksListResponse
  property_count: 2
  slug: chamelio-post-tasks-list-response
- name: PostV2AgentConversationsSessionidApprovalsRequest
  property_count: 2
  slug: chamelio-post-v2-agent-conversations-sessionid-approvals-request
- name: PostV2AgentConversationsSessionidMessagesResponse
  property_count: 3
  slug: chamelio-post-v2-agent-conversations-sessionid-messages-response
jsonld:
- class_count: 21
  name: Chamelio Context
  property_count: 43
  slug: chamelio-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.chamelio.ai.
  name: Chamelio MCP Server
  slug: chamelio-mcp-yml
modified: '2026-10-29'
name: Chamelio
nav: Providers
network: true
overview: 'Chamelio is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, LegalTech, SaaS, Contracts, and Compliance.


  The Chamelio catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Chamelio''s developer surface includes authentication, getting-started guide, documentation, API reference, engineering blog, and 19 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Chamelio API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 1
  slug: chamelio-rules
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 15.8
    contract_governance: 35.6
    contract_quality: 34.2
    developer_ergonomics: 42.9
    discoverability: 65.0
    operational_transparency: 34.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Chamelio Authentication
  slug: chamelio-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Chamelio Domain Security
  slug: chamelio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Chamelio Trust Center
  slug: chamelio-trust-center
  summary_line: SOC 2
slug: chamelio
tags:
- Company
- LegalTech
- SaaS
- Contracts
- Compliance
website: https://chamelio.ai/
---
