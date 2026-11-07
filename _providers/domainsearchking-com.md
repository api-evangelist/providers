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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Check any domain's availability via the free API documented at the provider's site.
  name: Domain Availability API
  slug: domain-availability-api
- description: 'Domain Search King API as documented publicly: 8 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: Domain Search King API
  slug: domainsearchking-com-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/domainsearchking-com/rules/domainsearchking-com-rules.yml
  title: ''
  type: Spectral
  url: rules/domainsearchking-com-rules.yml
- group: design
  href: https://artifacts.apis.io/domainsearchking-com/json-ld/domainsearchking-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/domainsearchking-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/domainsearchking-com/vocabulary/domainsearchking-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/domainsearchking-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/domainsearchking-com/data-model/domainsearchking-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/domainsearchking-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/domainsearchking-com/errors/domainsearchking-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/domainsearchking-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/domainsearchking-com/conformance/domainsearchking-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/domainsearchking-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/domainsearchking-com/llms/domainsearchking-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/domainsearchking-com-llms.txt
- group: build
  href: https://artifacts.apis.io/domainsearchking-com/mcp/domainsearchking-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/domainsearchking-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/domainsearchking-com/mcp/domainsearchking-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/domainsearchking-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/domainsearchking-com/well-known/domainsearchking-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/domainsearchking-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/domainsearchking-com/hosts/domainsearchking-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/domainsearchking-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/domainsearchking-com/vendors/domainsearchking-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/domainsearchking-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://domainsearchking.com/terms
- group: start
  title: ''
  type: SignUp
  url: https://domainsearchking.com/registered-domain-no-website
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://domainsearchking.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://domainsearchking.com/ideas/blog
- group: auth
  href: https://artifacts.apis.io/domainsearchking-com/security/domainsearchking-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/domainsearchking-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://domainsearchking.com/
coverage:
  checked: '2026-11-06'
  detail: Provider documents an API but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec is publicly available.
  evidence:
  - status: 200
    url: https://domainsearchking.com/domain-availability-api.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: Domain Search King provides a free AI‑enhanced domain name generator that checks each .com, .net, .ai and .io suggestion live against the registry via RDAP before displaying it. The service guarantees only truly available domains are shown, with no AI‑only guesses, and offers an MCP server for programmatic access.
image: https://domainsearchking.com/images/free-domain-name-generator-og.jpg
json_schemas:
- name: GetComV1DomainExampleComResponse
  property_count: 3
  slug: domainsearchking-com-get-com-v1-domain-example-com-response
- name: GetRdapDomainBrandlyIoResponse
  property_count: 4
  slug: domainsearchking-com-get-rdap-domain-brandly-io-response
- name: PostApiMcpRequest
  property_count: 4
  slug: domainsearchking-com-post-api-mcp-request
jsonld:
- class_count: 3
  name: Domainsearchking Com Context
  property_count: 9
  slug: domainsearchking-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at domainsearchking.com.
  name: Domain Search King MCP Server
  slug: domainsearchking-com-mcp-yml
modified: '2026-11-05'
name: Domain Search King
nav: Providers
network: true
overview: 'Domain Search King is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include domain name generator, business naming, registry‑checked availability, AI naming styles, and domain extensions.


  The Domain Search King catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Domain Search King''s developer surface includes signup flow, engineering blog, and 16 more developer resources.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 77
  extends:
  - spectral:oas
  name: Domain Search King API Rules
  rule_count: 36
  severity_counts:
    error: 34
    hint: 0
    info: 1
    warn: 1
  slug: domainsearchking-com-rules
score:
  band: emerging
  composite: 20.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 18.0
    developer_ergonomics: 2.4
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Domainsearchking Com Domain Security
  slug: domainsearchking-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: domainsearchking-com
tags:
- domain name generator
- business naming
- registry‑checked availability
- AI naming styles
- domain extensions
website: https://domainsearchking.com/
---
