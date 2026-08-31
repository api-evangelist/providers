---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
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
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Google Looker Agentic Access
  operation_count: 5
  slug: google-looker-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 1
apis:
- description: 'The Looker Studio API allows you to search for and manage Looker Studio assets programmatically, enabling automation and migration of Looker Studio resources within Google Workspace or Cloud Identity '
  name: Looker Studio API
  slug: looker-studio-api
- description: The Authentication API from Google Looker — 1 operation(s) for authentication.
  name: Google Looker Authentication API
  slug: google-looker-authentication-api
- description: The Looks API from Google Looker — 2 operation(s) for looks.
  name: Google Looker Looks API
  slug: google-looker-looks-api
- description: The Users API from Google Looker — 2 operation(s) for users.
  name: Google Looker Users API
  slug: google-looker-users-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Looker Authentication API
  slug: open-google-looker-authentication-api
- collection_type: open
  name: Google Looker Authentication Looks API
  slug: open-google-looker-looks-api
- collection_type: open
  name: Google Looker Authentication Users API
  slug: open-google-looker-users-api
- collection_type: open
  name: Google Looker API
  slug: open-openapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-looker-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-looker-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-looker-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-looker-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/looker
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/looker
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/looker/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://cloud.google.com/blog/products/data-analytics
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloud.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cloud.google.com/privacy
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://cloud.google.com/looker/docs/release-notes
- group: other
  title: ''
  type: Looker Studio
  url: https://cloud.google.com/looker-studio
- group: operate
  title: ''
  type: Community Connectors
  url: https://developers.google.com/looker-studio/connector
- group: docs
  title: ''
  type: Community Connectors Reference
  url: https://developers.google.com/looker-studio/connector/reference
created: '2024-01-01'
description: A collection of APIs for Google Looker, a modern business intelligence and analytics platform.
finops:
- name: Google Looker Finops
  service_category: Analytics
  slug: google-looker-finops
image: https://cloud.google.com/images/social-icon-google-cloud-1200-630.png
json_schemas:
- name: Look
  property_count: 7
  slug: Look
jsonld:
- class_count: 16
  name: context Context
  property_count: 0
  slug: context
layout: provider
modified: '2026-05-19'
name: Google Looker
nav: Providers
network: true
overview: 'Google Looker publishes 3 APIs on the [APIs.io](https://apis.io/) network: Authentication API, Looks API, and Users API.


  The Google Looker catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Google Looker''s developer surface includes authentication, developer portal, getting-started guide, engineering blog, release notes, and 9 more developer resources.'
plans:
- name: Google Looker Plans Pricing
  plan_count: 4
  slug: google-looker-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 7
  name: Google Looker Rate Limits
  slug: google-looker-rate-limits
rules:
- effective_rule_count: 4
  extends: []
  name: Google Looker API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: google-looker-jsonschema-spectral-rules
- effective_rule_count: 59
  extends:
  - spectral:oas
  name: Google Looker API Rules
  rule_count: 18
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 7
  slug: google-looker-spectral-rules
score:
  band: developing
  composite: 45.6
  coverage:
    artifact_dirs: 13
    catalog_gap: 66.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 13.6
    contract_quality: 56.5
    developer_ergonomics: 52.4
    discoverability: 57.4
    governance: 13.6
    operational_transparency: 31.6
  previous_composite: 46.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: false
    note: provider carries no tags; regime could not be determined
    undetermined: true
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-looker/refs/heads/main/screenshots/google-looker-2026-06-20T182214.png
security:
- kind: authentication
  name: Google Looker Authentication
  slug: google-looker-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Google Looker Domain Security
  slug: google-looker-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Looker Vulnerability Disclosure
  slug: google-looker-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-looker
website: https://cloud.google.com/looker
---
