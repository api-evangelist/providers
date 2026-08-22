---
access_model:
  confidence: high
  label: Enterprise · Requires approval
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - https://app.go-kelvin.com/api/docs
  - https://www.go-kelvin.com/demo-produit
  - https://www.go-kelvin.com/creer-un-compte-kelvin
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: REST API for kelvin's energy-renovation engine. Create a simulation from a latitude/longitude (and optionally a Base Adresse Nationale key), record the occupant's qualification profile, run kelvin's m
  name: kelvin API
  slug: kelvin-api
artifact_total: 9
collections:
- collection_type: open
  name: kelvin API
  slug: open-kelvin-api-v2
- collection_type: open
  name: kelvin API
  slug: open-kelvin-api
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/kelvin-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://go-kelvin.com
- group: company
  title: ''
  type: Blog
  url: https://go-kelvin.com/ressources
- group: start
  title: ''
  type: SignUp
  url: https://go-kelvin.com/creer-un-compte-kelvin
- group: start
  title: ''
  type: Login
  url: https://app.go-kelvin.com/users/sign_in
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://go-kelvin.com/gestion-des-donnees
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kelvin-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kelvin-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.go-kelvin.com/api/docs
- group: docs
  title: ''
  type: Documentation
  url: https://app.go-kelvin.com/api/docs
- group: docs
  title: ''
  type: APIReference
  url: https://app.go-kelvin.com/api/docs
- group: operate
  title: ''
  type: Support
  url: https://go-kelvin.com/demande-de-contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://go-kelvin.com/conditions-de-vente
- group: commercial
  title: ''
  type: LegalNotice
  url: https://go-kelvin.com/mentions-legales
- group: design
  title: ''
  type: Components
  url: components/kelvin-components.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/kelvin-plans-pricing.yml
created: '2026-07-17'
description: Kelvin (kelvin°) is a Paris-based startup, founded in 2023 and backed by Seedcamp, building an AI-powered commercial platform for the home energy-renovation industry in France. Its tools help RGE-certified artisans, renovation contractors, general contractors, CEE delegatees and trade platforms find and qualify renovation prospects, generate leads through embeddable address-based simulators, automatically compute energy-efficiency scenarios and government aids (MaPrimeRenov / CEE) with remaining customer cost, and assemble complete financing packages. The AI is trained by thermal engineers and architects and uses open data plus computer vision to assess buildings without a recent DPE. More than 4,000 artisans and sales reps use Kelvin to prospect, prepare appointments and quote work.
image: https://cdn.prod.website-files.com/6655caeb6e3835fd7ee50dd6/67a1271dde24f8ccdf843524_Kelvin-Wordmark.svg
layout: provider
mcp_servers:
- description: ''
  name: kelvin-mcp.yml
  slug: kelvin-mcpyml
modified: '2026-08-14'
name: Kelvin
nav: Providers
network: true
overview: 'Kelvin publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Energy Efficiency, Home Renovation, and Construction.


  Kelvin''s developer surface includes authentication, engineering blog, signup flow, documentation, API reference, support, and 10 more developer resources.'
plans:
- name: Kelvin Plans Pricing
  plan_count: 0
  slug: kelvin-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Kelvin Rate Limits
  slug: kelvin-rate-limits
scopes:
- name: Kelvin Scopes
  scope_count: 0
  slug: kelvin-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 44.3
  delta: 2.5
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 16.7
    contract_quality: 52.4
    developer_ergonomics: 45.2
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 41.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 50.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kelvin/refs/heads/main/screenshots/kelvin-2026-07-25T223602.png
security:
- kind: authentication
  name: Kelvin Authentication
  slug: kelvin-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Kelvin Domain Security
  slug: kelvin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kelvin
tags:
- Company
- Energy
- Energy Efficiency
- Home Renovation
- Construction
- Artificial Intelligence
- Lead Generation
- Sales Enablement
- France
- Sustainability
website: https://go-kelvin.com
---
