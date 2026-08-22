---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Freetogame Agentic Access
  operation_count: 3
  slug: freetogame-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- description: Browse and retrieve free-to-play game listings and details.
  name: FreeToGame Games API
  slug: freetogame-games-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: FreeToGame Games API
  slug: open-freetogame-games-api
- collection_type: open
  name: FreeToGame API
  slug: open-freetogame
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/freetogame-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/freetogame-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FreeToGame
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/freetogame
- group: company
  title: ''
  type: Website
  url: https://www.freetogame.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.freetogame.com/api-doc
created: '2025-02-08'
description: FreeToGame is a platform that offers a wide selection of free-to-play online games for gamers to enjoy.
finops:
- name: Freetogame Finops
  service_category: API
  slug: freetogame-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/freetogame.png
layout: provider
modified: '2026-05-19'
name: FreeToGame
nav: Providers
network: true
overview: 'FreeToGame publishes 1 API on the [APIs.io](https://apis.io/) network: Games API. Tagged areas include Games and Gaming.


  FreeToGame''s developer surface includes documentation and 5 more developer resources.'
plans:
- name: Freetogame Plans Pricing
  plan_count: 3
  slug: freetogame-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Freetogame Rate Limits
  slug: freetogame-rate-limits
score:
  band: emerging
  composite: 21.4
  delta: -4.2
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 52.4
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 25.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/freetogame/refs/heads/main/screenshots/freetogame-2026-06-20T181535.png
security:
- kind: domain-security
  name: Freetogame Domain Security
  slug: freetogame-domain-security
  summary_line: TLSv1.3 · DMARC
slug: freetogame
tags:
- Games
- Gaming
website: https://www.freetogame.com/
---
