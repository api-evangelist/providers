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
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.0
  scored_at: '2026-10-17'
api_count: 3
apis:
- description: API for SymphonyOS platform, documented at https://symphonyos.co/docs
  name: SymphonyOS API
  slug: symphonyos-api-2
- baseURL: https://api.symphonyos.co
  baseurl_source: declared
  description: The Campaigns API from SymphonyOS — 2 operation(s) for campaigns.
  name: SymphonyOS Campaigns API
  slug: symphonyos-campaigns-api
- baseURL: https://api.symphonyos.co
  baseurl_source: declared
  description: The Sym API from SymphonyOS — 3 operation(s) for sym.
  name: SymphonyOS Sym API
  slug: symphonyos-sym-api
artifact_total: 17
asyncapis:
- description: ''
  name: Symphonyos Webhooks
  slug: symphonyos-webhooks
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/symphonyos/refs/heads/main/rate-limits/symphonyos-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/symphonyos-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/symphonyos/refs/heads/main/plans/symphonyos-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/symphonyos-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/symphonyos/refs/heads/main/rules/symphonyos-rules.yml
  title: ''
  type: Spectral
  url: rules/symphonyos-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/symphonyos/refs/heads/main/json-ld/symphonyos-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/symphonyos-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/symphonyos/refs/heads/main/vocabulary/symphonyos-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/symphonyos-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/symphonyos/refs/heads/main/asyncapi/symphonyos-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/symphonyos-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/symphonyos/refs/heads/main/data-model/symphonyos-data-model.yml
  title: ''
  type: DataModel
  url: data-model/symphonyos-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/symphonyos/refs/heads/main/authentication/symphonyos-authentication.yml
  title: ''
  type: Authentication
  url: authentication/symphonyos-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/symphonyos/refs/heads/main/lifecycle/symphonyos-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/symphonyos-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/symphonyos/refs/heads/main/conformance/symphonyos-conformance.yml
  title: ''
  type: Conformance
  url: conformance/symphonyos-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/symphonyos/refs/heads/main/llms/symphonyos-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/symphonyos-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/symphonyos/refs/heads/main/mcp/symphonyos-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/symphonyos-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/symphonyos/refs/heads/main/well-known/symphonyos-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/symphonyos-support-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/symphonyos/refs/heads/main/well-known/symphonyos-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/symphonyos-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/symphonyos/refs/heads/main/hosts/symphonyos-hosts.yml
  title: ''
  type: Hosts
  url: hosts/symphonyos-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/symphonyos/refs/heads/main/vendors/symphonyos-vendors.yml
  title: ''
  type: Vendors
  url: vendors/symphonyos-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://symphonyos.co/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.symphonyos.co/docs/getting-started
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/symphonyos/refs/heads/main/security/symphonyos-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/symphonyos-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://symphonyos.co/
- group: docs
  title: ''
  type: Documentation
  url: https://symphonyos.co/docs
- group: docs
  title: ''
  type: APIReference
  url: https://symphonyos.co/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://symphonyos.co/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://symphonyos.co/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://symphonyos.co/privacy-policy
coverage:
  checked: '2026-10-12'
  detail: Documentation pages are HTML only and no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://symphonyos.co/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: SymphonyOS is an AI‑powered music‑industry platform that provides a suite of autonomous agents to manage every aspect of music release and promotion. Founded in 2016, it combines data‑driven marketing, royalty accounting, fan engagement, and creative campaign tools into a single service, enabling artists and labels to focus on creation while the platform handles distribution, advertising, and business operations. With a growing roster of specialized agents, SymphonyOS aims to streamline the complex workflow of modern music production and monetization.
image: https://symphonyos.co/og.png
json_schemas:
- name: DeleteApiSymV2Webhooks3Response
  property_count: 2
  slug: symphonyos-delete-api-sym-v2-webhooks3-response
- name: GetApiSymV2V2IdResponse
  property_count: 2
  slug: symphonyos-get-api-sym-v2-v2-id-response
- name: GetCampaignsCampaignidResponse
  property_count: 2
  slug: symphonyos-get-campaigns-campaignid-response
- name: PostApiSymV2WebhooksRequest
  property_count: 2
  slug: symphonyos-post-api-sym-v2-webhooks-request
- name: PostApiSymV2WebhooksResponse
  property_count: 2
  slug: symphonyos-post-api-sym-v2-webhooks-response
- name: PutApiSymV2Webhooks3Response
  property_count: 2
  slug: symphonyos-put-api-sym-v2-webhooks3-response
jsonld:
- class_count: 7
  name: Symphonyos Context
  property_count: 5
  slug: symphonyos-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.symphonyos.co.
  name: SymphonyOS MCP Server
  slug: symphonyos-mcp-yml
modified: '2026-10-12'
name: SymphonyOS
nav: Providers
network: true
overview: 'SymphonyOS is listed with 3 APIs on the [APIs.io](https://apis.io/) network, including Campaigns API, Sym API, and 1 more. Tagged areas include Company, Artificial Intelligence, Music, Platform, and Agents.


  The SymphonyOS catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  SymphonyOS''s developer surface includes authentication, changelog, getting-started guide, documentation, API reference, pricing, and 19 more developer resources.'
plans:
- name: Symphonyos Plans Pricing
  plan_count: 3
  slug: symphonyos-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Symphonyos Rate Limits
  slug: symphonyos-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: SymphonyOS API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: symphonyos-rules
score:
  band: developing
  composite: 44.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 77.8
    catalog_earned_first_party: 20.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 31.8
    developer_ergonomics: 40.5
    discoverability: 71.7
    operational_transparency: 44.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Symphonyos Authentication
  slug: symphonyos-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Symphonyos Domain Security
  slug: symphonyos-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: symphonyos
tags:
- Company
- Artificial Intelligence
- Music
- Platform
- Agents
website: https://symphonyos.co/
---
