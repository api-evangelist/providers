---
access_model:
  confidence: high
  label: Free and anonymous
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probe
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 24.6
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: BASIL — "The FuSa Spice" — is ELISA's own software quality management tool. It decomposes a software component specification into snippets, maps work items (software requirements, test specifications,
  name: BASIL REST API
  slug: elisa-basil-api
- baseURL: https://elisa.tech/wp-json/tribe/events/v1/
  baseurl_source: declared
  description: The Categories API from ELISA — 2 operation(s) for categories.
  name: ELISA Categories API
  slug: elisa-categories-api
- baseURL: https://elisa.tech/wp-json/tribe/events/v1/
  baseurl_source: declared
  description: The Doc API from ELISA — 1 operation(s) for doc.
  name: ELISA Doc API
  slug: elisa-doc-api
- baseURL: https://elisa.tech/wp-json/tribe/events/v1/
  baseurl_source: declared
  description: The Events API from ELISA — 3 operation(s) for events.
  name: ELISA Events API
  slug: elisa-events-api
- baseURL: https://elisa.tech/wp-json/tribe/events/v1/
  baseurl_source: declared
  description: The Organizers API from ELISA — 3 operation(s) for organizers.
  name: ELISA Organizers API
  slug: elisa-organizers-api
- baseURL: https://elisa.tech/wp-json/tribe/events/v1/
  baseurl_source: declared
  description: The Tags API from ELISA — 2 operation(s) for tags.
  name: ELISA Tags API
  slug: elisa-tags-api
- baseURL: https://elisa.tech/wp-json/tribe/events/v1/
  baseurl_source: declared
  description: The Venues API from ELISA — 3 operation(s) for venues.
  name: ELISA Venues API
  slug: elisa-venues-api
artifact_total: 12
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/elisa-tech/BASIL/blob/main/LICENSE
- group: start
  title: ''
  type: DeveloperPortal
  url: https://directory.elisa.tech/
- group: docs
  title: ''
  type: Documentation
  url: https://directory.elisa.tech/
- group: docs
  title: ''
  type: APIReference
  url: https://elisa.tech/wp-json/tribe/events/v1/doc
- group: start
  title: ''
  type: GettingStarted
  url: https://elisa.tech/about/faqs/
- group: operate
  title: ''
  type: Support
  url: https://lists.elisa.tech/g/devel
- group: operate
  title: ''
  type: HelpCenter
  url: https://elisa.tech/about/contact/
- group: company
  title: ''
  type: Blog
  url: https://elisa.tech/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://elisa.tech/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/elisa-tech
- group: start
  title: ''
  type: SignUp
  url: https://elisa.tech/membership/join/
- group: commercial
  title: ''
  type: Pricing
  url: https://elisa.tech/membership/join/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.linuxfoundation.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.linuxfoundation.org/privacy
- group: other
  title: ''
  type: WhitePapers
  url: https://elisa.tech/white-papers/
- group: other
  title: ''
  type: CaseStudies
  url: https://elisa.tech/case-studies/
- group: operate
  title: ''
  type: Community
  url: http://chat.elisa.tech/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/elisa-events-calendar-openapi.json
- group: other
  title: ''
  type: Overlay
  url: overlays/elisa-events-calendar-overlay.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/elisa-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/elisa-api-catalog.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/elisa-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/elisa-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/elisa-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/elisa-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/elisa-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/elisa-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/elisa-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/elisa-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/elisa-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/elisa-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/elisa-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/elisa-finops.yml
created: '2026-03-16'
description: 'ELISA (Enabling Linux in Safety Applications) is a Linux Foundation collaborative project that builds the shared tools, processes and evidence needed to use Linux in safety-critical systems. Its working groups and special interest groups span automotive, aerospace, medical devices, railways, space-grade Linux and open-source engineering process, producing white papers, case studies, kernel analysis tooling and a public technical directory. ELISA develops two tools of its own: BASIL, a software quality management and traceability application with an HTTP REST API and SPDX 3.0.1 export, and ks-nav, kernel-source navigation tooling. ELISA itself publishes a machine-readable API surface at https://elisa.tech/wp-json/ — declared through an RFC 9727 api-catalog and described by a live OpenAPI 3.0.0 document — plus an llms.txt and permissive Content Signals for AI use.'
finops:
- name: Elisa Finops
  service_category: API
  slug: elisa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/elisa.png
layout: provider
modified: '2026-08-27'
name: ELISA
nav: Providers
network: true
overview: 'ELISA publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Categories API, Doc API, Events API, and 3 more. Tagged areas include Embedded, Linux, Linux Foundation, Safety, and Functional Safety.


  ELISA''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, pricing, and 27 more developer resources.'
plans:
- name: Elisa Plans Pricing
  plan_count: 3
  slug: elisa-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Elisa Rate Limits
  slug: elisa-rate-limits
score:
  band: developing
  composite: 49.8
  coverage:
    artifact_dirs: 20
    catalog_gap: 68.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 37.3
    developer_ergonomics: 58.9
    discoverability: 66.7
    governance: 4.5
    operational_transparency: 21.1
  previous_composite: 49.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/elisa/refs/heads/main/screenshots/elisa-2026-06-20T180611.png
security:
- kind: authentication
  name: Elisa Authentication
  slug: elisa-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Elisa Domain Security
  slug: elisa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: elisa
tags:
- Embedded
- Linux
- Linux Foundation
- Safety
- Functional Safety
- Open-Source
- Automotive
- Aerospace
- Medical Devices
- Traceability
- Standards
- Event
website: https://directory.elisa.tech/
---
