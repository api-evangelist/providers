---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 12.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: A bank statement converter is the fallback, not the first answer. Six routes to machine-readable transactions compared on accuracy, coverage and where the file goes.
  name: Bank Convert API
  slug: bankconvert-api
artifact_total: 14
common:
- group: design
  href: https://artifacts.apis.io/bankconvert-uk/rules/bankconvert-uk-rules.yml
  title: ''
  type: Spectral
  url: rules/bankconvert-uk-rules.yml
- group: design
  href: https://artifacts.apis.io/bankconvert-uk/errors/bankconvert-uk-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bankconvert-uk-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bankconvert-uk/vocabulary/bankconvert-uk-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bankconvert-uk-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/bankconvert-uk/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://bankconvert.uk/terms
- group: auth
  href: https://artifacts.apis.io/bankconvert-uk/authentication/bankconvert-uk-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bankconvert-uk-authentication.yml
- group: design
  href: https://artifacts.apis.io/bankconvert-uk/conformance/bankconvert-uk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bankconvert-uk-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bankconvert-uk/llms/bankconvert-uk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bankconvert-uk-llms.txt
- group: build
  href: https://artifacts.apis.io/bankconvert-uk/mcp/bankconvert-uk-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/bankconvert-uk-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/bankconvert-uk/mcp/bankconvert-uk-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bankconvert-uk-mcp.yml
- group: auth
  href: https://artifacts.apis.io/bankconvert-uk/well-known/bankconvert-uk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bankconvert-uk-security.txt
- group: agent
  href: https://artifacts.apis.io/bankconvert-uk/well-known/bankconvert-uk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bankconvert-uk-well-known.yml
- group: other
  href: https://artifacts.apis.io/bankconvert-uk/hosts/bankconvert-uk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bankconvert-uk-hosts.yml
- group: other
  href: https://artifacts.apis.io/bankconvert-uk/vendors/bankconvert-uk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bankconvert-uk-vendors.yml
- group: auth
  href: https://artifacts.apis.io/bankconvert-uk/security/bankconvert-uk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bankconvert-uk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bankconvert-uk/security/bankconvert-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bankconvert-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bankconvert.uk/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bankconvert.uk/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bankconvert.uk/privacy/
- group: operate
  title: ''
  type: Support
  url: https://bankconvert.uk/contact/
- group: company
  title: ''
  type: About
  url: https://bankconvert.uk/about/
- group: commercial
  title: ''
  type: Pricing
  url: https://bankconvert.uk/datasets/converter-pricing-index/
created: '2026-11-02'
description: Bank Convert provides a UK‑focused bank statement conversion service that transforms PDF, CSV or OFX statements into structured transaction data. The site explains six conversion routes, compares accuracy, coverage and data handling, and offers guidance on safety, GDPR compliance and open‑banking alternatives. It includes pricing information, terms of service, privacy policy and contact support.
image: https://bankconvert.uk/icon-512.png
layout: provider
mcp_servers:
- description: Remote MCP server at bankconvert.uk.
  name: Bank Convert MCP Server
  slug: bankconvert-uk-mcp-yml
modified: '2026-11-02'
name: Bank Convert
nav: Providers
network: true
overview: 'Bank Convert publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Banking, Data Conversion, United Kingdom, and Open Banking.


  The Bank Convert catalog on APIs.io includes 1 Spectral governance ruleset.


  Bank Convert''s developer surface includes authentication, support, pricing, and 19 more developer resources.'
plans:
- name: Bankconvert Uk Plans Pricing
  plan_count: 0
  slug: bankconvert-uk-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: Bank Convert API Rules
  rule_count: 49
  severity_counts:
    error: 43
    hint: 0
    info: 5
    warn: 1
  slug: bankconvert-uk-rules
scopes:
- name: Bankconvert Uk Scopes
  scope_count: 0
  slug: bankconvert-uk-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.3
  coverage:
    artifact_dirs: 25
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.8
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 0.0
    developer_ergonomics: 20.7
    discoverability: 65.0
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 24.1
  provenance:
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 34.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bankconvert Uk Authentication
  slug: bankconvert-uk-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bankconvert Uk Domain Security
  slug: bankconvert-uk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bankconvert Uk Vulnerability Disclosure
  slug: bankconvert-uk-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 6
skills:
- name: compare-criteria
  slug: bankconvert-uk-compare_criteria
- name: compare-options
  slug: bankconvert-uk-compare_options
- name: compare-table
  slug: bankconvert-uk-compare_table
- name: enquiry-describe
  slug: bankconvert-uk-enquiry_describe
- name: enquiry-fields
  slug: bankconvert-uk-enquiry_fields
- name: submit-enquiry
  slug: bankconvert-uk-submit_enquiry
slug: bankconvert-uk
tags:
- Finance
- Banking
- Data Conversion
- United Kingdom
- Open Banking
website: https://bankconvert.uk/
---
