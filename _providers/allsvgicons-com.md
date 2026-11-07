---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Programmatic access to the SVG icon catalog and related tools.
  name: All SVG Icons API
  slug: all-svg-icons-api
- baseURL: https://i.allsvgicons.com
  baseurl_source: declared
  description: 'All SVG Icons API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: All SVG Icons API
  slug: allsvgicons-com-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/allsvgicons-com/rules/allsvgicons-com-rules.yml
  title: ''
  type: Spectral
  url: rules/allsvgicons-com-rules.yml
- group: design
  href: https://artifacts.apis.io/allsvgicons-com/json-ld/allsvgicons-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/allsvgicons-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/allsvgicons-com/vocabulary/allsvgicons-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/allsvgicons-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/allsvgicons-com/data-model/allsvgicons-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/allsvgicons-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/allsvgicons-com/changelog/allsvgicons-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/allsvgicons-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/allsvgicons-com/conformance/allsvgicons-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/allsvgicons-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/allsvgicons-com/llms/allsvgicons-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/allsvgicons-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/allsvgicons-com/well-known/allsvgicons-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/allsvgicons-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/allsvgicons-com/hosts/allsvgicons-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/allsvgicons-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/allsvgicons-com/vendors/allsvgicons-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/allsvgicons-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://allsvgicons.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://allsvgicons.com/privacy/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://allsvgicons.com/collections/developer/
- group: operate
  title: ''
  type: ChangeLog
  url: https://allsvgicons.com/changelog/
- group: company
  title: ''
  type: Blog
  url: https://allsvgicons.com/blog/
- group: auth
  href: https://artifacts.apis.io/allsvgicons-com/security/allsvgicons-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/allsvgicons-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://allsvgicons.com/
coverage:
  checked: '2026-11-01'
  detail: No public API base URL or machine‑readable contract was found on the provider's site.
  evidence:
  - status: 200
    url: https://allsvgicons.com/
  reason: no-developer-program
  state: none
created: '2026-11-01'
description: All SVG Icons provides a free and open‑source collection of SVG icon libraries, offering a searchable catalog of over 400 k icons across dozens of packs. The site includes tools such as an SVG optimizer, sprite maker, favicon generator, and AI‑ready MCP for agents. It serves developers, designers, and AI applications looking for royalty‑free vector icons and related utilities.
image: https://allsvgicons.com/og.png
json_schemas:
- name: GetMcpResponse
  property_count: 1
  slug: allsvgicons-com-get-mcp-response
- name: PostMcpRequest
  property_count: 4
  slug: allsvgicons-com-post-mcp-request
- name: PostMcpResponse
  property_count: 4
  slug: allsvgicons-com-post-mcp-response
jsonld:
- class_count: 3
  name: Allsvgicons Com Context
  property_count: 7
  slug: allsvgicons-com-context
layout: provider
modified: '2026-11-01'
name: All SVG Icons
nav: Providers
network: true
overview: 'All SVG Icons is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Icon, Open Source, Design, Developer Tools, and Artificial Intelligence.


  The All SVG Icons catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  All SVG Icons'' developer surface includes changelog, engineering blog, and 15 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: All SVG Icons API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: allsvgicons-com-rules
score:
  band: emerging
  composite: 18.2
  coverage:
    artifact_dirs: 15
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.9
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 19.8
    developer_ergonomics: 6.0
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 23.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Allsvgicons Com Domain Security
  slug: allsvgicons-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: allsvgicons-com
tags:
- Icon
- Open Source
- Design
- Developer Tools
- Artificial Intelligence
- Company
website: https://allsvgicons.com/
---
