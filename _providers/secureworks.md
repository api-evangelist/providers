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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.2
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Secureworks Agentic Access
  operation_count: 3
  slug: secureworks-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 3
apis:
- description: The Authentication API from Secureworks — 1 operation(s) for authentication.
  name: Secureworks Authentication API
  slug: secureworks-authentication-api
- description: The GraphQL API from Secureworks — 1 operation(s) for graphql.
  name: Secureworks GraphQL API
  slug: secureworks-graphql-api
- description: The System API from Secureworks — 1 operation(s) for system.
  name: Secureworks System API
  slug: secureworks-system-api
artifact_total: 17
collections:
- collection_type: open
  name: Secureworks Taegis XDR API
  slug: open-secureworks-taegis-xdr
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/secureworks-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/secureworks-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/secureworks-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/secureworks
- group: company
  title: ''
  type: Website
  url: https://www.secureworks.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.taegis.secureworks.com/apis/using_xdr_apis/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.taegis.secureworks.com/apis/api_authenticate/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/secureworks
- group: build
  title: ''
  type: SDKs
  url: https://github.com/secureworks/taegis-sdk-python
- group: docs
  title: ''
  type: Documentation
  url: https://us2.vdr.secureworks.com/api/v2/spec
- group: company
  title: ''
  type: Blog
  url: https://www.secureworks.com/blog/show-me-the-apis
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/secureworks-alert-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/secureworks-investigation-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/secureworks-context.jsonld
- group: build
  title: ''
  type: Examples
  url: examples/secureworks-query-alerts-example.json
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/secureworks-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/secureworks-vocabulary.yml
created: '2026-05-02'
description: Secureworks is a cybersecurity company that provides the Taegis XDR (Extended Detection and Response) platform, offering threat detection, investigation, and response capabilities backed by 20 years of security intelligence. Taegis ingests and correlates telemetry across endpoints, network, cloud, and identity sources to detect threats and automate response workflows. The Taegis XDR API exposes GraphQL APIs for alerts, investigations, endpoint assets, identities, threat intelligence, connectors, collectors, playbooks, and users, with OAuth2 client credentials authentication and multi-region deployment support.
examples:
- key_count: 2
  name: Secureworks Query Alerts Example
  slug: secureworks-query-alerts-example
finops:
- name: Secureworks Finops
  service_category: API
  slug: secureworks-finops
graphqls:
- description: 'The Secureworks Taegis XDR API provides GraphQL-based programmatic access to the Taegis extended detection and response platform. The API supports alerts, investigations, endpoint assets, identities, '
  name: Secureworks GraphQL API
  slug: secureworks-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/secureworks.png
json_schemas:
- name: Secureworks Taegis Alert
  property_count: 10
  slug: secureworks-alert
json_structures:
- name: Secureworks Investigation Structure
  property_count: 10
  slug: secureworks-investigation-structure
jsonld:
- class_count: 25
  name: Secureworks Context
  property_count: 3
  slug: secureworks-context
layout: provider
modified: '2026-05-19'
name: Secureworks
nav: Providers
network: true
overview: 'Secureworks publishes 3 APIs on the [APIs.io](https://apis.io/) network: Authentication API, GraphQL API, and System API. Tagged areas include Cybersecurity, XDR, Threat Detection, Security Operations, and Incident Response.


  The Secureworks catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Secureworks'' developer surface includes authentication, documentation, engineering blog, code examples, and 13 more developer resources.'
plans:
- name: Secureworks Plans Pricing
  plan_count: 3
  slug: secureworks-plans-pricing
random_paper: 73
rate_limits:
- limit_count: 5
  name: Secureworks Rate Limits
  slug: secureworks-rate-limits
rules:
- name: Secureworks API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: secureworks-jsonschema-spectral-rules
- name: Secureworks API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 2
    warn: 3
  slug: secureworks-rules
score:
  band: developing
  composite: 51.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 68.7
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 51.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/secureworks/refs/heads/main/screenshots/secureworks-2026-06-20T193632.png
security:
- kind: authentication
  name: Secureworks Authentication
  slug: secureworks-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Secureworks Domain Security
  slug: secureworks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: secureworks
tags:
- Cybersecurity
- XDR
- Threat Detection
- Security Operations
- Incident Response
- MDR
- Threat Intelligence
website: https://www.secureworks.com
---
