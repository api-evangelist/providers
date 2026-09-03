---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 18.0
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://urbanfootprint.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.urbanfootprint.com/resilienceinsights/
- group: operate
  title: ''
  type: Support
  url: https://urbanfootprint.us.document360.io/
- group: company
  title: ''
  type: Blog
  url: https://urbanfootprint.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://urbanfootprint.com/blog/feed/
- group: start
  title: ''
  type: Login
  url: https://app.urbanfootprint.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/UrbanFootprint
- group: commercial
  title: ''
  type: TermsOfService
  url: https://urbanfootprint.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://urbanfootprint.com/privacy-policy/
- group: operate
  title: ''
  type: ContactSales
  url: https://urbanfootprint.com/about/contact-sales/
- group: other
  title: ''
  type: CaseStudies
  url: https://urbanfootprint.com/case-studies/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/6629640
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/UFPlatform
- group: auth
  title: ''
  type: Authentication
  url: authentication/urbanfootprint-authentication.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/urbanfootprint-openid-configuration.json
- group: agent
  title: ''
  type: WellKnown
  url: well-known/urbanfootprint-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/urbanfootprint-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/urbanfootprint-problem-types.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/urbanfootprint-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/urbanfootprint-domain-security.yml
created: '2026-07-17'
description: UrbanFootprint is a resilient decision intelligence platform that delivers urban, climate, and community-resilience data and analytics, helping governments, utilities, financial institutions, and planners assess risk and make data-driven decisions. Its platform spans scenario analysis (Analyst), map-based data exploration (Explorer), and curated data subscriptions covering climate hazards, the built environment, and social vulnerability. UrbanFootprint is a closed SaaS platform sold via sales contact and publishes no public developer API; its application authenticates through Auth0 and consumes an internal platform API.
image: https://urbanfootprint.com/wp-content/uploads/2026/04/icon-512.png
layout: provider
modified: '2026-07-21'
name: UrbanFootprint
nav: Providers
network: true
overview: 'UrbanFootprint is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Climate, Geospatial, Urban Planning, and Data.


  UrbanFootprint''s developer surface includes documentation, support, engineering blog, authentication, and 16 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 18.3
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 18.3
  provenance:
    conformance: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/urbanfootprint/refs/heads/main/screenshots/urbanfootprint-2026-09-02T165201.png
security:
- kind: authentication
  name: Urbanfootprint Authentication
  slug: urbanfootprint-authentication
  summary_line: openIdConnect/oauth2 · 2 schemes
- kind: domain-security
  name: Urbanfootprint Domain Security
  slug: urbanfootprint-domain-security
  summary_line: TLSv1.3 · DMARC
slug: urbanfootprint
tags:
- Company
- Climate
- Geospatial
- Urban Planning
- Data
- Analytics
- Resilience
- Mapping
website: https://urbanfootprint.com
---
