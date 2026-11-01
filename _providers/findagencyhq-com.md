---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://findagencyhq.com
  baseurl_source: declared
  description: 'FindAgency HQ (https://findagencyhq.com/): the site''s own MCP server, served from its domain. FindAgency HQ: the median advertised marketing retainer starting price per month, read from verified agenc'
  name: FindAgency HQ API API
  slug: findagency-hq-api-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/findagencyhq-com/rules/findagencyhq-com-rules.yml
  title: ''
  type: Spectral
  url: rules/findagencyhq-com-rules.yml
- group: design
  href: https://artifacts.apis.io/findagencyhq-com/vocabulary/findagencyhq-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/findagencyhq-com-vocabulary.yml
- group: auth
  title: ''
  type: Security
  url: https://findagencyhq.com/terms
- group: design
  href: https://artifacts.apis.io/findagencyhq-com/errors/findagencyhq-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/findagencyhq-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/findagencyhq-com/conformance/findagencyhq-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/findagencyhq-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/findagencyhq-com/llms/findagencyhq-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/findagencyhq-com-llms.txt
- group: build
  href: https://artifacts.apis.io/findagencyhq-com/mcp/findagencyhq-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/findagencyhq-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/findagencyhq-com/mcp/findagencyhq-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/findagencyhq-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/findagencyhq-com/well-known/findagencyhq-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/findagencyhq-com-security.txt
- group: agent
  href: https://artifacts.apis.io/findagencyhq-com/well-known/findagencyhq-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/findagencyhq-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/findagencyhq-com/hosts/findagencyhq-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/findagencyhq-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/findagencyhq-com/vendors/findagencyhq-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/findagencyhq-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://findagencyhq.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://findagencyhq.com/privacy/
- group: auth
  href: https://artifacts.apis.io/findagencyhq-com/security/findagencyhq-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/findagencyhq-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/findagencyhq-com/security/findagencyhq-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/findagencyhq-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://findagencyhq.com/
created: '2026-10-30'
description: FindAgencyHQ is a digital marketing agency marketplace that connects businesses with specialized agencies across content marketing, SEO, PPC, social media, and web development. The platform offers searchable listings, detailed agency profiles, pricing guides, and resources to help companies hire the right marketing partner for their needs. It serves a wide range of industries, providing tools and insights for effective digital marketing strategy and execution.
image: https://findagencyhq.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at findagencyhq.com.
  name: findagencyhq-com MCP Server
  slug: findagencyhq-com-mcp-yml
modified: '2026-10-30'
name: findagencyhq-com
nav: Providers
network: true
overview: 'findagencyhq-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: FindAgency HQ API API. Tagged areas include Company, Marketing, Agency, Digital, and SEO.


  The findagencyhq-com catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: findagencyhq-com API Rules
  rule_count: 16
  severity_counts:
    error: 11
    hint: 0
    info: 4
    warn: 1
  slug: findagencyhq-com-rules
score:
  band: thin
  composite: 29.0
  coverage:
    artifact_dirs: 13
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 51.4
    developer_ergonomics: 0.0
    discoverability: 65.0
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Findagencyhq Com Domain Security
  slug: findagencyhq-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Findagencyhq Com Vulnerability Disclosure
  slug: findagencyhq-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: findagencyhq-com
tags:
- Company
- Marketing
- Agency
- Digital
- SEO
website: https://findagencyhq.com/
---
