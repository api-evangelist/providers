---
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Aquabyte Agentic Access
  operation_count: 19
  slug: aquabyte-agentic-access
  summary_line: 19 operations · 1 acting
api_count: 2
apis:
- description: Behaviour APIs
  name: Aquabyte Behaviour API
  slug: aquabyte-behaviour-api
- description: Biomass APIs
  name: Aquabyte Biomass API
  slug: aquabyte-biomass-api
- description: The Environmental API from Aquabyte — 2 operation(s) for environmental.
  name: Aquabyte Environmental API
  slug: aquabyte-environmental-api
- description: Lice APIs
  name: Aquabyte Lice API
  slug: aquabyte-lice-api
- description: The Sites API from Aquabyte — 2 operation(s) for sites.
  name: Aquabyte Sites API
  slug: aquabyte-sites-api
- description: Deprecated. Use v3.1 equivalents.
  name: Aquabyte V3.0 API
  slug: aquabyte-v3-0-api
- description: Welfare APIs
  name: Aquabyte Welfare API
  slug: aquabyte-welfare-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Aquabyte API Documentation Behaviour API
  slug: open-aquabyte-behaviour-api
- collection_type: open
  name: Aquabyte API Documentation Biomass API
  slug: open-aquabyte-biomass-api
- collection_type: open
  name: Aquabyte API Documentation Environmental API
  slug: open-aquabyte-environmental-api
- collection_type: open
  name: Aquabyte API Documentation Lice API
  slug: open-aquabyte-lice-api
- collection_type: open
  name: Aquabyte API Documentation Sites API
  slug: open-aquabyte-sites-api
- collection_type: open
  name: Aquabyte API Documentation V3.0 API
  slug: open-aquabyte-v3-0-api
- collection_type: open
  name: Aquabyte API Documentation Welfare API
  slug: open-aquabyte-welfare-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/aquabyte-capability-edges.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/aquabyte-harvest-planning.md
- group: other
  title: ''
  type: Overlay
  url: overlays/aquabyte-data-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.aquabyte.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://api.aquabyte.ai/v3/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.aquabyte.ai/v3/docs
- group: start
  title: ''
  type: Login
  url: https://app.aquabyte.ai/login
- group: operate
  title: ''
  type: Support
  url: https://www.aquabyte.ai/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aquabyte.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aquabyte.ai/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aquabyte-new
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aquabyte
- group: auth
  title: ''
  type: Authentication
  url: authentication/aquabyte-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aquabyte-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aquabyte-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aquabyte-domain-security.yml
created: '2026-08-06'
description: Aquabyte AS is a Norwegian-American aquaculture technology company, founded in 2017 with offices in Bergen (Laksevåg), Norway, San Francisco and Chile, that applies computer vision and machine learning to salmon and trout farming. Underwater cameras (Hydra 360, Hammerhead, Atlas) stream imagery into a cloud platform that produces biomass and weight estimation, sea-lice counting, welfare scoring, swim-speed and breathing-index behaviour metrics, environmental readings and feeding decision support, from smolt through harvest. Customers reach that data either through the Aquabyte customer portal at app.aquabyte.ai or through the Aquabyte Public API — a documented, API-key-authenticated REST service at api.aquabyte.ai/v3 whose OpenAPI 3.1 definition is served publicly at api.aquabyte.ai/openapi.json and rendered with ReDoc at /v3/docs.
image: https://www.aquabyte.ai/en/icon-illyi6.png
layout: provider
modified: '2026-08-06'
name: Aquabyte
nav: Providers
network: true
overview: 'Aquabyte publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Behaviour API, Biomass API, Environmental API, and 4 more. Tagged areas include Aquaculture, Fish Farming, Computer-Vision, Machine-Learning, and Biomass Estimation.


  Aquabyte''s developer surface includes documentation, API reference, support, authentication, and 12 more developer resources.'
random_paper: 20
rate_limits:
- limit_count: 1
  name: Aquabyte Rate Limits
  slug: aquabyte-rate-limits
score:
  band: thin
  composite: 36.0
  coverage:
    artifact_dirs: 17
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 47.9
    developer_ergonomics: 35.1
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 31.6
  previous_composite: 36.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aquabyte/refs/heads/main/screenshots/aquabyte-2026-08-07T161729.png
security:
- kind: authentication
  name: Aquabyte Authentication
  slug: aquabyte-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Aquabyte Domain Security
  slug: aquabyte-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aquabyte
tags:
- Aquaculture
- Fish Farming
- Computer-Vision
- Machine-Learning
- Biomass Estimation
- Sea Lice
- Fish Welfare
- Environmental Monitoring
- Agriculture Technology
- Norway
- Salmon
- Data
website: https://www.aquabyte.ai/
---
