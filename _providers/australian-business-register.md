---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 39.9
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: SOAP/XML web service for ABN Lookup that searches the Australian Business Register by ABN, ACN/ASIC number, name, postcode, charity, ABN status and registration/update events. It is free to registered
  name: ABN Lookup XML Search Web Service (ABRXMLSearch)
  slug: abn-lookup-xml-search-web-service
- description: 'RPC-style variant of the ABN Lookup SOAP web service, linked from the ABN Lookup web services methods page. It exposes the same search operations (27, without SearchByABNv202001). The provider-hosted '
  name: ABN Lookup XML Search Web Service, RPC (ABRXMLSearchRPC)
  slug: abn-lookup-xml-search-rpc-web-service
- description: JSONP services for ABN Lookup (AbnDetails.aspx, AcnDetails.aspx, MatchingNames.aspx) that take a callback and the registered user's GUID. No machine-readable contract is published for the JSON service
  name: ABN Lookup JSON Services
  slug: abn-lookup-json-services
artifact_total: 8
common:
- group: auth
  href: https://artifacts.apis.io/australian-business-register/well-known/australian-business-register-socket-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/australian-business-register-socket-security.txt
- group: commercial
  href: https://artifacts.apis.io/australian-business-register/plans/australian-business-register-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/australian-business-register-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/australian-business-register/changelog/australian-business-register-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/australian-business-register-changelog.yml
- group: design
  href: https://artifacts.apis.io/australian-business-register/conventions/australian-business-register-conventions.yml
  title: ''
  type: Conventions
  url: conventions/australian-business-register-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://www.ato.gov.au/online-services/cyber-safety/report-a-system-security-vulnerability
- group: auth
  href: https://artifacts.apis.io/australian-business-register/authentication/australian-business-register-authentication.yml
  title: ''
  type: Authentication
  url: authentication/australian-business-register-authentication.yml
- group: operate
  href: https://artifacts.apis.io/australian-business-register/lifecycle/australian-business-register-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/australian-business-register-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/australian-business-register/lifecycle/australian-business-register-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/australian-business-register-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/australian-business-register/errors/australian-business-register-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/australian-business-register-error-codes.yml
- group: design
  href: https://artifacts.apis.io/australian-business-register/conformance/australian-business-register-conformance.yml
  title: ''
  type: Conformance
  url: conformance/australian-business-register-conformance.yml
- group: auth
  href: https://artifacts.apis.io/australian-business-register/well-known/australian-business-register-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/australian-business-register-security.txt
- group: auth
  href: https://artifacts.apis.io/australian-business-register/well-known/australian-business-register-abr-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/australian-business-register-abr-security.txt
- group: agent
  href: https://artifacts.apis.io/australian-business-register/well-known/australian-business-register-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/australian-business-register-well-known.yml
- group: other
  href: https://artifacts.apis.io/australian-business-register/hosts/australian-business-register-hosts.yml
  title: ''
  type: Hosts
  url: hosts/australian-business-register-hosts.yml
- group: auth
  href: https://artifacts.apis.io/australian-business-register/security/australian-business-register-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/australian-business-register-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/australian-business-register/security/australian-business-register-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/australian-business-register-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://abr.gov.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://abr.business.gov.au/Tools/WebServices
- group: docs
  title: ''
  type: Documentation
  url: https://abr.business.gov.au/Documentation/Default
- group: docs
  title: ''
  type: APIReference
  url: https://abr.business.gov.au/Documentation/WebServiceMethods
- group: start
  title: ''
  type: GettingStarted
  url: https://abr.business.gov.au/Documentation/WebServiceRegistration
- group: start
  title: ''
  type: SignUp
  url: https://abr.business.gov.au/Documentation/WebServiceRegistration
- group: build
  title: ''
  type: SampleCode
  url: https://abr.business.gov.au/Documentation/SampleCodeResources
- group: operate
  title: ''
  type: ChangeLog
  url: https://abr.business.gov.au/Documentation/ChangeControl
- group: operate
  title: ''
  type: Support
  url: https://abr.business.gov.au/ContactUs
- group: operate
  title: ''
  type: FAQ
  url: https://abr.business.gov.au/Faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://abr.business.gov.au/Tools/WebServicesAgreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://abr.business.gov.au/Home/PrivacyPolicies
- group: company
  title: ''
  type: About
  url: https://abr.business.gov.au/Home/About
created: '2026-10-22'
description: 'The Australian Business Register (ABR), administered within the Australian Taxation Office (ATO), holds the publicly available information businesses provide when they register for an Australian Business Number (ABN). It exposes that data through ABN Lookup (abr.business.gov.au), hosted by the Department of Industry, Science and Resources, including free ABN Lookup web services: a SOAP/XML service (ABRXMLSearch, with WSDL) and JSON services for searching by ABN, ACN, name and postcode, available to registered users who accept the Web Services Agreement and obtain a GUID.'
image: https://abr.business.gov.au/Images/logo-abnl.png
layout: provider
modified: '2026-10-22'
name: Australian Business Register
nav: Providers
network: true
overview: 'Australian Business Register is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Government, Australia, Business Registry, and ABN.


  Australian Business Register''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, signup flow, support, and 22 more developer resources.'
plans:
- name: Australian Business Register Plans Pricing
  plan_count: 1
  slug: australian-business-register-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Australian Business Register Rate Limits
  slug: australian-business-register-rate-limits
score:
  band: thin
  composite: 34.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.1
  facets:
    access_clarity: 38.2
    contract_governance: 18.2
    contract_quality: 24.0
    developer_ergonomics: 33.3
    discoverability: 71.4
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 44.4
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/australian-business-register/australian-business-register-2026-11-03T121343.png
security:
- kind: authentication
  name: Australian Business Register Authentication
  slug: australian-business-register-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Australian Business Register Domain Security
  slug: australian-business-register-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Australian Business Register Vulnerability Disclosure
  slug: australian-business-register-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: australian-business-register
tags:
- Company
- Government
- Australia
- Business Registry
- ABN
- Tax
- Public Sector
- Open Data
website: https://abr.gov.au/
---
