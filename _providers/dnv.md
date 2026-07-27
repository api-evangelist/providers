---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Dnv Agentic Access
  operation_count: 5
  slug: dnv-agentic-access
  summary_line: 5 operations
api_count: 5
apis:
- description: DNV Veracity is an open and secure industry data platform facilitating exchange of datasets, APIs, applications, and insights across maritime, oil and gas, and energy sectors. Veracity APIs enable acc
  name: DNV Veracity Platform API
  slug: dnv-veracity-api
- description: DNV Vessel Register provides access to DNV's public registry of classified vessels including vessel identification, classification status, certificates, and survey history. The register supports fleet
  name: DNV Vessel Register
  slug: dnv-vessel-register-api
- description: Classification certificates and survey documents
  name: DNV Certificates API
  slug: dnv-certificates-api
- description: Survey schedules and records
  name: DNV Surveys API
  slug: dnv-surveys-api
- description: Vessel classification status and information
  name: DNV Vessels API
  slug: dnv-vessels-api
artifact_total: 17
collections:
- collection_type: open
  name: DNV Class Status API
  slug: open-dnv-class-status
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dnv-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dnv-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dnv-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dnv-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/dnv-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dnv-opensource
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/det-norske-veritas-dnv-gl-
- group: company
  title: ''
  type: Website
  url: https://www.dnv.com/
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/dnv/refs/heads/main/openapi/dnv-class-status-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/dnv/refs/heads/main/json-schema/dnv-vessel-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/dnv/refs/heads/main/json-ld/dnv-context.jsonld
- group: start
  title: ''
  type: Portal
  url: https://www.veracity.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.veracity.com/docs/section/api-explorer/api-explorer
- group: auth
  title: ''
  type: Authentication
  url: https://maritime.dnv.com/api/cs-iacs-customer
- group: operate
  title: ''
  type: Support
  url: https://help-center.veracity.com/en/
- group: operate
  title: ''
  type: Support
  url: https://support.veracity.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dnv.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dnv.com/terms/
- group: operate
  title: ''
  type: StatusPage
  url: https://vesselregister.dnv.com/vesselregister
- group: start
  title: ''
  type: GettingStarted
  url: https://www.dnv.com/maritime/
description: DNV is a global classification, certification, and assurance provider for the maritime, energy, and industrial sectors. The API portfolio includes the Class Status API for vessel classification data, the Veracity industry data platform, and the public Vessel Register, supporting fleet management, regulatory compliance, and operational analytics workflows.
finops:
- name: Dnv Finops
  service_category: Maritime Classification / Data Platform
  slug: dnv-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dnv.png
json_schemas:
- name: DNV Classified Vessel
  property_count: 15
  slug: dnv-vessel
jsonld:
- class_count: 1
  name: Dnv Context
  property_count: 22
  slug: dnv-context
layout: provider
modified: '2026-05-19'
name: DNV
nav: Providers
network: true
overview: 'DNV publishes 3 APIs on the [APIs.io](https://apis.io/) network: Certificates API, Surveys API, and Vessels API. Tagged areas include Maritime, Energy, Classification, Vessel, and Data Platform.


  The DNV catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DNV''s developer surface includes authentication, developer portal, documentation, support, getting-started guide, and 15 more developer resources.'
plans:
- name: Dnv Plans Pricing
  plan_count: 2
  slug: dnv-plans-pricing
random_paper: 56
rate_limits:
- limit_count: 1
  name: Dnv Rate Limits
  slug: dnv-rate-limits
rules:
- name: DNV API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: dnv-jsonschema-spectral-rules
scopes:
- name: Dnv Scopes
  scope_count: 1
  slug: dnv-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 59.8
  delta: 3.2
  facets:
    commercial_clarity: 50.0
    contract_quality: 67.3
    developer_ergonomics: 43.5
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 42.1
  previous_composite: 56.6
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dnv/refs/heads/main/screenshots/dnv-2026-06-20T180105.png
security:
- kind: authentication
  name: Dnv Authentication
  slug: dnv-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Dnv Domain Security
  slug: dnv-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Dnv Vulnerability Disclosure
  slug: dnv-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dnv
tags:
- Maritime
- Energy
- Classification
- Vessel
- Data Platform
website: https://www.dnv.com/
---
