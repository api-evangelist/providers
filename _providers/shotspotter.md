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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-08-03'
api_count: 2
apis:
- description: REST data APIs for ShotSpotter gunfire detection — incident data, CAD incident ID lookup, and ILS (Investigative Lead Summary) retrieval.
  name: ShotSpotter Data APIs
  slug: shotspotter-data-apis
- description: REST data APIs for SafePointe AI weapons detection — alert data and line-crossing data.
  name: SafePointe Data APIs
  slug: safepointe-data-apis
artifact_total: 5
asyncapis:
- description: ''
  name: Shotspotter Napi Webhooks
  slug: shotspotter-napi-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.soundthinking.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.soundthinking.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.soundthinking.com/api/overview
- group: auth
  title: ''
  type: Authentication
  url: https://docs.soundthinking.com/api/authentication
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/shotspotter-napi-webhooks.yml
- group: operate
  title: ''
  type: Support
  url: https://www.soundthinking.com/contact/support-and-training/support/
- group: company
  title: ''
  type: Blog
  url: https://www.soundthinking.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.soundthinking.com/privacy-policy/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/shotspotter-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shotspotter-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/shotspotter-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shotspotter-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.soundthinking.com
created: '2026-07-17'
description: 'ShotSpotter is the flagship acoustic gunshot detection service of SoundThinking, Inc. (Nasdaq: SSTI), the public safety technology company formerly named ShotSpotter, Inc. SoundThinking operates a portfolio of law-enforcement and security products including ShotSpotter gunfire detection, SafePointe AI weapons detection, PlateRanger license-plate recognition, CrimeTracer investigative search, CaseBuilder case management, and ResourceRouter patrol analytics. Developers integrate via the SoundThinking developer documentation at docs.soundthinking.com, which publishes REST data APIs for ShotSpotter (incident data, CAD incident ID, ILS) and SafePointe (alert data, line-crossing data), plus NAPI, a webhook/push notification interface that delivers real-time XML alert documents (ShotSpotter IALRT incident presentations and SafePointe SPALRT alerts) to a customer network endpoint, alongside an Applications IT Resource Guide.'
image: https://www.soundthinking.com/wp-content/themes/soundthinking/assets/images/soundthinking-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: shotspotter-mcp.yml
  slug: shotspotter-mcpyml
modified: '2026-07-21'
name: ShotSpotter (SoundThinking)
nav: Providers
network: true
overview: 'ShotSpotter (SoundThinking) publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Public Safety, Gunshot Detection, Law Enforcement, and Weapons Detection.


  The ShotSpotter (SoundThinking) catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ShotSpotter (SoundThinking)''s developer surface includes documentation, API reference, authentication, support, engineering blog, and 8 more developer resources.'
random_paper: 91
score:
  band: thin
  composite: 32.1
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 51.6
    developer_ergonomics: 43.5
    discoverability: 77.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 32.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 29.6
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: domain-security
  name: Shotspotter Domain Security
  slug: shotspotter-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shotspotter
tags:
- Company
- Public Safety
- Gunshot Detection
- Law Enforcement
- Weapons Detection
- Acoustic Sensors
- Government
- Security
- Webhooks
website: https://www.soundthinking.com
---
