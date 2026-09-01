---
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 12.9
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Single unauthenticated endpoint that validates a remotely hosted SVG for BIMI suitability (SVG Tiny P/S). Described by the provider's own llms.txt as "the unauthenticated SVG validation endpoint", con
  name: makeBIMI SVG Validation API
  slug: makebimi-validation-api
artifact_total: 1
common:
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/makebimi-llms.txt
- group: auth
  title: ''
  type: SecurityPolicy
  url: security/makebimi-security.txt
- group: company
  title: ''
  type: Website
  url: https://makebimi.com
- group: docs
  title: ''
  type: Documentation
  url: https://makebimi.com/standard
- group: operate
  title: ''
  type: Support
  url: https://veribimi.com/services/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://veribimi.com/privacy
created: '2026-08-21'
description: makeBIMI is a free web tool for preparing and validating brand logos for BIMI (Brand Indicators for Message Identification). It converts supported image inputs to SVG Tiny P/S, checks SVG suitability, audits a domain's DMARC configuration, and suggests a BIMI DNS TXT record. It does not issue certificates and does not guarantee mailbox-provider logo display. The public API is a single unauthenticated endpoint, GET /api/validate, for validating a remotely hosted SVG in an automated workflow. Operated alongside veriBIMI, an independent BIMI certificate-brokerage and implementation-support service, and DMARCSwiss, a Swiss-hosted DMARC monitoring service.
layout: provider
modified: '2026-08-21'
name: makeBIMI
nav: Providers
network: true
overview: 'makeBIMI publishes 1 API on the [APIs.io](https://apis.io/) network: SVG Validation API. Tagged areas include BIMI, DMARC, Email Authentication, SVG, and brand indicators.


  makeBIMI''s developer surface includes documentation, support, and 4 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 18.7
  coverage:
    artifact_dirs: 3
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 5.3
    commercial_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 26.7
    developer_ergonomics: 11.9
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 18.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
slug: makebimi
tags:
- BIMI
- DMARC
- Email Authentication
- SVG
- brand indicators
- SVG validation
website: https://makebimi.com
---
