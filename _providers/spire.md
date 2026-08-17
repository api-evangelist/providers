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
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.0
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Spire Agentic Access
  operation_count: 4
  slug: spire-agentic-access
  summary_line: 4 operations
api_count: 5
apis:
- description: The SPIRE Agent exposes the SPIFFE Workload API as a Unix domain socket, allowing workloads running on the same node to request their X.509-SVIDs and JWT-SVIDs without requiring any credentials. The W
  name: SPIRE Workload API
  slug: spire-workload-api
- description: The SPIRE Server exposes a gRPC API used by administrators and the SPIRE Agent to manage registration entries, node attestation, bundle federation, and server health. It allows creating and managing w
  name: SPIRE Server API
  slug: spire-server-api
- description: OpenID Connect discovery document endpoint that describes the OIDC provider configuration and supported capabilities.
  name: SPIRE Discovery API
  slug: spire-discovery-api
- description: Liveness and readiness health check endpoints for SPIRE Server and SPIRE Agent components, suitable for use as Kubernetes probes.
  name: SPIRE Health API
  slug: spire-health-api
- description: JSON Web Key Set endpoint that exposes public keys used to verify JWT-SVIDs issued by SPIRE.
  name: SPIRE Keys API
  slug: spire-keys-api
artifact_total: 30
asyncapis:
- description: 'The SPIRE Workload API is a gRPC streaming interface exposed by the SPIRE Agent on each node, through which workloads request and receive SPIFFE Verifiable Identity Documents (SVIDs) and trust bundle '
  name: SPIRE Workload API Events
  slug: spire-workload-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SPIRE Health Check Discovery API
  slug: open-spire-discovery-api
- collection_type: open
  name: SPIRE Check Discovery Health API
  slug: open-spire-health-api
- collection_type: open
  name: SPIRE Health Check API
  slug: open-spire-health
- collection_type: open
  name: SPIRE Health Check Discovery Keys API
  slug: open-spire-keys-api
- collection_type: open
  name: SPIRE OIDC Discovery Provider API
  slug: open-spire-oidc-discovery
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/spiffe/spire/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spire-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spire-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://spiffe.io/
- group: docs
  title: ''
  type: Documentation
  url: https://spiffe.io/docs/latest/
- group: start
  title: ''
  type: GettingStarted
  url: https://spiffe.io/docs/latest/try/getting-started-k8s/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spiffe
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/spiffe/spire
- group: operate
  title: ''
  type: Community
  url: https://spiffe.io/community/
- group: operate
  title: ''
  type: Slack
  url: https://slack.spiffe.io
- group: company
  title: ''
  type: Blog
  url: https://spiffe.io/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/spiffe/spire/blob/main/CHANGELOG.md
- group: auth
  title: ''
  type: Security
  url: https://github.com/spiffe/spire/blob/main/SECURITY.md
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/spiffe
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/spire-svid-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/spire-registration-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/spire-svid-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/spire-registration-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/spire-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/spire-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/spire-vocabulary.yml
created: '2025'
description: SPIRE (SPIFFE Runtime Environment) is the reference implementation of the SPIFFE standard, providing a toolchain for establishing trust between software systems across a wide variety of hosting platforms through automated attestation and workload identity distribution. SPIRE manages a certificate authority, performs node and workload attestation, and issues SVIDs to workloads through the SPIFFE Workload API.
examples:
- key_count: 2
  name: Spire Get Jwks Example
  slug: spire-get-jwks-example
- key_count: 2
  name: Spire Get Liveness Example
  slug: spire-get-liveness-example
- key_count: 2
  name: Spire Get Openid Configuration Example
  slug: spire-get-openid-configuration-example
- key_count: 2
  name: Spire Get Readiness Example
  slug: spire-get-readiness-example
finops:
- name: Spire Finops
  service_category: API
  slug: spire-finops
graphqls:
- description: Spire is a global maritime and aviation intelligence company using satellite data. The API covers vessel tracking (AIS), flight tracking (ADSB), weather intelligence, maritime trade analytics, and ves
  name: SPIRE GraphQL API
  slug: spire-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spire.png
json_schemas:
- name: SPIRE Registration Entries
  property_count: 0
  slug: spire-registration
- name: SPIRE SVID
  property_count: 5
  slug: spire-svid
json_structures:
- name: Spire Registration Structure
  property_count: 0
  slug: spire-registration-structure
- name: Spire Svid Structure
  property_count: 0
  slug: spire-svid-structure
jsonld:
- class_count: 0
  name: Spire Context
  property_count: 9
  slug: spire-context
layout: provider
modified: '2026-05-19'
name: SPIRE
nav: Providers
network: true
overview: 'SPIRE publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Workload API, Discovery API, Health API, and 1 more. Tagged areas include Authentication, Cloud Native, Graduated, Identity, and Security.


  The SPIRE catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  SPIRE''s developer surface includes documentation, getting-started guide, engineering blog, changelog, Stack Overflow tag, and 16 more developer resources.'
plans:
- name: Spire Plans Pricing
  plan_count: 3
  slug: spire-plans-pricing
random_paper: 100
rate_limits:
- limit_count: 5
  name: Spire Rate Limits
  slug: spire-rate-limits
rules:
- name: SPIRE API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 6
  slug: spire-asyncapi-spectral-rules
- name: SPIRE API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: spire-jsonschema-spectral-rules
- name: SPIRE API Rules
  rule_count: 9
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 5
  slug: spire-rules
score:
  band: developing
  composite: 45.5
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 69.2
    developer_ergonomics: 26.1
    discoverability: 72.2
    governance: 62.5
    operational_transparency: 39.5
  previous_composite: 45.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spire/refs/heads/main/screenshots/spire-2026-06-20T194318.png
security:
- kind: domain-security
  name: Spire Domain Security
  slug: spire-domain-security
  summary_line: TLSv1.3 · HSTS
slug: spire
tags:
- Authentication
- Cloud Native
- Graduated
- Identity
- Security
- Zero Trust
website: https://spiffe.io/
---
