---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The production REST API behind the SponsorUnited platform. Its OpenAPI 3.0 description is publicly served at https://api.sponsorunited.com/docs and describes 547 operations across 422 paths and 561 sc
  name: SponsorUnited API
  slug: sponsorunited-api
artifact_total: 8
asyncapis:
- description: ''
  name: Sponsorunited Event Surface
  slug: sponsorunited-event-surface
common:
- group: company
  title: ''
  type: Website
  url: https://www.sponsorunited.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.sponsorunited.com/en/
- group: operate
  title: ''
  type: Support
  url: https://www.sponsorunited.com/contact
- group: start
  title: ''
  type: SignUp
  url: https://www.sponsorunited.com/request-a-demo
- group: start
  title: ''
  type: Login
  url: https://pro.sponsorunited.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sponsorunited.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sponsorunited.com/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://sponsorunited.statuspage.io/
- group: auth
  title: ''
  type: TrustCenter
  url: security/sponsorunited-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.sponsorunited.com/security
- group: auth
  title: ''
  type: Security
  url: https://www.sponsorunited.com/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SponsorUnited
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.sponsorunited.com/en/collections/7168679-data-product-releases
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sponsorunited-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sponsorunited-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sponsorunited-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sponsorunited-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sponsorunited-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sponsorunited-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/sponsorunited-packages.yml
created: '2026-08-29'
description: SponsorUnited is a sports and entertainment sponsorship intelligence platform, founded in 2018 and headquartered in Stamford, Connecticut. Its B2B SaaS product gives brands, rights holders (teams, leagues, venues and events), agencies and media companies a searchable dataset of marketing partnerships — the company reports 403,000+ brands, 2.2M+ tracked deals and 21.1M+ data points across sports, entertainment, media and talent — used to discover, evaluate, price, negotiate and activate sponsorships. The platform (SponsorUnited 4.0) layers AI features on that dataset, including the Surface AI analyst, a Proposal Evaluator, and SPND (Sponsorship Price of Negotiated Deals), a pricing-transparency product built on verified deal data. SponsorUnited runs a production REST API at api.sponsorunited.com whose OpenAPI 3.0 description is publicly served, but it publishes no developer portal, API reference or partner program around it; access is sold as a paid subscription with custom pricing
  and no self-serve sign-up.
image: https://cdn.prod.website-files.com/69150d2cbcfa91eb0672f267/691cc16ce42d7f8320d6e4d0_SU-logotype-light.svg
layout: provider
mcp_servers:
- description: ''
  name: SponsorUnited MCP Server
  slug: sponsorunited-mcp-server
modified: '2026-08-29'
name: SponsorUnited
nav: Providers
network: true
overview: 'SponsorUnited publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sponsorship, Sports, Entertainment, and Marketing.


  The SponsorUnited catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SponsorUnited''s developer surface includes documentation, support, signup flow, changelog, and 16 more developer resources.'
plans:
- name: Sponsorunited Plans Pricing
  plan_count: 0
  slug: sponsorunited-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Sponsorunited Rate Limits
  slug: sponsorunited-rate-limits
score:
  band: developing
  composite: 45.6
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -1.2
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 57.6
    developer_ergonomics: 28.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 46.8
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Sponsorunited Authentication
  slug: sponsorunited-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Sponsorunited Domain Security
  slug: sponsorunited-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Sponsorunited Trust Center
  slug: sponsorunited-trust-center
  summary_line: SOC 2 Type II, GDPR
slug: sponsorunited
tags:
- Company
- Sponsorship
- Sports
- Entertainment
- Marketing
- Advertising
- Media
- Data
- Analytics
- Market Intelligence
- Software-as-a-Service
- Partnerships
website: https://www.sponsorunited.com/
---
