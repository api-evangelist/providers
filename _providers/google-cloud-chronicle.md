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
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Google Cloud Chronicle Agentic Access
  operation_count: 9
  slug: google-cloud-chronicle-agentic-access
  summary_line: 9 operations · 4 acting
api_count: 1
apis:
- description: Operations for managing security alerts
  name: Google Cloud Chronicle Alerts API
  slug: google-cloud-chronicle-alerts-api
- description: Operations for managing data ingestion feeds
  name: Google Cloud Chronicle Feeds API
  slug: google-cloud-chronicle-feeds-api
- description: Operations for managing reference lists
  name: Google Cloud Chronicle ReferenceLists API
  slug: google-cloud-chronicle-referencelists-api
- description: Operations for managing detection rules
  name: Google Cloud Chronicle Rules API
  slug: google-cloud-chronicle-rules-api
artifact_total: 25
collections:
- collection_type: postman
  name: Google Cloud Chronicle Alerts API
  slug: postman-google-cloud-chronicle-alerts-api
- collection_type: postman
  name: Google Cloud Chronicle Alerts Feeds API
  slug: postman-google-cloud-chronicle-feeds-api
- collection_type: postman
  name: Google Cloud Chronicle Alerts ReferenceLists API
  slug: postman-google-cloud-chronicle-referencelists-api
- collection_type: postman
  name: Google Cloud Chronicle Alerts Rules API
  slug: postman-google-cloud-chronicle-rules-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Cloud Chronicle API
  slug: open-chronicle-api
- collection_type: open
  name: Google Cloud Chronicle Alerts API
  slug: open-google-cloud-chronicle-alerts-api
- collection_type: open
  name: Google Cloud Chronicle Alerts Feeds API
  slug: open-google-cloud-chronicle-feeds-api
- collection_type: open
  name: Google Cloud Chronicle Alerts ReferenceLists API
  slug: open-google-cloud-chronicle-referencelists-api
- collection_type: open
  name: Google Cloud Chronicle Alerts Rules API
  slug: open-google-cloud-chronicle-rules-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-chronicle/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-chronicle-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-chronicle-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-chronicle-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-chronicle-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-chronicle-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chronicle
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chroniclesec
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/chronicle
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/chronicle/docs/get-started
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/chronicle/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/chronicle/docs/reference/rest#authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/chronicle/pricing
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
  url: https://status.cloud.google.com
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/chronicle/docs/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/google-cloud-chronicle-context.jsonld
created: '2026-03-13'
description: Google Cloud Chronicle is a cloud-native security information and event management (SIEM) platform that enables enterprises to store, search, and analyze massive volumes of security telemetry data. Built on Google infrastructure, Chronicle provides sub-second search across petabytes of security data, threat detection using rules and intelligence, and investigation tools for security operations teams.
finops:
- name: Google Cloud Chronicle Finops
  service_category: API
  slug: google-cloud-chronicle-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-chronicle.png
json_schemas:
- name: Google Cloud Chronicle UDM Event
  property_count: 7
  slug: google-cloud-chronicle-event
jsonld:
- class_count: 0
  name: Google Cloud Chronicle Context
  property_count: 4
  slug: google-cloud-chronicle-context
layout: provider
modified: '2026-05-19'
name: Google Cloud Chronicle
nav: Providers
network: true
overview: 'Google Cloud Chronicle publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Feeds API, ReferenceLists API, and 1 more. Tagged areas include Incident Response, Log Management, Security Analytics, Security Operations, and SIEM.


  The Google Cloud Chronicle catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Chronicle''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 12 more developer resources.'
plans:
- name: Google Cloud Chronicle Plans Pricing
  plan_count: 3
  slug: google-cloud-chronicle-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Google Cloud Chronicle Rate Limits
  slug: google-cloud-chronicle-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Google Cloud Chronicle API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: google-cloud-chronicle-jsonschema-spectral-rules
scopes:
- name: Google Cloud Chronicle Scopes
  scope_count: 1
  slug: google-cloud-chronicle-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 42.4
  coverage:
    artifact_dirs: 14
    catalog_gap: 54.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 9.8
    contract_quality: 61.9
    developer_ergonomics: 40.5
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 42.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-chronicle/refs/heads/main/screenshots/google-cloud-chronicle-2026-06-20T182100.png
security:
- kind: authentication
  name: Google Cloud Chronicle Authentication
  slug: google-cloud-chronicle-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Chronicle Domain Security
  slug: google-cloud-chronicle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Chronicle Vulnerability Disclosure
  slug: google-cloud-chronicle-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-chronicle
tags:
- Incident Response
- Log Management
- Security Analytics
- Security Operations
- SIEM
- Threat Detection
website: https://cloud.google.com/chronicle
---
