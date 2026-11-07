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
    error_semantics: false
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
  score: 12.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Furniture catalogue API exposing product browse, search and filter operations.
  name: Decor Depot API
  slug: decor-depot-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/decordepot-co-uk/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://decordepot.co.uk/terms
- group: design
  href: https://artifacts.apis.io/decordepot-co-uk/vocabulary/decordepot-co-uk-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/decordepot-co-uk-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/decordepot-co-uk/conformance/decordepot-co-uk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/decordepot-co-uk-conformance.yml
- group: agent
  href: https://artifacts.apis.io/decordepot-co-uk/llms/decordepot-co-uk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/decordepot-co-uk-llms.txt
- group: build
  href: https://artifacts.apis.io/decordepot-co-uk/mcp/decordepot-co-uk-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/decordepot-co-uk-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/decordepot-co-uk/mcp/decordepot-co-uk-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/decordepot-co-uk-mcp.yml
- group: auth
  href: https://artifacts.apis.io/decordepot-co-uk/well-known/decordepot-co-uk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/decordepot-co-uk-security.txt
- group: agent
  href: https://artifacts.apis.io/decordepot-co-uk/well-known/decordepot-co-uk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/decordepot-co-uk-well-known.yml
- group: other
  href: https://artifacts.apis.io/decordepot-co-uk/hosts/decordepot-co-uk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/decordepot-co-uk-hosts.yml
- group: other
  href: https://artifacts.apis.io/decordepot-co-uk/vendors/decordepot-co-uk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/decordepot-co-uk-vendors.yml
- group: auth
  href: https://artifacts.apis.io/decordepot-co-uk/authentication/decordepot-co-uk-authentication.yml
  title: ''
  type: Authentication
  url: authentication/decordepot-co-uk-authentication.yml
- group: auth
  href: https://artifacts.apis.io/decordepot-co-uk/security/decordepot-co-uk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/decordepot-co-uk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/decordepot-co-uk/security/decordepot-co-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/decordepot-co-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://decordepot.co.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://decordepot.co.uk/llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://decordepot.co.uk/feeds/products.json
- group: commercial
  title: ''
  type: TermsOfService
  url: https://decordepot.co.uk/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://decordepot.co.uk/legal/privacy
- group: other
  title: ''
  type: Imprint
  url: https://decordepot.co.uk/legal/imprint
created: '2026-11-05'
description: Decor Depot is a UK‑based online furniture retailer offering a curated catalogue of 145 products across categories such as bedroom, dining, garden, home and living room. The site provides detailed specifications, pricing in GBP including VAT, and integrates with merchant feeds for Google and other platforms. It operates under a legal entity disclosed on its imprint page and offers terms, privacy, returns policies, and an API‑style product feed for developers.
layout: provider
mcp_servers:
- description: Remote MCP server at decordepot.co.uk.
  name: Decor Depot MCP Server
  slug: decordepot-co-uk-mcp-yml
modified: '2026-11-05'
name: Decor Depot
nav: Providers
network: true
overview: 'Decor Depot is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Furniture, United Kingdom, and Retail.


  Decor Depot''s developer surface includes authentication, documentation, API reference, and 17 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 22.0
  coverage:
    artifact_dirs: 13
    catalog_earned: 36.3
    catalog_earned_first_party: 0.0
    catalog_gap: 78.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 8.3
    contract_quality: 0.0
    developer_ergonomics: 35.0
    discoverability: 61.7
    operational_transparency: 10.5
  provenance:
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Decordepot Co Uk Authentication
  slug: decordepot-co-uk-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Decordepot Co Uk Domain Security
  slug: decordepot-co-uk-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Decordepot Co Uk Vulnerability Disclosure
  slug: decordepot-co-uk-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: decordepot-co-uk
tags:
- Company
- E-Commerce
- Furniture
- United Kingdom
- Retail
website: https://decordepot.co.uk/
---
