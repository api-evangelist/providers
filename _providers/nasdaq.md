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
    asyncapi_events: true
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
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
random_paper: 65
rules:
- name: Nasdaq API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 4
  slug: nasdaq-asyncapi-spectral-rules
score:
  band: emerging
  composite: 23.8
  delta: 4.2
  facets:
    commercial_clarity: 0.0
    contract_quality: 51.6
    developer_ergonomics: 0.0
    discoverability: 44.4
    governance: 47.9
    operational_transparency: 5.3
  previous_composite: 19.6
  schema_version: 0.6
  scored_at: '2026-07-28'
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
