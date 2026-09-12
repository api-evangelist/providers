---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-12'
api_count: 1
apis:
- description: The Advisr REST API exposes the objects inside the Advisr Platform — company, groups, clients, agencies, campaigns (including product summary and detail, product recommendations, geo, audience, presen
  name: Advisr API
  slug: advisr-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/advisr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.advisr.com/
- group: company
  title: ''
  type: Blog
  url: https://www.advisr.com/resources
- group: operate
  title: ''
  type: Support
  url: https://support.advisr.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.advisr.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.advisr.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://app.advisr.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/advisr-io
- group: build
  title: ''
  type: Packages
  url: packages/advisr-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/advisr-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/advisr-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/advisr-mcp.yml
created: '2026-09-09'
description: Advisr is a New York-based sales operating system built for the media and advertising industry. Its platform helps broadcast, publishing, cable and agency sales teams plan campaigns, match products to advertiser goals and budgets, dynamically generate client-ready proposals and presentations, automate collaboration and approval workflows, and forecast revenue from real-time dashboards. Advisr publishes a public, read-oriented REST API at https://api.advisr.com/v1 covering companies, groups, clients, agencies, campaigns, products, users, industries and categories, goals, files, bulk exports and custom fields, documented as a static HTML reference at https://apidocs.advisr.com. Access tokens are issued by Advisr support rather than self-service.
image: https://cdn.prod.website-files.com/63e3bd34df9e1947a4fd9a7a/63e99a7ce0068292ab161dba_advisr-icon.png
layout: provider
modified: '2026-09-09'
name: Advisr
nav: Providers
network: true
overview: 'Advisr publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Media, Sales, and Sales Enablement.


  Advisr''s developer surface includes engineering blog, support, and 10 more developer resources.'
plans:
- name: Advisr Plans Pricing
  plan_count: 0
  slug: advisr-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Advisr Rate Limits
  slug: advisr-rate-limits
score:
  band: emerging
  composite: 23.2
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 75.9
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 23.2
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Advisr Authentication
  slug: advisr-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Advisr Domain Security
  slug: advisr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: advisr
tags:
- Company
- Advertising
- Media
- Sales
- Sales Enablement
- Media Planning
- Proposals
- Advertising Sales
- Campaigns
- CRM
website: https://www.advisr.com/
---
