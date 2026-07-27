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
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Harbor Compliance Agentic Access
  operation_count: 18
  slug: harbor-compliance-agentic-access
  summary_line: 18 operations · 5 acting
api_count: 6
apis:
- description: Annual reports, compliance filings, and deadline tracking.
  name: Harbor Compliance Compliance Filings API
  slug: harbor-compliance-compliance-filings-api
- description: Business entity management including corporations, LLCs, and other legal entities.
  name: Harbor Compliance Entities API
  slug: harbor-compliance-entities-api
- description: State and jurisdiction information for compliance requirements.
  name: Harbor Compliance Jurisdictions API
  slug: harbor-compliance-jurisdictions-api
- description: Business license applications, renewals, and status tracking across jurisdictions.
  name: Harbor Compliance Licenses API
  slug: harbor-compliance-licenses-api
- description: Compliance service orders and fulfillment tracking.
  name: Harbor Compliance Orders API
  slug: harbor-compliance-orders-api
- description: Registered agent appointment and management for business entities.
  name: Harbor Compliance Registered Agents API
  slug: harbor-compliance-registered-agents-api
artifact_total: 16
collections:
- collection_type: open
  name: Harbor Compliance API
  slug: open-harbor-compliance
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/harbor-compliance-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/harbor-compliance-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/harbor-compliance-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/harbor-compliance
- group: start
  title: ''
  type: Portal
  url: https://developers.harborcompliance.com/
- group: company
  title: ''
  type: Website
  url: https://www.harborcompliance.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.harborcompliance.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.harborcompliance.com/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.harborcompliance.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.harborcompliance.com/contact
- group: start
  title: ''
  type: Login
  url: https://www.harborcompliance.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.harborcompliance.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.harborcompliance.com/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.harborcompliance.com/security
- group: design
  title: ''
  type: JSONLD
  url: json-ld/harbor-compliance-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/harbor-compliance-entity-schema.json
created: '2025-02-17'
description: Harbor Compliance is a compliance management platform that helps businesses streamline compliance workflows, save staff hours, and enhance client relationships. The platform provides tools for managing business licensing, registered agent services, and compliance tracking.
finops:
- name: Harbor Compliance Finops
  service_category: API
  slug: harbor-compliance-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/harbor-compliance.png
json_schemas:
- name: Harbor Compliance Business Entity
  property_count: 12
  slug: harbor-compliance-entity
jsonld:
- class_count: 0
  name: Harbor Compliance Context
  property_count: 5
  slug: harbor-compliance-context
layout: provider
modified: '2026-05-19'
name: Harbor Compliance
nav: Providers
network: true
overview: 'Harbor Compliance publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Compliance Filings API, Entities API, Jurisdictions API, and 3 more. Tagged areas include Business Licensing, Compliance, Legal, and Regulatory.


  The Harbor Compliance catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Harbor Compliance''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, support, and 10 more developer resources.'
plans:
- name: Harbor Compliance Plans Pricing
  plan_count: 3
  slug: harbor-compliance-plans-pricing
random_paper: 34
rate_limits:
- limit_count: 5
  name: Harbor Compliance Rate Limits
  slug: harbor-compliance-rate-limits
rules:
- name: Harbor Compliance API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: harbor-compliance-jsonschema-spectral-rules
score:
  band: strong
  composite: 63.2
  delta: 3.4
  facets:
    commercial_clarity: 73.7
    contract_quality: 69.9
    developer_ergonomics: 45.7
    discoverability: 75.0
    governance: 73.7
    operational_transparency: 42.1
  previous_composite: 59.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/harbor-compliance/refs/heads/main/screenshots/harbor-compliance-2026-06-20T182514.png
security:
- kind: authentication
  name: Harbor Compliance Authentication
  slug: harbor-compliance-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Harbor Compliance Domain Security
  slug: harbor-compliance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: harbor-compliance
tags:
- Business Licensing
- Compliance
- Legal
- Regulatory
website: https://www.harborcompliance.com/
---
