---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/energyaisolution-com/authentication/energyaisolution-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/energyaisolution-com-authentication.yml
- group: agent
  href: https://artifacts.apis.io/energyaisolution-com/llms/energyaisolution-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/energyaisolution-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/energyaisolution-com/mcp/energyaisolution-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/energyaisolution-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/energyaisolution-com/hosts/energyaisolution-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/energyaisolution-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/energyaisolution-com/security/energyaisolution-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/energyaisolution-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://energyaisolution.com/
- group: docs
  title: ''
  type: Documentation
  url: https://energyaisolution.com/guides
- group: docs
  title: ''
  type: APIReference
  url: https://energyaisolution.com/agents
- group: start
  title: ''
  type: GettingStarted
  url: https://energyaisolution.com/quote-review
- group: operate
  title: ''
  type: Support
  url: https://energyaisolution.com/installer-standards
- group: commercial
  title: ''
  type: TermsOfService
  url: https://energyaisolution.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://energyaisolution.com/privacy
coverage:
  checked: '2026-10-30'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found despite accessible documentation.
  evidence:
  - status: 404
    url: https://api.energyaisolution.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: EnergyAI provides AI‑driven decision support for residential energy choices, offering tools for solar, weatherization, EV charging, battery storage and heat pump planning. Users can obtain personalized quotes, incentive information, and evidence‑based recommendations, while agents can call the platform to retrieve estimates and compliance data. The service emphasizes transparency, human review options, and integrates with energy‑related data sources to help people and their agents make informed energy decisions.
image: https://energyaisolution.com/logo.png
layout: provider
mcp_servers:
- description: Remote MCP server at energyaisolution.com.
  name: energyaisolution-com MCP Server
  slug: energyaisolution-com-mcp-yml
modified: '2026-10-30'
name: energyaisolution-com
nav: Providers
network: true
overview: 'energyaisolution-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, AI, DecisionSupport, RenewableEnergy, and HomeImprovement.


  energyaisolution-com''s developer surface includes authentication, documentation, API reference, getting-started guide, support, and 7 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 18.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 48.3
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 15.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Energyaisolution Com Authentication
  slug: energyaisolution-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Energyaisolution Com Domain Security
  slug: energyaisolution-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: energyaisolution-com
tags:
- Energy
- AI
- DecisionSupport
- RenewableEnergy
- HomeImprovement
website: https://energyaisolution.com/
---
