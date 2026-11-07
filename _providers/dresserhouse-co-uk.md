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
    agent_skills: derived
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 7.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Chests of drawers catalogue API
  name: Dresser House API
  slug: dresser-house-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/dresserhouse-co-uk/rules/dresserhouse-co-uk-rules.yml
  title: ''
  type: Spectral
  url: rules/dresserhouse-co-uk-rules.yml
- group: design
  href: https://artifacts.apis.io/dresserhouse-co-uk/vocabulary/dresserhouse-co-uk-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dresserhouse-co-uk-vocabulary.yml
- group: auth
  title: ''
  type: Security
  url: https://dresserhouse.co.uk/terms
- group: design
  href: https://artifacts.apis.io/dresserhouse-co-uk/conformance/dresserhouse-co-uk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dresserhouse-co-uk-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dresserhouse-co-uk/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/dresserhouse-co-uk/errors/dresserhouse-co-uk-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dresserhouse-co-uk-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/dresserhouse-co-uk/llms/dresserhouse-co-uk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dresserhouse-co-uk-llms.txt
- group: build
  href: https://artifacts.apis.io/dresserhouse-co-uk/mcp/dresserhouse-co-uk-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/dresserhouse-co-uk-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/dresserhouse-co-uk/mcp/dresserhouse-co-uk-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dresserhouse-co-uk-mcp.yml
- group: auth
  href: https://artifacts.apis.io/dresserhouse-co-uk/well-known/dresserhouse-co-uk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dresserhouse-co-uk-security.txt
- group: agent
  href: https://artifacts.apis.io/dresserhouse-co-uk/well-known/dresserhouse-co-uk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dresserhouse-co-uk-well-known.yml
- group: other
  href: https://artifacts.apis.io/dresserhouse-co-uk/hosts/dresserhouse-co-uk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dresserhouse-co-uk-hosts.yml
- group: other
  href: https://artifacts.apis.io/dresserhouse-co-uk/vendors/dresserhouse-co-uk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dresserhouse-co-uk-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://dresserhouse.co.uk/guides/how-to-choose-chests-of-drawers
- group: auth
  href: https://artifacts.apis.io/dresserhouse-co-uk/security/dresserhouse-co-uk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dresserhouse-co-uk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dresserhouse-co-uk/security/dresserhouse-co-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dresserhouse-co-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dresserhouse.co.uk/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dresserhouse.co.uk/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dresserhouse.co.uk/legal/privacy
created: '2026-11-05'
description: Dresser House is a UK‑based retailer specialising in chests of drawers, bedside chests, tallboys and related bedroom furniture. The online store offers a curated range of products from multiple brands, providing detailed specifications, pricing and stock information directly sourced from suppliers. Customers can browse categories, read buying guides such as “How to choose chests of drawers”, and purchase items with delivery across the United Kingdom. The site emphasizes comparison of features and values to help shoppers make informed decisions.
layout: provider
mcp_servers:
- description: Remote MCP server at dresserhouse.co.uk.
  name: Dresser House MCP Server
  slug: dresserhouse-co-uk-mcp-yml
modified: '2026-11-05'
name: Dresser House
nav: Providers
network: true
overview: 'Dresser House publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, Furniture, United Kingdom, and E-Commerce.


  The Dresser House catalog on APIs.io includes 1 Spectral governance ruleset.


  Dresser House''s developer surface includes documentation and 18 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Dresser House API Rules
  rule_count: 53
  severity_counts:
    error: 43
    hint: 0
    info: 4
    warn: 6
  slug: dresserhouse-co-uk-rules
score:
  band: emerging
  composite: 18.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 40.8
    catalog_earned_first_party: 0.0
    catalog_gap: 74.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 0.0
    developer_ergonomics: 11.3
    discoverability: 61.7
    operational_transparency: 10.5
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
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
  name: Dresserhouse Co Uk Domain Security
  slug: dresserhouse-co-uk-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Dresserhouse Co Uk Vulnerability Disclosure
  slug: dresserhouse-co-uk-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: dresserhouse-co-uk-browse-add-checkout
  slug: dresserhouse-co-uk-browse-add-checkout
slug: dresserhouse-co-uk
tags:
- Company
- Retail
- Furniture
- United Kingdom
- E-Commerce
website: https://dresserhouse.co.uk/
---
