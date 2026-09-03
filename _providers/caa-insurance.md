---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/caa-insurance-domain-security.yml
- group: other
  title: ''
  type: WSDL
  url: wsdl/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/caa-insurance-authentication.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/caa-insurance-openid-configuration.json
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/caa-insurance-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/caa-insurance-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/caa-insurance-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/caa-insurance-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/caa-insurance-problem-types.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/caa-insurance-llms.txt
- group: company
  title: ''
  type: Website
  url: https://caainsurancecompany.ca/
- group: company
  title: ''
  type: About
  url: https://caainsurancecompany.ca/about
- group: company
  title: ''
  type: Blog
  url: https://caainsurancecompany.ca/blog
- group: operate
  title: ''
  type: FAQ
  url: https://caainsurancecompany.ca/faq
- group: operate
  title: ''
  type: Support
  url: https://caainsurancecompany.ca/claims-and-inquires
- group: start
  title: ''
  type: Login
  url: https://customer.caainsurancecompany.ca/
- group: start
  title: ''
  type: PartnerPortal
  url: https://www.caabrokerportal.ca/
- group: company
  title: ''
  type: Partners
  url: https://broker.caainsurance.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://caainsurancecompany.ca/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://caainsurancecompany.ca/terms-of-use
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/caa-insurance-company/
created: '2026-07-25'
description: 'CAA Insurance Company is a Canadian property and casualty carrier that began underwriting in 1974 and is part of CAA Club Group, the CAA South Central Ontario federation, with its head office at 60 Commerce Valley Drive East in Thornhill, Ontario. It underwrites personal-lines auto insurance (including accident benefits, the CAA MyPace pay-as-you-drive product, CAA Connect telematics, and antique and classic vehicle coverage) and personal property insurance (homeowners, condominium, and tenant), plus optional endorsements such as tire coverage, home equipment breakdown, service line, renewable energy equipment, and legal expense coverage. It sells in British Columbia, Saskatchewan, Manitoba, Ontario, New Brunswick, Nova Scotia, and Prince Edward Island through a direct-to-consumer channel and through independent brokers. Its API posture is honestly none: as of the July 2026 review there is no public developer portal, no self-serve API program, no downloadable OpenAPI or Swagger
  definition, and no published event or webhook catalog. Every developer-style host and path probed (developer/developers/docs/api subdomains, and /developers, /api, /developer, /partners, /integrations on both caainsurancecompany.com and caainsurancecompany.ca) either failed DNS or returned 404. The only integration surface is the CAA Broker Portal at caabrokerportal.ca, which is a Microsoft Entra External ID (CIAM) WS-Federation login wall in front of a SharePoint broker workspace, and the broker program microsite at broker.caainsurance.com, which is marketing and business-development content only. The one machine-readable contract anywhere in the estate is platform-provided rather than authored by CAA: the broker portal runs Microsoft SharePoint 16.0.0.5552 and serves twenty SOAP WSDL documents (199 operations, none of them insurance operations) anonymously at /_vti_bin/<service>.asmx?WSDL, with its REST/OData sibling at /_api/web returning 403 to anonymous callers; the CAA Club Group
  Entra External ID tenant likewise serves standard OpenID Connect discovery. Consumer quoting runs through hosted web applications rather than an exposed quote API. This is a representative record of the Canadian carrier tier, where there is no open-insurance mandate — OSFI supervises prudentially, provincial regulators such as FSRA and the AMF handle market conduct, and Consumer-Driven Banking excludes insurance entirely — so carriers face no forcing function to publish anything.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: CAA Insurance
nav: Providers
network: true
overview: 'CAA Insurance is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Canada, Property and Casualty, Auto Insurance, and Home Insurance.


  CAA Insurance''s developer surface includes authentication, engineering blog, FAQ, support, and 17 more developer resources.'
random_paper: 4
scopes:
- name: Caa Insurance Scopes
  scope_count: 4
  slug: caa-insurance-scopes
  summary_line: 4 scopes · authorizationCode/deviceCode
score:
  band: thin
  composite: 27.0
  coverage:
    artifact_dirs: 11
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 26.7
    developer_ergonomics: 19.0
    discoverability: 50.0
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 27.0
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 63.6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/caa-insurance/refs/heads/main/screenshots/caa-insurance-2026-07-25T204155.png
security:
- kind: authentication
  name: Caa Insurance Authentication
  slug: caa-insurance-authentication
  summary_line: ws-federation/openIdConnect/oauth2/session-cookie · 4 schemes
- kind: domain-security
  name: Caa Insurance Domain Security
  slug: caa-insurance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: caa-insurance
tags:
- Insurance
- Canada
- Property and Casualty
- Auto Insurance
- Home Insurance
- Carrier
- Brokers
- Personal Lines
- Telematics
- Partner Gated
- No Public API
website: https://caainsurancecompany.ca/
---
