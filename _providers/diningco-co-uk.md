---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 11.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Diningco Co Uk Agentic Access
  operation_count: 1
  slug: diningco-co-uk-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: Tables catalog API for Dining Co, providing product browsing, search and filter via MCP tools.
  name: Dining Co API
  slug: dining-co-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: Security
  url: https://diningco.co.uk/terms
- group: agent
  href: https://artifacts.apis.io/diningco-co-uk/agentic-access/diningco-co-uk-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/diningco-co-uk-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/diningco-co-uk/rules/diningco-co-uk-rules.yml
  title: ''
  type: Spectral
  url: rules/diningco-co-uk-rules.yml
- group: design
  href: https://artifacts.apis.io/diningco-co-uk/vocabulary/diningco-co-uk-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/diningco-co-uk-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/diningco-co-uk/errors/diningco-co-uk-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/diningco-co-uk-problem-types.yml
- group: design
  href: https://artifacts.apis.io/diningco-co-uk/conformance/diningco-co-uk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/diningco-co-uk-conformance.yml
- group: agent
  href: https://artifacts.apis.io/diningco-co-uk/llms/diningco-co-uk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/diningco-co-uk-llms.txt
- group: build
  href: https://artifacts.apis.io/diningco-co-uk/mcp/diningco-co-uk-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/diningco-co-uk-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/diningco-co-uk/mcp/diningco-co-uk-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/diningco-co-uk-mcp.yml
- group: auth
  href: https://artifacts.apis.io/diningco-co-uk/well-known/diningco-co-uk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/diningco-co-uk-security.txt
- group: agent
  href: https://artifacts.apis.io/diningco-co-uk/well-known/diningco-co-uk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/diningco-co-uk-well-known.yml
- group: other
  href: https://artifacts.apis.io/diningco-co-uk/hosts/diningco-co-uk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/diningco-co-uk-hosts.yml
- group: other
  href: https://artifacts.apis.io/diningco-co-uk/vendors/diningco-co-uk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/diningco-co-uk-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://diningco.co.uk/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://diningco.co.uk/legal/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://diningco.co.uk/guides/how-to-choose-bar-tables
- group: auth
  href: https://artifacts.apis.io/diningco-co-uk/authentication/diningco-co-uk-authentication.yml
  title: ''
  type: Authentication
  url: authentication/diningco-co-uk-authentication.yml
- group: auth
  href: https://artifacts.apis.io/diningco-co-uk/security/diningco-co-uk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/diningco-co-uk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/diningco-co-uk/security/diningco-co-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/diningco-co-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://diningco.co.uk/
created: '2026-10-30'
description: DiningCo is a UK‑based online restaurant reservation and table‑booking platform that connects diners with a wide range of restaurants across the United Kingdom. The service allows users to search for venues, view menus, read reviews, and secure reservations in real time. DiningCo also offers restaurant partners tools to manage bookings, optimize seating, and integrate with point‑of‑sale systems. Founded to simplify the dining experience, the company provides a modern API for developers to access reservation data, restaurant listings, and customer insights, supporting both web and mobile applications.
layout: provider
mcp_servers:
- description: Remote MCP server at diningco.co.uk.
  name: diningco-co-uk MCP Server
  slug: diningco-co-uk-mcp-yml
modified: '2026-10-30'
name: diningco-co-uk
nav: Providers
network: true
overview: 'diningco-co-uk is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Restaurant, Reservations, API, and UK.


  The diningco-co-uk catalog on APIs.io includes 1 Spectral governance ruleset.


  diningco-co-uk''s developer surface includes documentation, authentication, and 18 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: diningco-co-uk API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: diningco-co-uk-rules
score:
  band: emerging
  composite: 21.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 40.8
    catalog_earned_first_party: 0.0
    catalog_gap: 74.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 61.7
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Diningco Co Uk Authentication
  slug: diningco-co-uk-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Diningco Co Uk Domain Security
  slug: diningco-co-uk-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Diningco Co Uk Vulnerability Disclosure
  slug: diningco-co-uk-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: diningco-co-uk
tags:
- Company
- Restaurant
- Reservations
- API
- UK
website: https://diningco.co.uk/
---
