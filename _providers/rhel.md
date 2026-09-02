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
    auth_clarity: bearer
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
  score: 22.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Rhel Agentic Access
  operation_count: 8
  slug: rhel-agentic-access
  summary_line: 8 operations
api_count: 2
apis:
- description: Red Hat Security Advisories (CSAF/CVRF)
  name: Red Hat Enterprise Linux Advisories API
  slug: rhel-advisories-api
- description: Common Vulnerabilities and Exposures data
  name: Red Hat Enterprise Linux CVEs API
  slug: rhel-cves-api
- description: Open Vulnerability and Assessment Language data
  name: Red Hat Enterprise Linux OVAL API
  slug: rhel-oval-api
- description: Subscription and entitlement management
  name: Red Hat Enterprise Linux Subscriptions API
  slug: rhel-subscriptions-api
- description: Registered system management
  name: Red Hat Enterprise Linux Systems API
  slug: rhel-systems-api
artifact_total: 37
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Red Hat Security Data Advisories API
  slug: open-rhel-advisories-api
- collection_type: open
  name: Red Hat Security Data Advisories CVEs API
  slug: open-rhel-cves-api
- collection_type: open
  name: Red Hat Security Data Advisories OVAL API
  slug: open-rhel-oval-api
- collection_type: open
  name: Red Hat Security Data API
  slug: open-rhel-security-data
- collection_type: open
  name: Red Hat Subscription Management API
  slug: open-rhel-subscription-management
- collection_type: open
  name: Red Hat Security Data Advisories Subscriptions API
  slug: open-rhel-subscriptions-api
- collection_type: open
  name: Red Hat Security Data Advisories Systems API
  slug: open-rhel-systems-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/RedHatOfficial/rhsecapi/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/RedHatOfficial/rhsecapi/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/RedHatOfficial/rhsecapi/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rhel-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/rhel-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/rhel-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rhel-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rhel-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/rhel-scopes.yml
- group: company
  title: ''
  type: Blog
  url: https://www.redhat.com/en/rss/blog
- group: start
  title: ''
  type: Portal
  url: https://access.redhat.com
- group: other
  title: ''
  type: Developer
  url: https://developers.redhat.com/products/rhel
- group: docs
  title: ''
  type: Documentation
  url: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/
- group: start
  title: ''
  type: HybridCloudConsole
  url: https://console.redhat.com
- group: other
  title: ''
  type: APIManagement
  url: https://access.redhat.com/management/api
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/RedHatOfficial
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/redhat-cop
- group: operate
  title: ''
  type: Support
  url: https://access.redhat.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.redhat.com/en/about/terms-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.redhat.com/en/about/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.redhat.com
- group: auth
  title: ''
  type: Authentication
  url: https://access.redhat.com/articles/3626371
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/rhel/refs/heads/main/rules/rhel-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/rhel/refs/heads/main/json-schema/rhel-cve-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/rhel/refs/heads/main/json-schema/rhel-system-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/rhel/refs/heads/main/json-ld/rhel-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/rhel/refs/heads/main/vocabulary/rhel-vocabulary.yml
created: '2024-01-01'
description: Red Hat Enterprise Linux (RHEL) is the world's leading enterprise Linux platform, providing APIs and services for subscription management, security insights, compliance monitoring, vulnerability assessment, patch management, content delivery, and automation. The Red Hat Hybrid Cloud Console exposes a comprehensive suite of REST APIs for managing RHEL systems at scale.
examples:
- key_count: 2
  name: Rhel Get Cve Example
  slug: rhel-get-cve-example
- key_count: 2
  name: Rhel List Cves Example
  slug: rhel-list-cves-example
finops:
- name: Rhel Finops
  service_category: Operating System Subscription
  slug: rhel-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rhel.png
json_schemas:
- name: Advisory
  property_count: 5
  slug: rhel-advisory
- name: Allocation
  property_count: 6
  slug: rhel-allocation
- name: RHEL CVE
  property_count: 11
  slug: rhel-cve
- name: CVEDetail
  property_count: 11
  slug: rhel-cvedetail
- name: CVESummary
  property_count: 11
  slug: rhel-cvesummary
- name: Pagination
  property_count: 3
  slug: rhel-pagination
- name: Subscription
  property_count: 7
  slug: rhel-subscription
- name: RHEL System
  property_count: 10
  slug: rhel-system
json_structures:
- name: Rhel Cve Structure
  property_count: 0
  slug: rhel-cve-structure
- name: Rhel Structure
  property_count: 0
  slug: rhel-structure
jsonld:
- class_count: 33
  name: Rhel Context
  property_count: 0
  slug: rhel-context
layout: provider
modified: '2026-05-19'
name: Red Hat Enterprise Linux
nav: Providers
network: true
overview: 'Red Hat Enterprise Linux publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Advisories API, CVEs API, OVAL API, and 2 more. Tagged areas include Automation, Compliance, Enterprise, Linux, and Operating System.


  The Red Hat Enterprise Linux catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Red Hat Enterprise Linux''s developer surface includes authentication, engineering blog, developer portal, documentation, support, and 22 more developer resources.'
plans:
- name: Rhel Plans Pricing
  plan_count: 7
  slug: rhel-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Rhel Rate Limits
  slug: rhel-rate-limits
rules:
- effective_rule_count: 4
  extends: []
  name: Red Hat Enterprise Linux API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 2
  slug: rhel-jsonschema-spectral-rules
- effective_rule_count: 9
  extends: []
  name: Red Hat Enterprise Linux API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 5
  slug: rhel-rules
scopes:
- name: Rhel Scopes
  scope_count: 1
  slug: rhel-scopes
  summary_line: 1 scope · password
score:
  band: developing
  composite: 47.8
  coverage:
    artifact_dirs: 17
    catalog_gap: 44.8
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 78.6
    commercial_clarity: 78.6
    contract_governance: 25.0
    contract_quality: 55.1
    developer_ergonomics: 38.1
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 25.0
  previous_composite: 47.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rhel/refs/heads/main/screenshots/rhel-2026-06-20T193105.png
security:
- kind: authentication
  name: Rhel Authentication
  slug: rhel-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Rhel Domain Security
  slug: rhel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Rhel Vulnerability Disclosure
  slug: rhel-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Rhel Trust Center
  slug: rhel-trust-center
  summary_line: ISO 27001, ISO 27018, HIPAA
slug: rhel
tags:
- Automation
- Compliance
- Enterprise
- Linux
- Operating System
- Red Hat
- RHEL
- Security
- Subscription Management
- Vulnerability Management
website: https://www.redhat.com
---
