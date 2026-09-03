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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 14.0
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://docs.poloniex.com
  baseurl_source: declared
  description: US based digital asset exchange
  name: Poloniex
  slug: poloniex
artifact_total: 4
asyncapis:
- description: AsyncAPI 2.6 description of the Poloniex public, private (spot) and futures (v3) WebSocket interfaces. All channels and message field names are derived from Poloniex's official Java and Python SDKs pu
  name: Poloniex WebSocket API
  slug: poloniex-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/poloniex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docs.poloniex.com
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: US based digital asset exchange
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/poloniex.png
layout: provider
modified: '2026-05-29'
name: Poloniex
nav: Providers
network: true
overview: 'Poloniex publishes 1 API on the [APIs.io](https://apis.io/) network: Poloniex. Tagged areas include Cryptocurrency and Public APIs.


  The Poloniex catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.'
random_paper: 17
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Poloniex API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: poloniex-asyncapi-spectral-rules
score:
  band: emerging
  composite: 18.8
  coverage:
    artifact_dirs: 4
    catalog_gap: 83.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 13.6
    contract_quality: 45.8
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 13.6
    operational_transparency: 0.0
  previous_composite: 18.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/poloniex/refs/heads/main/screenshots/poloniex-2026-06-20T191855.png
security:
- kind: domain-security
  name: Poloniex Domain Security
  slug: poloniex-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: poloniex
tags:
- Cryptocurrency
- Public APIs
website: https://docs.poloniex.com
---
