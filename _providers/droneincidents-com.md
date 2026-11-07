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
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: OpenAPI documented API for DroneLedger
  name: DroneLedger API
  slug: droneledger-api
- baseURL: https://droneincidents.com
  baseurl_source: declared
  description: 'Source-backed drone incident dossiers. Each dossier separates three claims: drone presence, impact and attribution, each with its own evidence state and supporting sources. ''reported'' means a source d'
  name: DroneLedger API V1 API
  slug: droneledger-api-v1-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/droneincidents-com/rules/droneincidents-com-rules.yml
  title: ''
  type: Spectral
  url: rules/droneincidents-com-rules.yml
- group: design
  href: https://artifacts.apis.io/droneincidents-com/conformance/droneincidents-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/droneincidents-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/droneincidents-com/errors/droneincidents-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/droneincidents-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/droneincidents-com/llms/droneincidents-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/droneincidents-com-llms.txt
- group: build
  href: https://artifacts.apis.io/droneincidents-com/mcp/droneincidents-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/droneincidents-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/droneincidents-com/mcp/droneincidents-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/droneincidents-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/droneincidents-com/hosts/droneincidents-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/droneincidents-com-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://droneincidents.com/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://droneincidents.com/newsroom/
- group: docs
  title: ''
  type: Documentation
  url: https://droneincidents.com/ecosystem/guides/fly/
- group: docs
  title: ''
  type: APIReference
  url: https://droneincidents.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/droneincidents-com/security/droneincidents-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/droneincidents-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://droneincidents.com/
created: '2026-11-05'
description: DroneLedger provides a source‑backed archive of drone incident dossiers worldwide, aggregating verified reports, impact assessments, and attribution data. The platform offers open data downloads, API access to incident records, and research tools to track trends, safety concerns, and regulatory implications across the global drone ecosystem.
image: https://droneincidents.com/assets/og-default.png
layout: provider
mcp_servers:
- description: Remote MCP server at droneincidents.com.
  name: DroneLedger MCP Server
  slug: droneincidents-com-mcp-yml
modified: '2026-11-05'
name: DroneLedger
nav: Providers
network: true
overview: 'DroneLedger publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API V1 API, and 1 more. Tagged areas include Drone, Data, Open Data, Aviation, and Incident.


  The DroneLedger catalog on APIs.io includes 1 Spectral governance ruleset.


  DroneLedger''s developer surface includes documentation, API reference, and 11 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 67
  extends:
  - spectral:oas
  name: DroneLedger API Rules
  rule_count: 26
  severity_counts:
    error: 24
    hint: 0
    info: 1
    warn: 1
  slug: droneincidents-com-rules
score:
  band: emerging
  composite: 23.1
  coverage:
    artifact_dirs: 13
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 34.3
    developer_ergonomics: 16.7
    discoverability: 66.7
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Droneincidents Com Domain Security
  slug: droneincidents-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: droneincidents-com
tags:
- Drone
- Data
- Open Data
- Aviation
- Incident
website: https://droneincidents.com/
---
