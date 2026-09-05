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
    agentic_commerce: false
    auth_clarity: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
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
- effective_rule_count: 5
  extends: []
  name: Valence Security API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: valence-security-jsonschema-spectral-rules
score:
  band: emerging
  composite: 20.1
  coverage:
    artifact_dirs: 12
    catalog_earned: 57.3
    catalog_earned_first_party: 0.0
    catalog_gap: 57.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 25.0
    contract_quality: 10.7
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 25.0
    operational_transparency: 10.5
  previous_composite: 20.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
