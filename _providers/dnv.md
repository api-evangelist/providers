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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Dnv Agentic Access
  operation_count: 5
  slug: dnv-agentic-access
  summary_line: 5 operations
api_count: 1
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
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: DNV Class Status Certificates API
  slug: open-dnv-certificates-api
- collection_type: open
  name: DNV Class Status API
  slug: open-dnv-class-status
- collection_type: open
  name: DNV Class Status Certificates Surveys API
  slug: open-dnv-surveys-api
- collection_type: open
  name: DNV Class Status Certificates Vessels API
  slug: open-dnv-vessels-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/dnv-capability-edges.yml
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


  DNV''s developer surface includes authentication, developer portal, documentation, support, getting-started guide, and 16 more developer resources.'
plans:
- name: Dnv Plans Pricing
  plan_count: 2
  slug: dnv-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: Dnv Rate Limits
  slug: dnv-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: DNV API Rules
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
  composite: 51.6
  coverage:
    artifact_dirs: 15
    catalog_gap: 59.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 9.8
    contract_quality: 63.3
    developer_ergonomics: 54.8
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 23.7
  previous_composite: 51.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 64.9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
