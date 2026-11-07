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
  score: 25.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Access Control Cost provides an MCP JSON-RPC API for enquiry tools.
  name: Access Control Cost API
  slug: access-control-cost-api
- baseURL: https://accesscontrolcost.co.uk
  baseurl_source: declared
  description: 'Access Control Cost (https://accesscontrolcost.co.uk/): the site''s own MCP server, served from its domain. Access control system costs turn on door count, reader type, standalone or cloud, door hardwa'
  name: Access Control Cost API API
  slug: access-control-cost-api-api
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/accesscontrolcost-co-uk/rules/accesscontrolcost-co-uk-rules.yml
  title: ''
  type: Spectral
  url: rules/accesscontrolcost-co-uk-rules.yml
- group: design
  href: https://artifacts.apis.io/accesscontrolcost-co-uk/vocabulary/accesscontrolcost-co-uk-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/accesscontrolcost-co-uk-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/accesscontrolcost-co-uk/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://accesscontrolcost.co.uk/terms
- group: design
  href: https://artifacts.apis.io/accesscontrolcost-co-uk/errors/accesscontrolcost-co-uk-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/accesscontrolcost-co-uk-problem-types.yml
- group: design
  href: https://artifacts.apis.io/accesscontrolcost-co-uk/conformance/accesscontrolcost-co-uk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/accesscontrolcost-co-uk-conformance.yml
- group: agent
  href: https://artifacts.apis.io/accesscontrolcost-co-uk/llms/accesscontrolcost-co-uk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/accesscontrolcost-co-uk-llms.txt
- group: agent
  href: https://artifacts.apis.io/accesscontrolcost-co-uk/mcp/accesscontrolcost-co-uk-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/accesscontrolcost-co-uk-mcp.yml
- group: auth
  href: https://artifacts.apis.io/accesscontrolcost-co-uk/well-known/accesscontrolcost-co-uk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/accesscontrolcost-co-uk-security.txt
- group: agent
  href: https://artifacts.apis.io/accesscontrolcost-co-uk/well-known/accesscontrolcost-co-uk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/accesscontrolcost-co-uk-well-known.yml
- group: other
  href: https://artifacts.apis.io/accesscontrolcost-co-uk/hosts/accesscontrolcost-co-uk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/accesscontrolcost-co-uk-hosts.yml
- group: other
  href: https://artifacts.apis.io/accesscontrolcost-co-uk/vendors/accesscontrolcost-co-uk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/accesscontrolcost-co-uk-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://accesscontrolcost.co.uk/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://accesscontrolcost.co.uk/privacy/
- group: auth
  href: https://artifacts.apis.io/accesscontrolcost-co-uk/security/accesscontrolcost-co-uk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/accesscontrolcost-co-uk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/accesscontrolcost-co-uk/security/accesscontrolcost-co-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/accesscontrolcost-co-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://accesscontrolcost.co.uk/
created: '2026-10-31'
description: Access Control Cost provides detailed information on the pricing of commercial access control systems in the UK. The site offers free quotes from installers, guides on various credential types such as fob, card, mobile, and biometric, and sector-specific advice for schools and fire safety integration. It also publishes data tables with methodology and sources, helping users compare costs and understand factors influencing prices.
image: https://accesscontrolcost.co.uk/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at accesscontrolcost.co-uk.
  name: Access Control Cost MCP Server
  slug: accesscontrolcost-co-uk-mcp-yml
modified: '2026-10-31'
name: Access Control Cost
nav: Providers
network: true
overview: 'Access Control Cost publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API API, and 1 more. Tagged areas include Access Control, Pricing, Guides, United Kingdom, and Security.


  The Access Control Cost catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Access Control Cost API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: accesscontrolcost-co-uk-rules
score:
  band: emerging
  composite: 25.2
  coverage:
    artifact_dirs: 14
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 48.4
    developer_ergonomics: 1.8
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
  previous_composite: 28.6
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Accesscontrolcost Co Uk Domain Security
  slug: accesscontrolcost-co-uk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Accesscontrolcost Co Uk Vulnerability Disclosure
  slug: accesscontrolcost-co-uk-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: enquiry
  slug: accesscontrolcost-co-uk-enquiry
slug: accesscontrolcost-co-uk
tags:
- Access Control
- Pricing
- Guides
- United Kingdom
- Security
website: https://accesscontrolcost.co.uk/
---
