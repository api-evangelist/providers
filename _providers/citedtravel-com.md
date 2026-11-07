---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 31.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Citedtravel Com Agentic Access
  operation_count: 14
  slug: citedtravel-com-agentic-access
  summary_line: 14 operations · 4 acting
api_count: 1
apis:
- baseURL: https://citedtravel.com
  baseurl_source: declared
  description: The billing API from CitedTravel — 3 operation(s) for billing.
  name: CitedTravel Billing API
  slug: citedtravel-com-billing-api
- baseURL: https://citedtravel.com
  baseurl_source: declared
  description: The entry API from CitedTravel — 2 operation(s) for entry.
  name: CitedTravel Entry API
  slug: citedtravel-com-entry-api
- baseURL: https://citedtravel.com
  baseurl_source: declared
  description: The facts API from CitedTravel — 3 operation(s) for facts.
  name: CitedTravel Facts API
  slug: citedtravel-com-facts-api
- baseURL: https://citedtravel.com
  baseurl_source: declared
  description: The meta API from CitedTravel — 6 operation(s) for meta.
  name: CitedTravel Meta API
  slug: citedtravel-com-meta-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/citedtravel-com/agentic-access/citedtravel-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/citedtravel-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/citedtravel-com/plans/citedtravel-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/citedtravel-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/citedtravel-com/rules/citedtravel-com-rules.yml
  title: ''
  type: Spectral
  url: rules/citedtravel-com-rules.yml
- group: design
  href: https://artifacts.apis.io/citedtravel-com/json-ld/citedtravel-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/citedtravel-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/citedtravel-com/vocabulary/citedtravel-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/citedtravel-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/citedtravel-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/citedtravel-com/data-model/citedtravel-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/citedtravel-com-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://citedtravel.com/support/
- group: design
  href: https://artifacts.apis.io/citedtravel-com/errors/citedtravel-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/citedtravel-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/citedtravel-com/conformance/citedtravel-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/citedtravel-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/citedtravel-com/llms/citedtravel-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/citedtravel-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/citedtravel-com/mcp/citedtravel-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/citedtravel-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/citedtravel-com/well-known/citedtravel-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/citedtravel-com-security.txt
- group: agent
  href: https://artifacts.apis.io/citedtravel-com/well-known/citedtravel-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/citedtravel-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/citedtravel-com/hosts/citedtravel-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/citedtravel-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/citedtravel-com/vendors/citedtravel-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/citedtravel-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://citedtravel.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://citedtravel.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://citedtravel.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://citedtravel.com/pricing/
- group: docs
  title: ''
  type: APIReference
  url: https://citedtravel.com/docs/
- group: auth
  href: https://artifacts.apis.io/citedtravel-com/authentication/citedtravel-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/citedtravel-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/citedtravel-com/security/citedtravel-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/citedtravel-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/citedtravel-com/security/citedtravel-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/citedtravel-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://citedtravel.com/
created: '2026-11-03'
description: CitedTravel provides travelers with factual, sourced, and dated information about travel essentials such as currency, driving side, public holidays, plugs, emergency numbers, and tipping for nearly every country. The data is verified against public sources and includes timestamps, enabling developers and agencies to build reliable travel applications. The service offers a free tier and paid plans for higher usage, with clear pricing and usage limits.
image: https://citedtravel.com/og.png
json_schemas:
- name: CategoryResponse
  property_count: 6
  slug: citedtravel-com-category-response
- name: ChangeFeed
  property_count: 3
  slug: citedtravel-com-change-feed
- name: EntryAnswer
  property_count: 10
  slug: citedtravel-com-entry-answer
jsonld:
- class_count: 8
  name: Citedtravel Com Context
  property_count: 49
  slug: citedtravel-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at citedtravel.com.
  name: CitedTravel MCP Server
  slug: citedtravel-com-mcp-yml
modified: '2026-11-03'
name: CitedTravel
nav: Providers
network: true
overview: 'CitedTravel publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Billing API, Entry API, Facts API, and 1 more. Tagged areas include Travel, Data, TravelFacts, and Open Data.


  The CitedTravel catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CitedTravel''s developer surface includes support, pricing, API reference, authentication, and 21 more developer resources.'
plans:
- name: Citedtravel Com Plans Pricing
  plan_count: 4
  slug: citedtravel-com-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: CitedTravel API Rules
  rule_count: 61
  severity_counts:
    error: 57
    hint: 0
    info: 1
    warn: 3
  slug: citedtravel-com-rules
score:
  band: developing
  composite: 41.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 35.6
    contract_quality: 61.8
    developer_ergonomics: 19.6
    discoverability: 56.7
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Citedtravel Com Authentication
  slug: citedtravel-com-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Citedtravel Com Domain Security
  slug: citedtravel-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Citedtravel Com Vulnerability Disclosure
  slug: citedtravel-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: citedtravel-com-billing-subscription
  slug: citedtravel-com-billing-subscription
- name: citedtravel-com-get-country-info
  slug: citedtravel-com-get-country-info
slug: citedtravel-com
tags:
- Travel
- Data
- TravelFacts
- Open Data
website: https://citedtravel.com/
---
