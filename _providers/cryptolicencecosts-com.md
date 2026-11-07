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
- description: Crypto Licence Costs API providing calculator and enquiry tools.
  name: Crypto Licence Costs API
  slug: crypto-licence-costs-api
- baseURL: https://cryptolicencecosts.com
  baseurl_source: declared
  description: 'Crypto Licence Costs (https://cryptolicencecosts.com/): the site''s own MCP server, served from its domain. Crypto license cost comparison by country: MFSA fees of EUR 10,000 to EUR 25,000 to apply, an'
  name: Crypto Licence Costs API API
  slug: crypto-licence-costs-api-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/cryptolicencecosts-com/rules/cryptolicencecosts-com-rules.yml
  title: ''
  type: Spectral
  url: rules/cryptolicencecosts-com-rules.yml
- group: design
  href: https://artifacts.apis.io/cryptolicencecosts-com/vocabulary/cryptolicencecosts-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cryptolicencecosts-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cryptolicencecosts-com/conformance/cryptolicencecosts-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cryptolicencecosts-com-conformance.yml
- group: auth
  title: ''
  type: Security
  url: https://cryptolicencecosts.com/terms
- group: design
  href: https://artifacts.apis.io/cryptolicencecosts-com/errors/cryptolicencecosts-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cryptolicencecosts-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/cryptolicencecosts-com/llms/cryptolicencecosts-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cryptolicencecosts-com-llms.txt
- group: build
  href: https://artifacts.apis.io/cryptolicencecosts-com/mcp/cryptolicencecosts-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/cryptolicencecosts-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/cryptolicencecosts-com/mcp/cryptolicencecosts-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cryptolicencecosts-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/cryptolicencecosts-com/well-known/cryptolicencecosts-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cryptolicencecosts-com-security.txt
- group: agent
  href: https://artifacts.apis.io/cryptolicencecosts-com/well-known/cryptolicencecosts-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cryptolicencecosts-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cryptolicencecosts-com/hosts/cryptolicencecosts-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cryptolicencecosts-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cryptolicencecosts-com/vendors/cryptolicencecosts-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cryptolicencecosts-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/cryptolicencecosts-com/security/cryptolicencecosts-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cryptolicencecosts-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cryptolicencecosts-com/security/cryptolicencecosts-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cryptolicencecosts-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cryptolicencecosts.com/
- group: company
  title: ''
  type: About
  url: https://cryptolicencecosts.com/about/
- group: operate
  title: ''
  type: Contact
  url: https://cryptolicencecosts.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cryptolicencecosts.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cryptolicencecosts.com/terms/
created: '2026-11-04'
description: Crypto Licence Costs provides a data-driven comparison of crypto licensing fees across jurisdictions, offering calculators, guides, and up‑to‑date fee tables sourced directly from regulators. The site aggregates published regulator fees for MiCA, UK FCA, New York BitLicense and others, clearly indicating where fees are unavailable, and supplies tools for budgeting crypto licence applications without legal advice.
image: https://cryptolicencecosts.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at cryptolicencecosts.com.
  name: Crypto Licence Costs MCP Server
  slug: cryptolicencecosts-com-mcp-yml
modified: '2026-11-04'
name: Crypto Licence Costs
nav: Providers
network: true
overview: 'Crypto Licence Costs publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API API, and 1 more. Tagged areas include Cryptocurrency, Licensing, Fees, Comparison, and Guides.


  The Crypto Licence Costs catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: Crypto Licence Costs API Rules
  rule_count: 49
  severity_counts:
    error: 43
    hint: 0
    info: 5
    warn: 1
  slug: cryptolicencecosts-com-rules
score:
  band: thin
  composite: 28.2
  coverage:
    artifact_dirs: 15
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
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
  name: Cryptolicencecosts Com Domain Security
  slug: cryptolicencecosts-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cryptolicencecosts Com Vulnerability Disclosure
  slug: cryptolicencecosts-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cryptolicencecosts-com
tags:
- Cryptocurrency
- Licensing
- Fees
- Comparison
- Guides
website: https://cryptolicencecosts.com/
---
