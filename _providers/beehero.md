---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Beehero Agentic Access
  operation_count: 12
  slug: beehero-agentic-access
  summary_line: 12 operations · 12 acting
api_count: 1
apis:
- baseURL: https://backend.beehero.io/external
  baseurl_source: declared
  description: Get audio files from sensors
  name: BeeHero Audio API
  slug: beehero-audio-api
- baseURL: https://backend.beehero.io/external
  baseurl_source: declared
  description: Login to BeeHero API
  name: BeeHero Auth API
  slug: beehero-auth-api
- baseURL: https://backend.beehero.io/external
  baseurl_source: declared
  description: Get gateways sample data
  name: BeeHero Gateways API
  slug: beehero-gateways-api
- baseURL: https://backend.beehero.io/external
  baseurl_source: declared
  description: Get sensors sample data
  name: BeeHero Sensors API
  slug: beehero-sensors-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: BeeHero API Documentation Audio API
  slug: open-beehero-audio-api
- collection_type: open
  name: BeeHero API Documentation Auth API
  slug: open-beehero-auth-api
- collection_type: open
  name: BeeHero API Documentation Gateways API
  slug: open-beehero-gateways-api
- collection_type: open
  name: BeeHero API Documentation Sensors API
  slug: open-beehero-sensors-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/beehero-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/beehero-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/beehero-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.beehero.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.beehero.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.beehero.io/
- group: company
  title: ''
  type: Blog
  url: https://www.beehero.io/the-buzz
- group: operate
  title: ''
  type: Support
  url: https://www.beehero.io/contact-us
- group: start
  title: ''
  type: Login
  url: https://accounts.beehero.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.beehero.io/legals
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.beehero.io/privacy-policy
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/beehero-openapi-original.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/beehero-api-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/beehero-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/beehero-tool-crosswalk.yml
- group: build
  title: ''
  type: Packages
  url: packages/beehero-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/beehero-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/beehero-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/beehero-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/beehero-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/beehero-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/beehero-conformance.yml
created: '2026-08-02'
description: BeeHero is a precision-pollination company that instruments commercial beehives and crop fields with low-cost IoT sensors, then turns the resulting acoustic, temperature, humidity and bee-activity data into pollination analytics for growers, beekeepers and agribusinesses. Founded in 2017 by Omer Davidi, Itai Kanot and Yuval Regev, with operations in California and Tel Aviv, it runs an in-hive Precision-Pollination-as-a-Service offering and an in-field Pollination Insight Platform (PIP) across crops including almonds, apples, avocados, blueberries, canola, cherries, carrot and onion seed, cucurbits and macadamia. BeeHero exposes a bearer-token REST API at backend.beehero.io/external — documented with Swagger UI at docs.beehero.io — for sensor samples, in-hive audio samples and gateway configuration, and publishes an official BeeHero MCP server to npm for agent access to its platform entities (groups, farms, orchards, yards, gateways, sensors, inspections, experiments).
image: https://cdn.prod.website-files.com/66e1eedeb9c7b4bebe0ed8f2/66e1fc3a9a94b85ef4c2e341_BeeHero_Logo_Horizontal_Black.png
layout: provider
mcp_servers:
- description: ''
  name: BeeHero MCP Server
  slug: beehero-mcp-server
modified: '2026-08-02'
name: BeeHero
nav: Providers
network: true
overview: 'BeeHero publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Audio API, Auth API, Gateways API, and 1 more. Tagged areas include Company, Agriculture, AgTech, Pollination, and beekeeping.


  BeeHero''s developer surface includes authentication, documentation, API reference, engineering blog, support, and 18 more developer resources.'
random_paper: 16
score:
  band: thin
  composite: 35.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 58.5
    developer_ergonomics: 37.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 35.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/beehero/refs/heads/main/screenshots/beehero-2026-08-07T162253.png
security:
- kind: authentication
  name: Beehero Authentication
  slug: beehero-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Beehero Domain Security
  slug: beehero-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: beehero
tags:
- Company
- Agriculture
- AgTech
- Pollination
- beekeeping
- Precision Agriculture
- IoT
- Sensors
- Environmental Data
- MCP
- agent-native
website: https://www.beehero.io/
---
