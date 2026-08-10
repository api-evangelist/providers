---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Whatfix Agentic Access
  operation_count: 9
  slug: whatfix-agentic-access
  summary_line: 9 operations · 1 acting
api_count: 5
apis:
- description: The Analytics API from Whatfix — 4 operation(s) for analytics.
  name: Whatfix Analytics API
  slug: whatfix-analytics-api
- description: The Content API from Whatfix — 1 operation(s) for content.
  name: Whatfix Content API
  slug: whatfix-content-api
- description: The End Users API from Whatfix — 2 operation(s) for end users.
  name: Whatfix End Users API
  slug: whatfix-end-users-api
- description: The Reports API from Whatfix — 1 operation(s) for reports.
  name: Whatfix Reports API
  slug: whatfix-reports-api
- description: The Segments API from Whatfix — 1 operation(s) for segments.
  name: Whatfix Segments API
  slug: whatfix-segments-api
artifact_total: 24
collections:
- collection_type: open
  name: Whatfix API
  slug: open-whatfix
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/whatfix-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/whatfix-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/whatfix-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/whatfix-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/whatfix
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/whatfix
- group: company
  title: ''
  type: Website
  url: https://whatfix.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.whatfix.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/whatfix-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/whatfix-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/whatfix-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://whatfix.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://whatfix.com/blog/feed/
created: '2026-05-08'
description: Whatfix is a Digital Adoption Platform that delivers in-app guidance, self-help, and product analytics to drive software adoption and user productivity.
examples:
- key_count: 2
  name: Whatfix Get Flow Analytics Example
  slug: whatfix-get-flow-analytics-example
- key_count: 2
  name: Whatfix List Content Example
  slug: whatfix-list-content-example
- key_count: 2
  name: Whatfix List End Users Example
  slug: whatfix-list-end-users-example
- key_count: 2
  name: Whatfix Upsert End User Example
  slug: whatfix-upsert-end-user-example
finops:
- name: Whatfix Finops
  service_category: Product
  slug: whatfix-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/whatfix.png
json_schemas:
- name: Whatfix Content
  property_count: 8
  slug: whatfix-content
- name: Whatfix End User
  property_count: 6
  slug: whatfix-end-user
json_structures:
- name: Whatfix Content Structure
  property_count: 0
  slug: whatfix-content-structure
- name: Whatfix End User Structure
  property_count: 0
  slug: whatfix-end-user-structure
jsonld:
- class_count: 38
  name: Whatfix Context
  property_count: 0
  slug: whatfix-context
layout: provider
modified: '2026-05-19'
name: Whatfix
nav: Providers
network: true
overview: 'Whatfix publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Content API, End Users API, and 2 more. Tagged areas include Digital Adoption, In-App Guidance, Onboarding, Analytics, and Self-Help.


  The Whatfix catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Whatfix''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Whatfix Plans Pricing
  plan_count: 1
  slug: whatfix-plans-pricing
random_paper: 67
rate_limits:
- limit_count: 1
  name: Whatfix Rate Limits
  slug: whatfix-rate-limits
rules:
- name: Whatfix API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: whatfix-jsonschema-spectral-rules
- name: Whatfix API Rules
  rule_count: 10
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 6
  slug: whatfix-rules
score:
  band: developing
  composite: 45.7
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 68.5
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 45.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/whatfix/refs/heads/main/screenshots/whatfix-2026-06-20T201422.png
security:
- kind: authentication
  name: Whatfix Authentication
  slug: whatfix-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Whatfix Domain Security
  slug: whatfix-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Whatfix Trust Center
  slug: whatfix-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, GDPR, CSA STAR
slug: whatfix
tags:
- Digital Adoption
- In-App Guidance
- Onboarding
- Analytics
- Self-Help
website: https://whatfix.com/
---
