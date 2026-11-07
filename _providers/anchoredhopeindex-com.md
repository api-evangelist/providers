---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
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
    agentic_access: derived
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Anchoredhopeindex Com Agentic Access
  operation_count: 2
  slug: anchoredhopeindex-com-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- description: Educational information only; not a clinical assessment or medical advice.
  name: Anchored Hope Index Decision API
  slug: anchored-hope-index-decision-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/anchoredhopeindex-com/agentic-access/anchoredhopeindex-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/anchoredhopeindex-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/anchoredhopeindex-com/rules/anchoredhopeindex-com-rules.yml
  title: ''
  type: Spectral
  url: rules/anchoredhopeindex-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/anchoredhopeindex-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/anchoredhopeindex-com/conformance/anchoredhopeindex-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/anchoredhopeindex-com-conformance.yml
- group: build
  href: https://artifacts.apis.io/anchoredhopeindex-com/mcp/anchoredhopeindex-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/anchoredhopeindex-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/anchoredhopeindex-com/mcp/anchoredhopeindex-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/anchoredhopeindex-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/anchoredhopeindex-com/hosts/anchoredhopeindex-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anchoredhopeindex-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/anchoredhopeindex-com/vendors/anchoredhopeindex-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anchoredhopeindex-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/anchoredhopeindex-com/security/anchoredhopeindex-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anchoredhopeindex-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anchoredhopeindex.com/
- group: docs
  title: ''
  type: Documentation
  url: https://anchoredhopeindex.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://anchoredhopeindex.com/openapi.json
- group: company
  title: ''
  type: Blog
  url: https://anchoredhopeindex.com/blog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://anchoredhopeindex.com/docs
created: '2026-11-01'
description: Anchored Hope Index™ is an educational resilience and future‑orientation assessment offered by Mental Resilience Counseling. It helps leaders, executives, and high‑performance professionals measure and improve meaning, future direction, agency, emotional endurance, motivation stability, support connection, and stress stability. Based on THE P.H.O.E.N.I.X.™ model, the tool delivers instant results via a brief online questionnaire.
image: https://anchoredhopeindex.com/images/logo.png
layout: provider
mcp_servers:
- description: Remote MCP server at anchoredhopeindex.com.
  name: Anchored Hope Index MCP Server
  slug: anchoredhopeindex-com-mcp-yml
modified: '2026-11-01'
name: Anchored Hope Index
nav: Providers
network: true
overview: 'Anchored Hope Index is listed with 1 API on the [APIs.io](https://apis.io/) network: Decision API. Tagged areas include Mental Health, Resilience, Assessment, Leadership, and Organizational Development.


  The Anchored Hope Index catalog on APIs.io includes 1 Spectral governance ruleset.


  Anchored Hope Index''s developer surface includes documentation, API reference, engineering blog, and 11 more developer resources.'
random_paper: 4
rate_limits:
- limit_count: 0
  name: Anchoredhopeindex Com Rate Limits
  slug: anchoredhopeindex-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Anchored Hope Index API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: anchoredhopeindex-com-rules
scopes:
- name: Anchoredhopeindex Com Scopes
  scope_count: 0
  slug: anchoredhopeindex-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 20.3
  coverage:
    artifact_dirs: 23
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 24.0
    developer_ergonomics: 20.7
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 23.2
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Anchoredhopeindex Com Authentication
  slug: anchoredhopeindex-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Anchoredhopeindex Com Domain Security
  slug: anchoredhopeindex-com-domain-security
  summary_line: TLSv1.3
skill_count: 2
skills:
- name: get-framework-metadata
  slug: anchoredhopeindex-com-get-framework-metadata
- name: run-anchored-hope-index
  slug: anchoredhopeindex-com-run-anchored-hope-index
slug: anchoredhopeindex-com
tags:
- Mental Health
- Resilience
- Assessment
- Leadership
- Organizational Development
website: https://anchoredhopeindex.com/
---
