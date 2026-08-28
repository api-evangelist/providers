---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alpha-natural-resources-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.alphanr.com/
- group: operate
  title: ''
  type: Support
  url: https://www.alphanr.com/contact/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alpha-natural-resources-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/alpha-natural-resources-well-known.yml
created: '2024-01-01'
description: Alpha Natural Resources is a producer of metallurgical and thermal coal in the United States, mining and processing coal for steelmaking and electric power generation. The company does not offer public developer APIs, but participates in commodity trading data exchanges and supply chain integration with steel producers and utilities.
features:
- description: EDI and supply chain integration with steel producers and electric utilities for coal supply contract management and shipment tracking.
  name: Supply Chain Integration
- description: Participation in commodity trading data networks for metallurgical and thermal coal price discovery and contract settlement.
  name: Commodity Data Exchange
- description: Internal operational data systems for mine production, safety metrics, environmental compliance, and logistics management.
  name: Mining Operations Data
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alpha-natural-resources.png
integrations:
- description: Electronic data interchange with steel producers and utilities for purchase orders, advance ship notices, and invoices.
  name: EDI Networks
- description: Data integration with commodity trading systems for coal price indices and contract settlement.
  name: Commodity Trading Platforms
layout: provider
modified: '2026-06-20'
name: Alpha Natural Resources
nav: Providers
network: true
overview: 'Alpha Natural Resources is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Mining, Coal, Natural Resources, Energy, and Commodities.


  Alpha Natural Resources'' developer surface includes support and 4 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 5.0
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 5.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alpha-natural-resources/refs/heads/main/screenshots/alpha-natural-resources-2026-07-25T195753.png
security:
- kind: domain-security
  name: Alpha Natural Resources Domain Security
  slug: alpha-natural-resources-domain-security
  summary_line: no transport/DNS hardening detected
slug: alpha-natural-resources
tags:
- Mining
- Coal
- Natural Resources
- Energy
- Commodities
use_cases:
- description: Supply chain integration with integrated steel mills for metallurgical coal delivery scheduling, quality certificates, and logistics coordination.
  name: Steel Producer Integration
- description: Long-term thermal coal supply contract management with electric utilities including delivery scheduling and quality reporting.
  name: Utility Coal Supply
website: https://www.alphanr.com/
---
