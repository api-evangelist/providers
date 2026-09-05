---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Stellar Cyber Agentic Access
  operation_count: 34
  slug: stellar-cyber-agentic-access
  summary_line: 34 operations · 21 acting
api_count: 1
apis:
- baseURL: https://{platform-hostname}/connect/api/v1
  baseurl_source: declared
  description: Alert management, tagging, and status updates
  name: Stellar Cyber Alerts API
  slug: stellar-cyber-alerts-api
- baseURL: https://{platform-hostname}/connect/api/v1
  baseurl_source: declared
  description: API key and JWT token management
  name: Stellar Cyber Authentication API
  slug: stellar-cyber-authentication-api
- baseURL: https://{platform-hostname}/connect/api/v1
  baseurl_source: declared
  description: Security case creation, retrieval, update, and closure
  name: Stellar Cyber Cases API
  slug: stellar-cyber-cases-api
- baseURL: https://{platform-hostname}/connect/api/v1
  baseurl_source: declared
  description: Data connector management for security telemetry ingestion
  name: Stellar Cyber Connectors API
  slug: stellar-cyber-connectors-api
- baseURL: https://{platform-hostname}/connect/api/v1
  baseurl_source: declared
  description: Security event management and bulk ingestion
  name: Stellar Cyber Events API
  slug: stellar-cyber-events-api
- baseURL: https://{platform-hostname}/connect/api/v1
  baseurl_source: declared
  description: ATH Playbook response action management
  name: Stellar Cyber Playbooks API
  slug: stellar-cyber-playbooks-api
- baseURL: https://{platform-hostname}/connect/api/v1
  baseurl_source: declared
  description: Saved query management
  name: Stellar Cyber Queries API
  slug: stellar-cyber-queries-api
- baseURL: https://{platform-hostname}/connect/api/v1
  baseurl_source: declared
  description: Security report generation and retrieval
  name: Stellar Cyber Reports API
  slug: stellar-cyber-reports-api
- baseURL: https://{platform-hostname}/connect/api/v1
  baseurl_source: declared
  description: Sensor monitoring and management
  name: Stellar Cyber Sensors API
  slug: stellar-cyber-sensors-api
- baseURL: https://{platform-hostname}/connect/api/v1
  baseurl_source: declared
  description: Multi-tenant administration and grouping
  name: Stellar Cyber Tenants API
  slug: stellar-cyber-tenants-api
- baseURL: https://{platform-hostname}/connect/api/v1
  baseurl_source: declared
  description: Watchlist creation and management
  name: Stellar Cyber Watchlists API
  slug: stellar-cyber-watchlists-api
artifact_total: 50
collections:
- collection_type: postman
  name: Stellar Cyber Open XDR Alerts API
  slug: postman-stellar-cyber-alerts-api
- collection_type: postman
  name: Stellar Cyber Open XDR Alerts Authentication API
  slug: postman-stellar-cyber-authentication-api
- collection_type: postman
  name: Stellar Cyber Open XDR Alerts Cases API
  slug: postman-stellar-cyber-cases-api
- collection_type: postman
  name: Stellar Cyber Open XDR Alerts Connectors API
  slug: postman-stellar-cyber-connectors-api
- collection_type: postman
  name: Stellar Cyber Open XDR Alerts Events API
  slug: postman-stellar-cyber-events-api
- collection_type: postman
  name: Stellar Cyber Open XDR Alerts Playbooks API
  slug: postman-stellar-cyber-playbooks-api
- collection_type: postman
  name: Stellar Cyber Open XDR Alerts Queries API
  slug: postman-stellar-cyber-queries-api
- collection_type: postman
  name: Stellar Cyber Open XDR Alerts Reports API
  slug: postman-stellar-cyber-reports-api
- collection_type: postman
  name: Stellar Cyber Open XDR Alerts Sensors API
  slug: postman-stellar-cyber-sensors-api
- collection_type: postman
  name: Stellar Cyber Open XDR Alerts Tenants API
  slug: postman-stellar-cyber-tenants-api
- collection_type: postman
  name: Stellar Cyber Open XDR Alerts Watchlists API
  slug: postman-stellar-cyber-watchlists-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Stellar Cyber Open XDR Alerts API
  slug: open-stellar-cyber-alerts-api
- collection_type: open
  name: Stellar Cyber Open XDR Alerts Authentication API
  slug: open-stellar-cyber-authentication-api
- collection_type: open
  name: Stellar Cyber Open XDR Alerts Cases API
  slug: open-stellar-cyber-cases-api
- collection_type: open
  name: Stellar Cyber Open XDR Alerts Connectors API
  slug: open-stellar-cyber-connectors-api
- collection_type: open
  name: Stellar Cyber Open XDR Alerts Events API
  slug: open-stellar-cyber-events-api
- collection_type: open
  name: Stellar Cyber Open XDR Alerts Playbooks API
  slug: open-stellar-cyber-playbooks-api
- collection_type: open
  name: Stellar Cyber Open XDR Alerts Queries API
  slug: open-stellar-cyber-queries-api
- collection_type: open
  name: Stellar Cyber Open XDR Alerts Reports API
  slug: open-stellar-cyber-reports-api
- collection_type: open
  name: Stellar Cyber Open XDR Alerts Sensors API
  slug: open-stellar-cyber-sensors-api
- collection_type: open
  name: Stellar Cyber Open XDR Alerts Tenants API
  slug: open-stellar-cyber-tenants-api
- collection_type: open
  name: Stellar Cyber Open XDR Alerts Watchlists API
  slug: open-stellar-cyber-watchlists-api
- collection_type: open
  name: Stellar Cyber Open XDR API
  slug: open-stellar-cyber
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/stellar-cyber/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stellar-cyber-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/stellar-cyber-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stellar-cyber-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stellar-cyber-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stellar-cyber
- group: start
  title: ''
  type: Portal
  url: https://stellarcyber.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.stellarcyber.ai/
- group: company
  title: ''
  type: Website
  url: https://stellarcyber.ai/
- group: start
  title: ''
  type: Login
  url: https://stellarcyber.ai/login/
- group: commercial
  title: ''
  type: Pricing
  url: https://stellarcyber.ai/pricing/
- group: company
  title: ''
  type: Blog
  url: https://stellarcyber.ai/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stellarcyber
created: '2025-02-06'
description: Stellar Cyber is an Open XDR platform that provides AI-driven security operations capabilities including threat detection, investigation, and response. The platform offers an OAS-compliant REST API that enables downstream applications to perform complex queries, join results, analyze data, and automate security operations workflows. Stellar Cyber maintains several sample Python Jupyter Notebooks in GitHub that can help build analyses outside of the platform with the API or connect custom applications.
examples:
- key_count: 4
  name: Stellar Cyber Create Case Example
  slug: stellar-cyber-create-case-example
- key_count: 4
  name: Stellar Cyber List Cases Example
  slug: stellar-cyber-list-cases-example
finops:
- name: Stellar Cyber Finops
  service_category: API
  slug: stellar-cyber-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stellar-cyber.png
json_schemas:
- name: Stellar Cyber Alert
  property_count: 8
  slug: stellar-cyber-alert
- name: Stellar Cyber Case
  property_count: 10
  slug: stellar-cyber-case
json_structures:
- name: Stellar Cyber Case Structure
  property_count: 0
  slug: stellar-cyber-case-structure
jsonld:
- class_count: 23
  name: Stellar Cyber Context
  property_count: 7
  slug: stellar-cyber-context
layout: provider
modified: '2026-05-19'
name: Stellar Cyber
nav: Providers
network: true
overview: 'Stellar Cyber publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Authentication API, Cases API, and 8 more. Tagged areas include Cybersecurity, Security, XDR, SIEM, and SOAR.


  The Stellar Cyber catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Stellar Cyber''s developer surface includes authentication, developer portal, documentation, pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Stellar Cyber Plans Pricing
  plan_count: 3
  slug: stellar-cyber-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Stellar Cyber Rate Limits
  slug: stellar-cyber-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Stellar Cyber API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: stellar-cyber-jsonschema-spectral-rules
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Stellar Cyber API Rules
  rule_count: 11
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 8
  slug: stellar-cyber-rules
score:
  band: developing
  composite: 39.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 58.5
    catalog_earned_first_party: 0.0
    catalog_gap: 56.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 30.3
    commercial_clarity: 30.3
    contract_governance: 13.6
    contract_quality: 62.0
    developer_ergonomics: 39.3
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 10.5
  previous_composite: 40.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stellar-cyber/refs/heads/main/screenshots/stellar-cyber-2026-06-20T194541.png
security:
- kind: authentication
  name: Stellar Cyber Authentication
  slug: stellar-cyber-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Stellar Cyber Domain Security
  slug: stellar-cyber-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Stellar Cyber Trust Center
  slug: stellar-cyber-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: stellar-cyber
tags:
- Cybersecurity
- Security
- XDR
- SIEM
- SOAR
- Artificial Intelligence
website: https://stellarcyber.ai/
---
