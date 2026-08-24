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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.9
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Zoho Sign Agentic Access
  operation_count: 9
  slug: zoho-sign-agentic-access
  summary_line: 9 operations · 3 acting
api_count: 4
apis:
- description: The Accounts API from Zoho Sign — 1 operation(s) for accounts.
  name: Zoho Sign Accounts API
  slug: zoho-sign-accounts-api
- description: The Requests API from Zoho Sign — 2 operation(s) for requests.
  name: Zoho Sign Requests API
  slug: zoho-sign-requests-api
- description: The Templates API from Zoho Sign — 2 operation(s) for templates.
  name: Zoho Sign Templates API
  slug: zoho-sign-templates-api
- description: The Users API from Zoho Sign — 1 operation(s) for users.
  name: Zoho Sign Users API
  slug: zoho-sign-users-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zoho Sign Accounts API
  slug: open-zoho-sign-accounts-api
- collection_type: open
  name: Zoho Sign Accounts Requests API
  slug: open-zoho-sign-requests-api
- collection_type: open
  name: Zoho Sign Accounts Templates API
  slug: open-zoho-sign-templates-api
- collection_type: open
  name: Zoho Sign Accounts Users API
  slug: open-zoho-sign-users-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zoho-sign-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zoho-sign-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zoho-sign-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zoho-sign-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zoho-sign-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.zoho.com/sign/
- group: docs
  title: ''
  type: Documentation
  url: https://www.zoho.com/sign/api/introduction.html
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/zoho
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zohosign
- group: company
  title: ''
  type: Blog
  url: https://www.zoho.com/blog/sign/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zoho.com/sign/pricing.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zoho.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/ZohoSign
- group: commercial
  title: ''
  type: Plans
  url: plans/zoho-sign-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zoho-sign-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zoho-sign-finops.yml
created: 2026-06-13
description: Zoho Sign is a cloud-based electronic signature platform that provides a REST API for sending documents for signature, managing templates, tracking signing status, and automating signature workflows. The API supports OAuth 2.0 authentication and enables developers to create envelopes, manage recipients, configure signing fields, trigger bulk sends, and retrieve audit trails programmatically. Over 25,000 envelopes are sent daily through Zoho Sign APIs, covering use cases from simple document signing to embedded signing, in-person signing, and enterprise compliance workflows including 21 CFR Part 11 and QES.
examples:
- key_count: 5
  name: Create Request
  slug: create-request
- key_count: 5
  name: List Requests
  slug: list-requests
- key_count: 4
  name: List Templates
  slug: list-templates
finops:
- name: Zoho Sign Finops
  service_category: ''
  slug: zoho-sign-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zoho-sign.png
json_schemas:
- name: Zoho Sign API Schemas
  property_count: 0
  slug: zoho-sign
jsonld:
- class_count: 0
  name: Zoho Sign Context
  property_count: 0
  slug: zoho-sign
layout: provider
modified: 2026-06-13
name: Zoho Sign
nav: Providers
network: true
overview: 'Zoho Sign publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Requests API, Templates API, and 1 more. Tagged areas include Electronic Signatures, E-Signature, Document-Management, Digital Signatures, and Signature Workflows.


  The Zoho Sign catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Zoho Sign''s developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Zoho Sign Plans Pricing
  plan_count: 5
  slug: zoho-sign-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Zoho Sign Rate Limits
  slug: zoho-sign-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Zoho Sign API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: zoho-sign-jsonschema-spectral-rules
scopes:
- name: Zoho Sign Scopes
  scope_count: 3
  slug: zoho-sign-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 46.3
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 64.3
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 52.6
  previous_composite: 46.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zoho-sign/refs/heads/main/screenshots/zoho-sign-2026-06-20T201947.png
security:
- kind: authentication
  name: Zoho Sign Authentication
  slug: zoho-sign-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Zoho Sign Domain Security
  slug: zoho-sign-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zoho Sign Vulnerability Disclosure
  slug: zoho-sign-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: zoho-sign
tags:
- Electronic Signatures
- E-Signature
- Document-Management
- Digital Signatures
- Signature Workflows
- Templates
- Compliance
website: https://www.zoho.com/sign/
---
