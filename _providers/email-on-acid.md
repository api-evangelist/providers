---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Email On Acid Agentic Access
  operation_count: 23
  slug: email-on-acid-agentic-access
  summary_line: 23 operations · 6 acting
api_count: 1
apis:
- description: Verify API credentials
  name: Email on Acid Authentication API
  slug: email-on-acid-authentication-api
- description: Manage email client lists and defaults for testing
  name: Email on Acid Email Clients API
  slug: email-on-acid-email-clients-api
- description: Create and manage email rendering tests
  name: Email on Acid Email Testing API
  slug: email-on-acid-email-testing-api
- description: Standalone spam filter analysis and seed list management
  name: Email on Acid Spam Testing API
  slug: email-on-acid-spam-testing-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Email on Acid Authentication API
  slug: open-email-on-acid-authentication-api
- collection_type: open
  name: Email on Acid Authentication Email Clients API
  slug: open-email-on-acid-email-clients-api
- collection_type: open
  name: Email on Acid Authentication Email Testing API
  slug: open-email-on-acid-email-testing-api
- collection_type: open
  name: Email on Acid Authentication Spam Testing API
  slug: open-email-on-acid-spam-testing-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/email-on-acid-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/email-on-acid-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/email-on-acid-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/email-on-acid-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.emailonacid.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.emailonacid.com/docs/latest
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/emailonacid
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/email-on-acid
- group: company
  title: ''
  type: Blog
  url: https://www.emailonacid.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.emailonacid.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.emailonacid.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/EmailOnAcid
- group: commercial
  title: ''
  type: Plans
  url: plans/email-on-acid-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/email-on-acid-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/email-on-acid-finops.yml
created: '2026-06-13'
description: Email on Acid (now branded as Mailgun Inspect) is an email testing and pre-deployment quality assurance platform with a REST API for rendering email previews across 100+ email clients and devices, checking accessibility compliance (WCAG 2.2), validating HTML/CSS compatibility, running spam filter analysis, and automating pre-send email testing workflows via HTTP Basic Authentication.
examples:
- key_count: 7
  name: Create Email Test
  slug: create-email-test
- key_count: 6
  name: Create Spam Test
  slug: create-spam-test
- key_count: 4
  name: Email Test Response
  slug: email-test-response
- key_count: 3
  name: Email Test Results
  slug: email-test-results
finops:
- name: Email On Acid Finops
  service_category: ''
  slug: email-on-acid-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/email-on-acid.png
json_schemas:
- name: CreateEmailTestRequest
  property_count: 13
  slug: email-test-request
- name: EmailTestResult
  property_count: 0
  slug: email-test-response
- name: CreateSpamTestRequest
  property_count: 12
  slug: spam-test-request
jsonld:
- class_count: 9
  name: Email On Acid Context
  property_count: 46
  slug: email-on-acid-context
layout: provider
modified: '2026-06-13'
name: Email on Acid
nav: Providers
network: true
overview: 'Email on Acid publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Email Clients API, Email Testing API, and 1 more. Tagged areas include Email Testing, Email Previews, Email Clients, Spam Testing, and Accessibility.


  The Email on Acid catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Email on Acid''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Email On Acid Plans Pricing
  plan_count: 3
  slug: email-on-acid-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 4
  name: Email On Acid Rate Limits
  slug: email-on-acid-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Email on Acid API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: email-on-acid-jsonschema-spectral-rules
score:
  band: developing
  composite: 47.5
  coverage:
    artifact_dirs: 15
    catalog_gap: 36.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 9.8
    contract_quality: 65.2
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 52.6
  previous_composite: 47.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/email-on-acid/refs/heads/main/screenshots/email-on-acid-2026-06-20T180618.png
security:
- kind: authentication
  name: Email On Acid Authentication
  slug: email-on-acid-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Email On Acid Domain Security
  slug: email-on-acid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Email On Acid Trust Center
  slug: email-on-acid-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: email-on-acid
tags:
- Email Testing
- Email Previews
- Email Clients
- Spam Testing
- Accessibility
- HTML Validation
- Email Quality Assurance
- Pre-Deployment Testing
website: https://www.emailonacid.com
---
