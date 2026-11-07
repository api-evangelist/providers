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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: self
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Blbestate Com Agentic Access
  operation_count: 16
  slug: blbestate-com-agentic-access
  summary_line: 16 operations · 9 acting
api_count: 1
apis:
- baseURL: https://blbestate.com
  baseurl_source: declared
  description: The Agent API from SalesSwipe — 13 operation(s) for agent.
  name: SalesSwipe Agent API
  slug: blbestate-com-agent-api
- baseURL: https://blbestate.com
  baseurl_source: declared
  description: The Mcp API from SalesSwipe — 1 operation(s) for mcp.
  name: SalesSwipe MCP API
  slug: blbestate-com-mcp-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/blbestate-com/agentic-access/blbestate-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/blbestate-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/blbestate-com/rules/blbestate-com-rules.yml
  title: ''
  type: Spectral
  url: rules/blbestate-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/blbestate-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/blbestate-com/conventions/blbestate-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/blbestate-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/blbestate-com/conventions/blbestate-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/blbestate-com-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://blbestate.com/privacy
- group: design
  href: https://artifacts.apis.io/blbestate-com/errors/blbestate-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/blbestate-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/blbestate-com/conformance/blbestate-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blbestate-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/blbestate-com/llms/blbestate-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blbestate-com-llms.txt
- group: build
  href: https://artifacts.apis.io/blbestate-com/mcp/blbestate-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/blbestate-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/blbestate-com/mcp/blbestate-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/blbestate-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/blbestate-com/well-known/blbestate-com-tryacee-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/blbestate-com-tryacee-security.txt
- group: auth
  href: https://artifacts.apis.io/blbestate-com/well-known/blbestate-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/blbestate-com-security.txt
- group: auth
  href: https://artifacts.apis.io/blbestate-com/well-known/blbestate-com-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/blbestate-com-api-security.txt
- group: agent
  href: https://artifacts.apis.io/blbestate-com/well-known/blbestate-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blbestate-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/blbestate-com/hosts/blbestate-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blbestate-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/blbestate-com/vendors/blbestate-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blbestate-com-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.blbestate.com</code
- group: auth
  href: https://artifacts.apis.io/blbestate-com/security/blbestate-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/blbestate-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/blbestate-com/security/blbestate-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blbestate-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blbestate.com/
- group: docs
  title: ''
  type: Documentation
  url: https://blbestate.com/guides/
- group: docs
  title: ''
  type: APIReference
  url: https://api.blbestate.com
- group: start
  title: ''
  type: GettingStarted
  url: https://blbestate.com/developers
- group: operate
  title: ''
  type: Support
  url: https://blbestate.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blbestate.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blbestate.com/privacy
created: '2026-11-02'
description: SalesSwipe provides a platform that allows real estate professionals to quickly assess property deals by swiping through listings. Users can view property details, owner contact information, and key metrics, enabling faster decision-making. The service offers free initial access, integrates with various tools, and supports both web and mobile applications, aiming to streamline the deal evaluation process for agents and investors.
image: https://blbestate.com/og-card.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at blbestate.com.
  name: SalesSwipe MCP Server
  slug: blbestate-com-mcp-yml
modified: '2026-11-02'
name: SalesSwipe
nav: Providers
network: true
overview: 'SalesSwipe publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Agent API and MCP API. Tagged areas include Real Estate, Platform, Property, Sales, and Software-as-a-Service.


  The SalesSwipe catalog on APIs.io includes 1 Spectral governance ruleset.


  SalesSwipe''s developer surface includes documentation, API reference, getting-started guide, support, and 23 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 77
  extends:
  - spectral:oas
  name: SalesSwipe API Rules
  rule_count: 36
  severity_counts:
    error: 31
    hint: 0
    info: 3
    warn: 2
  slug: blbestate-com-rules
score:
  band: thin
  composite: 26.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 39.8
    developer_ergonomics: 23.2
    discoverability: 65.0
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
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
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blbestate Com Domain Security
  slug: blbestate-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Blbestate Com Vulnerability Disclosure
  slug: blbestate-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: blbestate-com-create-and-complete-ucp-checkout
  slug: blbestate-com-create-and-complete-ucp-checkout
slug: blbestate-com
tags:
- Real Estate
- Platform
- Property
- Sales
- Software-as-a-Service
website: https://blbestate.com/
---
