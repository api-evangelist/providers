---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The Valence Security REST API enables integration with the Valence platform for ingesting security data from custom sources, exporting alerts and audit logs, and configuring security monitoring via th
  name: Valence Security API
  slug: valence-security-api
artifact_total: 12
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/valence-security-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/valence-security-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/valencesec
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/valence-security
- group: company
  title: ''
  type: Website
  url: https://www.valencesecurity.com
- group: company
  title: ''
  type: Blog
  url: https://www.valencesecurity.com/resources/blogs
- group: docs
  title: ''
  type: Documentation
  url: https://www.valencesecurity.com/resources
- group: other
  title: ''
  type: Connector Studio
  url: https://www.valencesecurity.com/solutions/valence-connector-studio
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/valence-security/refs/heads/main/json-schema/valence-security-alert-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/valence-security/refs/heads/main/json-schema/valence-security-integration-schema.json
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/valence-security/refs/heads/main/json-ld/valence-security-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/valence-security/refs/heads/main/vocabulary/valence-security-vocabulary.yml
created: '2026-03-27'
description: Valence Security is the leader in SaaS and AI Security, built for the agentic era. The platform provides SaaS security posture management (SSPM), AI security posture management (AI-SPM), identity threat detection and response (ITDR), and risk remediation across 175+ SaaS and AI applications including Microsoft 365, Google Workspace, Salesforce, Okta, GitHub, OpenAI, and Anthropic.
examples:
- key_count: 2
  name: Valence Security Alert Example
  slug: valence-security-alert-example
finops:
- name: Valence Security Finops
  service_category: API
  slug: valence-security-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/valence-security.png
json_schemas:
- name: Valence Security Alert
  property_count: 13
  slug: valence-security-alert
- name: Valence Security SaaS Integration
  property_count: 10
  slug: valence-security-integration
json_structures:
- name: Valence Security Alert Structure
  property_count: 0
  slug: valence-security-alert-structure
jsonld:
- class_count: 16
  name: Valence Security Context
  property_count: 0
  slug: valence-security-context
layout: provider
modified: '2026-05-03'
name: Valence Security
nav: Providers
network: true
overview: 'Valence Security publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include SaaS Security, SSPM, AI Security, Identity Security, and ITDR.


  The Valence Security catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Valence Security''s developer surface includes engineering blog, documentation, and 10 more developer resources.'
plans:
- name: Valence Security Plans Pricing
  plan_count: 3
  slug: valence-security-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Valence Security Rate Limits
  slug: valence-security-rate-limits
rules:
- name: Valence Security API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: valence-security-jsonschema-spectral-rules
score:
  band: thin
  composite: 33.9
  delta: -4.7
  facets:
    commercial_clarity: 47.4
    contract_quality: 12.9
    developer_ergonomics: 10.9
    discoverability: 59.3
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 38.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/valence-security/refs/heads/main/screenshots/valence-security-2026-06-20T200753.png
security:
- kind: domain-security
  name: Valence Security Domain Security
  slug: valence-security-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Valence Security Trust Center
  slug: valence-security-trust-center
  summary_line: SOC 2
slug: valence-security
tags:
- SaaS Security
- SSPM
- AI Security
- Identity Security
- ITDR
- Posture Management
- Risk Remediation
website: https://www.valencesecurity.com
---
