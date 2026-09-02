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
    error_semantics: verified
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
  score: 25.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Litmus Agentic Access
  operation_count: 21
  slug: litmus-agentic-access
  summary_line: 21 operations · 5 acting
api_count: 3
apis:
- description: Campaign engagement metrics and breakdowns
  name: Litmus Analytics API
  slug: litmus-analytics-api
- description: Email campaign tracking and management
  name: Litmus Campaigns API
  slug: litmus-campaigns-api
- description: Available email client configurations
  name: Litmus Clients API
  slug: litmus-clients-api
- description: Email preview generation and management
  name: Litmus Previews API
  slug: litmus-previews-api
- description: Test result retrieval
  name: Litmus Results API
  slug: litmus-results-api
- description: Email test creation and management
  name: Litmus Tests API
  slug: litmus-tests-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Litmus Email Analytics API
  slug: open-litmus-analytics-api
- collection_type: open
  name: Litmus Email Analytics Campaigns API
  slug: open-litmus-campaigns-api
- collection_type: open
  name: Litmus Email Analytics Clients API
  slug: open-litmus-clients-api
- collection_type: open
  name: Litmus Email Analytics API
  slug: open-litmus-email-analytics
- collection_type: open
  name: Litmus Instant API
  slug: open-litmus-instant
- collection_type: open
  name: Litmus Email Analytics Results API
  slug: open-litmus-results-api
- collection_type: open
  name: Litmus Email Analytics Tests API
  slug: open-litmus-tests-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/litmus-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/litmus-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/litmus-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/litmus-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/litmus
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/litmus-com
- group: company
  title: ''
  type: Website
  url: https://www.litmus.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.litmus.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.litmus.com/getting-started/test-your-email
- group: company
  title: ''
  type: Blog
  url: https://www.litmus.com/blog/
- group: operate
  title: ''
  type: Community
  url: https://litmus.com/community
- group: auth
  title: ''
  type: Authentication
  url: https://docs.litmus.com/oauth-integration-guide
- group: auth
  title: ''
  type: Authentication
  url: https://docs.litmus.com/oauth/web-application-flow
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/litmus-email-test-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/litmus-context.jsonld
created: '2025-01-01'
description: Email testing and analytics platform that allows developers and marketers to preview, test, and analyze email campaigns across multiple email clients and devices before sending.
finops:
- name: Litmus Finops
  service_category: Email Testing / Marketing Tools
  slug: litmus-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/litmus.png
json_schemas:
- name: Litmus Email Test
  property_count: 13
  slug: litmus-email-test
jsonld:
- class_count: 7
  name: Litmus Context
  property_count: 46
  slug: litmus-context
layout: provider
modified: '2026-05-19'
name: Litmus
nav: Providers
network: true
overview: 'Litmus publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Campaigns API, Clients API, and 3 more. Tagged areas include Developer Tools, Email Testing, Marketing Tools, and Quality Assurance.


  The Litmus catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Litmus'' developer surface includes authentication, documentation, getting-started guide, engineering blog, and 11 more developer resources.'
plans:
- name: Litmus Plans Pricing
  plan_count: 7
  slug: litmus-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 4
  name: Litmus Rate Limits
  slug: litmus-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Litmus API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: litmus-jsonschema-spectral-rules
score:
  band: thin
  composite: 37.2
  coverage:
    artifact_dirs: 13
    catalog_gap: 61.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 9.8
    contract_quality: 65.0
    developer_ergonomics: 40.5
    discoverability: 55.6
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 37.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/litmus/refs/heads/main/screenshots/litmus-2026-06-20T184609.png
security:
- kind: authentication
  name: Litmus Authentication
  slug: litmus-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Litmus Domain Security
  slug: litmus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Litmus Trust Center
  slug: litmus-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: litmus
tags:
- Developer Tools
- Email Testing
- Marketing Tools
- Quality Assurance
website: https://www.litmus.com/
---
