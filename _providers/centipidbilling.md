---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 33.5
  scored_at: '2026-10-17'
api_count: 5
apis:
- description: API for Centipid Technologies ISP billing platform, as documented in the developer reference.
  name: Centipid Billing API
  slug: centipid-billing-api
- baseURL: https://mcp.centipidbilling.com
  baseurl_source: declared
  description: The Async API from Centipid Technologies — 2 operation(s) for async.
  name: Centipid Technologies Async API
  slug: centipidbilling-async-api
- baseURL: https://mcp.centipidbilling.com
  baseurl_source: declared
  description: The Collections API from Centipid Technologies — 2 operation(s) for collections.
  name: Centipid Technologies Collections API
  slug: centipidbilling-collections-api
- baseURL: https://mcp.centipidbilling.com
  baseurl_source: declared
  description: The Interface API from Centipid Technologies — 1 operation(s) for interface.
  name: Centipid Technologies Interface API
  slug: centipidbilling-interface-api
- baseURL: https://mcp.centipidbilling.com
  baseurl_source: declared
  description: The Mcp API from Centipid Technologies — 1 operation(s) for mcp.
  name: Centipid Technologies MCP API
  slug: centipidbilling-mcp-api
artifact_total: 13
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/centipidbilling/refs/heads/main/plans/centipidbilling-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/centipidbilling-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/centipidbilling/refs/heads/main/rules/centipidbilling-rules.yml
  title: ''
  type: Spectral
  url: rules/centipidbilling-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/centipidbilling/refs/heads/main/json-ld/centipidbilling-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/centipidbilling-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/centipidbilling/refs/heads/main/vocabulary/centipidbilling-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/centipidbilling-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/centipidbilling/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/centipidbilling/refs/heads/main/data-model/centipidbilling-data-model.yml
  title: ''
  type: DataModel
  url: data-model/centipidbilling-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/centipidbilling/refs/heads/main/conformance/centipidbilling-conformance.yml
  title: ''
  type: Conformance
  url: conformance/centipidbilling-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/centipidbilling/refs/heads/main/llms/centipidbilling-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/centipidbilling-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/centipidbilling/refs/heads/main/well-known/centipidbilling-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/centipidbilling-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/centipidbilling/refs/heads/main/hosts/centipidbilling-hosts.yml
  title: ''
  type: Hosts
  url: hosts/centipidbilling-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/centipidbilling/refs/heads/main/vendors/centipidbilling-vendors.yml
  title: ''
  type: Vendors
  url: vendors/centipidbilling-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.centipidbilling.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://centipidbilling.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://centipidbilling.com/privacy
- group: start
  title: ''
  type: Login
  url: https://community.centipidbilling.com/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://centipidbilling.com/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.centipidbilling.com/reference/support
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.centipidbilling.com/quickstart
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/centipidbilling/refs/heads/main/security/centipidbilling-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/centipidbilling-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://centipidbilling.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.centipidbilling.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.centipidbilling.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://centipidbilling.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://centipidbilling.com/blog
- group: operate
  title: ''
  type: Support
  url: https://centipidbilling.com/contact
coverage:
  checked: '2026-10-16'
  detail: Documentation pages are HTML only and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://docs.centipidbilling.com/reference/support
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-16'
description: Centipid Technologies provides a comprehensive ISP billing and OSS/BSS platform that enables broadband providers to manage subscriber records, billing, payments, and network access. The solution integrates PPPoE, Hotspot, RADIUS, and various router platforms, offering features such as automated invoicing, payment reconciliation, captive‑portal promotions, lead management, and AI‑assisted staff tools. It supports multi‑country tax compliance, extensive reporting, and flexible deployment options for ISPs seeking to streamline operations and improve customer experience.
image: https://centipidbilling.com/brand/centipid-og-v4.jpg
json_schemas:
- name: GetApiV2AsyncPaymentsOrderidResponse
  property_count: 2
  slug: centipidbilling-get-api-v2-async-payments-orderid-response
- name: PostApiV2AsyncPaymentsRequest
  property_count: 3
  slug: centipidbilling-post-api-v2-async-payments-request
- name: PostApiV2AsyncPaymentsResponse
  property_count: 1
  slug: centipidbilling-post-api-v2-async-payments-response
- name: PostMcpRequest
  property_count: 3
  slug: centipidbilling-post-mcp-request
jsonld:
- class_count: 4
  name: Centipidbilling Context
  property_count: 9
  slug: centipidbilling-context
layout: provider
modified: '2026-10-16'
name: Centipid Technologies
nav: Providers
network: true
overview: 'Centipid Technologies is listed with 5 APIs on the [APIs.io](https://apis.io/) network, including Async API, Collections API, Interface API, and 2 more. Tagged areas include Company, ISP, Billing, OSS/BSS, and Telecommunications.


  The Centipid Technologies catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Centipid Technologies'' developer surface includes changelog, API reference, getting-started guide, documentation, pricing, engineering blog, support, and 18 more developer resources.'
plans:
- name: Centipidbilling Plans Pricing
  plan_count: 4
  slug: centipidbilling-plans-pricing
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Centipid Technologies API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: centipidbilling-rules
score:
  band: developing
  composite: 44.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 66.8
    catalog_earned_first_party: 12.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 84.2
    contract_governance: 22.0
    contract_quality: 21.4
    developer_ergonomics: 51.7
    discoverability: 69.6
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 25.0
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Centipidbilling Domain Security
  slug: centipidbilling-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: centipidbilling
tags:
- Company
- ISP
- Billing
- OSS/BSS
- Telecommunications
website: https://centipidbilling.com/
---
