---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Cloudrf Agentic Access
  operation_count: 29
  slug: cloudrf-agentic-access
  summary_line: 29 operations · 18 acting
api_count: 7
apis:
- description: 3D coverage and model upload operations.
  name: CloudRF 3D API
  slug: cloudrf-3d-api
- description: Account-level resources such as metrics.
  name: CloudRF Account API
  slug: cloudrf-account-api
- description: Analyse calculations including best-site, best-server, interference, merge, and signal location.
  name: CloudRF Analyse API
  slug: cloudrf-analyse-api
- description: Create coverage, path, multipoint, mesh, and HF calculations.
  name: CloudRF Create API
  slug: cloudrf-create-api
- description: Archive, export, clutter, and noise data management.
  name: CloudRF Manage API
  slug: cloudrf-manage-api
- description: Satellite coverage modeling.
  name: CloudRF Satellite API
  slug: cloudrf-satellite-api
- description: User and system templates.
  name: CloudRF Template API
  slug: cloudrf-template-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CloudRF 3D API
  slug: open-cloudrf-3d-api
- collection_type: open
  name: CloudRF 3D Account API
  slug: open-cloudrf-account-api
- collection_type: open
  name: CloudRF 3D Analyse API
  slug: open-cloudrf-analyse-api
- collection_type: open
  name: CloudRF 3D Create API
  slug: open-cloudrf-create-api
- collection_type: open
  name: CloudRF 3D Manage API
  slug: open-cloudrf-manage-api
- collection_type: open
  name: CloudRF 3D Satellite API
  slug: open-cloudrf-satellite-api
- collection_type: open
  name: CloudRF 3D Template API
  slug: open-cloudrf-template-api
- collection_type: open
  name: CloudRF API
  slug: open-cloudrf
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudrf-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudrf-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloudrf-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cloudrf
- group: company
  title: ''
  type: Website
  url: https://cloudrf.com/
- group: docs
  title: ''
  type: Documentation
  url: https://cloudrf.com/documentation/
- group: docs
  title: ''
  type: Documentation
  url: https://cloudrf.com/documentation/developer/
- group: docs
  title: ''
  type: APIReference
  url: https://cloudrf.com/documentation/developer/swagger-ui/
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/Cloud-RF/CloudRF-API-clients
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cloudrf.com/privacy
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/cloudrf-openapi.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/cloudrf-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/cloudrf-rules.yml
- group: company
  title: ''
  type: Blog
  url: https://cloudrf.com/feed/
created: '2024-07-02'
description: CloudRF is a radio frequency (RF) propagation, coverage modeling, and wireless network planning service. The HTTPS REST API at api.cloudrf.com offers point-to-multipoint coverage heatmaps, point-to-point path analysis, mesh networks, multisite, HF point-to-multipoint and point-to-point analysis, 3D coverage, satellite modeling, interference detection, geo-location of signals, archive and export of calculations, clutter and noise data management, account metrics, and reusable templates. Authentication is by API key passed as the `key` HTTP header.
finops:
- name: Cloudrf Finops
  service_category: API
  slug: cloudrf-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudrf.png
jsonld:
- class_count: 0
  name: Cloudrf Context
  property_count: 6
  slug: cloudrf-context
layout: provider
modified: '2026-05-19'
name: CloudRF
nav: Providers
network: true
overview: 'CloudRF publishes 7 APIs on the [APIs.io](https://apis.io/) network, including 3D API, Account API, Analyse API, and 4 more. Tagged areas include Coverage Modeling, HF Propagation, Mesh Network, Radio Frequency, and RF.


  The CloudRF catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CloudRF''s developer surface includes authentication, documentation, API reference, code examples, engineering blog, and 9 more developer resources.'
plans:
- name: Cloudrf Plans Pricing
  plan_count: 3
  slug: cloudrf-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Cloudrf Rate Limits
  slug: cloudrf-rate-limits
rules:
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: CloudRF API Rules
  rule_count: 10
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 6
  slug: cloudrf-rules
score:
  band: thin
  composite: 35.1
  delta: -0.6
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 45.5
    contract_quality: 60.5
    developer_ergonomics: 23.8
    discoverability: 64.8
    governance: 45.5
    operational_transparency: 7.9
  previous_composite: 35.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 23.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudrf/refs/heads/main/screenshots/cloudrf-2026-06-20T174617.png
security:
- kind: authentication
  name: Cloudrf Authentication
  slug: cloudrf-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Cloudrf Domain Security
  slug: cloudrf-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cloudrf
tags:
- Coverage Modeling
- HF Propagation
- Mesh Network
- Radio Frequency
- RF
- Satellite
- Signal Analysis
- Telecommunications
- Wireless Planning
website: https://cloudrf.com/
---
