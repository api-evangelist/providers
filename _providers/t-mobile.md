---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 12.9
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: T-Mobile operates a developer portal that provides programmatic access to T-Mobile services for partners, enterprises, and IoT customers. Specific API documentation requires partner registration.
  name: T-Mobile Developer Portal
  slug: developer-portal
artifact_total: 4
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/t-mobile-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/t-mobile-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tmobile
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/t-mobile
- group: company
  title: ''
  type: Website
  url: https://www.t-mobile.com/
- group: other
  title: ''
  type: Developer
  url: https://developer.t-mobile.com/
- group: other
  title: ''
  type: Business
  url: https://www.t-mobile.com/business
- group: other
  title: ''
  type: IoT
  url: https://www.t-mobile.com/business/iot
- group: company
  title: ''
  type: About
  url: https://www.t-mobile.com/our-story
- group: company
  title: ''
  type: News
  url: https://www.t-mobile.com/news
- group: company
  title: ''
  type: Investors
  url: https://investor.t-mobile.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.t-mobile.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.t-mobile.com/llms.txt
created: '2026-05-05'
description: A major American wireless network operator and the second-largest carrier in the United States. Known for its Un-carrier strategy disrupting the wireless industry with simplified plans, no-contract offerings, and aggressive 5G network expansion.
graphqls:
- description: This conceptual GraphQL schema represents the T-Mobile wireless carrier platform, covering the full range of T-Mobile services including wireless accounts, device management, network connectivity, IoT
  name: T-Mobile GraphQL Schema
  slug: t-mobile-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/t-mobile.png
layout: provider
modified: '2026-05-16'
name: T-Mobile
nav: Providers
network: true
overview: 'T-Mobile publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Telecommunications, Wireless, Mobile, and 5G.


  T-Mobile''s developer surface includes product news and 12 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 19.6
  coverage:
    artifact_dirs: 4
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 19.0
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 19.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 15.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: T Mobile Domain Security
  slug: t-mobile-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: T Mobile Trust Center
  slug: t-mobile-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: t-mobile
tags:
- Telecommunications
- Wireless
- Mobile
- 5G
website: https://www.t-mobile.com/
---
