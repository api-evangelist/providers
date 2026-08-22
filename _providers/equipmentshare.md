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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.6
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The T3OS developer platform's GraphQL ERP API (es-erp-api). A single GraphQL endpoint served over authenticated Bearer (user-delegated OAuth2) or X-API-Key (workspace-installed) access.
  name: T3OS ERP GraphQL API
  slug: t3os-erp-graphql-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://equipmentshare.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.t3os.ai
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/EquipmentShare/t3os-examples
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EquipmentShare
- group: operate
  title: ''
  type: ChangeLog
  url: https://updates.equipmentshare.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/equipmentshare-changelog.yml
- group: company
  title: ''
  type: Blog
  url: https://equipmentshare.com/resources
- group: operate
  title: ''
  type: Support
  url: https://www.equipmentshare.com/contact
- group: start
  title: ''
  type: Login
  url: https://app.t3os.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.equipmentshare.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.equipmentshare.com/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/equipmentshare-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/equipmentshare-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/equipmentshare-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/equipmentshare-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/equipmentshare-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/equipmentshare-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/equipmentshare-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/equipmentshare-llms.txt
created: '2026-07-17'
description: 'EquipmentShare is a construction technology and equipment-solutions company (founded 2015, headquartered in Columbia, Missouri) whose proprietary platform, T3, unifies telematics, rental and fleet operations across one of the largest mixed fleets in the US — 349,000+ connected assets across 380+ locations. Its developer surface, T3OS, exposes a GraphQL ERP API (es-erp-api) at api.equipmentshare.com with three first-party auth flows backed by Auth0: user-delegated OAuth 2.0 (Authorization Code + PKCE), workspace-installed API keys (X-API-Key), and sign-in-only OpenID Connect. T3 also offers an Outbound Developer API for structured fleet-data access (XML/JSON) and aggregates AEMP-compliant OEM telematics. Access is granted through the T3OS developer portal (app.t3os.ai) and app registration.'
image: https://cdn.prod.website-files.com/60cb2013a506c737cfeddf74/620bbc52f1de86cc1ff1e219_Company%20Page-100.jpg
layout: provider
modified: '2026-07-19'
name: EquipmentShare
nav: Providers
network: true
overview: 'EquipmentShare publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Construction Technology, Fleet Management, Telematics, and Equipment Rental.


  EquipmentShare''s developer surface includes documentation, changelog, engineering blog, support, authentication, and 15 more developer resources.'
random_paper: 3
scopes:
- name: Equipmentshare Scopes
  scope_count: 2
  slug: equipmentshare-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: emerging
  composite: 24.4
  delta: -1.5
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 39.9
    discoverability: 87.0
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 25.9
  provenance:
    conformance: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/equipmentshare/refs/heads/main/screenshots/equipmentshare-2026-07-25T213550.png
security:
- kind: authentication
  name: Equipmentshare Authentication
  slug: equipmentshare-authentication
  summary_line: oauth2/apiKey/openIdConnect · 3 schemes
- kind: domain-security
  name: Equipmentshare Domain Security
  slug: equipmentshare-domain-security
  summary_line: TLSv1.2 · DMARC
slug: equipmentshare
tags:
- Company
- Construction Technology
- Fleet Management
- Telematics
- Equipment Rental
- GraphQL
- Developer Platform
- OAuth
website: https://equipmentshare.com/
---
