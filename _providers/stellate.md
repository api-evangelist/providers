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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Stellate public GraphQL API at graph.stellate.co enables programmatic access to organizational and service-level data. It supports querying organizations and their associated services, with authen
  name: Stellate GraphQL API
  slug: graphql-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/stellate-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/stellate-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stellate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stellate.co
- group: docs
  title: ''
  type: Documentation
  url: https://stellate.co/docs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stellatehq
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/StellateHQ
- group: commercial
  title: ''
  type: Pricing
  url: https://stellate.co/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/stellate-plans.md
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/stellate-rate-limits.md
- group: commercial
  title: ''
  type: FinOps
  url: finops/stellate-finops.md
- group: company
  title: ''
  type: Blog
  url: https://stellate.co/blog
created: 2026-06-14
description: Stellate is a GraphQL edge caching and API management platform that caches GraphQL query results at 60 data centers worldwide, reducing origin traffic by up to 95% and delivering responses in milliseconds. The platform provides edge caching, real-time metrics and insights, rate limiting, and security features to help teams scale, protect, and optimize their GraphQL APIs.
graphqls:
- description: The Stellate public GraphQL API at `https://graph.stellate.co` provides programmatic access to organizational and service-level data for the Stellate edge caching and API management platform. It expos
  name: Stellate GraphQL API
  slug: stellate-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stellate.png
layout: provider
modified: 2026-06-14
name: Stellate
nav: Providers
network: true
overview: 'Stellate publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include GraphQL, CDN, Edge Caching, API Management, and Rate Limiting.


  Stellate''s developer surface includes documentation, pricing, engineering blog, and 9 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 23.6
  coverage:
    artifact_dirs: 7
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 11.9
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 23.6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stellate/refs/heads/main/screenshots/stellate-2026-06-20T194539.png
security:
- kind: domain-security
  name: Stellate Domain Security
  slug: stellate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Stellate Vulnerability Disclosure
  slug: stellate-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Stellate Trust Center
  slug: stellate-trust-center
  summary_line: SOC 2
slug: stellate
tags:
- GraphQL
- CDN
- Edge Caching
- API Management
- Rate Limiting
- GraphQL Security
- Developer Tools
website: https://stellate.co
---
