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
    auth_clarity: false
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Provides calculators for California court deadlines via a web interface; no public machine-readable API contract is available.
  name: CalCourtDeadlines API
  slug: calcourtdeadlines-api
- description: 'CalCourtDeadlines.com API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: CalCourtDeadlines.com API
  slug: calcourtdeadlines-com-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/calcourtdeadlines-com/rules/calcourtdeadlines-com-rules.yml
  title: ''
  type: Spectral
  url: rules/calcourtdeadlines-com-rules.yml
- group: design
  href: https://artifacts.apis.io/calcourtdeadlines-com/vocabulary/calcourtdeadlines-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/calcourtdeadlines-com-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/calcourtdeadlines-com/changelog/calcourtdeadlines-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/calcourtdeadlines-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/calcourtdeadlines-com/conformance/calcourtdeadlines-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/calcourtdeadlines-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/calcourtdeadlines-com/llms/calcourtdeadlines-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/calcourtdeadlines-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/calcourtdeadlines-com/mcp/calcourtdeadlines-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/calcourtdeadlines-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/calcourtdeadlines-com/hosts/calcourtdeadlines-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/calcourtdeadlines-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/calcourtdeadlines-com/vendors/calcourtdeadlines-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/calcourtdeadlines-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://calcourtdeadlines.com/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://calcourtdeadlines.com/changelog
- group: auth
  href: https://artifacts.apis.io/calcourtdeadlines-com/security/calcourtdeadlines-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/calcourtdeadlines-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://calcourtdeadlines.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://calcourtdeadlines.com/privacy
- group: company
  title: ''
  type: About
  url: https://calcourtdeadlines.com/about
coverage:
  checked: '2026-11-03'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found despite public documentation pages.
  evidence:
  - status: 405
    url: https://calcourtdeadlines.com/api/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: CalCourtDeadlines.com provides free California court deadline calculators for discovery responses, trial chain, motions, and other procedural dates. The site offers over 70 verified rules, CCP citations, and applies court holidays automatically, requiring no login.
image: https://calcourtdeadlines.com/opengraph-image
layout: provider
mcp_servers:
- description: Remote MCP server at calcourtdeadlines.com.
  name: CalCourtDeadlines.com MCP Server
  slug: calcourtdeadlines-com-mcp-yml
modified: '2026-11-03'
name: CalCourtDeadlines.com
nav: Providers
network: true
overview: 'CalCourtDeadlines.com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Legal Tech, California, Court, Deadlines, and Free Tools.


  The CalCourtDeadlines.com catalog on APIs.io includes 1 Spectral governance ruleset.


  CalCourtDeadlines.com''s developer surface includes changelog and 13 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 61
  extends:
  - spectral:oas
  name: CalCourtDeadlines.com API Rules
  rule_count: 20
  severity_counts:
    error: 18
    hint: 0
    info: 1
    warn: 1
  slug: calcourtdeadlines-com-rules
score:
  band: emerging
  composite: 13.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 11.8
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 0.0
    discoverability: 56.7
    operational_transparency: 7.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Calcourtdeadlines Com Domain Security
  slug: calcourtdeadlines-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: calcourtdeadlines-com
tags:
- Legal Tech
- California
- Court
- Deadlines
- Free Tools
website: https://calcourtdeadlines.com/
---
