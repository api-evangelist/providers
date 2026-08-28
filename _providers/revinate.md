---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
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
  score: 34.4
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The Porter API is Revinate's structured review-data REST API. It provides read access to hotel reviews aggregated across more than 100 review sites, plus key metrics (review counts, average ratings, T
  name: Revinate Porter API
  slug: porter
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.revinate.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://porter.revinate.com/documentation
- group: docs
  title: ''
  type: Documentation
  url: https://porter.revinate.com/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://porter.revinate.com/documentation#api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://porter.revinate.com/documentation#introduction
- group: operate
  title: ''
  type: Support
  url: https://www.revinate.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.revinate.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/revinate
- group: start
  title: ''
  type: Login
  url: https://www.revinate.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.revinate.com/website-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.revinate.com/website-privacy-policy/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.revinate.com/
- group: auth
  title: ''
  type: Compliance
  url: security/revinate-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/revinate-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/revinate-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/revinate-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/revinate-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/revinate-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/revinate-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/revinate-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/revinate-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/revinate-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/revinate-rate-limits.yml
created: '2026-08-26'
description: Revinate is a hospitality technology company providing a Guest Data Platform and CRM for hotels — unifying guest profiles from property-management systems, then driving direct revenue through email marketing, a voice/call-center product, a virtual concierge, and reputation and guest-feedback management. Revinate states it powers 950 million-plus guest profiles and $17.2 billion in direct revenue for over 12,500 hotels worldwide. Its public developer surface is the Porter API — a read-only REST API for structured review data covering 100-plus review sites, exposing hotels, hotel sets, reviews, competitor reviews, review-volume and rating snapshots, survey email statistics, and hospitality-specific sentiment analysis broken out by topic category.
image: https://www.revinate.com/wp-content/uploads/2022/09/revinate-logo-400px.png
layout: provider
modified: '2026-08-26'
name: Revinate
nav: Providers
network: true
overview: 'Revinate publishes 1 API on the [APIs.io](https://apis.io/) network: Porter API. Tagged areas include Hospitality, Hotels, Reviews, Reputation Management, and Guest Data Platform.


  Revinate''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 17 more developer resources.'
plans:
- name: Revinate Plans Pricing
  plan_count: 0
  slug: revinate-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Revinate Rate Limits
  slug: revinate-rate-limits
scopes:
- name: Revinate Scopes
  scope_count: 0
  slug: revinate-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 46.3
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 16.7
    contract_quality: 59.2
    developer_ergonomics: 58.9
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 2.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Revinate Authentication
  slug: revinate-authentication
  summary_line: apiKey/openIdConnect · 4 schemes
- kind: domain-security
  name: Revinate Domain Security
  slug: revinate-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Revinate Vulnerability Disclosure
  slug: revinate-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Revinate Trust Center
  slug: revinate-trust-center
  summary_line: trust center published
slug: revinate
tags:
- Hospitality
- Hotels
- Reviews
- Reputation Management
- Guest Data Platform
- CRM
- Sentiment Analysis
- Travel
- Marketing
- Customer Feedback
website: https://www.revinate.com/
---
