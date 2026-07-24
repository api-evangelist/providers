---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 27
  human_in_the_loop: 2
  name: Trellix Web Gateway Agentic Access
  operation_count: 63
  slug: trellix-web-gateway-agentic-access
  summary_line: 63 operations · 27 acting · 2 human-in-the-loop
api_count: 17
apis:
- description: Anti-malware scanning configuration
  name: Trellix Web Gateway Anti-Malware API
  slug: trellix-web-gateway-anti-malware-api
- description: Authentication policy settings
  name: Trellix Web Gateway Authentication API
  slug: trellix-web-gateway-authentication-api
- description: Configuration management and commit operations
  name: Trellix Web Gateway Configuration API
  slug: trellix-web-gateway-configuration-api
- description: Dashboard data for visualization
  name: Trellix Web Gateway Dashboards API
  slug: trellix-web-gateway-dashboards-api
- description: DLP policy configuration
  name: Trellix Web Gateway Data Loss Prevention API
  slug: trellix-web-gateway-data-loss-prevention-api
- description: File upload and download operations
  name: Trellix Web Gateway Files API
  slug: trellix-web-gateway-files-api
- description: Manage custom lists used in policy rules
  name: Trellix Web Gateway Lists API
  slug: trellix-web-gateway-lists-api
- description: Report generation and retrieval
  name: Trellix Web Gateway Reports API
  slug: trellix-web-gateway-reports-api
- description: Manage policy rule sets
  name: Trellix Web Gateway Rule Sets API
  slug: trellix-web-gateway-rule-sets-api
- description: Manage individual policy rules within rule sets
  name: Trellix Web Gateway Rules API
  slug: trellix-web-gateway-rules-api
- description: Security event and threat detection data
  name: Trellix Web Gateway Security Events API
  slug: trellix-web-gateway-security-events-api
- description: SSL/TLS inspection configuration
  name: Trellix Web Gateway SSL Scanning API
  slug: trellix-web-gateway-ssl-scanning-api
- description: Aggregated traffic and security statistics
  name: Trellix Web Gateway Statistics API
  slug: trellix-web-gateway-statistics-api
- description: System information and appliance management
  name: Trellix Web Gateway System API
  slug: trellix-web-gateway-system-api
- description: Web traffic log access and search
  name: Trellix Web Gateway Traffic Logs API
  slug: trellix-web-gateway-traffic-logs-api
- description: Log access and diagnostic operations
  name: Trellix Web Gateway Troubleshooting API
  slug: trellix-web-gateway-troubleshooting-api
- description: URL categorization and filtering settings
  name: Trellix Web Gateway URL Filtering API
  slug: trellix-web-gateway-url-filtering-api
artifact_total: 33
collections:
- collection_type: open
  name: Trellix Web Gateway Policy API
  slug: open-trellix-web-gateway-policy
- collection_type: open
  name: Trellix Web Gateway Reporting API
  slug: open-trellix-web-gateway-reporting
- collection_type: open
  name: Trellix Web Gateway REST API
  slug: open-trellix-web-gateway-rest
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/trellix-web-gateway-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trellix-web-gateway-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trellix-web-gateway-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trellixsecurity
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.trellix.com/bundle/web-gateway-getting-started
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.trellix.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.trellix.com/bundle/web-gateway-release-notes
- group: operate
  title: ''
  type: StatusPage
  url: https://status.trellix.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.trellix.com/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trellix.com/privacy/
- group: start
  title: ''
  type: Portal
  url: https://www.trellix.com/login/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/trellix-enterprise/mwg-sdk
- group: design
  title: ''
  type: JSONLD
  url: json-ld/trellix-web-gateway-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/trellix-web-gateway-security-event-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/trellix-web-gateway-rule-set-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/trellix-web-gateway-security-event-structure.json
- group: design
  title: ''
  type: SpectralRules
  url: rules/trellix-web-gateway-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/trellix-web-gateway-vocabulary.yml
created: '2024'
description: Trellix Web Gateway (formerly McAfee Web Gateway) provides advanced threat protection and secure web access for enterprises. It offers URL filtering, malware detection, data loss prevention, SSL inspection, and cloud security capabilities through a comprehensive web security platform with REST APIs for appliance management, policy configuration, and security reporting.
examples:
- key_count: 2
  name: Trellix Web Gateway Get Security Events Example
  slug: trellix-web-gateway-get-security-events-example
finops:
- name: Trellix Web Gateway Finops
  service_category: Cybersecurity
  slug: trellix-web-gateway-finops
image: https://www.trellix.com/assets/images/trellix-logo.png
json_schemas:
- name: Trellix Web Gateway Rule Set
  property_count: 8
  slug: trellix-web-gateway-rule-set
- name: Trellix Web Gateway Security Event
  property_count: 11
  slug: trellix-web-gateway-security-event
json_structures:
- name: Trellix Web Gateway Security Event Structure
  property_count: 0
  slug: trellix-web-gateway-security-event-structure
jsonld:
- class_count: 0
  name: Trellix Web Gateway Context
  property_count: 9
  slug: trellix-web-gateway-context
layout: provider
modified: '2026-05-19'
name: Trellix Web Gateway
nav: Providers
network: true
overview: 'Trellix Web Gateway publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Anti-Malware API, Authentication API, Configuration API, and 14 more. Tagged areas include Cybersecurity, Data Loss Prevention, Enterprise Security, Malware Protection, and Network Security.


  The Trellix Web Gateway catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Trellix Web Gateway''s developer surface includes authentication, getting-started guide, changelog, developer portal, and 14 more developer resources.'
plans:
- name: Trellix Web Gateway Plans Pricing
  plan_count: 1
  slug: trellix-web-gateway-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 1
  name: Trellix Web Gateway Rate Limits
  slug: trellix-web-gateway-rate-limits
rules:
- name: Trellix Web Gateway API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: trellix-web-gateway-jsonschema-spectral-rules
- name: Trellix Web Gateway API Rules
  rule_count: 19
  severity_counts:
    error: 3
    hint: 0
    info: 4
    warn: 12
  slug: trellix-web-gateway-spectral-rules
score:
  band: developing
  composite: 57.6
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 64.6
    developer_ergonomics: 37.0
    discoverability: 67.5
    governance: 86.8
    operational_transparency: 52.6
  previous_composite: 57.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trellix-web-gateway/refs/heads/main/screenshots/trellix-web-gateway-2026-06-20T195750.png
security:
- kind: authentication
  name: Trellix Web Gateway Authentication
  slug: trellix-web-gateway-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Trellix Web Gateway Domain Security
  slug: trellix-web-gateway-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: trellix-web-gateway
tags:
- Cybersecurity
- Data Loss Prevention
- Enterprise Security
- Malware Protection
- Network Security
- SSL Inspection
- Threat Protection
- URL Filtering
- Web Gateway
website: https://developer.trellix.com/
---
