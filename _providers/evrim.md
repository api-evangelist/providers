---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-07-28'
api_count: 18
apis:
- description: The answers API from Evrim — 2 operation(s) for answers.
  name: Evrim answers API
  slug: evrim-answers-api
- description: The blank API from Evrim — 2 operation(s) for blank.
  name: Evrim blank API
  slug: evrim-blank-api
- description: The bulk API from Evrim — 3 operation(s) for bulk.
  name: Evrim bulk API
  slug: evrim-bulk-api
- description: The collections API from Evrim — 2 operation(s) for collections.
  name: Evrim collections API
  slug: evrim-collections-api
- description: The compose API from Evrim — 1 operation(s) for compose.
  name: Evrim compose API
  slug: evrim-compose-api
- description: The costs API from Evrim — 8 operation(s) for costs.
  name: Evrim costs API
  slug: evrim-costs-api
- description: The created-fields API from Evrim — 3 operation(s) for created-fields.
  name: Evrim created-fields API
  slug: evrim-created-fields-api
- description: The extract API from Evrim — 8 operation(s) for extract.
  name: Evrim extract API
  slug: evrim-extract-api
- description: The fields API from Evrim — 3 operation(s) for fields.
  name: Evrim fields API
  slug: evrim-fields-api
- description: The health API from Evrim — 2 operation(s) for health.
  name: Evrim health API
  slug: evrim-health-api
- description: The prod API from Evrim — 1 operation(s) for prod.
  name: Evrim prod API
  slug: evrim-prod-api
- description: The profiles API from Evrim — 10 operation(s) for profiles.
  name: Evrim profiles API
  slug: evrim-profiles-api
- description: The prompt-templates API from Evrim — 2 operation(s) for prompt-templates.
  name: Evrim prompt-templates API
  slug: evrim-prompt-templates-api
- description: The questions API from Evrim — 1 operation(s) for questions.
  name: Evrim questions API
  slug: evrim-questions-api
- description: The snapshots API from Evrim — 2 operation(s) for snapshots.
  name: Evrim snapshots API
  slug: evrim-snapshots-api
- description: The tags API from Evrim — 4 operation(s) for tags.
  name: Evrim tags API
  slug: evrim-tags-api
- description: The templates API from Evrim — 3 operation(s) for templates.
  name: Evrim templates API
  slug: evrim-templates-api
- description: The transform API from Evrim — 1 operation(s) for transform.
  name: Evrim transform API
  slug: evrim-transform-api
artifact_total: 21
common:
- group: company
  title: ''
  type: Website
  url: https://www.evrim.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.evrim.ai
- group: company
  title: ''
  type: Blog
  url: https://www.evrim.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/evrimai
- group: auth
  title: ''
  type: Authentication
  url: authentication/evrim-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/evrim-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/evrim-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/evrim-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/evrim-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/evrim-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/evrim-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/evrim-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/evrim-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/evrim-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/evrim-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/evrim-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Evrim is the upstream signal layer for U.S. financial institutions, the defense industrial base, and federal agencies. The Evrim REST API ("Data when and how you want it.", v0.5.18) builds structured intelligence profiles from reusable templates and fields, captures point-in-time snapshots, and extracts values and relationships from source content. Every operation authenticates with a Knox-issued API token sent as an HTTP Bearer credential, and an official Stainless-generated Python SDK is published on PyPI.
image: https://www.evrim.ai/assets/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: evrim-mcp.yml
  slug: evrim-mcpyml
modified: '2026-07-19'
name: Evrim
nav: Providers
network: true
overview: 'Evrim publishes 18 APIs on the [APIs.io](https://apis.io/) network, including answers API, blank API, bulk API, and 15 more. Tagged areas include Company, Intelligence, Signals, Data Enrichment, and Profiles.


  Evrim''s developer surface includes documentation, engineering blog, authentication, changelog, and 13 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 28.5
  delta: -4.1
  facets:
    commercial_clarity: 0.0
    contract_quality: 37.3
    developer_ergonomics: 32.1
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 32.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/evrim/refs/heads/main/screenshots/evrim-2026-07-25T213819.png
security:
- kind: authentication
  name: Evrim Authentication
  slug: evrim-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Evrim Domain Security
  slug: evrim-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: evrim
tags:
- Company
- Intelligence
- Signals
- Data Enrichment
- Profiles
- Entity Resolution
- Defense
- Financial Services
- Government
website: https://www.evrim.ai/
---
