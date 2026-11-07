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
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API providing enquiry tools for damp survey price information.
  name: Damp Survey Prices API
  slug: damp-survey-prices-api
- baseURL: https://dampsurveyprices.co.uk
  baseurl_source: declared
  description: 'Damp Survey Prices (https://dampsurveyprices.co.uk/): the site''s own MCP server, served from its domain. Damp survey costs: £150–£400 for an independent survey with a written report, £200–£500 for com'
  name: Damp Survey Prices API API
  slug: damp-survey-prices-api-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/dampsurveyprices-co-uk/rules/dampsurveyprices-co-uk-rules.yml
  title: ''
  type: Spectral
  url: rules/dampsurveyprices-co-uk-rules.yml
- group: design
  href: https://artifacts.apis.io/dampsurveyprices-co-uk/vocabulary/dampsurveyprices-co-uk-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dampsurveyprices-co-uk-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dampsurveyprices-co-uk/conformance/dampsurveyprices-co-uk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dampsurveyprices-co-uk-conformance.yml
- group: auth
  title: ''
  type: Security
  url: https://dampsurveyprices.co.uk/terms
- group: design
  href: https://artifacts.apis.io/dampsurveyprices-co-uk/errors/dampsurveyprices-co-uk-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dampsurveyprices-co-uk-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/dampsurveyprices-co-uk/llms/dampsurveyprices-co-uk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dampsurveyprices-co-uk-llms.txt
- group: build
  href: https://artifacts.apis.io/dampsurveyprices-co-uk/mcp/dampsurveyprices-co-uk-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/dampsurveyprices-co-uk-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/dampsurveyprices-co-uk/mcp/dampsurveyprices-co-uk-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dampsurveyprices-co-uk-mcp.yml
- group: auth
  href: https://artifacts.apis.io/dampsurveyprices-co-uk/well-known/dampsurveyprices-co-uk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dampsurveyprices-co-uk-security.txt
- group: agent
  href: https://artifacts.apis.io/dampsurveyprices-co-uk/well-known/dampsurveyprices-co-uk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dampsurveyprices-co-uk-well-known.yml
- group: other
  href: https://artifacts.apis.io/dampsurveyprices-co-uk/hosts/dampsurveyprices-co-uk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dampsurveyprices-co-uk-hosts.yml
- group: other
  href: https://artifacts.apis.io/dampsurveyprices-co-uk/vendors/dampsurveyprices-co-uk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dampsurveyprices-co-uk-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dampsurveyprices.co.uk/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dampsurveyprices.co.uk/privacy/
- group: auth
  href: https://artifacts.apis.io/dampsurveyprices-co-uk/security/dampsurveyprices-co-uk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dampsurveyprices-co-uk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dampsurveyprices-co-uk/security/dampsurveyprices-co-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dampsurveyprices-co-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dampsurveyprices.co.uk/
- group: commercial
  title: ''
  type: Pricing
  url: https://dampsurveyprices.co.uk/datasets/damp-survey-price-index/
created: '2026-11-04'
description: Damp Survey Prices provides independent damp survey cost information and quotes for UK homeowners. The site offers detailed guides on independent versus free surveys, rising damp, mortgage survey requirements, and specialist damp services. It includes a price index dataset, methodology explanations, and links to authoritative sources such as BRE, Historic England, and Property Care. The platform aims to help users obtain transparent, market‑based pricing for damp surveys without vendor bias.
image: https://dampsurveyprices.co.uk/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at dampsurveyprices.co.uk.
  name: Damp Survey Prices MCP Server
  slug: dampsurveyprices-co-uk-mcp-yml
modified: '2026-11-04'
name: Damp Survey Prices
nav: Providers
network: true
overview: 'Damp Survey Prices publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API API, and 1 more. Tagged areas include Company, Surveys, Damp, United Kingdom, and Real Estate.


  The Damp Survey Prices catalog on APIs.io includes 1 Spectral governance ruleset.


  Damp Survey Prices'' developer surface includes pricing and 17 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: Damp Survey Prices API Rules
  rule_count: 48
  severity_counts:
    error: 43
    hint: 0
    info: 4
    warn: 1
  slug: dampsurveyprices-co-uk-rules
score:
  band: thin
  composite: 30.3
  coverage:
    artifact_dirs: 14
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 48.4
    developer_ergonomics: 0.0
    discoverability: 65.0
    operational_transparency: 10.5
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dampsurveyprices Co Uk Domain Security
  slug: dampsurveyprices-co-uk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dampsurveyprices Co Uk Vulnerability Disclosure
  slug: dampsurveyprices-co-uk-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dampsurveyprices-co-uk
tags:
- Company
- Surveys
- Damp
- United Kingdom
- Real Estate
- Pricing
website: https://dampsurveyprices.co.uk/
---
