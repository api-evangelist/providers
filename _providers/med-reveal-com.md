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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Med Reveal Com Agentic Access
  operation_count: 16
  slug: med-reveal-com-agentic-access
  summary_line: 16 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.med-reveal.com
  baseurl_source: declared
  description: The benchmarking-api API from MedReveal — 2 operation(s) for benchmarking-api.
  name: MedReveal Benchmarking API
  slug: med-reveal-com-benchmarking-api-api
- baseURL: https://api.med-reveal.com
  baseurl_source: declared
  description: ❤️ Health check endpoints
  name: MedReveal Health API
  slug: med-reveal-com-health-api
- baseURL: https://api.med-reveal.com
  baseurl_source: declared
  description: 📊 Market search and benchmarking endpoints
  name: MedReveal Market API
  slug: med-reveal-com-market-api-api
- baseURL: https://api.med-reveal.com
  baseurl_source: declared
  description: 🏥 NPI lookup and search endpoints
  name: MedReveal Npi API
  slug: med-reveal-com-npi-api-api
- baseURL: https://api.med-reveal.com
  baseurl_source: declared
  description: 💰 Provider-specific rate search endpoints
  name: MedReveal Provider API
  slug: med-reveal-com-provider-api-api
- baseURL: https://api.med-reveal.com
  baseurl_source: declared
  description: 🏷️ Taxonomy code lookup (public)
  name: MedReveal Taxonomy API
  slug: med-reveal-com-taxonomy-api-api
- baseURL: https://api.med-reveal.com
  baseurl_source: declared
  description: 🏢 TIN/Provider Group lookup and search endpoints
  name: MedReveal Tin API
  slug: med-reveal-com-tin-api-api
- baseURL: https://api.med-reveal.com
  baseurl_source: declared
  description: 📈 API usage statistics
  name: MedReveal Usage API
  slug: med-reveal-com-usage-api-api
artifact_total: 20
common:
- group: agent
  href: https://artifacts.apis.io/med-reveal-com/agentic-access/med-reveal-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/med-reveal-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/med-reveal-com/rules/med-reveal-com-rules.yml
  title: ''
  type: Spectral
  url: rules/med-reveal-com-rules.yml
- group: design
  href: https://artifacts.apis.io/med-reveal-com/json-ld/med-reveal-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/med-reveal-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/med-reveal-com/vocabulary/med-reveal-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/med-reveal-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/med-reveal-com/data-model/med-reveal-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/med-reveal-com-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.med-reveal.com/security
- group: design
  href: https://artifacts.apis.io/med-reveal-com/errors/med-reveal-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/med-reveal-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/med-reveal-com/conformance/med-reveal-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/med-reveal-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/med-reveal-com/llms/med-reveal-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/med-reveal-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/med-reveal-com/well-known/med-reveal-com-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/med-reveal-com-www-security.txt
- group: auth
  href: https://artifacts.apis.io/med-reveal-com/well-known/med-reveal-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/med-reveal-com-security.txt
- group: auth
  href: https://artifacts.apis.io/med-reveal-com/well-known/med-reveal-com-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/med-reveal-com-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/med-reveal-com/well-known/med-reveal-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/med-reveal-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/med-reveal-com/hosts/med-reveal-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/med-reveal-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/med-reveal-com/vendors/med-reveal-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/med-reveal-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.med-reveal.com/security
- group: start
  title: ''
  type: Login
  url: https://www.med-reveal.com/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.med-reveal.com/
- group: auth
  href: https://artifacts.apis.io/med-reveal-com/security/med-reveal-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/med-reveal-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/med-reveal-com/security/med-reveal-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/med-reveal-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/med-reveal-com/security/med-reveal-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/med-reveal-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.med-reveal.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.med-reveal.com/mcp
- group: docs
  title: ''
  type: APIReference
  url: https://www.med-reveal.com/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://www.med-reveal.com/developers
- group: company
  title: ''
  type: Blog
  url: https://www.med-reveal.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.med-reveal.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.med-reveal.com/privacy
created: '2026-11-05'
description: MedReveal provides a transparent healthcare pricing platform that offers data‑driven tools for rate benchmarking, contract negotiation, price transparency, and under‑paid contract identification. It aggregates CPT, HCPCS, and ICD‑10 coding data to help providers, consultants, MSOs, IPAs, and employers benchmark payer rates, prepare for negotiations, and ensure compliance with CMS transparency requirements. The platform also offers an MCP server for AI‑assisted queries and integrates with major LLMs.
image: https://www.med-reveal.com/og?title=Benchmark+your+negotiated+rates+with+peers
json_schemas:
- name: BenchmarkRequest
  property_count: 3
  slug: med-reveal-com-benchmark-request
- name: MarketSearchRequest
  property_count: 10
  slug: med-reveal-com-market-search-request
- name: NpiSearchRequest
  property_count: 8
  slug: med-reveal-com-npi-search-request
- name: ProviderSearchRatesRequest
  property_count: 11
  slug: med-reveal-com-provider-search-rates-request
- name: ProviderSearchRatesResponse
  property_count: 6
  slug: med-reveal-com-provider-search-rates-response
- name: TinSearchRequest
  property_count: 7
  slug: med-reveal-com-tin-search-request
jsonld:
- class_count: 116
  name: Med Reveal Com Context
  property_count: 304
  slug: med-reveal-com-context
layout: provider
modified: '2026-11-05'
name: MedReveal
nav: Providers
network: true
overview: 'MedReveal publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Benchmarking API, Health API, Market API, and 5 more. Tagged areas include Company, Healthcare, Pricing, Data Analytics, and MCP.


  The MedReveal catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  MedReveal''s developer surface includes documentation, API reference, getting-started guide, engineering blog, and 24 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: MedReveal API Rules
  rule_count: 44
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 3
  slug: med-reveal-com-rules
score:
  band: developing
  composite: 46.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.0
    contract_governance: 35.6
    contract_quality: 54.2
    developer_ergonomics: 40.5
    discoverability: 66.1
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 28.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Med Reveal Com Domain Security
  slug: med-reveal-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Med Reveal Com Vulnerability Disclosure
  slug: med-reveal-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Med Reveal Com Trust Center
  slug: med-reveal-com-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA
slug: med-reveal-com
tags:
- Company
- Healthcare
- Pricing
- Data Analytics
- MCP
website: https://www.med-reveal.com
---
