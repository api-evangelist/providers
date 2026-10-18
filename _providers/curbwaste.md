---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
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
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.3
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Partner API for CurbWaste providing endpoints for catalog and pricing lists.
  name: CurbWaste Partner API
  slug: curbwaste-partner-api
- baseURL: https://api.curbwaste.com
  baseurl_source: spec
  description: The Catalog API from Curbwaste — 5 operation(s) for catalog.
  name: Curbwaste Catalog API
  slug: curbwaste-catalog-api
- baseURL: https://api.curbwaste.com
  baseurl_source: spec
  description: Company CRM customers under /v1/customers. Requires customers:read or customers:write.
  name: Curbwaste Customers API
  slug: curbwaste-customers-api
- baseURL: https://api.curbwaste.com
  baseurl_source: spec
  description: The Locations API from Curbwaste — 3 operation(s) for locations.
  name: Curbwaste Locations API
  slug: curbwaste-locations-api
- baseURL: https://api.curbwaste.com
  baseurl_source: spec
  description: The Zones API from Curbwaste — 2 operation(s) for zones.
  name: Curbwaste Zones API
  slug: curbwaste-zones-api
artifact_total: 11
asyncapis:
- description: ''
  name: Curbwaste Webhooks
  slug: curbwaste-webhooks
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/curbwaste/refs/heads/main/rules/curbwaste-rules.yml
  title: ''
  type: Spectral
  url: rules/curbwaste-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/curbwaste/refs/heads/main/json-ld/curbwaste-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/curbwaste-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/curbwaste/refs/heads/main/vocabulary/curbwaste-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/curbwaste-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/curbwaste/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/curbwaste/refs/heads/main/asyncapi/curbwaste-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/curbwaste-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/curbwaste/refs/heads/main/data-model/curbwaste-data-model.yml
  title: ''
  type: DataModel
  url: data-model/curbwaste-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/curbwaste/refs/heads/main/authentication/curbwaste-authentication.yml
  title: ''
  type: Authentication
  url: authentication/curbwaste-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/curbwaste/refs/heads/main/conformance/curbwaste-conformance.yml
  title: ''
  type: Conformance
  url: conformance/curbwaste-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/curbwaste/refs/heads/main/llms/curbwaste-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/curbwaste-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/curbwaste/refs/heads/main/a2a/curbwaste-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/curbwaste-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/curbwaste/refs/heads/main/mcp/curbwaste-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/curbwaste-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/curbwaste/refs/heads/main/well-known/curbwaste-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/curbwaste-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/curbwaste/refs/heads/main/hosts/curbwaste-hosts.yml
  title: ''
  type: Hosts
  url: hosts/curbwaste-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/curbwaste/refs/heads/main/vendors/curbwaste-vendors.yml
  title: ''
  type: Vendors
  url: vendors/curbwaste-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.curbwaste.com/terms-conditions
- group: operate
  title: ''
  type: Support
  url: https://www.curbwaste.com/help-center
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.curbwaste.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.curbwaste.com/blog/wasteexpo-2025
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.curbwaste.com/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://dev.curbwaste.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.curbwaste.com/api-reference/catalog/list-pricelists
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/curbwaste/refs/heads/main/security/curbwaste-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/curbwaste-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.curbwaste.com
- group: other
  title: ''
  type: Image
  url: https://cdn.prod.website-files.com/64a711ad4800f51470aab34c/64ce40c89e1879e4a84b725d_OpenGraph.png
coverage:
  checked: '2026-10-12'
  detail: Docs pages are rendered via JavaScript and no machine‑readable OpenAPI spec is available.
  evidence:
  - status: 200
    url: https://docs.curbwaste.com/api-reference/catalog/list-pricelists
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-12'
description: Curbwaste provides cloud‑based waste management software for haulers, offering order management, real‑time dispatch, inventory tracking, automated invoicing, and driver mobile apps. Built by industry veterans, the platform helps waste businesses increase revenue, improve cash flow, and streamline operations through integrated e‑commerce and data‑centric reporting.
image: https://cdn.prod.website-files.com/64a711ad4800f51470aab34c/64ce40c89e1879e4a84b725d_OpenGraph.png
jsonld:
- class_count: 37
  name: Curbwaste Context
  property_count: 63
  slug: curbwaste-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.curbwaste.com requiring an API key.
  name: Curbwaste MCP Server
  slug: curbwaste-mcp-yml
modified: '2026-10-12'
name: Curbwaste
nav: Providers
network: true
overview: 'Curbwaste publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Catalog API, Customers API, Locations API, and 2 more. Tagged areas include Waste, Software, Software-as-a-Service, Logistics, and Haulers.


  The Curbwaste catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Curbwaste''s developer surface includes authentication, support, engineering blog, getting-started guide, documentation, API reference, and 18 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Curbwaste API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: curbwaste-rules
score:
  band: developing
  composite: 40.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 48.8
    catalog_earned_first_party: 0.0
    catalog_gap: 66.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 62.4
    developer_ergonomics: 49.4
    discoverability: 66.7
    operational_transparency: 7.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Curbwaste Authentication
  slug: curbwaste-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Curbwaste Domain Security
  slug: curbwaste-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: curbwaste
tags:
- Waste
- Software
- Software-as-a-Service
- Logistics
- Haulers
website: https://www.curbwaste.com
---
