---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Propeller Aero Agentic Access
  operation_count: 17
  slug: propeller-aero-agentic-access
  summary_line: 17 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.propelleraero.com/v1
  baseurl_source: declared
  description: Top-level accounts that own sites, workspaces, and surveys.
  name: Propeller Aero Organizations API
  slug: propeller-aero-organizations-api
- baseURL: https://api.propelleraero.com/v1
  baseurl_source: declared
  description: DirtMate position-monitoring configs and recorded epochs.
  name: Propeller Aero Position Monitoring API
  slug: propeller-aero-position-monitoring-api
- baseURL: https://api.propelleraero.com/v1
  baseurl_source: declared
  description: User-defined polygons, lines, and points drawn in a workspace.
  name: Propeller Aero Shapes API
  slug: propeller-aero-shapes-api
- baseURL: https://api.propelleraero.com/v1
  baseurl_source: declared
  description: Survey projects (job sites) within an organization.
  name: Propeller Aero Sites API
  slug: propeller-aero-sites-api
- baseURL: https://api.propelleraero.com/v1
  baseurl_source: declared
  description: Individual drone survey captures and their downloadable files.
  name: Propeller Aero Surveys API
  slug: propeller-aero-surveys-api
- baseURL: https://api.propelleraero.com/v1
  baseurl_source: declared
  description: Calculated measurements (volumes, distances, areas) tied to a shape.
  name: Propeller Aero Widgets API
  slug: propeller-aero-widgets-api
- baseURL: https://api.propelleraero.com/v1
  baseurl_source: declared
  description: Analysis contexts within a site that hold shapes and widgets.
  name: Propeller Aero Workspaces API
  slug: propeller-aero-workspaces-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Propeller Public Organizations API
  slug: open-propeller-aero-organizations-api
- collection_type: open
  name: Propeller Public Organizations Position Monitoring API
  slug: open-propeller-aero-position-monitoring-api
- collection_type: open
  name: Propeller Public Organizations Shapes API
  slug: open-propeller-aero-shapes-api
- collection_type: open
  name: Propeller Public Organizations Sites API
  slug: open-propeller-aero-sites-api
- collection_type: open
  name: Propeller Public Organizations Surveys API
  slug: open-propeller-aero-surveys-api
- collection_type: open
  name: Propeller Public Organizations Widgets API
  slug: open-propeller-aero-widgets-api
- collection_type: open
  name: Propeller Public Organizations Workspaces API
  slug: open-propeller-aero-workspaces-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/propeller-aero-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/propeller-aero-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/propeller-aero-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/propeller-aero-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/propeller-aero
- group: company
  title: ''
  type: Website
  url: https://www.propelleraero.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PropellerAero
- group: docs
  title: ''
  type: Documentation
  url: https://propelleraero.readme.io/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://propelleraero.readme.io/reference
- group: operate
  title: ''
  type: Support
  url: https://help.propelleraero.com/hc/en-us/articles/19383843944599-Using-Propeller-API
- group: commercial
  title: ''
  type: Plans
  url: plans/propeller-aero-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/propeller-aero-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/propeller-aero-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.propelleraero.com/blog/
created: '2026-07-04'
description: Propeller Aero is a drone survey and earthworks analytics platform for construction, mining, aggregates, and waste sites. Teams fly a drone, process imagery with Propeller's AeroPoints ground control and photogrammetry pipeline, and get accurate 3D site surveys, terrain models, volumes, and progress tracking in the Propeller Platform. The Propeller Public API is a paid, premium feature (available on higher tiers such as Scale) that gives programmatic, read-oriented access to organizations, sites, workspaces, surveys, downloadable survey files (orthophotos, terrain, point clouds), user-defined shapes and their calculated widgets (volumes, distances, areas), and DirtMate position-monitoring data. It is a REST API over HTTPS authenticated with a Bearer access token or via OpenID Connect.
finops:
- name: Propeller Aero Finops
  service_category: Analytics
  slug: propeller-aero-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/propeller-aero.png
layout: provider
modified: '2026-07-04'
name: Propeller Aero
nav: Providers
network: true
overview: 'Propeller Aero publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Organizations API, Position Monitoring API, Shapes API, and 4 more. Tagged areas include Drone Survey, Geospatial, Earthworks, Construction, and Mining.


  Propeller Aero''s developer surface includes authentication, documentation, API reference, support, engineering blog, and 9 more developer resources.'
plans:
- name: Propeller Aero Plans Pricing
  plan_count: 3
  slug: propeller-aero-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Propeller Aero Rate Limits
  slug: propeller-aero-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/propeller-aero/refs/heads/main/screenshots/propeller-aero-2026-09-02T152151.png
security:
- kind: authentication
  name: Propeller Aero Authentication
  slug: propeller-aero-authentication
  summary_line: http/openIdConnect · 2 schemes
- kind: domain-security
  name: Propeller Aero Domain Security
  slug: propeller-aero-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Propeller Aero Trust Center
  slug: propeller-aero-trust-center
  summary_line: SOC 2, GDPR
slug: propeller-aero
tags:
- Drone Survey
- Geospatial
- Earthworks
- Construction
- Mining
- Photogrammetry
- Surveying
- Analytics
website: https://www.propelleraero.com/
---
