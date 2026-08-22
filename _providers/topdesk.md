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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: REST API for managing TOPdesk incidents, changes, assets, persons, operators, locations, and other service management resources. Authentication uses application passwords (HTTP Basic) created per TOPd
  name: TOPdesk REST API
  slug: rest-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/topdesk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/topdesk-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TOPdesk
- group: company
  title: ''
  type: Website
  url: https://www.topdesk.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.topdesk.com
- group: start
  title: ''
  type: Documentation Portal
  url: https://www.topdesk.com/en/documentation-portal/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.topdesk.com/en/pricing/
- group: start
  title: ''
  type: Signup
  url: https://www.topdesk.com/en/free-trial/
- group: operate
  title: ''
  type: Support
  url: https://my.topdesk.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/topdesk
- group: company
  title: ''
  type: Blog
  url: https://www.topdesk.com/en/blog/feed/
created: '2026-05-11'
description: TOPdesk is a Netherlands-based service management vendor offering an ITSM and Enterprise Service Management platform used by IT, facilities, HR, and customer service teams for incident management, change management, asset management, self-service portals, and shared service workflows. The TOPdesk REST API uses application password authentication (basic auth) and exposes resources for incidents, changes, assets, persons, operators, and locations for building integrations against on-premises and SaaS TOPdesk environments.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/topdesk.png
layout: provider
modified: '2026-05-11'
name: TOPdesk
nav: Providers
network: true
overview: 'TOPdesk publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include ITSM, Enterprise Service Management, Help Desk, Incident Management, and Change Management.


  TOPdesk''s developer surface includes documentation, pricing, signup flow, support, engineering blog, and 6 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 15.3
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 15.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/topdesk/refs/heads/main/screenshots/topdesk-2026-06-20T195453.png
security:
- kind: domain-security
  name: Topdesk Domain Security
  slug: topdesk-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Topdesk Vulnerability Disclosure
  slug: topdesk-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: topdesk
tags:
- ITSM
- Enterprise Service Management
- Help Desk
- Incident Management
- Change Management
- Asset Management
website: https://www.topdesk.com
---
