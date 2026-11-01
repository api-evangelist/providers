---
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Kenect's API provides programmatic access to messaging, voice, reviews, payments, and AI-driven engagement features as described in their developer documentation.
  name: Kenect API
  slug: kenect-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/kenect/llms/kenect-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kenect-llms.txt
- group: other
  href: https://artifacts.apis.io/kenect/hosts/kenect-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kenect-hosts.yml
- group: other
  href: https://artifacts.apis.io/kenect/vendors/kenect-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kenect-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kenect.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kenect.com/privacy-policy
- group: auth
  href: https://artifacts.apis.io/kenect/security/kenect-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kenect-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kenect.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.kenect.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kenect.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.kenect.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.kenect.com/
- group: operate
  title: ''
  type: Support
  url: https://resourcecenter.kenect.com/
- group: company
  title: ''
  type: Blog
  url: https://kenect.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kenect
coverage:
  checked: '2026-10-28'
  detail: OpenAPI spec endpoints (e.g., https://api.kenect.com/v1/openapi.json) return HTTP 401, indicating the API contracts are behind authentication.
  evidence:
  - status: 401
    url: https://api.kenect.com/v1/openapi.json
  reason: partner-login
  state: gated
created: '2026-10-28'
description: Kenect provides AI-driven customer engagement tools for dealerships, enabling texting, voice, reviews, payments, and reputation management. Their platform integrates messaging, AI chat, and analytics to help automotive businesses improve sales, service, and online presence. The service offers a suite of products including Engage AI, Voice AI, Text Messaging, Reviews, Payments, and a mobile app, all designed to streamline communication and boost customer satisfaction.
image: https://cdn.prod.website-files.com/69727da0bb0d6209780690d6/69727da0bb0d6209780694bc_Favicon%20-%20Kenect.png
layout: provider
modified: '2026-10-28'
name: Kenect
nav: Providers
network: true
overview: 'Kenect is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Messaging, AI, Customer Engagement, and Reputation Management.


  Kenect''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, and 9 more developer resources.'
random_paper: 10
rate_limits:
- limit_count: 0
  name: Kenect Rate Limits
  slug: kenect-rate-limits
scopes:
- name: Kenect Scopes
  scope_count: 0
  slug: kenect-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 21.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Kenect Authentication
  slug: kenect-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Kenect Domain Security
  slug: kenect-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kenect
tags:
- Automotive
- Messaging
- AI
- Customer Engagement
- Reputation Management
website: https://kenect.com/
---
