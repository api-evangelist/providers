---
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: Atomik is CaboLabs' standardized Clinical Data Repository and Demographic Data Repository. Its REST API implements the official openEHR ITS REST specification Release 1.0.2 for EHR, EHR_STATUS, CONTRI
  name: Atomik openEHR REST API
  slug: cabolabs-atomik-openehr-rest-api
- description: EHRServer is CaboLabs' Apache-2.0 open source, service-oriented openEHR clinical data repository. It exposes a REST API under /rest/v1 for authentication, organizations, users, EHRs, operational templ
  name: CaboLabs EHRServer REST API
  slug: cabolabs-ehrserver-rest-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://cabolabs.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://atomik.app/documentation
- group: docs
  title: ''
  type: Documentation
  url: https://cabolabs.com/our_software/atomik/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://atomik.app/documentation/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://atomik.app/documentation/getting_started
- group: operate
  title: ''
  type: Support
  url: https://cabolabs.com/our_software/atomik/faq
- group: company
  title: ''
  type: Blog
  url: https://cabolabs.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CaboLabs
- group: commercial
  title: ''
  type: Pricing
  url: https://cabolabs.com/our_software/atomik/pricing
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cabolabs-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/cabolabs-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cabolabs-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/cabolabs-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cabolabs-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cabolabs-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cabolabs-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cabolabs-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cabolabs-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cabolabs-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cabolabs-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cabolabs-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cabolabs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cabolabs-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cabolabs-domain-security.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cabolabs-sandbox.yml
- group: build
  title: ''
  type: Examples
  url: examples/cabolabs-ehrserver-2.0-insomnia.json
created: '2026-09-02'
description: CaboLabs Health Informatics is a Montevideo, Uruguay based health informatics company founded in 2012 by Pablo Pazos Gutierrez, specializing in clinical data standards and interoperability. It builds and licenses Atomik, a standardized openEHR Clinical Data Repository and Demographic Data Repository that implements the openEHR ITS REST API Release 1.0.2 over a JWT-authenticated JSON API, and maintains a family of Apache-2.0 open source openEHR tooling including the EHRServer clinical data repository, the openEHR-SDK for JVM languages, the openEHR-CLI, an openEHR conformance verification framework, and the openEHR Toolkit. Alongside the software it delivers consultancy, audit and training services covering openEHR, HL7 FHIR, HL7 v2.x, CDA, DICOM and SNOMED CT for hospitals, health-tech startups and software vendors worldwide.
examples:
- key_count: 5
  name: Cabolabs Ehrserver 2.0 Insomnia
  slug: cabolabs-ehrserver-2.0-insomnia
image: https://cabolabs.com/images/cabolabs_vertical_square_web_text.png
layout: provider
mcp_servers:
- description: ''
  name: openehr-cli MCP server
  slug: openehr-cli-mcp-server
modified: '2026-09-02'
name: CaboLabs
nav: Providers
network: true
overview: 'CaboLabs publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Interoperability, and openEHR.


  CaboLabs'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, CLI, and 19 more developer resources.'
plans:
- name: Cabolabs Plans Pricing
  plan_count: 3
  slug: cabolabs-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Cabolabs Rate Limits
  slug: cabolabs-rate-limits
score:
  band: thin
  composite: 38.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.4
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 6.7
    developer_ergonomics: 78.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 38.0
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Cabolabs Authentication
  slug: cabolabs-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Cabolabs Domain Security
  slug: cabolabs-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cabolabs
tags:
- Company
- Health
- Healthcare
- Interoperability
- openEHR
- FHIR
- HL7
- Clinical Data Repository
- Electronic Health Records
- Standards
- SNOMED CT
- DICOM
- Medical Records
- Uruguay
website: https://cabolabs.com/
---
