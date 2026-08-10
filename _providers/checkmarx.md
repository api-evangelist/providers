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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Checkmarx Agentic Access
  operation_count: 61
  slug: checkmarx-agentic-access
  summary_line: 61 operations · 25 acting
api_count: 15
apis:
- description: Manage applications that group related projects
  name: Checkmarx Applications API
  slug: checkmarx-applications-api
- description: Obtain and manage authentication tokens via OAuth 2.0
  name: Checkmarx Authentication API
  slug: checkmarx-authentication-api
- description: Manage project and tenant-level scan configuration
  name: Checkmarx Configuration API
  slug: checkmarx-configuration-api
- description: Manage scan engines and engine servers
  name: Checkmarx Engines API
  slug: checkmarx-engines-api
- description: Manage access control groups
  name: Checkmarx Groups API
  slug: checkmarx-groups-api
- description: Query open source package information
  name: Checkmarx Packages API
  slug: checkmarx-packages-api
- description: Manage scan configuration presets
  name: Checkmarx Presets API
  slug: checkmarx-presets-api
- description: Manage scanning projects and their configuration
  name: Checkmarx Projects API
  slug: checkmarx-projects-api
- description: Manage custom SAST queries and presets
  name: Checkmarx Queries API
  slug: checkmarx-queries-api
- description: Generate and download scan reports
  name: Checkmarx Reports API
  slug: checkmarx-reports-api
- description: Retrieve and manage scan results and findings
  name: Checkmarx Results API
  slug: checkmarx-results-api
- description: Retrieve vulnerability and risk analysis results
  name: Checkmarx Risk Reports API
  slug: checkmarx-risk-reports-api
- description: Trigger, monitor, and manage security scans
  name: Checkmarx Scans API
  slug: checkmarx-scans-api
- description: Manage project and organization settings
  name: Checkmarx Settings API
  slug: checkmarx-settings-api
- description: Manage teams and access control
  name: Checkmarx Teams API
  slug: checkmarx-teams-api
artifact_total: 45
collections:
- collection_type: postman
  name: Checkmarx One Applications API
  slug: postman-checkmarx-applications-api
- collection_type: postman
  name: Checkmarx One Applications Authentication API
  slug: postman-checkmarx-authentication-api
- collection_type: postman
  name: Checkmarx One Applications Configuration API
  slug: postman-checkmarx-configuration-api
- collection_type: postman
  name: Checkmarx One Applications Engines API
  slug: postman-checkmarx-engines-api
- collection_type: postman
  name: Checkmarx One Applications Groups API
  slug: postman-checkmarx-groups-api
- collection_type: postman
  name: Checkmarx One Applications Packages API
  slug: postman-checkmarx-packages-api
- collection_type: postman
  name: Checkmarx One Applications Presets API
  slug: postman-checkmarx-presets-api
- collection_type: postman
  name: Checkmarx One Applications Projects API
  slug: postman-checkmarx-projects-api
- collection_type: postman
  name: Checkmarx One Applications Queries API
  slug: postman-checkmarx-queries-api
- collection_type: postman
  name: Checkmarx One Applications Reports API
  slug: postman-checkmarx-reports-api
- collection_type: postman
  name: Checkmarx One Applications Results API
  slug: postman-checkmarx-results-api
- collection_type: postman
  name: Checkmarx One Applications Risk Reports API
  slug: postman-checkmarx-risk-reports-api
- collection_type: postman
  name: Checkmarx One Applications Scans API
  slug: postman-checkmarx-scans-api
- collection_type: postman
  name: Checkmarx One Applications Settings API
  slug: postman-checkmarx-settings-api
- collection_type: postman
  name: Checkmarx One Applications Teams API
  slug: postman-checkmarx-teams-api
- collection_type: open
  name: Checkmarx One API
  slug: open-checkmarx-one
- collection_type: open
  name: Checkmarx SAST API
  slug: open-checkmarx-sast
- collection_type: open
  name: Checkmarx SCA API
  slug: open-checkmarx-sca
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/checkmarx/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/checkmarx-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/checkmarx-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/checkmarx-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/checkmarx-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/checkmarx
- group: company
  title: ''
  type: Website
  url: https://www.checkmarx.com
- group: docs
  title: ''
  type: Documentation
  url: https://checkmarx.com/resource/documents/
- group: operate
  title: ''
  type: Support
  url: https://support.checkmarx.com/
- group: start
  title: ''
  type: Login
  url: https://checkmarx.com/login/
- group: company
  title: ''
  type: Blog
  url: https://checkmarx.com/blog/
- group: company
  title: ''
  type: News
  url: https://checkmarx.com/news/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/checkmarx
- group: operate
  title: ''
  type: StatusPage
  url: https://status.checkmarx.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://checkmarx.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://checkmarx.com/terms-of-use/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/checkmarx-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/checkmarx-scan-result-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/checkmarx-vulnerability-schema.json
- group: design
  title: ''
  type: Spectral
  url: spectral/checkmarx-spectral.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://checkmarx.com/llms.txt
created: '2024'
description: Checkmarx is a leading application security testing solution provider, offering static application security testing (SAST), software composition analysis (SCA), and other security tools to help organizations identify and remediate vulnerabilities in their code.
finops:
- name: Checkmarx Finops
  service_category: Application Security
  slug: checkmarx-finops
graphqls:
- description: Checkmarx provides application security testing covering SAST, SCA, DAST, API security, and container security. The API covers scan management, vulnerability results, project configuration, code quali
  name: Checkmarx GraphQL API
  slug: checkmarx-graphql
image: https://www.checkmarx.com/wp-content/uploads/2022/03/checkmarx-logo.svg
json_schemas:
- name: Checkmarx Scan Result
  property_count: 19
  slug: checkmarx-scan-result
- name: Checkmarx Vulnerability
  property_count: 18
  slug: checkmarx-vulnerability
jsonld:
- class_count: 0
  name: Checkmarx Context
  property_count: 10
  slug: checkmarx-context
layout: provider
modified: '2026-05-19'
name: Checkmarx
nav: Providers
network: true
overview: 'Checkmarx publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Authentication API, Configuration API, and 12 more. Tagged areas include Application Security, Code Analysis, DevSecOps, SAST, and Security Testing.


  The Checkmarx catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Checkmarx''s developer surface includes authentication, documentation, support, engineering blog, product news, GitHub presence, and 15 more developer resources.'
plans:
- name: Checkmarx Plans Pricing
  plan_count: 5
  slug: checkmarx-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 3
  name: Checkmarx Rate Limits
  slug: checkmarx-rate-limits
rules:
- name: Checkmarx API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: checkmarx-jsonschema-spectral-rules
score:
  band: strong
  composite: 63.0
  delta: 0.0
  facets:
    commercial_clarity: 81.6
    contract_quality: 74.4
    developer_ergonomics: 30.4
    discoverability: 81.5
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 63.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/checkmarx/refs/heads/main/screenshots/checkmarx-2026-06-20T174245.png
security:
- kind: authentication
  name: Checkmarx Authentication
  slug: checkmarx-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Checkmarx Domain Security
  slug: checkmarx-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Checkmarx Trust Center
  slug: checkmarx-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: checkmarx
tags:
- Application Security
- Code Analysis
- DevSecOps
- SAST
- Security Testing
- Vulnerability Scanning
website: https://www.checkmarx.com
---
