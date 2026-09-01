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
- acting_count: 3
  human_in_the_loop: 0
  name: Google Distributed Cloud Agentic Access
  operation_count: 7
  slug: google-distributed-cloud-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 1
apis:
- description: The GDC Hardware Management API provides programmatic access to manage hardware lifecycle for Google Distributed Cloud deployments. Developers can use the API to track hardware orders, manage hardware
  name: GDC Hardware Management API
  slug: gdc-hardware-management-api
- description: Operations for managing edge networks
  name: Google Distributed Cloud Networks API
  slug: google-distributed-cloud-networks-api
- description: Operations for managing edge routers
  name: Google Distributed Cloud Routers API
  slug: google-distributed-cloud-routers-api
- description: Operations for managing subnets within edge networks
  name: Google Distributed Cloud Subnets API
  slug: google-distributed-cloud-subnets-api
- description: Operations for listing available edge zones
  name: Google Distributed Cloud Zones API
  slug: google-distributed-cloud-zones-api
artifact_total: 27
collections:
- collection_type: postman
  name: Google Distributed Cloud Edge Network Networks API
  slug: postman-google-distributed-cloud-networks-api
- collection_type: postman
  name: Google Distributed Cloud Edge Network Networks Routers API
  slug: postman-google-distributed-cloud-routers-api
- collection_type: postman
  name: Google Distributed Cloud Edge Network Networks Subnets API
  slug: postman-google-distributed-cloud-subnets-api
- collection_type: postman
  name: Google Distributed Cloud Edge Network Networks Zones API
  slug: postman-google-distributed-cloud-zones-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Distributed Cloud Edge Network API
  slug: open-distributed-cloud-edge-network-api
- collection_type: open
  name: Google Distributed Cloud Edge Network Networks API
  slug: open-google-distributed-cloud-networks-api
- collection_type: open
  name: Google Distributed Cloud Edge Network Networks Routers API
  slug: open-google-distributed-cloud-routers-api
- collection_type: open
  name: Google Distributed Cloud Edge Network Networks Subnets API
  slug: open-google-distributed-cloud-subnets-api
- collection_type: open
  name: Google Distributed Cloud Edge Network Networks Zones API
  slug: open-google-distributed-cloud-zones-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-distributed-cloud/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-distributed-cloud-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-distributed-cloud-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-distributed-cloud-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-distributed-cloud-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-distributed-cloud-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/distributed-cloud
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/distributed-cloud/docs/overview
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/distributed-cloud/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/distributed-cloud/edge/pricing
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
  url: https://cloud.google.com/distributed-cloud/docs/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/google-distributed-cloud-context.jsonld
created: '2026-03-13'
description: Google Distributed Cloud provides fully managed hardware and software solutions that extend Google Cloud infrastructure and services to the edge and into customer data centers. It supports both connected and air-gapped deployments, enabling organizations to run workloads locally while leveraging Google Cloud management, security, and services.
finops:
- name: Google Distributed Cloud Finops
  service_category: API
  slug: google-distributed-cloud-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-distributed-cloud.png
json_schemas:
- name: Google Distributed Cloud Edge Network
  property_count: 8
  slug: google-distributed-cloud-network
jsonld:
- class_count: 0
  name: Google Distributed Cloud Context
  property_count: 4
  slug: google-distributed-cloud-context
layout: provider
modified: '2026-05-19'
name: Google Distributed Cloud
nav: Providers
network: true
overview: 'Google Distributed Cloud publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Networks API, Routers API, Subnets API, and 1 more. Tagged areas include Distributed Infrastructure, Edge Computing, Hardware, Hybrid Cloud, and Kubernetes.


  The Google Distributed Cloud catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Google Distributed Cloud''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 11 more developer resources.'
plans:
- name: Google Distributed Cloud Plans Pricing
  plan_count: 3
  slug: google-distributed-cloud-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Google Distributed Cloud Rate Limits
  slug: google-distributed-cloud-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Distributed Cloud API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-distributed-cloud-jsonschema-spectral-rules
- effective_rule_count: 58
  extends:
  - spectral:oas
  name: Google Distributed Cloud API Rules
  rule_count: 17
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 5
  slug: google-distributed-cloud-spectral-rules
scopes:
- name: Google Distributed Cloud Scopes
  scope_count: 1
  slug: google-distributed-cloud-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 46.4
  coverage:
    artifact_dirs: 14
    catalog_gap: 53.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 13.6
    contract_quality: 61.9
    developer_ergonomics: 47.6
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 26.3
  previous_composite: 46.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-distributed-cloud/refs/heads/main/screenshots/google-distributed-cloud-2026-06-20T182158.png
security:
- kind: authentication
  name: Google Distributed Cloud Authentication
  slug: google-distributed-cloud-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Distributed Cloud Domain Security
  slug: google-distributed-cloud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Distributed Cloud Vulnerability Disclosure
  slug: google-distributed-cloud-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-distributed-cloud
tags:
- Distributed Infrastructure
- Edge Computing
- Hardware
- Hybrid Cloud
- Kubernetes
- On-Premises
website: https://cloud.google.com/distributed-cloud
---
