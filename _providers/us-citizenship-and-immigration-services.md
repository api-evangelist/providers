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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Us Citizenship And Immigration Services Agentic Access
  operation_count: 3
  slug: us-citizenship-and-immigration-services-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 2
apis:
- description: Immigration case status retrieval by receipt number
  name: US Citizenship and Immigration Services Case Status API
  slug: us-citizenship-and-immigration-services-case-status-api
- description: Submit and manage FOIA and Privacy Act requests for Alien File records
  name: US Citizenship and Immigration Services FOIA Requests API
  slug: us-citizenship-and-immigration-services-foia-requests-api
artifact_total: 18
collections:
- collection_type: open
  name: USCIS Case Status API
  slug: open-uscis-case-status-api
- collection_type: open
  name: USCIS FOIA Request and Status API
  slug: open-uscis-foia-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/us-citizenship-and-immigration-services-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/us-citizenship-and-immigration-services-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/us-citizenship-and-immigration-services-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/us-citizenship-and-immigration-services-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/uscis
created: '2024-12-03'
description: The US Citizenship and Immigration Services (USCIS) is a government agency responsible for overseeing lawful immigration to the United States. Its primary function is to process and adjudicate applications for various immigration benefits, such as green cards, work permits, and naturalization. USCIS provides a public developer portal (developer.uscis.gov) with APIs for case status lookup and FOIA request submission. The Torch API Program enables qualified software developers to integrate USCIS services into immigration case management applications, providing OAuth 2.0 secured access to case status information and Freedom of Information Act (FOIA) request capabilities.
examples:
- key_count: 2
  name: Uscis Get Case Status Example
  slug: uscis-get-case-status-example
- key_count: 2
  name: Uscis Submit Foia Request Example
  slug: uscis-submit-foia-request-example
finops:
- name: Us Citizenship And Immigration Services Finops
  service_category: API
  slug: us-citizenship-and-immigration-services-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/us-citizenship-and-immigration-services.png
json_schemas:
- name: USCIS Case Status
  property_count: 8
  slug: uscis-case-status
json_structures:
- name: Uscis Case Status Structure
  property_count: 0
  slug: uscis-case-status-structure
jsonld:
- class_count: 1
  name: Us Citizenship And Immigration Services Context
  property_count: 25
  slug: us-citizenship-and-immigration-services-context
layout: provider
modified: '2026-05-19'
name: US Citizenship and Immigration Services
nav: Providers
network: true
overview: 'US Citizenship and Immigration Services publishes 2 APIs on the [APIs.io](https://apis.io/) network: Case Status API and FOIA Requests API. Tagged areas include Federal Government, Immigration, Citizenship, Case Status, and FOIA.


  The US Citizenship and Immigration Services catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  US Citizenship and Immigration Services'' developer surface includes authentication and 4 more developer resources.'
plans:
- name: Us Citizenship And Immigration Services Plans Pricing
  plan_count: 3
  slug: us-citizenship-and-immigration-services-plans-pricing
random_paper: 77
rate_limits:
- limit_count: 5
  name: Us Citizenship And Immigration Services Rate Limits
  slug: us-citizenship-and-immigration-services-rate-limits
rules:
- name: US Citizenship and Immigration Services API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: us-citizenship-and-immigration-services-jsonschema-spectral-rules
- name: US Citizenship and Immigration Services API Rules
  rule_count: 12
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 8
  slug: uscis-api-rules
scopes:
- name: Us Citizenship And Immigration Services Scopes
  scope_count: 3
  slug: us-citizenship-and-immigration-services-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: developing
  composite: 46.0
  delta: -4.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 72.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 50.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/us-citizenship-and-immigration-services/refs/heads/main/screenshots/us-citizenship-and-immigration-services-2026-06-20T200606.png
security:
- kind: authentication
  name: Us Citizenship And Immigration Services Authentication
  slug: us-citizenship-and-immigration-services-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Us Citizenship And Immigration Services Domain Security
  slug: us-citizenship-and-immigration-services-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: us-citizenship-and-immigration-services
tags:
- Federal Government
- Immigration
- Citizenship
- Case Status
- FOIA
---
