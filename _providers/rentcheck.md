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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.0
  scored_at: '2026-07-28'
api_count: 31
apis:
- description: The Account Settings API from RentCheck — 9 operation(s) for account settings.
  name: RentCheck Account Settings API
  slug: rentcheck-account-settings-api
- description: The Automations API from RentCheck — 2 operation(s) for automations.
  name: RentCheck Automations API
  slug: rentcheck-automations-api
- description: The Buildings API from RentCheck — 3 operation(s) for buildings.
  name: RentCheck Buildings API
  slug: rentcheck-buildings-api
- description: The Chargebee API from RentCheck — 3 operation(s) for chargebee.
  name: RentCheck Chargebee API
  slug: rentcheck-chargebee-api
- description: The Communities API from RentCheck — 3 operation(s) for communities.
  name: RentCheck Communities API
  slug: rentcheck-communities-api
- description: The Dashboard API from RentCheck — 2 operation(s) for dashboard.
  name: RentCheck Dashboard API
  slug: rentcheck-dashboard-api
- description: The File Requests API from RentCheck — 2 operation(s) for file requests.
  name: RentCheck File Requests API
  slug: rentcheck-file-requests-api
- description: The Filter Segments API from RentCheck — 2 operation(s) for filter segments.
  name: RentCheck Filter Segments API
  slug: rentcheck-filter-segments-api
- description: The Inspection Features API from RentCheck — 13 operation(s) for inspection features.
  name: RentCheck Inspection Features API
  slug: rentcheck-inspection-features-api
- description: The Inspections API from RentCheck — 26 operation(s) for inspections.
  name: RentCheck Inspections API
  slug: rentcheck-inspections-api
- description: The Inspections Templates API from RentCheck — 4 operation(s) for inspections templates.
  name: RentCheck Inspections Templates API
  slug: rentcheck-inspections-templates-api
- description: The Inspections V2 API from RentCheck — 2 operation(s) for inspections v2.
  name: RentCheck Inspections V2 API
  slug: rentcheck-inspections-v2-api
- description: The Integrations API from RentCheck — 1 operation(s) for integrations.
  name: RentCheck Integrations API
  slug: rentcheck-integrations-api
- description: The LatchelProxy API from RentCheck — 6 operation(s) for latchelproxy.
  name: RentCheck LatchelProxy API
  slug: rentcheck-latchelproxy-api
- description: The Leases API from RentCheck — 9 operation(s) for leases.
  name: RentCheck Leases API
  slug: rentcheck-leases-api
- description: The Maintenance Flags API from RentCheck — 3 operation(s) for maintenance flags.
  name: RentCheck Maintenance Flags API
  slug: rentcheck-maintenance-flags-api
- description: The Maintenance Reports API from RentCheck — 2 operation(s) for maintenance reports.
  name: RentCheck Maintenance Reports API
  slug: rentcheck-maintenance-reports-api
- description: The Maintenance Reports V2 API from RentCheck — 1 operation(s) for maintenance reports v2.
  name: RentCheck Maintenance Reports V2 API
  slug: rentcheck-maintenance-reports-v2-api
- description: The oAuth2 API from RentCheck — 8 operation(s) for oauth2.
  name: RentCheck oAuth2 API
  slug: rentcheck-oauth2-api
- description: The Permission Groups API from RentCheck — 2 operation(s) for permission groups.
  name: RentCheck Permission Groups API
  slug: rentcheck-permission-groups-api
- description: The Properties V2 API from RentCheck — 4 operation(s) for properties v2.
  name: RentCheck Properties V2 API
  slug: rentcheck-properties-v2-api
- description: The Properties V3 API from RentCheck — 4 operation(s) for properties v3.
  name: RentCheck Properties V3 API
  slug: rentcheck-properties-v3-api
- description: The Residents (deprecated) API from RentCheck — 3 operation(s) for residents (deprecated).
  name: RentCheck Residents (deprecated) API
  slug: rentcheck-residents-deprecated-api
- description: The Residents V2 API from RentCheck — 2 operation(s) for residents v2.
  name: RentCheck Residents V2 API
  slug: rentcheck-residents-v2-api
- description: The Residents V3 API from RentCheck — 1 operation(s) for residents v3.
  name: RentCheck Residents V3 API
  slug: rentcheck-residents-v3-api
- description: The Subscriptions API from RentCheck — 6 operation(s) for subscriptions.
  name: RentCheck Subscriptions API
  slug: rentcheck-subscriptions-api
- description: The Teams API from RentCheck — 11 operation(s) for teams.
  name: RentCheck Teams API
  slug: rentcheck-teams-api
- description: The Units API from RentCheck — 4 operation(s) for units.
  name: RentCheck Units API
  slug: rentcheck-units-api
- description: The Users API from RentCheck — 20 operation(s) for users.
  name: RentCheck Users API
  slug: rentcheck-users-api
- description: The Work Orders API from RentCheck — 3 operation(s) for work orders.
  name: RentCheck Work Orders API
  slug: rentcheck-work-orders-api
- description: The Work Orders V2 API from RentCheck — 1 operation(s) for work orders v2.
  name: RentCheck Work Orders V2 API
  slug: rentcheck-work-orders-v2-api
artifact_total: 34
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/rentcheck-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rentcheck-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rentcheck-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rentcheck-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rentcheck-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://help.getrentcheck.com/en/articles/9045668-rentcheck-api-updates
- group: design
  title: ''
  type: Conformance
  url: conformance/rentcheck-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rentcheck-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rentcheck-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rentcheck-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/rentcheck-schedule-inspection.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/rentcheck-process-inspection-results.md
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/rentcheck-changelog.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.getrentcheck.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.getrentcheck.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://app.getrentcheck.com/account/integrations/rentcheck-api
- group: operate
  title: ''
  type: Support
  url: https://help.getrentcheck.com/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.getrentcheck.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.getrentcheck.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getrentcheck
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getrentcheck.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.getrentcheck.com/get-started
- group: start
  title: ''
  type: Login
  url: https://app.getrentcheck.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getrentcheck.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getrentcheck.com/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://getrentcheck.com/
created: '2026-07-17'
description: RentCheck is a resident-led property inspection platform used by 1,000+ property management companies to run guided move-in, move-out, routine, and maintenance inspections that residents complete from their smartphone, producing standardized, time-stamped photo reports. Its REST API (OpenAPI 3.1, 160 paths / 217 operations) lets developers pull property, unit, building, community, and resident data, schedule and create inspections from customizable templates, review inspection features and photos, flag maintenance issues, and wire results into property-management systems such as AppFolio, Rent Manager, Rentvine, Buildium, Latchel, and Zapier.
image: https://cdn.prod.website-files.com/64c252917dda086383e12e96/6945920e3577a32b09f7b34d_RentCheck_Open_Graph.png
layout: provider
mcp_servers:
- description: ''
  name: rentcheck-mcp.yml
  slug: rentcheck-mcpyml
modified: '2026-07-20'
name: RentCheck
nav: Providers
network: true
overview: 'RentCheck publishes 31 APIs on the [APIs.io](https://apis.io/) network, including Account Settings API, Automations API, Buildings API, and 28 more. Tagged areas include Company, Property Management, Property Inspection, Real Estate, and PropTech.


  RentCheck''s developer surface includes authentication, changelog, documentation, getting-started guide, support, engineering blog, pricing, and 19 more developer resources.'
random_paper: 3
score:
  band: developing
  composite: 47.2
  delta: -2.3
  facets:
    commercial_clarity: 44.7
    contract_quality: 60.2
    developer_ergonomics: 49.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 49.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 31
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Rentcheck Authentication
  slug: rentcheck-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Rentcheck Domain Security
  slug: rentcheck-domain-security
  summary_line: TLSv1.3 · HSTS
slug: rentcheck
tags:
- Company
- Property Management
- Property Inspection
- Real Estate
- PropTech
- Inspections
- Maintenance
- Rental
website: https://getrentcheck.com/
---
