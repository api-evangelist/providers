---
agent_readiness:
  band: human-only
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
    error_semantics: false
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
  score: 5.0
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: SightCall's REST API is used by application back ends to request session tokens, manage users and sessions, provision providers and pull reporting. Authentication is by API key in the Authorization he
  name: SightCall REST API
  slug: rest-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/sightcall-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sightcall-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sightcall.com/
- group: operate
  title: ''
  type: Support
  url: https://support.sightcall.com/
- group: company
  title: ''
  type: Blog
  url: https://sightcall.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sightcall
- group: commercial
  title: ''
  type: Pricing
  url: https://sightcall.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://get.sightcall.com/demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sightcall.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sightcall.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sightcall.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sightcall-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/sightcall-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sightcall-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sightcall-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sightcall-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/sightcall-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sightcall-conventions.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sightcall-plans-pricing.yml
coverage:
  checked: '2026-08-27'
  detail: SightCall's entire developer surface moved behind the tenant console - every path on docs.sightcall.com now returns HTTP 307 to the admin.sightcall.com login, and SightCall's own llms.txt states the developer portal requires contacting the company for access, so the REST API reference, SDK docs and any spec are unreadable without a customer account.
  evidence:
  - status: 307
    url: https://docs.sightcall.com/gd/rest-api
  - status: 307
    url: https://docs.sightcall.com/gd/how-to/authenticate
  - status: 200
    url: https://sightcall.com/llms.txt
  - status: 403
    url: https://api.sightcall.com/openapi.json
  - status: 404
    url: https://sightcall.com/openapi.json
  - status: 0
    url: https://api.rtccloud.net/v2.0/
  reason: customer-only-docs
  state: gated
created: '2026-08-27'
description: SightCall is a San Francisco headquartered enterprise remote visual support platform. Its VISION product connects experts, technicians and customers over live AR-enhanced WebRTC video so that field service, customer service, insurance and telehealth teams can diagnose and resolve issues without an on-site visit. The platform layers computer vision (defect detection, parts recognition, OCR of serial numbers, gauges and meter readings), AI session insights, and Xpert Knowledge, which turns recorded sessions into structured step-by-step tutorials. SightCall ships iOS, Android and Web client SDKs plus a REST API for session management, user provisioning, reporting and workflow integration, and is embedded into Salesforce Service Cloud, Microsoft Dynamics 365, ServiceNow, SAP, Zendesk, Genesys, Five9, NICE and Guidewire. The developer portal carrying the REST API reference and SDK documentation is not public - SightCall directs developers to contact the company for access.
image: https://sightcall.com/wp-content/uploads/SightCall.jpg
layout: provider
modified: '2026-08-27'
name: SightCall
nav: Providers
network: true
overview: 'SightCall publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Video, WebRTC, Remote Support, and Field Service.


  SightCall''s developer surface includes support, engineering blog, pricing, signup flow, and 15 more developer resources.'
plans:
- name: Sightcall Plans Pricing
  plan_count: 0
  slug: sightcall-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Sightcall Rate Limits
  slug: sightcall-rate-limits
score:
  band: thin
  composite: 28.0
  coverage:
    artifact_dirs: 11
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 28.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 45.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Sightcall Authentication
  slug: sightcall-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Sightcall Domain Security
  slug: sightcall-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Sightcall Trust Center
  slug: sightcall-trust-center
  summary_line: SOC 2, HIPAA, GDPR, CSA STAR
slug: sightcall
tags:
- Company
- Video
- WebRTC
- Remote Support
- Field Service
- Augmented Reality
- Computer-Vision
- Customer Service
- Insurance
- Telehealth
- Communications
website: https://sightcall.com/
---
