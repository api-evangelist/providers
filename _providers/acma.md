---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.1
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Acma Agentic Access
  operation_count: 22
  slug: acma-agentic-access
  summary_line: 22 operations
api_count: 2
apis:
- description: 'The ACMA Spectrum Licensing API is an application programming interface which allows members of the public to query the ACMA''s spectrum licensing data — the Register of Radiocommunications Licences — '
  name: ACMA Spectrum Licensing API
  slug: spectrum-licensing
- description: The Do Not Call Register is operated by the ACMA under the Do Not Call Register Act 2006. Telemarketers and fax marketers must check ("wash") their contact lists against the register before calling. A
  name: Do Not Call Register Real Time Access (RTA) Washing Service
  slug: do-not-call-register-washing
arazzos:
- description: Resolve an Australian organisation to its ACMA client number, list every radiocommunications licence it holds, pull the registered devices on a licence and resolve the transmitter site those devices s
  name: ACMA — organisation spectrum footprint
  slug: acma-organisation-spectrum-footprint
- description: From a latitude/longitude, find the nearest licensed transmitter sites, pull the frequency assignments in a band and postcode range around them, and attribute an assignment back to its licensee.
  name: ACMA — spectrum survey by location
  slug: acma-spectrum-survey-by-location
artifact_total: 23
collections:
- collection_type: open
  name: ACMA Spectrum Licensing API
  slug: open-acma-spectrum-licensing
common:
- group: company
  title: ''
  type: Website
  url: https://www.acma.gov.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.acma.gov.au/
- group: start
  title: ''
  type: Portal
  url: https://developer.acma.gov.au/
- group: docs
  title: ''
  type: Documentation
  url: https://www.acma.gov.au/radiocomms-licence-data
- group: docs
  title: ''
  type: APIReference
  url: https://www.acma.gov.au/sites/default/files/2019-11/Spectrum%20licensing%20API.docx
- group: start
  title: ''
  type: GettingStarted
  url: https://www.acma.gov.au/register-radiocommunication-licences-rrl
- group: operate
  title: ''
  type: Support
  url: https://www.acma.gov.au/contact-us
- group: commercial
  title: ''
  type: Pricing
  url: https://www.donotcall.gov.au/industry/subscription-overview
- group: start
  title: ''
  type: SignUp
  url: https://www.donotcall.gov.au/industry/create-account
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.acma.gov.au/radiocomms-licence-data#terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acma.gov.au/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.acma.gov.au/vulnerability-disclosure-policy
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/acma-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acma-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/acma-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/acma-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/acma-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/acma-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/acma-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/acma-plans.yml
- group: build
  title: ''
  type: Packages
  url: packages/acma-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/acma-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.donotcall.gov.au/
- group: company
  title: ''
  type: Website
  url: https://www.thenumberingsystem.com.au/
- group: company
  title: ''
  type: Website
  url: https://myswitch.digitalready.gov.au/
- group: docs
  title: ''
  type: Documentation
  url: https://data.gov.au/data/organization/australiancommunicationsandmediaauthority
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/australian-communications-and-media-authority
created: '2026-07-25'
description: 'The Australian Communications and Media Authority (ACMA) is the Commonwealth regulator for telecommunications, radiocommunications, broadcasting and online content in Australia. It issues carrier licences and apparatus and spectrum licences, maintains the Register of Radiocommunications Licences, administers the Australian telephone numbering plan through the Numbering System, operates the Do Not Call Register, and polices the Telecommunications Consumer Protections and scam-call rules that bind Telstra, Optus, TPG and every other Australian carrier. Its API posture is that of a regulator: two real programmatic surfaces, both attached to a statutory register rather than to a platform. The ACMA Spectrum Licensing API is fully public and anonymous — a WCF service at api.acma.gov.au exposing 22 REST operations (XML and JSON projections of eleven web methods) plus a SOAP endpoint and a live WSDL, letting anyone query licences, licensees, transmitter sites, device registrations,
  antennas, access areas and the 400 MHz band register, capped at 2,000 records per query. The Do Not Call Register''s Real Time Access washing service is a live, publicly-retrievable ColdFusion SOAP WSDL whose three operations require a paid industry subscription, alongside an SFTP automated washing channel at sftp.donotcall.gov.au. ACMA also runs an Azure API Management developer portal at developer.acma.gov.au that is entirely behind a sign-in wall. Public register and licence bulk data is published as daily file downloads and on data.gov.au rather than as a queryable API. ACMA is a regulator, not an operator, so it sits outside the CAMARA and GSMA Open Gateway commitment layer entirely; no CAMARA reference was found anywhere in its public surface.'
examples:
- key_count: 1
  name: Acma 400Mhz Register Search
  slug: acma-400mhz-register-search
- key_count: 1
  name: Acma Access Area
  slug: acma-access-area
- key_count: 1
  name: Acma Antenna Search
  slug: acma-antenna-search
- key_count: 1
  name: Acma Assignment Range
  slug: acma-assignment-range
- key_count: 1
  name: Acma Category List
  slug: acma-category-list
- key_count: 1
  name: Acma Client Search
  slug: acma-client-search
- key_count: 1
  name: Acma Licence List
  slug: acma-licence-list
- key_count: 1
  name: Acma Licence Search
  slug: acma-licence-search
- key_count: 1
  name: Acma Registration Search
  slug: acma-registration-search
- key_count: 1
  name: Acma Site By Location
  slug: acma-site-by-location
- key_count: 1
  name: Acma Site Search
  slug: acma-site-search
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: ACMA MCP Server
  slug: acma-mcp-server
modified: '2026-07-25'
name: ACMA
nav: Providers
network: true
overview: 'ACMA publishes 1 API on the [APIs.io](https://apis.io/) network: Spectrum Licensing API. Tagged areas include Telecommunications, Australia, Regulator, Spectrum, and Broadcasting.


  ACMA''s developer surface includes developer portal, documentation, API reference, getting-started guide, support, pricing, signup flow, and 20 more developer resources.'
plans:
- name: Acma Plans
  plan_count: 9
  slug: acma-plans
random_paper: 3
rate_limits:
- limit_count: 6
  name: Acma Rate Limits
  slug: acma-rate-limits
score:
  band: developing
  composite: 53.8
  delta: 1.1
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 16.7
    contract_quality: 59.9
    developer_ergonomics: 38.7
    discoverability: 68.5
    governance: 16.7
    operational_transparency: 36.8
  previous_composite: 52.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 50.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/acma/refs/heads/main/screenshots/acma-2026-08-17T082235.png
security:
- kind: authentication
  name: Acma Authentication
  slug: acma-authentication
  summary_line: none/soap-body-credentials/ssh-key/session · 5 schemes
- kind: domain-security
  name: Acma Domain Security
  slug: acma-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Acma Vulnerability Disclosure
  slug: acma-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: acma
tags:
- Telecommunications
- Australia
- Regulator
- Spectrum
- Broadcasting
- Numbering
- Do Not Call Register
- Radio Communications
- Licensing
- Open Data
- Government
- SOAP
website: https://www.acma.gov.au/
---
