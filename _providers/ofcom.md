---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ofcom Agentic Access
  operation_count: 2
  slug: ofcom-agentic-access
  summary_line: 2 operations
api_count: 2
apis:
- baseURL: https://api-proxy.ofcom.org.uk/broadband
  baseurl_source: declared
  description: The Coverage API from Ofcom — 1 operation(s) for coverage.
  name: Ofcom Coverage API
  slug: ofcom-coverage-api
arazzos:
- description: Build a complete connectivity picture for one UK postcode by calling both Ofcom Connected Nations APIs — fixed broadband availability and mobile coverage across all four UK operators — and joining the
  name: Ofcom postcode connectivity profile
  slug: ofcom-postcode-connectivity-profile
artifact_total: 9
collections:
- collection_type: open
  name: Ofcom Connected Nations Broadband API
  slug: open-ofcom-connected-nations-broadband-api
- collection_type: open
  name: Ofcom Connected Nations Mobile API
  slug: open-ofcom-connected-nations-mobile-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/ofcom-connected-nations-broadband-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/ofcom-check-broadband-coverage.md
- group: other
  title: ''
  type: Overlay
  url: overlays/ofcom-connected-nations-mobile-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/ofcom-check-mobile-coverage.md
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/ofcom-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ofcom-agentic-access.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/ofcom-tool-crosswalk.yml
- group: build
  title: ''
  type: Packages
  url: packages/ofcom-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ofcom-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/ofcom-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ofcom-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ofcom-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ofcom-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ofcom-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ofcom-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ofcom-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ofcom-postcode-connectivity-profile.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ofcom-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ofcom-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.ofcom.org.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.ofcom.org.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://api.ofcom.org.uk/apis
- group: start
  title: ''
  type: SignUp
  url: https://api.ofcom.org.uk/signup
- group: other
  title: ''
  type: SignIn
  url: https://api.ofcom.org.uk/signin
- group: docs
  title: ''
  type: APIReference
  url: https://api.ofcom.org.uk/api-details
- group: start
  title: ''
  type: Console
  url: https://api.ofcom.org.uk/api-details
- group: commercial
  title: ''
  type: Plans
  url: https://api.ofcom.org.uk/products
- group: commercial
  title: ''
  type: Plans
  url: plans/ofcom-plans.yml
- group: operate
  title: ''
  type: Support
  url: mailto:cnapisupport@ofcom.org.uk
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ofcom.org.uk/siteassets/ofcom/phones-telecoms-and-internet/advice-for-consumers-/broadband-and-mobile-coverage-checker/ofcom-api-terms-of-use-2025.pdf?v=399736
- group: other
  title: ''
  type: MobileAndBroadbandChecker
  url: https://checker.ofcom.org.uk/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ofcom
created: '2026-07-25'
description: Ofcom is the Office of Communications, the United Kingdom's independent regulator and competition authority for telecommunications, spectrum, broadcasting, post, and online safety. It licenses UK spectrum, administers the national numbering plan, publishes the Connected Nations reports on fixed and mobile coverage, and supervises the operators (EE, VMO2, Vodafone, Three) rather than selling connectivity itself. Its position in the telecom value chain is therefore upstream of the market it measures — it is a data producer and rule-setter, not a network or a CPaaS aggregator. Its API posture is unusually good for a regulator and unusually narrow in scope. Ofcom runs a real, Ofcom-branded Azure API Management developer portal at api.ofcom.org.uk with open sign-up, an interactive console, published rate-limit tiers, and anonymously downloadable OpenAPI 3.0.1 documents for two APIs — the Connected Nations Broadband API and the Connected Nations Mobile API — both served from the live
  gateway at api-proxy.ofcom.org.uk and authenticated with an Azure APIM subscription key. Everything else Ofcom publishes (spectrum licence registers, numbering data, market research) is documents and datasets, not APIs, and the community has repeatedly built third-party APIs on top of those files. Ofcom appears once in the CAMARA project participant register but exposes no CAMARA network APIs and is not a GSMA Open Gateway participant — Open Gateway is an operator commitment programme and Ofcom is the regulator, not an operator.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Ofcom
nav: Providers
network: true
overview: 'Ofcom publishes 1 API on the [APIs.io](https://apis.io/) network: Coverage API. Tagged areas include Telecommunications, United Kingdom, Regulator, Broadband, and Mobile Network Coverage.


  Ofcom''s developer surface includes sandbox, authentication, documentation, signup flow, API reference, developer console, support, and 26 more developer resources.'
plans:
- name: Ofcom Plans
  plan_count: 4
  slug: ofcom-plans
random_paper: 7
rate_limits:
- limit_count: 8
  name: Ofcom Rate Limits
  slug: ofcom-rate-limits
score:
  band: developing
  composite: 48.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 4.5
    contract_quality: 55.8
    developer_ergonomics: 51.8
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 31.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 48.1
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
    regime: Telecommunications
    regime_id: telecommunications
    score: 37.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ofcom/refs/heads/main/screenshots/ofcom-2026-08-07T190010.png
security:
- kind: authentication
  name: Ofcom Authentication
  slug: ofcom-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Ofcom Domain Security
  slug: ofcom-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ofcom
tags:
- Telecommunications
- United Kingdom
- Regulator
- Broadband
- Mobile Network Coverage
- Spectrum
- Open Data
- Connected Nations
website: https://www.ofcom.org.uk/
---
