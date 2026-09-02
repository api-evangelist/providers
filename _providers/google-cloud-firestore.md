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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Google Cloud Firestore Agentic Access
  operation_count: 10
  slug: google-cloud-firestore-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 1
apis:
- description: Operations on Firestore databases
  name: Google Cloud Firestore Databases API
  slug: google-cloud-firestore-databases-api
- description: Operations on Firestore documents
  name: Google Cloud Firestore Documents API
  slug: google-cloud-firestore-documents-api
artifact_total: 19
collections:
- collection_type: postman
  name: Google Cloud Firestore Databases API
  slug: postman-google-cloud-firestore-databases-api
- collection_type: postman
  name: Google Cloud Firestore Databases Documents API
  slug: postman-google-cloud-firestore-documents-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Cloud Firestore API
  slug: open-cloud-firestore
- collection_type: open
  name: Google Cloud Firestore Databases API
  slug: open-google-cloud-firestore-databases-api
- collection_type: open
  name: Google Cloud Firestore Databases Documents API
  slug: open-google-cloud-firestore-documents-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-firestore/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-firestore-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-firestore-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-firestore-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-firestore-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-firestore-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleapis
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/firestore
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/firestore/docs/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/firestore/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/firestore/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/firestore/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloud.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/firestore/docs/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/google-cloud-firestore-context.jsonld
created: '2026-03-13'
description: Google Cloud Firestore is a flexible, scalable NoSQL cloud database for mobile, web, and server development. It keeps data in sync across client apps through real-time listeners and offers offline support for mobile and web, enabling responsive apps that work regardless of network latency or internet connectivity. Firestore supports ACID transactions, automatic multi-region data replication, and strong consistency guarantees.
finops:
- name: Google Cloud Firestore Finops
  service_category: API
  slug: google-cloud-firestore-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-firestore.png
json_schemas:
- name: Google Cloud Firestore Document
  property_count: 4
  slug: document
jsonld:
- class_count: 18
  name: Google Cloud Firestore Context
  property_count: 0
  slug: google-cloud-firestore-context
layout: provider
modified: '2026-05-19'
name: Google Cloud Firestore
nav: Providers
network: true
overview: 'Google Cloud Firestore publishes 2 APIs on the [APIs.io](https://apis.io/) network: Databases API and Documents API. Tagged areas include Database, Documents, Google Cloud, NoSQL, and Real-Time.


  The Google Cloud Firestore catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Firestore''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 11 more developer resources.'
plans:
- name: Google Cloud Firestore Plans Pricing
  plan_count: 3
  slug: google-cloud-firestore-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Google Cloud Firestore Rate Limits
  slug: google-cloud-firestore-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Cloud Firestore API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-firestore-jsonschema-spectral-rules
scopes:
- name: Google Cloud Firestore Scopes
  scope_count: 2
  slug: google-cloud-firestore-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 47.7
  coverage:
    artifact_dirs: 14
    catalog_gap: 51.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 9.8
    contract_quality: 65.0
    developer_ergonomics: 52.4
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 47.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-firestore/refs/heads/main/screenshots/google-cloud-firestore-2026-06-20T182112.png
security:
- kind: authentication
  name: Google Cloud Firestore Authentication
  slug: google-cloud-firestore-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Firestore Domain Security
  slug: google-cloud-firestore-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Firestore Vulnerability Disclosure
  slug: google-cloud-firestore-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-firestore
tags:
- Database
- Documents
- Google Cloud
- NoSQL
- Real-Time
website: https://cloud.google.com/firestore
---
