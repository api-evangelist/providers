---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-09-02'
api_count: 2
apis:
- baseURL: https://api.ons.io
  baseurl_source: declared
  description: The REST API for the Nedap Ons electronic health record suite used by Dutch care organisations. 926 operations across 782 paths covering clients, employees, dossiers and reports, care plans, goals and
  name: Nedap Ons API
  slug: nedap-ons-api
- description: The API for iD Cloud, Nedap's RFID item-level inventory platform for unified commerce, used to integrate store and supply-chain stock data with ERP and point-of-sale systems on top of an EPCIS engine.
  name: Nedap Retail iD Cloud API
  slug: nedap-retail-id-cloud-api
artifact_total: 8
asyncapis:
- description: ''
  name: Nedap Ons Webhooks
  slug: nedap-ons-webhooks
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nedap-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nedap-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nedap.com/en
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ons-api.nl/english/english.html
- group: docs
  title: ''
  type: Documentation
  url: https://ons-api.nl/english/technical/technical.html
- group: docs
  title: ''
  type: APIReference
  url: https://ons-api.nl/english/technical/APIS.html
- group: start
  title: ''
  type: GettingStarted
  url: https://ons-api.nl/english/integration_process/Integration_process.html
- group: start
  title: ''
  type: SignUp
  url: https://api-dashboard.ons.io/intake
- group: operate
  title: ''
  type: Support
  url: https://support.nedap-ons.nl/
- group: operate
  title: ''
  type: Roadmap
  url: https://portal.productboard.com/za1bhxsuikno2tvic9kvcryd
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nedap
- group: company
  title: ''
  type: Blog
  url: https://www.nedap.com/en/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nedap.com/en/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nedap.com/en/privacy-statement-disclaimer
- group: auth
  title: ''
  type: Security
  url: https://www.nedap.com/en/coordinated-vulnerability-disclosure-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://support.nedap-ons.nl/
- group: operate
  title: ''
  type: Deprecation
  url: https://ons-api.nl/english/technical/APIS-deprecated.html
- group: build
  title: ''
  type: Packages
  url: packages/nedap-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/nedap-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nedap-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/nedap-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nedap-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/nedap-ons-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/nedap-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nedap-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nedap-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/nedap-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nedap-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nedap-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/nedap-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nedap-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/nedap-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nedap-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/nedap-ons-webhooks.yml
created: '2026-09-02'
description: Nedap N.V. is a Dutch technology company founded in 1929 and listed on Euronext Amsterdam, headquartered in Groenlo, the Netherlands, with roughly 1,000 employees. It builds what it calls Digital Twin Technology across four markets — Healthcare (the Ons electronic health record suite and MediKIT for general practitioners), Livestock (cow monitoring), Retail (the iD Cloud RFID inventory platform and iSenseOS loss prevention) and Security (Nedap Access physical identity management and long-range vehicle/driver identification readers). Its most openly documented API surface is Ons API at ons-api.nl, a 926-operation OpenAPI 3.0.3 REST contract for the Ons care platform covering client dossiers, care planning, scheduling, rostering, payroll and finance, together with a 31-path openEHR composition and archetype surface, a webhook event service described in OpenAPI 3.1 webhooks, and a small scopes-and-clearances authorization API. A FHIR read/search surface built on the Dutch ZIB information
  models is documented but is not in the public specification — those endpoints sit behind the Ons API Dashboard. Access is gated on a client TLS certificate signed by Nedap's own CA and issued through the Ons API Dashboard, so the specifications are public while the runtime is not.
image: https://stream.nedap.com/57pq0bsyu489/w_1200,ex_0,ey_247,ew_1200,eh_628/nedap-logo-avatar-blue-at-2x.jpg
layout: provider
modified: '2026-09-02'
name: Nedap
nav: Providers
network: true
overview: 'Nedap publishes 1 API on the [APIs.io](https://apis.io/) network: Ons API. Tagged areas include Company, Healthcare, Electronic Health Records, Interoperability, and FHIR.


  The Nedap catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Nedap''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, changelog, and 28 more developer resources.'
plans:
- name: Nedap Plans Pricing
  plan_count: 0
  slug: nedap-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 3
  name: Nedap Rate Limits
  slug: nedap-rate-limits
score:
  band: strong
  composite: 60.2
  coverage:
    artifact_dirs: 19
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 54.8
    developer_ergonomics: 73.2
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 100.0
  provenance:
    conformance: first-party
    contracts:
      callable: 66.7
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 38.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
security:
- kind: authentication
  name: Nedap Authentication
  slug: nedap-authentication
  summary_line: mutualTLS · 1 scheme
- kind: domain-security
  name: Nedap Domain Security
  slug: nedap-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Nedap Vulnerability Disclosure
  slug: nedap-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: nedap
tags:
- Company
- Healthcare
- Electronic Health Records
- Interoperability
- FHIR
- openEHR
- RFID
- Retail
- Physical Security
- Livestock
- Netherlands
- Webhooks
website: https://www.nedap.com/en
---
