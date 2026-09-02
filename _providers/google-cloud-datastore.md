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
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Google Cloud Datastore Agentic Access
  operation_count: 9
  slug: google-cloud-datastore-agentic-access
  summary_line: 9 operations · 8 acting
api_count: 1
apis:
- description: Stable REST API for Google Cloud Datastore / Firestore in Datastore mode. Provides entity lookup, commit, rollback, allocateIds, reserveIds, runQuery, and runAggregationQuery operations against a Goog
  name: Cloud Datastore API v1
  slug: rest-api-v1
- description: Beta REST API for Cloud Datastore exposing the same surface as v1 with newer features. Discovery document available for tooling and code generation.
  name: Cloud Datastore API v1beta3
  slug: rest-api-v1beta3
- description: The Projects API from Google Cloud Datastore — 9 operation(s) for projects.
  name: Google Cloud Datastore Projects API
  slug: google-cloud-datastore-projects-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cloud Datastore Projects API
  slug: open-google-cloud-datastore-projects-api
- collection_type: open
  name: Cloud Datastore API
  slug: open-google-cloud-datastore
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-datastore-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-datastore-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-datastore-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-datastore-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-datastore-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleapis
- group: company
  title: ''
  type: Website
  url: https://cloud.google.com/datastore
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/datastore/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/datastore/pricing
- group: start
  title: ''
  type: Signup
  url: https://console.cloud.google.com/freetrial
- group: start
  title: ''
  type: Console
  url: https://console.cloud.google.com/datastore
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com
- group: other
  title: ''
  type: Firestore (Successor)
  url: https://cloud.google.com/firestore/docs/firestore-or-datastore
created: '2026-05-11'
description: Google Cloud Datastore is a fully managed, schemaless, highly scalable NoSQL document database for web and mobile applications, originally based on Google's Bigtable / Megastore stack. The service has since been rebranded as Firestore in Datastore mode, which preserves the Datastore API and data model while running on Firestore's storage layer for strong consistency and higher throughput. The Cloud Datastore REST API provides entity lookups, queries (including GQL), transactions, and project operations against datastore.googleapis.com, authenticated with Google OAuth 2.0 / service-account credentials.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-datastore.png
layout: provider
modified: '2026-05-11'
name: Google Cloud Datastore
nav: Providers
network: true
overview: 'Google Cloud Datastore publishes 1 API on the [APIs.io](https://apis.io/) network: Projects API. Tagged areas include NoSQL, Database, Document Database, Google Cloud, and Firestore.


  Google Cloud Datastore''s developer surface includes authentication, documentation, pricing, signup flow, developer console, and 8 more developer resources.'
random_paper: 3
scopes:
- name: Google Cloud Datastore Scopes
  scope_count: 2
  slug: google-cloud-datastore-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 30.2
  coverage:
    artifact_dirs: 7
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 47.6
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 30.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-datastore/refs/heads/main/screenshots/google-cloud-datastore-2026-06-20T182103.png
security:
- kind: authentication
  name: Google Cloud Datastore Authentication
  slug: google-cloud-datastore-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Datastore Domain Security
  slug: google-cloud-datastore-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Datastore Vulnerability Disclosure
  slug: google-cloud-datastore-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-datastore
tags:
- NoSQL
- Database
- Document Database
- Google Cloud
- Firestore
- Managed Service
- Key-Value Store
website: https://cloud.google.com/datastore
---
