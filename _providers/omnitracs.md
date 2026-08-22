---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
api_count: 3
apis:
- description: Integration web services for the Omnitracs Roadnet routing and dispatch platform (route planning and optimization, orders/stops, and schedules). A live Swagger UI is published at the integration host,
  name: Omnitracs Web Services (Roadnet Platform)
  slug: omnitracs-web-services-api
- description: 'Services Portal entity-management web services for maintaining fleet master data - vehicle maintenance (add/edit), driver maintenance (add/edit), and trailer management, with HOS Group membership and '
  name: Omnitracs Entity Management Web Services
  slug: omnitracs-entity-management-api
- description: A publish-subscribe integration service in which Omnitracs applications continually publish transactions (vehicle positions/GPS, driver messages, Hours-of-Service logs, and critical-event / driver-coa
  name: Omnitracs Event Subscription Service (ESS)
  slug: omnitracs-event-subscription-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/omnitracs-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/omnitracs
- group: company
  title: ''
  type: Website
  url: https://www.omnitracs.com
- group: docs
  title: ''
  type: Documentation
  url: https://apex-prod-integration.aws.roadnet.com/integration/api-docs/index.html
- group: start
  title: ''
  type: SignupURL
  url: https://services.omnitracs.com/portalWeb/
- group: commercial
  title: ''
  type: Plans
  url: plans/omnitracs-plans-pricing.yml
- group: other
  title: ''
  type: Parent
  url: https://www.solera.com/solutions/fleet-solutions/omnitracs/
created: '2026-07-04'
description: Omnitracs is a commercial fleet management, telematics, and transportation-management provider, now part of Solera Inc. (acquired 2021, operating under Solera Fleet Solutions). Its Omnitracs One platform and the Omnitracs Roadnet routing platform serve roughly 15,000 fleet customers with ELD / Hours-of-Service compliance, telematics and GPS positioning, driver workflow and messaging, routing and dispatch, and video safety. Omnitracs exposes real integration APIs and web services (Roadnet Web Services, the Services Portal Entity Management web services, and the SOAP/XML Event Subscription Service that streams positions, messages, HOS, and critical events), but access is partner- and customer-account gated - there is no open, self-service public developer portal. API credentials (a username/password with API access) and the integration developer wiki are provisioned to contracted customers and integration partners. Endpoints documented here for gated surfaces are honestly modeled
  from public integration notes, not from an open reference.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/omnitracs.png
layout: provider
modified: '2026-07-04'
name: Omnitracs
nav: Providers
network: true
overview: 'Omnitracs publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Fleet Management, Telematics, ELD, Hours of Service, and Transportation.


  Omnitracs'' developer surface includes documentation and 6 more developer resources.'
plans:
- name: Omnitracs Plans Pricing
  plan_count: 3
  slug: omnitracs-plans-pricing
random_paper: 10
score:
  band: emerging
  composite: 14.7
  delta: 0.2
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/omnitracs/refs/heads/main/screenshots/omnitracs-2026-08-07T190158.png
security:
- kind: domain-security
  name: Omnitracs Domain Security
  slug: omnitracs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: omnitracs
tags:
- Fleet Management
- Telematics
- ELD
- Hours of Service
- Transportation
- Routing
- Trucking
- GPS
- Solera
website: https://www.omnitracs.com
---
