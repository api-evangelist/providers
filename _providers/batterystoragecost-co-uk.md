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
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 26.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Batterystoragecost Co Uk Agentic Access
  operation_count: 5
  slug: batterystoragecost-co-uk-agentic-access
  summary_line: 5 operations · 4 acting
api_count: 1
apis:
- baseURL: https://batterystoragecost.co.uk
  baseurl_source: declared
  description: enquiry
  name: Battery Storage Cost Enquiry API
  slug: batterystoragecost-co-uk-enquiry-api
- baseURL: https://batterystoragecost.co.uk
  baseurl_source: declared
  description: The mcp API from Battery Storage Cost — 1 operation(s) for mcp.
  name: Battery Storage Cost MCP API
  slug: batterystoragecost-co-uk-mcp-api
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/batterystoragecost-co-uk/agentic-access/batterystoragecost-co-uk-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/batterystoragecost-co-uk-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/batterystoragecost-co-uk/rules/batterystoragecost-co-uk-rules.yml
  title: ''
  type: Spectral
  url: rules/batterystoragecost-co-uk-rules.yml
- group: design
  href: https://artifacts.apis.io/batterystoragecost-co-uk/vocabulary/batterystoragecost-co-uk-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/batterystoragecost-co-uk-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/batterystoragecost-co-uk/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://batterystoragecost.co.uk/terms
- group: design
  href: https://artifacts.apis.io/batterystoragecost-co-uk/errors/batterystoragecost-co-uk-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/batterystoragecost-co-uk-problem-types.yml
- group: design
  href: https://artifacts.apis.io/batterystoragecost-co-uk/conformance/batterystoragecost-co-uk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/batterystoragecost-co-uk-conformance.yml
- group: agent
  href: https://artifacts.apis.io/batterystoragecost-co-uk/llms/batterystoragecost-co-uk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/batterystoragecost-co-uk-llms.txt
- group: agent
  href: https://artifacts.apis.io/batterystoragecost-co-uk/mcp/batterystoragecost-co-uk-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/batterystoragecost-co-uk-mcp.yml
- group: auth
  href: https://artifacts.apis.io/batterystoragecost-co-uk/well-known/batterystoragecost-co-uk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/batterystoragecost-co-uk-security.txt
- group: agent
  href: https://artifacts.apis.io/batterystoragecost-co-uk/well-known/batterystoragecost-co-uk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/batterystoragecost-co-uk-well-known.yml
- group: other
  href: https://artifacts.apis.io/batterystoragecost-co-uk/hosts/batterystoragecost-co-uk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/batterystoragecost-co-uk-hosts.yml
- group: other
  href: https://artifacts.apis.io/batterystoragecost-co-uk/vendors/batterystoragecost-co-uk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/batterystoragecost-co-uk-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://batterystoragecost.co.uk/privacy/
- group: auth
  href: https://artifacts.apis.io/batterystoragecost-co-uk/authentication/batterystoragecost-co-uk-authentication.yml
  title: ''
  type: Authentication
  url: authentication/batterystoragecost-co-uk-authentication.yml
- group: auth
  href: https://artifacts.apis.io/batterystoragecost-co-uk/security/batterystoragecost-co-uk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/batterystoragecost-co-uk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/batterystoragecost-co-uk/security/batterystoragecost-co-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/batterystoragecost-co-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://batterystoragecost.co.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://batterystoragecost.co.uk/about/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://batterystoragecost.co.uk/terms
created: '2026-11-02'
description: Battery Storage Cost provides detailed information on commercial battery storage costs in the UK, explaining the factors that influence pricing, payback periods, VAT status, and the impact of solar integration. The service offers free quotes by connecting users with commercial renewable energy providers, funded through referral fees. It aims to increase transparency in the battery storage market for both commercial and residential sectors.
image: https://batterystoragecost.co.uk/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at batterystoragecost.co.uk.
  name: Battery Storage Cost MCP Server
  slug: batterystoragecost-co-uk-mcp-yml
modified: '2026-11-02'
name: Battery Storage Cost
nav: Providers
network: true
overview: 'Battery Storage Cost publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Enquiry API and MCP API. Tagged areas include Energy, Battery, Storage, United Kingdom, and Cost.


  The Battery Storage Cost catalog on APIs.io includes 1 Spectral governance ruleset.


  Battery Storage Cost''s developer surface includes authentication, documentation, and 18 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: Battery Storage Cost API Rules
  rule_count: 48
  severity_counts:
    error: 43
    hint: 0
    info: 4
    warn: 1
  slug: batterystoragecost-co-uk-rules
score:
  band: thin
  composite: 28.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 47.4
    developer_ergonomics: 18.5
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
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 22.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Batterystoragecost Co Uk Authentication
  slug: batterystoragecost-co-uk-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Batterystoragecost Co Uk Domain Security
  slug: batterystoragecost-co-uk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Batterystoragecost Co Uk Vulnerability Disclosure
  slug: batterystoragecost-co-uk-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: batterystoragecost-co-uk-enquiry-process
  slug: batterystoragecost-co-uk-enquiry-process
slug: batterystoragecost-co-uk
tags:
- Energy
- Battery
- Storage
- United Kingdom
- Cost
website: https://batterystoragecost.co.uk/
---
