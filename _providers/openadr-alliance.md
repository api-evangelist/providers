---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.6
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 75
  human_in_the_loop: 0
  name: Openadr Alliance Agentic Access
  operation_count: 152
  slug: openadr-alliance-agentic-access
  summary_line: 152 operations · 75 acting
api_count: 4
apis:
- baseURL: http://localhost:8081/openadr3
  baseurl_source: spec
  description: The Auth API from OpenADR Alliance — 2 operation(s) for auth.
  name: OpenADR Alliance Auth API
  slug: openadr-alliance-auth-api
- baseURL: http://localhost:8081/openadr3
  baseurl_source: spec
  description: The events API from OpenADR Alliance — 2 operation(s) for events.
  name: OpenADR Alliance Events API
  slug: openadr-alliance-events-api
- baseURL: https://virtserver.swaggerhub.com/OPENADR3_1/openADR3.1.0/1.0.0
  baseurl_source: spec
  description: The MQTT_notifier API from OpenADR Alliance — 12 operation(s) for mqtt_notifier.
  name: OpenADR Alliance MQTT Notifier API
  slug: openadr-alliance-mqtt-notifier-api
- baseURL: https://virtserver.swaggerhub.com/OPENADR3_1/openADR3.1.0/1.0.0
  baseurl_source: spec
  description: The notifiers API from OpenADR Alliance — 1 operation(s) for notifiers.
  name: OpenADR Alliance Notifiers API
  slug: openadr-alliance-notifiers-api
- baseURL: http://localhost:8081/openadr3
  baseurl_source: spec
  description: The programs API from OpenADR Alliance — 2 operation(s) for programs.
  name: OpenADR Alliance Programs API
  slug: openadr-alliance-programs-api
- baseURL: http://localhost:8081/openadr3
  baseurl_source: spec
  description: The reports API from OpenADR Alliance — 2 operation(s) for reports.
  name: OpenADR Alliance Reports API
  slug: openadr-alliance-reports-api
- baseURL: https://virtserver.swaggerhub.com/OPENADR3_1/openADR3.1.0/1.0.0
  baseurl_source: spec
  description: The resources API from OpenADR Alliance — 2 operation(s) for resources.
  name: OpenADR Alliance Resources API
  slug: openadr-alliance-resources-api
- baseURL: http://localhost:8081/openadr3
  baseurl_source: spec
  description: The subscriptions API from OpenADR Alliance — 2 operation(s) for subscriptions.
  name: OpenADR Alliance Subscriptions API
  slug: openadr-alliance-subscriptions-api
- baseURL: http://localhost:8081/openadr3
  baseurl_source: spec
  description: The vens API from OpenADR Alliance — 4 operation(s) for vens.
  name: OpenADR Alliance Vens API
  slug: openadr-alliance-vens-api
arazzos:
- description: 'BL/VTN-side flow against an OpenADR 3.1.1 VTN: authenticate with the client-credentials grant, create (or reuse) a program, publish an event carrying priced intervals against it, then read the event b'
  name: Publish a program and dispatch a demand response event
  slug: openadr-alliance-dispatch-event
- description: 'VEN-side onboarding against an OpenADR 3.1.1 VTN: authenticate, register the VEN, attach a controllable resource, ask the VTN which notifier bindings it supports, and register a webhook subscription f'
  name: Onboard a VEN, attach a resource, and subscribe to event notifications
  slug: openadr-alliance-ven-onboard-and-subscribe
artifact_total: 18
asyncapis:
- description: Event surface of the OpenADR 3 protocol, derived from the OpenADR 3.1.1 OpenAPI contract and the Alliance-published notifications design document. The OpenADR Alliance publishes no AsyncAPI document o
  name: OpenADR 3 Object Operation Notifications
  slug: openadr-alliance-notifications-asyncapi
- description: ''
  name: Openadr Alliance Webhooks
  slug: openadr-alliance-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/openadr-alliance-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/grid-coordination/openadr3-specification/issues
- group: other
  title: ''
  type: Overlay
  url: overlays/openadr-alliance-openadr-3-1-1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/openadr-alliance-openadr-3-1-0-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/openadr-alliance-openadr-3-0-1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/openadr-alliance-openadr-3-0-0-overlay.yaml
- group: commercial
  title: ''
  type: License
  url: https://github.com/grid-coordination/openadr3-specification/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openadr-alliance-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openadr-alliance-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openadr-alliance-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/openadr-alliance-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.openadr.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.openadr.org/specification
- group: start
  title: ''
  type: Portal
  url: https://www.openadr.org/specification-download
- group: design
  title: ''
  type: Conformance
  url: https://www.openadr.org/openadr-3-certification
- group: build
  title: ''
  type: Tools
  url: https://test-tool.openadr.org/
- group: other
  title: ''
  type: Directory
  url: https://products.openadr.org/
- group: other
  title: ''
  type: Directory
  url: https://ecoport.openadr.org/
- group: operate
  title: ''
  type: Support
  url: https://www.openadr.org/faq
- group: company
  title: ''
  type: Blog
  url: https://www.openadr.org/openadr-alliance-blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oadr3-org
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/openadr-alliance
- group: start
  title: ''
  type: Login
  url: https://www.openadr.org/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.openadr.org/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.openadr.org/contact-us
- group: build
  title: ''
  type: Packages
  url: packages/openadr-alliance-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/openadr-alliance-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/openadr-alliance-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/openadr-alliance-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/openadr-alliance-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/openadr-alliance-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/openadr-alliance-sandbox.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/openadr-alliance-vocabulary.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/openadr-alliance-dispatch-event.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/openadr-alliance-ven-onboard-and-subscribe.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/openadr-alliance-plans.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.openadr.org/specification-download
- group: docs
  title: ''
  type: APIReference
  url: https://www.openadr.org/specification
- group: start
  title: ''
  type: GettingStarted
  url: https://www.openadr.org/how-to-build-a-product
- group: commercial
  title: ''
  type: Pricing
  url: https://www.openadr.org/join
- group: commercial
  title: ''
  type: Pricing
  url: https://www.openadr.org/openadr-test-tool-store
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.openadr.org/assets/docs/OpenADR%20Alliance%20Bylaws%20%26%20Member%20Agreement.zip
- group: start
  title: ''
  type: SignUp
  url: https://www.openadr.org/join
- group: build
  title: ''
  type: Tools
  url: https://www.openadr.org/openadr-test-tool-store
- group: learn
  title: ''
  type: Training
  url: https://www.openadr.org/openadr-training
- group: other
  title: ''
  type: CaseStudies
  url: https://www.openadr.org/case-studies
- group: operate
  title: ''
  type: PressReleases
  url: https://www.openadr.org/press-releases
- group: other
  title: ''
  type: Events
  url: https://www.openadr.org/event-conference-calendar
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/grid-coordination/openadr3-specification
- group: other
  title: ''
  type: Probe
  url: well-known/openadr-alliance-well-known.yml
created: '2026-07-27'
description: 'The OpenADR Alliance is a San Ramon, California mutual-benefit membership corporation that develops, certifies, and promotes OpenADR, the open information-exchange model utilities, ISOs/RTOs, aggregators, and device makers use to automate demand response and dispatch distributed energy resources. It is a standards body, not a service operator: it publishes the OpenADR 2.0a/2.0b profile specifications (approved by the IEC as IEC/PAS 62746-10-1) and OpenADR 3.0/3.1, which abandoned the SOAP-era design and is now defined entirely by an OpenAPI 3.0 contract covering programs, events, reports, subscriptions, VENs, and resources, secured with OAuth 2.0 client credentials. It also runs the OpenADR and EcoPort (CTA-2045-B) certification programmes and their public certified-product databases. Its API posture is honest but narrow: the OpenADR 3 OpenAPI is a genuine, parseable machine-readable contract, and the specifications are license-free, but the Alliance itself operates no developer
  portal, no api./developer./docs. subdomain, and no hosted API — its canonical specification repository (github.com/oadr3-org) has zero public repositories and requires membership, and the public route to the spec is a registration form that emails download links under terms and conditions. It publishes no consumer energy data and no open grid or market data; it defines the protocol that other parties implement. Home market is the United States, with adoption across Europe, Japan, Korea, and Australia.'
image: https://www.openadr.org/assets/site/openadrlogo347x75.png
layout: provider
modified: '2026-07-27'
name: OpenADR Alliance
nav: Providers
network: true
overview: 'OpenADR Alliance publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Events API, MQTT Notifier API, and 6 more. Tagged areas include Energy, United States, Utilities, Electricity, and Demand Response.


  The OpenADR Alliance catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  OpenADR Alliance''s developer surface includes authentication, documentation, developer portal, tooling, support, engineering blog, changelog, and 44 more developer resources.'
plans:
- name: Openadr Alliance Plans
  plan_count: 10
  slug: openadr-alliance-plans
random_paper: 19
scopes:
- name: Openadr Alliance Scopes
  scope_count: 9
  slug: openadr-alliance-scopes
  summary_line: 9 scopes · clientCredentials
score:
  band: strong
  composite: 59.2
  coverage:
    artifact_dirs: 27
    catalog_gap: 60.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 71.8
    developer_ergonomics: 66.1
    discoverability: 64.8
    governance: 22.0
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 0.0
  previous_composite: 59.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 60.1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openadr-alliance/refs/heads/main/screenshots/openadr-alliance-2026-08-07T190522.png
security:
- kind: authentication
  name: Openadr Alliance Authentication
  slug: openadr-alliance-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Openadr Alliance Domain Security
  slug: openadr-alliance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: openadr-alliance
tags:
- Energy
- United States
- Utilities
- Electricity
- Demand Response
- Grid
- DER
- OpenADR
- Standards
- Smart Grid
- EV Charging
- Certification
website: https://www.openadr.org/
---
