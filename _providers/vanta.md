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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 11
  human_in_the_loop: 1
  name: Vanta Agentic Access
  operation_count: 37
  slug: vanta-agentic-access
  summary_line: 37 operations · 11 acting · 1 human-in-the-loop
api_count: 11
apis:
- description: The Auditors API from Vanta — 1 operation(s) for auditors.
  name: Vanta Auditors API
  slug: vanta-auditors-api
- description: The Audits API from Vanta — 15 operation(s) for audits.
  name: Vanta Audits API
  slug: vanta-audits-api
- description: OAuth 2.0 token management
  name: Vanta Authentication API
  slug: vanta-authentication-api
- description: Compliance controls and framework management
  name: Vanta Controls API
  slug: vanta-controls-api
- description: Compliance evidence document management
  name: Vanta Documents API
  slug: vanta-documents-api
- description: Integration configuration and status management
  name: Vanta Integrations API
  slug: vanta-integrations-api
- description: Monitored resource management and scoping
  name: Vanta Resources API
  slug: vanta-resources-api
- description: Automated test results and evidence
  name: Vanta Tests API
  slug: vanta-tests-api
- description: User and personnel management
  name: Vanta Users API
  slug: vanta-users-api
- description: Third-party vendor security review management
  name: Vanta Vendors API
  slug: vanta-vendors-api
- description: Vulnerability tracking and remediation management
  name: Vanta Vulnerabilities API
  slug: vanta-vulnerabilities-api
artifact_total: 44
collections:
- collection_type: postman
  name: Conduct an audit Auditors API
  slug: postman-vanta-auditors-api
- collection_type: postman
  name: Conduct an audit Auditors Audits API
  slug: postman-vanta-audits-api
- collection_type: postman
  name: Conduct an audit Auditors Authentication API
  slug: postman-vanta-authentication-api
- collection_type: postman
  name: Conduct an audit Auditors Controls API
  slug: postman-vanta-controls-api
- collection_type: postman
  name: Conduct an audit Auditors Documents API
  slug: postman-vanta-documents-api
- collection_type: postman
  name: Conduct an audit Auditors Integrations API
  slug: postman-vanta-integrations-api
- collection_type: postman
  name: Conduct an audit Auditors Resources API
  slug: postman-vanta-resources-api
- collection_type: postman
  name: Conduct an audit Auditors Tests API
  slug: postman-vanta-tests-api
- collection_type: postman
  name: Conduct an audit Auditors Users API
  slug: postman-vanta-users-api
- collection_type: postman
  name: Conduct an audit Auditors Vendors API
  slug: postman-vanta-vendors-api
- collection_type: postman
  name: Conduct an audit Auditors Vulnerabilities API
  slug: postman-vanta-vulnerabilities-api
- collection_type: open
  name: Conduct an audit
  slug: open-vanta-auditor
- collection_type: open
  name: Vanta API
  slug: open-vanta
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/vanta/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vanta-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/vanta-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vanta-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vanta-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/vanta-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vanta-security
- group: start
  title: ''
  type: Portal
  url: https://developer.vanta.com/docs/vanta-api-overview
- group: auth
  title: ''
  type: Authentication
  url: https://developer.vanta.com/docs/api-access-setup
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.vanta.com/docs/vanta-first-api-request
- group: build
  title: ''
  type: PostmanCollection
  url: https://developer.vanta.com/docs/vanta-postman-setup
- group: operate
  title: ''
  type: FAQ
  url: https://developer.vanta.com/docs/faq
- group: docs
  title: ''
  type: Documentation
  url: https://developer.vanta.com/docs/build-integrations
- group: docs
  title: ''
  type: Documentation
  url: https://developer.vanta.com/docs/manage-vendors
- group: company
  title: ''
  type: Blog
  url: https://www.vanta.com/resources/introducing-vantas-connectors-api
- group: other
  title: ''
  type: Product
  url: https://www.vanta.com/products/vanta-api
- group: build
  title: ''
  type: SDKs
  url: https://github.com/VantaInc/vanta-auditor-api-sdk-typescript
- group: build
  title: ''
  type: SDKs
  url: https://github.com/VantaInc/vanta-auditor-api-sdk-java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/VantaInc/vanta-mcp-server
- group: build
  title: ''
  type: SDKs
  url: https://github.com/VantaInc/eslint-plugin-vanta
- group: docs
  title: ''
  type: Schema
  url: https://github.com/VantaInc/vanta-control-set
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.vanta.com/resources/new-in-vanta-april-2026
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/vanta/refs/heads/main/openapi/vanta-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/vanta/refs/heads/main/openapi/vanta-auditor-openapi.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.vanta.com/llms.txt
created: '2024-11-14'
description: Vanta is a trust management platform that automates security compliance for frameworks including SOC 2, ISO 27001, HIPAA, PCI DSS, and GDPR. The Vanta API enables organizations to programmatically manage their compliance posture, automate security monitoring, manage vulnerabilities, track controls, manage vendors, and integrate with existing tools and workflows.
examples:
- key_count: 2
  name: Vanta Create Vendor Example
  slug: vanta-create-vendor-example
- key_count: 2
  name: Vanta List Computers Example
  slug: vanta-list-computers-example
- key_count: 2
  name: Vanta List Controls Example
  slug: vanta-list-controls-example
- key_count: 2
  name: Vanta List Vulnerabilities Example
  slug: vanta-list-vulnerabilities-example
finops:
- name: Vanta Finops
  service_category: API
  slug: vanta-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vanta.png
json_schemas:
- name: Vanta Control
  property_count: 8
  slug: vanta-control
- name: Vanta Vendor
  property_count: 10
  slug: vanta-vendor
- name: Vanta Vulnerability
  property_count: 11
  slug: vanta-vulnerability
json_structures:
- name: Vanta Vendor Structure
  property_count: 0
  slug: vanta-vendor-structure
- name: Vanta Vulnerability Structure
  property_count: 0
  slug: vanta-vulnerability-structure
jsonld:
- class_count: 15
  name: Vanta Context
  property_count: 27
  slug: vanta-context
layout: provider
modified: '2026-05-19'
name: Vanta
nav: Providers
network: true
overview: 'Vanta publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Auditors API, Audits API, Authentication API, and 8 more. Tagged areas include Cybersecurity, Compliance, Security, Governance, and Risk Management.


  The Vanta catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Vanta''s developer surface includes authentication, developer portal, getting-started guide, FAQ, documentation, engineering blog, changelog, and 18 more developer resources.'
plans:
- name: Vanta Plans Pricing
  plan_count: 3
  slug: vanta-plans-pricing
random_paper: 46
rate_limits:
- limit_count: 5
  name: Vanta Rate Limits
  slug: vanta-rate-limits
rules:
- name: Vanta API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: vanta-jsonschema-spectral-rules
- name: Vanta API Rules
  rule_count: 10
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 7
  slug: vanta-rules
scopes:
- name: Vanta Scopes
  scope_count: 8
  slug: vanta-scopes
  summary_line: 8 scopes · clientCredentials
score:
  band: strong
  composite: 57.4
  delta: -4.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 67.1
    developer_ergonomics: 60.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 47.4
  previous_composite: 61.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vanta/refs/heads/main/screenshots/vanta-2026-06-20T200811.png
security:
- kind: authentication
  name: Vanta Authentication
  slug: vanta-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Vanta Domain Security
  slug: vanta-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Vanta Vulnerability Disclosure
  slug: vanta-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: vanta
tags:
- Cybersecurity
- Compliance
- Security
- Governance
- Risk Management
website: https://developer.vanta.com/docs/vanta-api-overview
---
