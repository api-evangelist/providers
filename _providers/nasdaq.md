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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'Real-time Nasdaq market data delivered over Apache Kafka (TLS) with SASL/OAUTHBEARER authentication against a Keycloak pro-realm token endpoint. Topics documented in the NCDS Java and Python SDKs: GID'
  name: Nasdaq Cloud Data Service (NCDS) — Kafka Streams
  slug: nasdaq-cloud-data-service-ncds-kafka-streams
artifact_total: 4
asyncapis:
- description: AsyncAPI 2.6 description of the Nasdaq Cloud Data Service (NCDS) public delivery surface. NCDS delivers real-time exchange data over Apache Kafka (TLS) using SASL/OAUTHBEARER against a Keycloak `pro-r
  name: Nasdaq Cloud Data Service (NCDS) — Kafka Streams
  slug: nasdaq-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nasdaq-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Nasdaq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nasdaq
created: '2026-05-05'
description: Fortune 1000 company Nasdaq. Public real-time delivery is Apache Kafka via Nasdaq Cloud Data Service (NCDS); modeled here in AsyncAPI 2.6 with kafka bindings.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nasdaq.png
layout: provider
modified: '2026-05-29'
name: Nasdaq
nav: Providers
network: true
overview: 'Nasdaq publishes 1 API on the [APIs.io](https://apis.io/) network: Cloud Data Service (NCDS) — Kafka Streams. Tagged areas include Fortune 1000.


  The Nasdaq catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.'
random_paper: 2
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Nasdaq API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 4
  slug: nasdaq-asyncapi-spectral-rules
score:
  band: emerging
  composite: 20.3
  coverage:
    artifact_dirs: 4
    catalog_gap: 86.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 13.6
    contract_quality: 50.0
    developer_ergonomics: 7.1
    discoverability: 44.4
    governance: 13.6
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 20.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nasdaq/refs/heads/main/screenshots/nasdaq-2026-06-20T190000.png
security:
- kind: domain-security
  name: Nasdaq Domain Security
  slug: nasdaq-domain-security
  summary_line: DMARC
slug: nasdaq
tags:
- Fortune 1000
---
