---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.2
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: DSpace 8.3 REST (HAL) API for Western University's Open Repository, Scholarship@Western, hosted on the national Scholaris service by Scholars Portal. Exposes communities, collections, items, bitstream
  name: Scholaris (Scholarship@Western) DSpace REST API
  slug: scholaris-rest
- description: Western Technology Services operates an institutional Single Sign-On service supporting SAML2, OAuth, OpenID Connect (OIDC), and CAS for authenticating users against their Western institutional accoun
  name: Western Single Sign-On (SAML2 / OAuth / OIDC / CAS)
  slug: sso
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/western-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.uwo.ca/
- group: company
  title: ''
  type: LinkedIn
  url: https://ca.linkedin.com/school/westernuniversity/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/westernu
- group: auth
  title: ''
  type: Authentication
  url: https://wts.uwo.ca/services/o/single-sign-on-sso-saml2-oauth-oidc-cas/index.html
- group: commercial
  title: ''
  type: Plans
  url: plans/western-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/western-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/western-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: About
  url: https://uwo.scholaris.ca/home
created: '2026-06-03'
description: 'Western University is a public research university in London, Ontario, Canada, ranked #120 in the QS World University Rankings 2025. Its public, machine-readable developer footprint is centered on Western Libraries: the institutional repository Scholarship@Western migrated in 2025 to Scholaris, a national shared DSpace 8 service hosted by Scholars Portal, which exposes a live DSpace REST API and an OAI-PMH metadata harvesting endpoint. Western Technology Services also operates an institutional Single Sign-On service supporting SAML2, OAuth, OpenID Connect, and CAS, but it is gated behind institutional affiliation rather than self-service. Western does not publish an official open course/timetable or open-data API; timetable data is documented only as scrape targets and via unofficial third-party projects.'
finops:
- name: Western Finops
  service_category: Education
  slug: western-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/western.png
jsonld:
- class_count: 7
  name: Western Context
  property_count: 9
  slug: western-context
layout: provider
modified: '2026-07-25'
name: Western University
nav: Providers
network: true
overview: 'Western University publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Canada, and Library.


  The Western University catalog on APIs.io includes 1 JSON-LD context.


  Western University''s developer surface includes authentication and 9 more developer resources.'
plans:
- name: Western Plans Pricing
  plan_count: 2
  slug: western-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 1
  name: Western Rate Limits
  slug: western-rate-limits
score:
  band: emerging
  composite: 19.9
  delta: -2.6
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 10.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 22.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/western/refs/heads/main/screenshots/western-2026-06-20T201359.png
security:
- kind: domain-security
  name: Western Domain Security
  slug: western-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: western
tags:
- Education
- Higher Education
- University
- Canada
- Library
- Institutional Repository
- Open Access
- Identity
website: https://www.uwo.ca/
---
