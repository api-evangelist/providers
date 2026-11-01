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
  - sandbox
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://beemaps.com/api/developer
  baseurl_source: declared
  description: Devices, calibration, and query history.
  name: Hivemapper Account API
  slug: hivemapper-account-api
- baseURL: https://beemaps.com/api/developer
  baseurl_source: declared
  description: AI-detected driving event videos with synchronized sensor data.
  name: Hivemapper AI Events API
  slug: hivemapper-ai-events-api
- baseURL: https://beemaps.com/api/developer
  baseurl_source: declared
  description: On-demand incentivized mapping requests.
  name: Hivemapper Bursts API
  slug: hivemapper-bursts-api
- baseURL: https://beemaps.com/api/developer
  baseurl_source: declared
  description: Street-level dashcam imagery queries.
  name: Hivemapper Imagery API
  slug: hivemapper-imagery-api
- baseURL: https://beemaps.com/api/developer
  baseurl_source: declared
  description: ML-detected road objects and features.
  name: Hivemapper Map Features API
  slug: hivemapper-map-features-api
- baseURL: https://beemaps.com/api/developer
  baseurl_source: declared
  description: Camera calibration data
  name: Hivemapper Devices API
  slug: hivemapper-devices-api
artifact_total: 18
collections:
- collection_type: open
  name: Bee Maps (Hivemapper) Developer Account API
  slug: open-hivemapper-account-api
- collection_type: open
  name: Bee Maps (Hivemapper) Developer Account AI Events API
  slug: open-hivemapper-ai-events-api
- collection_type: open
  name: Bee Maps (Hivemapper) Developer Account Bursts API
  slug: open-hivemapper-bursts-api
- collection_type: open
  name: Bee Maps (Hivemapper) Developer Account Imagery API
  slug: open-hivemapper-imagery-api
- collection_type: open
  name: Bee Maps (Hivemapper) Developer Account Map Features API
  slug: open-hivemapper-map-features-api
common:
- group: commercial
  href: https://artifacts.apis.io/hivemapper/plans/hivemapper-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hivemapper-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/hivemapper/overlays/hivemapper-beemaps-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/hivemapper-beemaps-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/hivemapper/security/hivemapper-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hivemapper-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hivemapper.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://beemaps.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.beemaps.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.beemaps.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.beemaps.com/platform/road-intelligence-api
- group: commercial
  title: ''
  type: Pricing
  url: https://beemaps.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://beemaps.com/login
- group: company
  title: ''
  type: Blog
  url: https://beemaps.com/blog
- group: operate
  title: ''
  type: Support
  url: https://beemaps.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hivemapper.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hivemapper.com/privacy/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Hivemapper
- group: start
  href: https://artifacts.apis.io/hivemapper/sandbox/hivemapper-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/hivemapper-sandbox.yml
- group: build
  href: https://artifacts.apis.io/hivemapper/cli/hivemapper-cli.yml
  title: ''
  type: CLI
  url: cli/hivemapper-cli.yml
- group: agent
  href: https://artifacts.apis.io/hivemapper/mcp/hivemapper-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/hivemapper-mcp.yml
- group: agent
  href: https://artifacts.apis.io/hivemapper/llms/hivemapper-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hivemapper-llms.txt
- group: build
  href: https://artifacts.apis.io/hivemapper/packages/hivemapper-packages.yml
  title: ''
  type: Packages
  url: packages/hivemapper-packages.yml
- group: build
  href: https://artifacts.apis.io/hivemapper/packages/hivemapper-packages.yml
  title: ''
  type: SDKs
  url: packages/hivemapper-packages.yml
- group: agent
  href: https://artifacts.apis.io/hivemapper/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/hivemapper/well-known/hivemapper-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hivemapper-well-known.yml
- group: other
  title: ''
  type: X
  url: https://x.com/TryBeeMaps
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bee-maps
- group: operate
  title: ''
  type: Discord
  url: https://discord.com/invite/FRWMKyy5v2
created: '2026-07-17'
description: Hivemapper (Bee Maps) is a decentralized mapping network that turns a planetary-scale fleet of purpose-built "Bee" dashcams into fresh, structured, queryable street-level data. Contributors passively collect imagery while driving and earn HONEY tokens on Solana; the data is processed through on-device and cloud ML pipelines and delivered to developers as REST APIs. The Bee Maps Developer API offers a Street-Level Imagery API, a Map Features API (ML-detected signs, hydrants, lane lines and more), an AI Event Videos API (harsh braking, swerving, violations with synchronized sensor data), and Burst on-demand mapping, plus Edge AI for deploying custom ML workloads to cameras. Enterprise customers include HERE Technologies, Lyft, Mapbox, and Volkswagen. Billing is consumption-based (API credits plus per-view metering).
finops:
- has_sources: true
  method: derived
  name: Hivemapper Finops
  primary_unit: image
  service_category: ''
  slug: hivemapper-finops
  template: false
image: https://hivemapper.com/favicon.ico
layout: provider
mcp_servers:
- description: Bee Maps exposes an MCP Streamable HTTP endpoint on the Developer API that accepts JSON-RPC messages. Authentication is via the apiKey parameter (the same API key used for the REST Developer API).
  name: Hivemapper MCP Server
  slug: bee-maps
modified: '2026-07-19'
name: Hivemapper
nav: Providers
network: true
overview: 'Hivemapper publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, AI Events API, Bursts API, and 3 more. Tagged areas include Company, Logistics, Mapping, Geospatial, and Imagery.


  Hivemapper''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, engineering blog, support, and 19 more developer resources.'
plans:
- name: Hivemapper Plans Pricing
  plan_count: 6
  slug: hivemapper-plans-pricing
random_paper: 17
score:
  band: developing
  composite: 52.4
  coverage:
    artifact_dirs: 23
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 42.6
    developer_ergonomics: 80.4
    discoverability: 65.0
    operational_transparency: 5.3
  previous_composite: 51.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 14.3
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/hivemapper/hivemapper-2026-07-25T221306.png
security:
- kind: authentication
  name: Hivemapper Authentication
  slug: hivemapper-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Hivemapper Domain Security
  slug: hivemapper-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 2
skills:
- name: Pull road features and AI driving events
  slug: hivemapper-map-features-and-events
- name: Query street-level imagery for an area
  slug: hivemapper-query-imagery
slug: hivemapper
tags:
- Company
- Logistics
- Mapping
- Geospatial
- Imagery
- Location
- Street View
- Mobility
- Machine Learning
- Web3
website: https://hivemapper.com
---
