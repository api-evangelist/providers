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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Saas Alerts Agentic Access
  operation_count: 5
  slug: saas-alerts-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 2
apis:
- description: SaaS security event queries and reporting
  name: SaaS Alerts Events API
  slug: saas-alerts-events-api
- description: Security event report generation
  name: SaaS Alerts Reports API
  slug: saas-alerts-reports-api
artifact_total: 22
collections:
- collection_type: postman
  name: SaaS Alerts Events API
  slug: postman-saas-alerts-events-api
- collection_type: postman
  name: SaaS Alerts Events Reports API
  slug: postman-saas-alerts-reports-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SaaS Alerts Events API
  slug: open-saas-alerts-events-api
- collection_type: open
  name: SaaS Alerts Events Reports API
  slug: open-saas-alerts-reports-api
- collection_type: open
  name: SaaS Alerts API
  slug: open-saas-alerts
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/saas-alerts/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/saas-alerts-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/saas-alerts-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/saas-alerts-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/saas-alerts
- group: company
  title: ''
  type: Website
  url: https://www.saasalerts.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.saasalerts.kaseya.com/help/Content/Home/saas-alerts-msp-admin-guide.htm
- group: docs
  title: ''
  type: APIDocumentation
  url: https://help.saasalerts.kaseya.com/help/Content/How-To/using-the-saas-alerts-api.htm
- group: company
  title: ''
  type: Blog
  url: https://www.saasalerts.com/blog
- group: other
  title: ''
  type: PlatformOverview
  url: https://saasalerts.com/platform-overview-for-msps/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.saasalerts.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.saasalerts.com/terms
- group: start
  title: ''
  type: Login
  url: https://app.saasalerts.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.saasalerts.com/pricing
created: '2026-03-27'
description: SaaS Alerts is a SaaS security monitoring platform purpose-built for Managed Service Providers (MSPs). The platform detects anomalous user behavior, data exfiltration, account compromise, and unauthorized access across cloud applications including Microsoft 365, Google Workspace, Salesforce, Slack, and Dropbox. Key capabilities include machine learning-based threat detection, automated remediation workflows, multi-tenant MSP management, and integration with PSA and RMM platforms. SaaS Alerts was acquired by Kaseya in 2023.
examples:
- key_count: 2
  name: Saas Alerts List Security Events Example
  slug: saas-alerts-list-security-events-example
- key_count: 2
  name: Saas Alerts Query Security Events Example
  slug: saas-alerts-query-security-events-example
finops:
- name: Saas Alerts Finops
  service_category: API
  slug: saas-alerts-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/saas-alerts.png
json_schemas:
- name: SaaS Alerts Security Alert
  property_count: 12
  slug: saas-alerts-alert
- name: SaaS Alerts Security Event
  property_count: 11
  slug: saas-alerts-security-event
json_structures:
- name: Saas Alerts Security Event Structure
  property_count: 0
  slug: saas-alerts-security-event-structure
jsonld:
- class_count: 4
  name: Saas Alerts Context
  property_count: 12
  slug: saas-alerts-context
layout: provider
modified: '2026-05-19'
name: SaaS Alerts
nav: Providers
network: true
overview: 'SaaS Alerts publishes 2 APIs on the [APIs.io](https://apis.io/) network: Events API and Reports API. Tagged areas include MSP, SaaS Security, Security Monitoring, Threat Detection, and Microsoft 365.


  The SaaS Alerts catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SaaS Alerts'' developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Saas Alerts Plans Pricing
  plan_count: 3
  slug: saas-alerts-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Saas Alerts Rate Limits
  slug: saas-alerts-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: SaaS Alerts API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: saas-alerts-jsonschema-spectral-rules
- effective_rule_count: 58
  extends:
  - spectral:oas
  name: SaaS Alerts API Rules
  rule_count: 17
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 13
  slug: saas-alerts-spectral-rules
score:
  band: developing
  composite: 43.0
  delta: -7.3
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 9.8
    contract_quality: 64.0
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 50.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/saas-alerts/refs/heads/main/screenshots/saas-alerts-2026-08-17T083027.png
security:
- kind: authentication
  name: Saas Alerts Authentication
  slug: saas-alerts-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Saas Alerts Domain Security
  slug: saas-alerts-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: saas-alerts
tags:
- MSP
- SaaS Security
- Security Monitoring
- Threat Detection
- Microsoft 365
- Google Workspace
- MSSP
website: https://www.saasalerts.com
---
