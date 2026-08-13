---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Nvd Agentic Access
  operation_count: 5
  slug: nvd-agentic-access
  summary_line: 5 operations
api_count: 6
apis:
- description: The National Vulnerability Database (NVD) provides REST and RSS/Atom APIs for CVE (Common Vulnerabilities and Exposures) data. APIs deliver vulnerability descriptions, CVSS severity scores, affected p
  name: National Vulnerability Database API
  slug: nvd-overview
- description: Common Platform Enumeration product dictionary
  name: NVD CPE API
  slug: nvd-cpe-api
- description: CVE-to-product match criteria
  name: NVD CPE Match API
  slug: nvd-cpe-match-api
- description: Common Vulnerabilities and Exposures records
  name: NVD CVE API
  slug: nvd-cve-api
- description: CVE record modification tracking
  name: NVD CVE Change History API
  slug: nvd-cve-change-history-api
- description: NVD data source organizations
  name: NVD Sources API
  slug: nvd-sources-api
artifact_total: 27
collections:
- collection_type: open
  name: NVD CVE API
  slug: open-nvd-cve
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nvd-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nvd-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nvd-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://nvd.nist.gov/developers
- group: company
  title: ''
  type: Website
  url: https://nvd.nist.gov/
- group: start
  title: ''
  type: GettingStarted
  url: https://nvd.nist.gov/developers/start-here
- group: auth
  title: ''
  type: Authentication
  url: https://nvd.nist.gov/developers/request-an-api-key
- group: operate
  title: ''
  type: RateLimits
  url: https://nvd.nist.gov/developers/start-here
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nvd.nist.gov/developers/terms-of-use
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/nvd/refs/heads/main/openapi/nvd-cve-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/nvd/refs/heads/main/json-schema/nvd-cve-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/nvd/refs/heads/main/json-ld/nvd-context.jsonld
description: The National Vulnerability Database (NVD) provides REST APIs for CVE (Common Vulnerabilities and Exposures) data, CPE (Common Platform Enumeration) records, match criteria, and source organizations. APIs deliver vulnerability descriptions, CVSS severity scores, affected product lists, CWE classifications, and reference links for security monitoring and dependency alerting.
finops:
- name: Nvd Finops
  service_category: Public Sector / Security Data
  slug: nvd-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nvd.png
json_schemas:
- name: CPE
  property_count: 7
  slug: nvd-cpe
- name: CPEMatchResponse
  property_count: 5
  slug: nvd-cpematchresponse
- name: CPEResponse
  property_count: 7
  slug: nvd-cperesponse
- name: NVD CVE Record
  property_count: 14
  slug: nvd-cve
- name: CVEConfiguration
  property_count: 1
  slug: nvd-cveconfiguration
- name: CVEHistoryResponse
  property_count: 7
  slug: nvd-cvehistoryresponse
- name: CVEResponse
  property_count: 7
  slug: nvd-cveresponse
- name: CVSSMetricV2
  property_count: 4
  slug: nvd-cvssmetricv2
- name: CVSSMetricV3
  property_count: 5
  slug: nvd-cvssmetricv3
- name: ErrorResponse
  property_count: 1
  slug: nvd-errorresponse
- name: SourceResponse
  property_count: 5
  slug: nvd-sourceresponse
json_structures:
- name: Nvd Structure
  property_count: 0
  slug: nvd-structure
jsonld:
- class_count: 8
  name: Nvd Context
  property_count: 14
  slug: nvd-context
layout: provider
modified: '2026-05-19'
name: NVD
nav: Providers
network: true
overview: 'NVD publishes 5 APIs on the [APIs.io](https://apis.io/) network, including CPE API, CPE Match API, CVE API, and 2 more. Tagged areas include Security, CVE, CPE, Vulnerability, and CVSS.


  The NVD catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  NVD''s developer surface includes authentication, developer portal, getting-started guide, and 9 more developer resources.'
plans:
- name: Nvd Plans Pricing
  plan_count: 2
  slug: nvd-plans-pricing
random_paper: 88
rate_limits:
- limit_count: 2
  name: Nvd Rate Limits
  slug: nvd-rate-limits
rules:
- name: NVD API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: nvd-jsonschema-spectral-rules
score:
  band: developing
  composite: 43.2
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 73.0
    developer_ergonomics: 30.4
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 43.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nvd/refs/heads/main/screenshots/nvd-2026-06-20T190537.png
security:
- kind: authentication
  name: Nvd Authentication
  slug: nvd-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Nvd Domain Security
  slug: nvd-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: nvd
tags:
- Security
- CVE
- CPE
- Vulnerability
- CVSS
website: https://nvd.nist.gov/
---
