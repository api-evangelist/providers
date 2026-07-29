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
  name: Debounce Agentic Access
  operation_count: 6
  slug: debounce-agentic-access
  summary_line: 6 operations · 1 acting
api_count: 4
apis:
- description: Account balance and usage history
  name: DeBounce Account API
  slug: debounce-account-api
- description: Bulk email list upload and status
  name: DeBounce Bulk API
  slug: debounce-bulk-api
- description: Data enrichment and disposable email detection
  name: DeBounce Data API
  slug: debounce-data-api
- description: Email address validation endpoints
  name: DeBounce Validation API
  slug: debounce-validation-api
artifact_total: 18
collections:
- collection_type: postman
  name: DeBounce Email Validation Account API
  slug: postman-debounce-account-api
- collection_type: postman
  name: DeBounce Email Validation Account Bulk API
  slug: postman-debounce-bulk-api
- collection_type: postman
  name: DeBounce Email Validation Account Data API
  slug: postman-debounce-data-api
- collection_type: postman
  name: DeBounce Email Account Validation API
  slug: postman-debounce-validation-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/debounce/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/debounce-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/debounce-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/debounce-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://debounce.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.debounce.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/debounceio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/debounceio
- group: company
  title: ''
  type: Blog
  url: https://debounce.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://debounce.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.debounce.com/
- group: other
  title: ''
  type: X
  url: https://x.com/debounceio
- group: commercial
  title: ''
  type: Plans
  url: plans/debounce-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/debounce-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/debounce-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/debounce-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/debounce-context.jsonld
- group: company
  title: ''
  type: BlogPosts
  url: blogs/blogs.json
created: '2026-06-12'
description: DeBounce is an email validation and verification REST API that helps developers ensure the deliverability and quality of email addresses at scale. The API supports real-time single email validation, asynchronous bulk list processing, and data enrichment via reverse email lookup. It detects disposable addresses, role-based emails, catch-all domains, syntax errors, and performs MX record and SMTP-level mailbox verification. DeBounce offers pay-as-you-go credit-based pricing with no monthly subscription required, full API access at every tier, and credits that never expire.
examples:
- key_count: 9
  name: Debounce Single Validation Example
  slug: debounce-single-validation-example
finops:
- name: Debounce Finops
  service_category: ''
  slug: debounce-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/debounce.png
json_schemas:
- name: DeBounce Validation Result
  property_count: 3
  slug: debounce-validation-result
jsonld:
- class_count: 14
  name: Debounce Context
  property_count: 32
  slug: debounce-context
layout: provider
modified: '2026-06-12'
name: DeBounce
nav: Providers
network: true
overview: 'DeBounce publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Account API, Bulk API, Data API, and 1 more. Tagged areas include Email Validation, Email Verification, Deliverability, Disposable Email Detection, and MX Records.


  The DeBounce catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DeBounce''s developer surface includes authentication, documentation, engineering blog, pricing, and 14 more developer resources.'
plans:
- name: Debounce Plans Pricing
  plan_count: 9
  slug: debounce-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 4
  name: Debounce Rate Limits
  slug: debounce-rate-limits
rules:
- name: DeBounce API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: debounce-jsonschema-spectral-rules
score:
  band: strong
  composite: 57.2
  delta: -3.6
  facets:
    commercial_clarity: 50.0
    contract_quality: 78.0
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 60.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/debounce/refs/heads/main/screenshots/debounce-2026-06-20T175751.png
security:
- kind: authentication
  name: Debounce Authentication
  slug: debounce-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Debounce Domain Security
  slug: debounce-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: debounce
tags:
- Email Validation
- Email Verification
- Deliverability
- Disposable Email Detection
- MX Records
- Bulk Email Validation
- Data Enrichment
- Syntax Validation
website: https://debounce.com/
---
