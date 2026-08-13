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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: The private back-end API for CTM Portal, CTM's single sign-on customer portal. It is not documented, not announced and not offered to third parties — it was identified from the portal's own client boo
  name: CTM Portal Host API
  slug: ctm-portal-host-api
artifact_total: 14
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/corporate-travel-management-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/corporate-travel-management-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/corporate-travel-management-openid-configuration.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/corporate-travel-management-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/corporate-travel-management-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/corporate-travel-management-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/corporate-travel-management-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/corporate-travel-management-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/corporate-travel-management-packages.yml
- group: design
  title: ''
  type: Components
  url: components/corporate-travel-management-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/corporate-travel-management-llms.txt
- group: docs
  title: ''
  type: Documentation
  url: https://compass.ctmdevelopment.com/
- group: company
  title: ''
  type: Website
  url: https://www.travelctm.com/
- group: company
  title: ''
  type: Website
  url: https://au.travelctm.com/
- group: company
  title: ''
  type: Website
  url: https://us.travelctm.com/
- group: company
  title: ''
  type: Website
  url: https://uk.travelctm.com/
- group: company
  title: ''
  type: Website
  url: https://asia.travelctm.com/
- group: start
  title: ''
  type: Portal
  url: https://portal.travelctm.com/
- group: start
  title: ''
  type: Login
  url: https://www.ctmsmart.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://au.travelctm.com/technology/
- group: docs
  title: ''
  type: Documentation
  url: https://au.travelctm.com/technology/lightning/
- group: docs
  title: ''
  type: Documentation
  url: https://au.travelctm.com/technology/travel-portal/
- group: docs
  title: ''
  type: Documentation
  url: https://au.travelctm.com/technology/travel-reporting/
- group: docs
  title: ''
  type: Documentation
  url: https://au.travelctm.com/technology/pre-trip-approval/
- group: docs
  title: ''
  type: Documentation
  url: https://au.travelctm.com/technology/travel-forecasting/
- group: docs
  title: ''
  type: Documentation
  url: https://au.travelctm.com/technology/ctm-mobile-app/
- group: docs
  title: ''
  type: Documentation
  url: https://au.travelctm.com/technology/ctm-scout/
- group: docs
  title: ''
  type: Documentation
  url: https://au.travelctm.com/technology/risk-management/
- group: docs
  title: ''
  type: Documentation
  url: https://au.travelctm.com/ndc/
- group: docs
  title: ''
  type: Documentation
  url: https://us.travelctm.com/ndc/
- group: company
  title: ''
  type: Blog
  url: https://au.travelctm.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://au.travelctm.com/blog/feed/
- group: company
  title: ''
  type: BlogRSS
  url: https://us.travelctm.com/feed/
- group: company
  title: ''
  type: News
  url: https://au.travelctm.com/news/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://au.travelctm.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://au.travelctm.com/privacy/
- group: other
  title: ''
  type: CookiePolicy
  url: https://au.travelctm.com/cookie-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://au.travelctm.com/payment-card-industry-data-security-standard/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investor.travelctm.com.au/
- group: company
  title: ''
  type: Careers
  url: https://au.travelctm.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://au.travelctm.com/contact/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/corporate-travel-management-ctm-group
created: '2026-07-28'
description: 'Corporate Travel Management (CTM) is a Brisbane-founded, ASX-listed (CTD) travel management company established in 1994 that procures, books and services corporate, government, meetings and events, resources, sport and leisure travel across Australia and New Zealand, North America, Europe and Asia. CTM sits on the buy side of the travel distribution chain: an IATA-accredited agency that aggregates supplier content from GDS, direct airline APIs and airline NDC connections and resells it to corporate clients through its own proprietary technology stack — the Lightning online booking tool, CTM Portal, CTM Mobile app, CTM Approve pre-trip approval, CTM Fare Forecaster and CTM Data Hub reporting. Its API posture is closed. CTM publishes no developer portal and no public API: developer.travelctm.com, developers.travelctm.com, api.travelctm.com and docs.travelctm.com do not resolve in DNS, and /developers, /api, /docs, /openapi.json, /swagger.json, /api-docs and /.well-known/security.txt
  all return HTTP 404 across the AU, US and UK sites. The only live non-marketing front door is a customer login — CTM Portal at portal.travelctm.com and www.ctmsmart.com.au. CTM''s technology pages assert secure integration with client HR, expense, finance, ERP and single sign-on systems, but no interface contract, schema or endpoint is documented anywhere in public: the integration surface is proprietary and undocumented, reachable only under a managed-travel commercial agreement. The only published exit path is a GDPR/CCPA data-portability request by email to privacy@travelctm.com or DPO@travelctm.com; there is no self-service export.'
features:
- description: CTM's proprietary online booking tool, built and managed in-house, which aggregates GDS content, direct low-cost-carrier API connections and live airline NDC offers into a single policy-controlled corporate search and booking flow.
  name: Lightning
- description: Single sign-on customer portal that consolidates CTM's travel tools for pre-trip planning, approvals, in-trip tracking, risk alerts and post-trip reporting. Live at portal.travelctm.com and www.ctmsmart.com.au for existing customers only.
  name: CTM Portal
- description: End-to-end pre-trip approval workflow used to enforce corporate travel policy before a booking is ticketed.
  name: CTM Approve
- description: Cloud-based travel reporting and analytics platform covering air, hotel, car, rail, traveller tracking, carbon emissions and wellbeing. No export, feed or API is documented.
  name: CTM Data Hub
- description: Predictive fare forecasting tool used to time corporate air purchases.
  name: CTM Fare Forecaster
- description: Traveller mobile application for booking and itinerary management on the go.
  name: CTM Mobile App
- description: Chat-based booking and servicing channel for managing travel bookings.
  name: CTM Scout
- description: Real-time traveller risk alerts by SMS and email plus a Travel Risk Hub of destination requirements.
  name: Travel Risk Management
- description: Lightning ingests live NDC content from airlines — Qantas' Premium NDC connection in Australia, American Airlines and United Airlines in the United States — alongside GDS and direct API content. CTM consumes NDC; it does not publish an NDC endpoint of its own.
  name: NDC Content Integration
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-28'
name: Corporate Travel Management
nav: Providers
network: true
overview: 'Corporate Travel Management publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Australia, Corporate Travel, Travel Management Company, and Aviation.


  Corporate Travel Management''s developer surface includes authentication, documentation, developer portal, engineering blog, product news, and 37 more developer resources.'
random_paper: 12
scopes:
- name: Corporate Travel Management Scopes
  scope_count: 14
  slug: corporate-travel-management-scopes
  summary_line: 14 scopes · authorizationCode/clientCredentials/deviceCode/implicit
score:
  band: emerging
  composite: 24.7
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 24.7
  provenance:
    conformance: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/corporate-travel-management/refs/heads/main/screenshots/corporate-travel-management-2026-08-07T163917.png
security:
- kind: authentication
  name: Corporate Travel Management Authentication
  slug: corporate-travel-management-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Corporate Travel Management Domain Security
  slug: corporate-travel-management-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: trust-center
  name: Corporate Travel Management Trust Center
  slug: corporate-travel-management-trust-center
  summary_line: trust center published
slug: corporate-travel-management
tags:
- Travel
- Australia
- Corporate Travel
- Travel Management Company
- Aviation
- NDC
- Distribution
- Booking
- Hotels
- Meetings and Events
website: https://www.travelctm.com/
---
