---
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
  score: 13.3
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: 'Asynchronously add or update media and metadata for audio and text-based contacts in a CallMiner Eureka tenant. Hosted on the regional CallMiner API host and protected by OAuth 2.0 client credentials '
  name: CallMiner Eureka Ingestion API
  slug: callminer-eureka-ingestion-api
- description: Create and poll bulk export jobs that extract contact, transcript, score and metadata datasets out of a CallMiner Eureka tenant as downloadable archives. Protected by OAuth 2.0 client credentials agai
  name: CallMiner Eureka Bulk Export API
  slug: callminer-eureka-bulk-export-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/callminer-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/callminer-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://callminer.com/
- group: company
  title: ''
  type: Blog
  url: https://callminer.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://callminer.com/blog/feed
- group: operate
  title: ''
  type: Support
  url: https://callminer.com/contact
- group: operate
  title: ''
  type: Community
  url: https://community.callminer.com/
- group: operate
  title: ''
  type: FAQ
  url: https://callminer.com/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://callminer.com/terms-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://callminer.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.callminer.net/
- group: auth
  title: ''
  type: Compliance
  url: https://callminer.com/our-company-security
- group: auth
  title: ''
  type: Authentication
  url: authentication/callminer-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/callminer-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/callminer-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/callminer-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/callminer-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/callminer-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/callminer-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/callminer-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/callminer-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/callminer-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/callminer-rate-limits.yml
coverage:
  checked: '2026-08-14'
  detail: CallMiner's own Swagger document is live at the .NET Swashbuckle default path on both API mounts — /swagger/v1/swagger.json and /bulkexport/swagger/v1/swagger.json — and each 302s to https://idp.callminer.net/connect/authorize, so the contract exists and is named v1 but requires an interactive CallMiner tenant login to read.
  evidence:
  - status: 302
    url: https://api.callminer.net/swagger/v1/swagger.json
  - status: 302
    url: https://api.callminer.net/bulkexport/swagger/v1/swagger.json
  - status: 404
    url: https://api.callminer.net/openapi.json
  - status: 200
    url: https://community.callminer.com/
  reason: customer-only-docs
  state: gated
created: '2026-08-09'
description: CallMiner is a Waltham, Massachusetts conversation intelligence and contact-center analytics company whose Eureka platform captures and analyzes omnichannel customer interactions — recorded and real-time audio, screen recordings, chat, email, surveys and video — to surface customer experience, quality management, risk and compliance, fraud and sales-effectiveness insight. The product family spans Capture (Record, Screen Record, Redact), Intelligence (Analyze, Visualize), Augmentation (Coach, RealTime) and Automation (Outreach, OmniAgent, LiveTranslate). CallMiner exposes an OAuth 2.0 protected developer API — a media/metadata Ingestion API and a Bulk Export API — hosted on regional api*.callminer.net endpoints and secured by its own IdentityServer-based identity provider at idp*.callminer.net. The API reference is published as Swagger UI on the API host itself but sits behind an interactive login, so no machine-readable contract is publicly retrievable.
image: https://images.ctfassets.net/xj0skx6m69u2/cFRNy2dkU6bRc2iRmk7tF/6f1fc904dea9217c746c0b5cfd9eaa32/Logo_CallMiner_Color.svg
layout: provider
modified: '2026-08-14'
name: CallMiner
nav: Providers
network: true
overview: 'CallMiner publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Conversation Intelligence, Speech Analytics, Contact Center, and Customer Experience.


  CallMiner''s developer surface includes engineering blog, support, FAQ, authentication, and 19 more developer resources.'
plans:
- name: Callminer Plans Pricing
  plan_count: 0
  slug: callminer-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Callminer Rate Limits
  slug: callminer-rate-limits
scopes:
- name: Callminer Scopes
  scope_count: 5
  slug: callminer-scopes
  summary_line: 5 scopes · authorizationCode/clientCredentials
score:
  band: emerging
  composite: 23.0
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 23.0
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Callminer Authentication
  slug: callminer-authentication
  summary_line: oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Callminer Domain Security
  slug: callminer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Callminer Trust Center
  slug: callminer-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001:2022, HITRUST CSF, FISMA, PCI DSS, HIPAA
slug: callminer
tags:
- Company
- Conversation Intelligence
- Speech Analytics
- Contact Center
- Customer Experience
- Artificial Intelligence
- Analytics
- Transcription
- Quality Management
- Compliance
website: https://callminer.com/
---
