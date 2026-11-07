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
  dimensions:
    agent_card: conformant
    agent_skills: false
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
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 34.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Crewofthecaptain Com Agentic Access
  operation_count: 7
  slug: crewofthecaptain-com-agentic-access
  summary_line: 7 operations · 6 acting
api_count: 1
apis:
- description: Format and checksum validation for IBAN, EU VAT, Polish NIP/REGON/PESEL and email, pay-per-call via x402.
  name: Crew of the Captain API
  slug: crew-of-the-captain-api
- baseURL: https://validate.crewofthecaptain.com
  baseurl_source: declared
  description: The Types API from Crew of the Captain — 1 operation(s) for types.
  name: Crew of the Captain Types API
  slug: crewofthecaptain-com-types-api
- baseURL: https://validate.crewofthecaptain.com
  baseurl_source: declared
  description: The validation API from Crew of the Captain — 6 operation(s) for validation.
  name: Crew of the Captain Validation API
  slug: crewofthecaptain-com-validation-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/crewofthecaptain-com/agentic-access/crewofthecaptain-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/crewofthecaptain-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/crewofthecaptain-com/rules/crewofthecaptain-com-rules.yml
  title: ''
  type: Spectral
  url: rules/crewofthecaptain-com-rules.yml
- group: design
  href: https://artifacts.apis.io/crewofthecaptain-com/json-ld/crewofthecaptain-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/crewofthecaptain-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/crewofthecaptain-com/vocabulary/crewofthecaptain-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/crewofthecaptain-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/crewofthecaptain-com/data-model/crewofthecaptain-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/crewofthecaptain-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/crewofthecaptain-com/errors/crewofthecaptain-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/crewofthecaptain-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/crewofthecaptain-com/conformance/crewofthecaptain-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/crewofthecaptain-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/crewofthecaptain-com/llms/crewofthecaptain-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crewofthecaptain-com-llms.txt
- group: other
  href: https://artifacts.apis.io/crewofthecaptain-com/a2a/crewofthecaptain-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/crewofthecaptain-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/crewofthecaptain-com/mcp/crewofthecaptain-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/crewofthecaptain-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/crewofthecaptain-com/well-known/crewofthecaptain-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/crewofthecaptain-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/crewofthecaptain-com/hosts/crewofthecaptain-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crewofthecaptain-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/crewofthecaptain-com/vendors/crewofthecaptain-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crewofthecaptain-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/crewofthecaptain-com/security/crewofthecaptain-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crewofthecaptain-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crewofthecaptain.com/
created: '2026-11-04'
description: Crew of the Captain is a small software house that designs and builds web applications, marketplace add‑ons, and creative 3D tools. They work in clear, checkable steps, delivering projects with a focus on automation and AI‑assisted tooling. Their services include fast maintainable web apps, integrations for platforms like Zendesk and Atlassian, and procedural generators for game and design pipelines, all crafted by a steady crew of developers.
jsonld:
- class_count: 1
  name: Crewofthecaptain Com Context
  property_count: 5
  slug: crewofthecaptain-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at validate.crewofthecaptain.com.
  name: Crew of the Captain MCP Server
  slug: crewofthecaptain-com-mcp-yml
modified: '2026-11-04'
name: Crew of the Captain
nav: Providers
network: true
overview: 'Crew of the Captain publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including Types API, Validation API, and 1 more. Tagged areas include Software House, Web Development, Marketplace Apps, Creative Tools, and Automation.


  The Crew of the Captain catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: Crew of the Captain API Rules
  rule_count: 41
  severity_counts:
    error: 32
    hint: 0
    info: 8
    warn: 1
  slug: crewofthecaptain-com-rules
score:
  band: emerging
  composite: 19.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 40.8
    catalog_earned_first_party: 0.0
    catalog_gap: 74.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 48.7
    developer_ergonomics: 0.0
    discoverability: 53.3
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Crewofthecaptain Com Domain Security
  slug: crewofthecaptain-com-domain-security
  summary_line: TLSv1.3
slug: crewofthecaptain-com
tags:
- Software House
- Web Development
- Marketplace Apps
- Creative Tools
- Automation
website: https://crewofthecaptain.com/
---
