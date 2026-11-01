---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: near-conformant
    agent_skills: derived
    agentic_access: derived
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 13.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Energynorth Uk Agentic Access
  operation_count: 3
  slug: energynorth-uk-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- description: Public read‑only API for searching and retrieving Energy North guides.
  name: Energy North Guides API
  slug: energy-north-guides-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/energynorth-uk/agentic-access/energynorth-uk-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/energynorth-uk-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/energynorth-uk/rules/energynorth-uk-rules.yml
  title: ''
  type: Spectral
  url: rules/energynorth-uk-rules.yml
- group: design
  href: https://artifacts.apis.io/energynorth-uk/json-ld/energynorth-uk-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/energynorth-uk-context.jsonld
- group: design
  href: https://artifacts.apis.io/energynorth-uk/vocabulary/energynorth-uk-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/energynorth-uk-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/energynorth-uk/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/energynorth-uk/data-model/energynorth-uk-data-model.yml
  title: ''
  type: DataModel
  url: data-model/energynorth-uk-data-model.yml
- group: design
  href: https://artifacts.apis.io/energynorth-uk/errors/energynorth-uk-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/energynorth-uk-problem-types.yml
- group: design
  href: https://artifacts.apis.io/energynorth-uk/conformance/energynorth-uk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/energynorth-uk-conformance.yml
- group: other
  href: https://artifacts.apis.io/energynorth-uk/overlays/energynorth-uk-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/energynorth-uk-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/energynorth-uk/llms/energynorth-uk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/energynorth-uk-llms.txt
- group: other
  href: https://artifacts.apis.io/energynorth-uk/a2a/energynorth-uk-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/energynorth-uk-a2a.yml
- group: build
  href: https://artifacts.apis.io/energynorth-uk/mcp/energynorth-uk-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/energynorth-uk-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/energynorth-uk/mcp/energynorth-uk-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/energynorth-uk-mcp.yml
- group: agent
  href: https://artifacts.apis.io/energynorth-uk/well-known/energynorth-uk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/energynorth-uk-well-known.yml
- group: other
  href: https://artifacts.apis.io/energynorth-uk/hosts/energynorth-uk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/energynorth-uk-hosts.yml
- group: other
  href: https://artifacts.apis.io/energynorth-uk/vendors/energynorth-uk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/energynorth-uk-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://energynorth.uk/login
- group: auth
  href: https://artifacts.apis.io/energynorth-uk/security/energynorth-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/energynorth-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://energynorth.uk/
- group: commercial
  title: ''
  type: Pricing
  url: https://energynorth.uk/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://energynorth.uk/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://energynorth.uk/privacy
- group: company
  title: ''
  type: Blog
  url: https://energynorth.uk/blog/posts/
- group: company
  title: ''
  type: About
  url: https://energynorth.uk/about
- group: operate
  title: ''
  type: Contact
  url: https://energynorth.uk/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://energynorth.uk/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://energynorth.uk/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://energynorth.uk/privacy
- group: company
  title: ''
  type: Blog
  url: https://energynorth.uk/blog/posts/
- group: company
  title: ''
  type: About
  url: https://energynorth.uk/about
- group: operate
  title: ''
  type: Contact
  url: https://energynorth.uk/contact
created: '2026-10-19'
description: Energy North UK connects homeowners with verified local tradespeople such as electricians, plumbers, gas engineers, and builders across the United Kingdom. The platform offers free job posting, instant quotes, and a commission‑free marketplace, leveraging AI to match jobs with qualified professionals quickly and transparently.
image: https://energynorth.uk/images/og-default.png
jsonld:
- class_count: 3
  name: Energynorth Uk Context
  property_count: 11
  slug: energynorth-uk-context
layout: provider
mcp_servers:
- description: Remote MCP server at energynorth.uk.
  name: energynorth-uk MCP Server
  slug: energynorth-uk-mcp-yml
modified: '2026-10-19'
name: energynorth-uk
nav: Providers
network: true
overview: 'energynorth-uk is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Marketplace, Homeowners, Tradespeople, and United Kingdom.


  The energynorth-uk catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  energynorth-uk''s developer surface includes pricing, engineering blog, and 29 more developer resources.'
plans:
- name: Energynorth Uk Plans Pricing
  plan_count: 0
  slug: energynorth-uk-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: energynorth-uk API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: energynorth-uk-rules
score:
  band: emerging
  composite: 22.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 50.8
    catalog_earned_first_party: 0.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 10.7
    developer_ergonomics: 4.2
    discoverability: 65.0
    operational_transparency: 0.0
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
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 15.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Energynorth Uk Domain Security
  slug: energynorth-uk-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: search-guides
  slug: energynorth-uk-search-guides
slug: energynorth-uk
tags:
- Energy
- Marketplace
- Homeowners
- Tradespeople
- United Kingdom
website: https://energynorth.uk/
---
