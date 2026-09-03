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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: REST/JSON management API for the Webroot platform. Authenticate once via OAuth2 at /auth/token, then call /service/api resources with a bearer token to provision and update product licenses, place and
  name: Webroot Unity API
  slug: webroot-unity-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: http://www.webroot.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://unityapi.webrootcloudav.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://unityapi.webrootcloudav.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://unityapi.webrootcloudav.com/Docs/en/APIDoc/Documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://unityapi.webrootcloudav.com/docs
- group: operate
  title: ''
  type: StatusPage
  url: https://status.webroot.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.webroot.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.webroot.com/us/en/legal/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/webroot-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/webroot-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/webroot-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/webroot-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/webroot-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/webroot-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/webroot-llms.txt
created: '2026-07-17'
description: Webroot is a cybersecurity company, now part of OpenText Cybersecurity, that provides cloud-based endpoint protection, DNS protection, security awareness training, and the BrightCloud threat intelligence services. Its developer surface is the Webroot Unity API — a REST/JSON platform secured with OAuth2 that lets partners and administrators manage product licenses and orders, query order information, and request endpoint status across the Webroot Global Site Manager (GSM) console. Webroot business and BrightCloud product pages now redirect into OpenText Cybersecurity, and the Unity API documentation remains actively maintained.
image: https://unityapi.webrootcloudav.com/Docs/Images/ot_favicon.png
layout: provider
modified: '2026-07-21'
name: Webroot
nav: Providers
network: true
overview: 'Webroot publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Endpoint Protection, Threat Intelligence, and Security.


  Webroot''s developer surface includes documentation, API reference, getting-started guide, authentication, and 11 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 24.4
  coverage:
    artifact_dirs: 8
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 15.8
  previous_composite: 24.4
  provenance:
    conformance: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/webroot/refs/heads/main/screenshots/webroot-2026-09-02T170533.png
security:
- kind: authentication
  name: Webroot Authentication
  slug: webroot-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Webroot Domain Security
  slug: webroot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: webroot
tags:
- Company
- Cybersecurity
- Endpoint Protection
- Threat Intelligence
- Security
- Antivirus
- DNS Protection
- OpenText
website: http://www.webroot.com
---
