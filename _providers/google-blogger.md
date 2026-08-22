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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Google Blogger Agentic Access
  operation_count: 16
  slug: google-blogger-agentic-access
  summary_line: 16 operations · 6 acting
api_count: 2
apis:
- description: The Blogs API from Google Blogger — 8 operation(s) for blogs.
  name: Google Blogger Blogs API
  slug: google-blogger-blogs-api
- description: The Users API from Google Blogger — 2 operation(s) for users.
  name: Google Blogger Users API
  slug: google-blogger-users-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Blogger API
  slug: open-blogger
- collection_type: open
  name: Google Blogger Blogs API
  slug: open-google-blogger-blogs-api
- collection_type: open
  name: Google Blogger Blogs Users API
  slug: open-google-blogger-users-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-blogger-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-blogger-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-blogger-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-blogger-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-blogger-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/blogger
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/blogger/docs/3.0/getting_started
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.google.com/blogger/docs/3.0/using
- group: design
  title: ''
  type: JSONLD
  url: json-ld/blogger.jsonld
created: '2026-03-13'
description: The Google Blogger API v3 allows you to integrate Blogger content with your application. You can create, read, update, and delete blogs, posts, pages, comments, and user information using RESTful operations with OAuth 2.0 authentication.
finops:
- name: Google Blogger Finops
  service_category: API
  slug: google-blogger-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-blogger.png
json_schemas:
- name: Blogger Post
  property_count: 13
  slug: blogger
jsonld:
- class_count: 16
  name: Blogger Context
  property_count: 3
  slug: blogger
layout: provider
modified: '2026-05-19'
name: Google Blogger
nav: Providers
network: true
overview: 'Google Blogger publishes 2 APIs on the [APIs.io](https://apis.io/) network: Blogs API and Users API. Tagged areas include Blogging, CMS, Comments, Google, and Pages.


  The Google Blogger catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Blogger''s developer surface includes authentication, getting-started guide, pricing, and 6 more developer resources.'
plans:
- name: Google Blogger Plans Pricing
  plan_count: 3
  slug: google-blogger-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Google Blogger Rate Limits
  slug: google-blogger-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Blogger API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-blogger-jsonschema-spectral-rules
scopes:
- name: Google Blogger Scopes
  scope_count: 2
  slug: google-blogger-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 35.2
  delta: -6.2
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 9.8
    contract_quality: 64.7
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 41.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/google-blogger/refs/heads/main/screenshots/google-blogger-2026-06-20T182025.png
security:
- kind: authentication
  name: Google Blogger Authentication
  slug: google-blogger-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Google Blogger Domain Security
  slug: google-blogger-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Blogger Vulnerability Disclosure
  slug: google-blogger-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-blogger
tags:
- Blogging
- CMS
- Comments
- Google
- Pages
- Posts
- Publishing
---
