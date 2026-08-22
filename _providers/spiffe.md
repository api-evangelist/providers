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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: na
    error_semantics: verified
    event_surface_described: derived
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.2
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Spiffe Agentic Access
  operation_count: 1
  slug: spiffe-agentic-access
  summary_line: 1 operation
api_count: 4
apis:
- description: The SPIFFE Workload API is a gRPC streaming interface through which workloads request and receive SPIFFE Verifiable Identity Documents (SVIDs) including X.509-SVIDs and JWT-SVIDs, as well as trust bun
  name: SPIFFE Workload API
  slug: spiffe-workload-api
- description: The SPIFFE X.509 SVID (SPIFFE Verifiable Identity Document) is a standard for encoding SPIFFE identities into X.509 certificates. The Subject Alternative Name field carries the SPIFFE ID URI, enabling
  name: SPIFFE X.509 SVID
  slug: spiffe-x509-svid-api
- description: The SPIFFE JWT SVID standard defines a format for encoding SPIFFE identities as JSON Web Tokens. JWT-SVIDs are used in scenarios where X.509 certificates are not practical, such as HTTP header-based a
  name: SPIFFE JWT SVID
  slug: spiffe-jwt-svid-api
- description: SPIFFE trust bundle retrieval operations for fetching root CA certificates used to validate SVIDs issued by a trust domain
  name: SPIFFE Bundle API
  slug: spiffe-bundle-api
artifact_total: 20
asyncapis:
- description: 'The SPIFFE Workload API is a gRPC streaming interface through which workloads request and receive SPIFFE Verifiable Identity Documents (SVIDs) and trust bundle updates. Workloads subscribe to the API '
  name: SPIFFE Workload API Events
  slug: spiffe-workload-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SPIFFE Federation Endpoint Bundle API
  slug: open-spiffe-bundle-api
- collection_type: open
  name: SPIFFE Federation Bundle Endpoint API
  slug: open-spiffe-federation
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/spiffe/spiffe/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spiffe-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spiffe-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spiffe-secure-production-identity-framework-for-everyone
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/spiffe-svid-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/spiffe-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/spiffe-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/spiffe-vocabulary.yml
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
  url: https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spiffe
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/spiffe/spiffe
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
- group: auth
  title: ''
  type: Security
  url: https://github.com/spiffe/spiffe/blob/main/SECURITY.md
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/spiffe
created: '2025'
description: Secure Production Identity Framework for Everyone (SPIFFE) is a set of open-source standards for securely identifying software systems in dynamic and heterogeneous environments through platform-agnostic, cryptographic identities. SPIFFE defines the SPIFFE ID URI format, the X.509 SVID and JWT SVID identity document formats, and the Workload API for issuing and rotating identities without secrets or passwords. SPIFFE is a graduated CNCF project.
examples:
- key_count: 2
  name: Spiffe Get Trust Bundle Example
  slug: spiffe-get-trust-bundle-example
finops:
- name: Spiffe Finops
  service_category: API
  slug: spiffe-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spiffe.png
json_schemas:
- name: SPIFFE Identity Documents
  property_count: 0
  slug: spiffe-svid
json_structures:
- name: Spiffe Svid Structure
  property_count: 0
  slug: spiffe-svid-structure
jsonld:
- class_count: 0
  name: Spiffe Context
  property_count: 7
  slug: spiffe-context
layout: provider
modified: '2026-05-19'
name: SPIFFE
nav: Providers
network: true
overview: 'SPIFFE publishes 2 APIs on the [APIs.io](https://apis.io/) network: Workload API and Bundle API. Tagged areas include Authentication, Cloud Native, Graduated, Identity, and Security.


  The SPIFFE catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  SPIFFE''s developer surface includes documentation, getting-started guide, engineering blog, Stack Overflow tag, and 14 more developer resources.'
plans:
- name: Spiffe Plans Pricing
  plan_count: 3
  slug: spiffe-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Spiffe Rate Limits
  slug: spiffe-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: SPIFFE API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 6
  slug: spiffe-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: SPIFFE API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: spiffe-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: SPIFFE API Rules
  rule_count: 7
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 3
  slug: spiffe-rules
score:
  band: thin
  composite: 32.1
  delta: -10.1
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 26.5
    contract_quality: 60.5
    developer_ergonomics: 26.2
    discoverability: 72.2
    governance: 26.5
    operational_transparency: 10.5
  previous_composite: 42.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/spiffe/refs/heads/main/screenshots/spiffe-2026-06-20T194311.png
security:
- kind: domain-security
  name: Spiffe Domain Security
  slug: spiffe-domain-security
  summary_line: TLSv1.3 · HSTS
slug: spiffe
tags:
- Authentication
- Cloud Native
- Graduated
- Identity
- Security
- Zero Trust
website: https://spiffe.io/
---
