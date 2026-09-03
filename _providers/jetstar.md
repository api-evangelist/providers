---
access_model:
  confidence: high
  label: Commercial agreement · IATA-accredited Registered Travel Agents only
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - documentation
  - terms
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
- description: The Jetstar API is Jetstar's direct-connect distribution channel for Registered Travel Agents and partners. It is a Navitaire New Skies (NSK) SOAP / WCF web service, not a REST product and not IATA ND
  name: Jetstar API
  slug: jetstar-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.jetstar.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apiblog.jetstar.com/
- group: start
  title: ''
  type: Portal
  url: https://apiblog.jetstar.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.jetstar.com/us/en/travel-agents/information-centre/jetstar-api
- group: docs
  title: ''
  type: APIReference
  url: https://apiblog.jetstar.com/api-documentation/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.jetstar.com/us/en/travel-agents/why-become-a-registered-travel-agent-with-jetstar
- group: start
  title: ''
  type: SignUp
  url: https://www.jetstar.com/us/en/travel-agents
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jetstar.com/us/en/travel-agents/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jetstar.com/au/en/privacy-policy
- group: operate
  title: ''
  type: Support
  url: mailto:apisupport@jetstar.com
- group: operate
  title: ''
  type: Support
  url: mailto:sales@jetstar.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.jetstar.com/us/en/travel-agents/information-centre/bsp-settlement
- group: docs
  title: ''
  type: Documentation
  url: https://www.jetstar.com/us/en/travel-agents/bsp-payment-changes
- group: docs
  title: ''
  type: Documentation
  url: https://www.jetstar.com/au/en/travel-agents/remuneration
- group: operate
  title: ''
  type: FAQ
  url: https://www.jetstar.com/_/media/files/qantas-group/qantas-group-081-faqs.pdf
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/JetstarAirways
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jetstar-airways
- group: company
  title: ''
  type: Blog
  url: https://newsroom.jetstar.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/jetstar-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/jetstar-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/jetstar-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://apiblog.jetstar.com/category/outages/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/jetstar-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/jetstar-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/jetstar-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/jetstar-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/jetstar-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/jetstar-qantas-group-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jetstar-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/jetstar-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.qantas.com/.well-known/security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jetstar-llms.txt
created: '2026-07-28'
description: Jetstar Airways Pty Limited (ABN 33 069 720 243) is the Melbourne-based low-cost carrier of the Qantas Group and, with Virgin Australia, one half of the Australian domestic duopoly. The Jetstar Group flies as Jetstar Airways (JQ) and Jetstar Japan (GK); Jetstar Asia (3K) flew its last service on 31 July 2025. Jetstar sits at the direct-distribution end of the Australian travel chain — it sells through jetstar.com, through the Jetstar Agent Hub, through seven GDSs, and through a partner channel it calls, literally, the Jetstar API. That API is not a public developer product and it is not IATA NDC — it is the Navitaire New Skies SOAP web service (NSK 4.6) hosted on the vendor's own domain at jqapi.navitaire.com, with documentation, registration and downloads behind a login at apiblog.jetstar.com. There is no public developer portal, no OpenAPI or WSDL published, no self-serve signup and no bulk export operation. Access requires GoStandard or GoGlobal IATA accreditation for BSP
  settlement plus separate Jetstar approval, Registered Agent status under Jetstar's Travel Agent Terms and Conditions, a client certificate and IP allow-listing. Jetstar's own trade communications name only three authorised booking facilities for Registered Agents — API, GDS and Jetstar Agent Hub — and state that Registered Agents may only access Jetstar Data and make bookings via the API for all online distribution.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-28'
name: Jetstar
nav: Providers
network: true
overview: 'Jetstar publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Australia, Aviation, Airline, and Low Cost Carrier.


  Jetstar''s developer surface includes developer portal, documentation, API reference, getting-started guide, signup flow, support, FAQ, and 25 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 23.9
  coverage:
    artifact_dirs: 12
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 44.7
  previous_composite: 23.9
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 37.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jetstar/refs/heads/main/screenshots/jetstar-2026-08-07T171000.png
security:
- kind: authentication
  name: Jetstar Authentication
  slug: jetstar-authentication
  summary_line: mutualTLS/session-token/ip-allowlist · 3 schemes
- kind: domain-security
  name: Jetstar Domain Security
  slug: jetstar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Jetstar Vulnerability Disclosure
  slug: jetstar-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: jetstar
tags:
- Travel
- Australia
- Aviation
- Airline
- Low Cost Carrier
- Distribution
- Booking
- GDS
- Corporate Travel
- Qantas Group
website: https://www.jetstar.com/
---
