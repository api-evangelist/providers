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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 13
  human_in_the_loop: 2
  name: Ecosio Agentic Access
  operation_count: 32
  slug: ecosio-agentic-access
  summary_line: 32 operations · 13 acting · 2 human-in-the-loop
api_count: 5
apis:
- baseURL: https://api.test.ecosio-hub.com
  baseurl_source: declared
  description: Methods for retrieving approval request statuses
  name: ecosio Approval Request Status API
  slug: ecosio-approval-request-status-api
- baseURL: https://api.test.ecosio-hub.com
  baseurl_source: declared
  description: The Archive messages API from ecosio — 3 operation(s) for archive messages.
  name: ecosio Archive messages API
  slug: ecosio-archive-messages-api
- baseURL: https://api.test.ecosio-hub.com
  baseurl_source: declared
  description: The Check user credentials API from ecosio — 1 operation(s) for check user credentials.
  name: ecosio Check user credentials API
  slug: ecosio-check-user-credentials-api
- baseURL: https://api.test.ecosio-hub.com
  baseurl_source: declared
  description: Methods for managing companies
  name: ecosio Companies API
  slug: ecosio-companies-api
- baseURL: https://api.test.ecosio-hub.com
  baseurl_source: declared
  description: Methods for managing messaging connectors
  name: ecosio Connectors API
  slug: ecosio-connectors-api
- baseURL: https://api.test.ecosio-hub.com
  baseurl_source: declared
  description: The Deliver messages to the Hub API from ecosio — 3 operation(s) for deliver messages to the hub.
  name: ecosio Deliver messages to the Hub API
  slug: ecosio-deliver-messages-to-the-hub-api
- baseURL: https://api.test.ecosio-hub.com
  baseurl_source: declared
  description: The Fetch messages from the Hub API from ecosio — 3 operation(s) for fetch messages from the hub.
  name: ecosio Fetch messages from the Hub API
  slug: ecosio-fetch-messages-from-the-hub-api
- baseURL: https://api.test.ecosio-hub.com
  baseurl_source: declared
  description: The message-controller API from ecosio — 4 operation(s) for message-controller.
  name: ecosio Message Controller API
  slug: ecosio-message-controller-api
- baseURL: https://api.test.ecosio-hub.com
  baseurl_source: declared
  description: The Request the documents for an e-invoice API from ecosio — 1 operation(s) for request the documents for an e-invoice.
  name: ecosio Request the documents for an e-invoice API
  slug: ecosio-request-the-documents-for-an-e-invoice-api
- baseURL: https://api.test.ecosio-hub.com
  baseurl_source: declared
  description: Methods for managing scenarios
  name: ecosio Scenarios API
  slug: ecosio-scenarios-api
artifact_total: 37
common:
- group: agent
  href: https://artifacts.apis.io/ecosio/agentic-access/ecosio-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ecosio-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/ecosio/rate-limits/ecosio-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ecosio-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/ecosio/rules/ecosio-rules.yml
  title: ''
  type: Spectral
  url: rules/ecosio-rules.yml
- group: design
  href: https://artifacts.apis.io/ecosio/json-ld/ecosio-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ecosio-context.jsonld
- group: design
  href: https://artifacts.apis.io/ecosio/vocabulary/ecosio-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ecosio-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/ecosio/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/ecosio/data-model/ecosio-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ecosio-data-model.yml
- group: operate
  href: https://artifacts.apis.io/ecosio/changelog/ecosio-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ecosio-changelog.yml
- group: design
  href: https://artifacts.apis.io/ecosio/conventions/ecosio-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ecosio-conventions.yml
- group: start
  href: https://artifacts.apis.io/ecosio/sandbox/ecosio-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/ecosio-sandbox.yml
- group: auth
  title: ''
  type: Security
  url: https://ecosio.com/en/data-protection/
- group: operate
  href: https://artifacts.apis.io/ecosio/lifecycle/ecosio-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/ecosio-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/ecosio/lifecycle/ecosio-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ecosio-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/ecosio/errors/ecosio-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ecosio-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ecosio/conformance/ecosio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ecosio-conformance.yml
- group: other
  href: https://artifacts.apis.io/ecosio/overlays/ecosio-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ecosio-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/ecosio/llms/ecosio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ecosio-llms.txt
- group: auth
  href: https://artifacts.apis.io/ecosio/well-known/ecosio-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ecosio-security.txt
- group: agent
  href: https://artifacts.apis.io/ecosio/well-known/ecosio-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ecosio-well-known.yml
- group: other
  href: https://artifacts.apis.io/ecosio/hosts/ecosio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ecosio-hosts.yml
- group: other
  href: https://artifacts.apis.io/ecosio/vendors/ecosio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ecosio-vendors.yml
- group: auth
  href: https://artifacts.apis.io/ecosio/authentication/ecosio-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ecosio-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://ecosio.com
- group: auth
  href: https://artifacts.apis.io/ecosio/security/ecosio-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ecosio-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ecosio/security/ecosio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ecosio-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://connect.ecosio.com/docs/welcome-to-ecosio-connect
- group: docs
  title: ''
  type: APIReference
  url: https://connect.ecosio.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://connect.ecosio.com/reference/getting-started-with-our-api
- group: operate
  title: ''
  type: ChangeLog
  url: https://connect.ecosio.com/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://ecosio-status.com/
- group: company
  title: ''
  type: Blog
  url: https://ecosio.com/en/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ecosio.com/en/data-protection/
- group: auth
  title: ''
  type: TrustCenter
  url: https://ecosio.com/en/security-trust-center/
- group: operate
  title: ''
  type: Contact
  url: https://ecosio.com/en/get-in-touch/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ecosio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ecosiohq
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@ecosio
created: '2026-10-18'
description: 'ecosio (ecosio GmbH) provides automated B2B and B2G data exchange: managed EDI as a service, global e-invoicing and VAT compliance (Peppol and country clearance platforms), and supplier activation, delivered through its ecosio connect platform. Developers integrate via ecosio''s Messaging APIs and Management API documented at connect.ecosio.com. ecosio announced on its own blog that ecosio GmbH has been acquired by Vertex, the tax technology company.'
image: https://files.readme.io/bfa94a4c039edc706879ab499b2c7da9ce42e70cd258c8cc6c2c9c173317764f-0_Ecosio.svg
json_schemas:
- name: ApprovalStatusResponse
  property_count: 5
  slug: ecosio-approval-status-response
- name: CompanyRetrievalResponse
  property_count: 9
  slug: ecosio-company-retrieval-response
- name: ConfirmRequest
  property_count: 3
  slug: ecosio-confirm-request
- name: ConnectorRetrievalResponse
  property_count: 10
  slug: ecosio-connector-retrieval-response
- name: DeliveryRequest
  property_count: 1
  slug: ecosio-delivery-request
- name: MessageDetailsResponse
  property_count: 5
  slug: ecosio-message-details-response
- name: MessageListResponse
  property_count: 2
  slug: ecosio-message-list-response
- name: MessageRawResponse
  property_count: 2
  slug: ecosio-message-raw-response
- name: RomaniaEInvoiceCreateRequest
  property_count: 0
  slug: ecosio-romania-einvoice-create-request
- name: RomaniaEInvoiceUpdateRequest
  property_count: 0
  slug: ecosio-romania-einvoice-update-request
- name: ScenarioResponse
  property_count: 8
  slug: ecosio-scenario-response
- name: StatusResponse
  property_count: 5
  slug: ecosio-status-response
jsonld:
- class_count: 60
  name: Ecosio Context
  property_count: 91
  slug: ecosio-context
layout: provider
modified: '2026-10-18'
name: ecosio
nav: Providers
network: true
overview: 'ecosio publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Approval Request Status API, Archive messages API, Check user credentials API, and 7 more. Tagged areas include Company, EDI, E-Invoicing, B2B Integration, and VAT Compliance.


  The ecosio catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ecosio''s developer surface includes changelog, sandbox, authentication, documentation, API reference, getting-started guide, engineering blog, and 30 more developer resources.'
plans:
- name: Ecosio Plans Pricing
  plan_count: 0
  slug: ecosio-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Ecosio Rate Limits
  slug: ecosio-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: ecosio API Rules
  rule_count: 17
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 3
  slug: ecosio-rules
scopes:
- name: Ecosio Scopes
  scope_count: 0
  slug: ecosio-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 55.9
  coverage:
    artifact_dirs: 31
    catalog_earned: 73.8
    catalog_earned_first_party: 8.0
    catalog_gap: 41.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 18.4
    contract_governance: 35.6
    contract_quality: 66.4
    developer_ergonomics: 51.8
    discoverability: 71.4
    operational_transparency: 76.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 10.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 41.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ecosio Authentication
  slug: ecosio-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Ecosio Domain Security
  slug: ecosio-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Ecosio Vulnerability Disclosure
  slug: ecosio-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 6
skills:
- name: ecosio-archive-messages
  slug: ecosio-archive-messages
- name: ecosio-deliver-message
  slug: ecosio-deliver-message
- name: ecosio-fetch-messages
  slug: ecosio-fetch-messages
- name: ecosio-manage-connectors
  slug: ecosio-manage-connectors
- name: ecosio-onboard-company
  slug: ecosio-onboard-company
- name: ecosio-vertex-receive-messages
  slug: ecosio-vertex-receive-messages
slug: ecosio
tags:
- Company
- EDI
- E-Invoicing
- B2B Integration
- VAT Compliance
- PEPPOL
- Supply Chain
- Messaging
website: https://ecosio.com
---
