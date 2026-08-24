---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.5
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.gridpoint.com/
- group: docs
  title: ''
  type: Documentation
  url: https://knowledge.gridpoint.com/
- group: operate
  title: ''
  type: Support
  url: https://www.gridpoint.com/contact-us/
- group: operate
  title: ''
  type: HelpCenter
  url: https://knowledge.gridpoint.com/
- group: company
  title: ''
  type: Blog
  url: https://resources.gridpoint.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.gridpoint.com/get-started/
- group: start
  title: ''
  type: Login
  url: https://ems.gridpoint.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gridpoint.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gridpoint.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gridpoint-com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gridpoint.com/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/gridpoint-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gridpoint-authentication.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/gridpoint-openid-configuration.json
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/gridpoint-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/gridpoint-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gridpoint-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gridpoint-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gridpoint-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/gridpoint-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gridpoint-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gridpoint-llms.txt
coverage:
  checked: '2026-08-22'
  detail: GridPoint has no developer surface at all — developer/docs/api.gridpoint.com do not resolve and knowledge.gridpoint.com is hardware troubleshooting — yet its own ORY Hydra authorization server anonymously advertises the client_credentials grant plus ROLE_PARTNER_* and ROLE_SYSTEM scopes, so the API exists and is reachable only by an authenticated customer or commissioning partner.
  evidence:
  - status: 200
    url: https://hydra.gridpoint.com/.well-known/openid-configuration
  - status: 200
    url: https://ems.gridpoint.com/login
  - status: 404
    url: https://www.gridpoint.com/llms.txt
  - status: 404
    url: https://ems.gridpoint.com/openapi.json
  reason: customer-only-docs
  state: gated
created: '2026-08-22'
description: GridPoint is a Reston, Virginia clean-technology company, founded in 2003, that builds energy management and sustainability systems for commercial buildings, enterprises and government agencies. It combines its own edge hardware — EC2000 and Edge controllers, submeters, thermostats, lighting control panels and BACnet/Modbus gateways — with the cloud-based GridPoint Energy Manager analytics platform, delivering HVAC and lighting automation, equipment-level submetering, refrigeration monitoring, demand management, grid services and carbon/sustainability reporting for multi-site portfolios in retail, convenience, restaurant, automotive and public-sector estates. GridPoint sells the platform as a subscription service and integrates with existing building assets rather than requiring a rip-and-replace. It operates a customer application, a partner commissioning channel and a public knowledge base, but publishes no developer portal, no API reference and no machine-readable API contract;
  the only machine-readable artifacts it serves anonymously are the OpenID Connect discovery and JWKS documents of its own authorization server.
image: https://icon.horse/icon/gridpoint.com
layout: provider
modified: '2026-08-22'
name: GridPoint
nav: Providers
network: true
overview: 'GridPoint is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Energy Management, Buildings, and Building Automation.


  GridPoint''s developer surface includes documentation, support, engineering blog, signup flow, authentication, and 17 more developer resources.'
plans:
- name: Gridpoint Plans Pricing
  plan_count: 0
  slug: gridpoint-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Gridpoint Rate Limits
  slug: gridpoint-rate-limits
scopes:
- name: Gridpoint Scopes
  scope_count: 16
  slug: gridpoint-scopes
  summary_line: 16 scopes · authorizationCode/clientCredentials/implicit
score:
  band: thin
  composite: 29.6
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 18.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 56.8
  schema_version: 0.12.1
  scored_at: '2026-08-24'
security:
- kind: authentication
  name: Gridpoint Authentication
  slug: gridpoint-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Gridpoint Domain Security
  slug: gridpoint-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gridpoint
tags:
- Company
- Energy
- Energy Management
- Buildings
- Building Automation
- Sustainability
- Internet of Things
- Demand Response
- Facilities
- Analytics
website: https://www.gridpoint.com/
---
