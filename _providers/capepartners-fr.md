---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Capepartners Fr Agentic Access
  operation_count: 48
  slug: capepartners-fr-agentic-access
  summary_line: 48 operations · 16 acting
api_count: 1
apis:
- description: 'The A2A 1.0 surface of the Cape Partners agent exchange: SendMessage, GetTask and ListTasks on both the JSON-RPC binding (POST /a2a) and the HTTP+JSON binding (POST /a2a/message:send, GET /a2a/tasks, '
  name: Cape Partners Agent Exchange (A2A)
  slug: cape-partners-agent-exchange-a2a
- baseURL: https://sniffer.capepartners.fr
  baseurl_source: declared
  description: The Activity API from Cape Partners — 1 operation(s) for activity.
  name: Cape Partners Activity API
  slug: capepartners-fr-activity-api
- baseURL: https://sniffer.capepartners.fr
  baseurl_source: declared
  description: The Confidentiality API from Cape Partners — 3 operation(s) for confidentiality.
  name: Cape Partners Confidentiality API
  slug: capepartners-fr-confidentiality-api
- baseURL: https://sniffer.capepartners.fr
  baseurl_source: declared
  description: The DataQuality API from Cape Partners — 1 operation(s) for dataquality.
  name: Cape Partners Data Quality API
  slug: capepartners-fr-dataquality-api
- baseURL: https://sniffer.capepartners.fr
  baseurl_source: declared
  description: The DealFlow API from Cape Partners — 2 operation(s) for dealflow.
  name: Cape Partners Deal Flow API
  slug: capepartners-fr-dealflow-api
- baseURL: https://sniffer.capepartners.fr
  baseurl_source: declared
  description: The Discovery API from Cape Partners — 7 operation(s) for discovery.
  name: Cape Partners Discovery API
  slug: capepartners-fr-discovery-api
- baseURL: https://sniffer.capepartners.fr
  baseurl_source: declared
  description: The Exchange API from Cape Partners — 11 operation(s) for exchange.
  name: Cape Partners Exchange API
  slug: capepartners-fr-exchange-api
- baseURL: https://sniffer.capepartners.fr
  baseurl_source: declared
  description: The Identity API from Cape Partners — 3 operation(s) for identity.
  name: Cape Partners Identity API
  slug: capepartners-fr-identity-api
- baseURL: https://sniffer.capepartners.fr
  baseurl_source: declared
  description: The InfoMemos API from Cape Partners — 4 operation(s) for infomemos.
  name: Cape Partners Info Memos API
  slug: capepartners-fr-infomemos-api
- baseURL: https://sniffer.capepartners.fr
  baseurl_source: declared
  description: The Interest API from Cape Partners — 2 operation(s) for interest.
  name: Cape Partners Interest API
  slug: capepartners-fr-interest-api
- baseURL: https://sniffer.capepartners.fr
  baseurl_source: declared
  description: The Mandate API from Cape Partners — 3 operation(s) for mandate.
  name: Cape Partners Mandate API
  slug: capepartners-fr-mandate-api
- baseURL: https://sniffer.capepartners.fr
  baseurl_source: declared
  description: The Matching API from Cape Partners — 3 operation(s) for matching.
  name: Cape Partners Matching API
  slug: capepartners-fr-matching-api
- baseURL: https://sniffer.capepartners.fr
  baseurl_source: declared
  description: The Pairings API from Cape Partners — 4 operation(s) for pairings.
  name: Cape Partners Pairings API
  slug: capepartners-fr-pairings-api
- baseURL: https://sniffer.capepartners.fr
  baseurl_source: declared
  description: The Registration API from Cape Partners — 1 operation(s) for registration.
  name: Cape Partners Registration API
  slug: capepartners-fr-registration-api
- baseURL: https://sniffer.capepartners.fr
  baseurl_source: declared
  description: The Search API from Cape Partners — 1 operation(s) for search.
  name: Cape Partners Search API
  slug: capepartners-fr-search-api
- baseURL: https://sniffer.capepartners.fr
  baseurl_source: declared
  description: The Valuation API from Cape Partners — 1 operation(s) for valuation.
  name: Cape Partners Valuation API
  slug: capepartners-fr-valuation-api
artifact_total: 60
common:
- group: agent
  href: https://artifacts.apis.io/capepartners-fr/agentic-access/capepartners-fr-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/capepartners-fr-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/capepartners-fr/rules/capepartners-fr-rules.yml
  title: ''
  type: Spectral
  url: rules/capepartners-fr-rules.yml
- group: design
  href: https://artifacts.apis.io/capepartners-fr/json-ld/capepartners-fr-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/capepartners-fr-context.jsonld
- group: design
  href: https://artifacts.apis.io/capepartners-fr/vocabulary/capepartners-fr-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/capepartners-fr-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/capepartners-fr/security/capepartners-fr-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/capepartners-fr-vulnerability-disclosure.yml
- group: other
  href: https://artifacts.apis.io/capepartners-fr/hosts/capepartners-fr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/capepartners-fr-hosts.yml
- group: build
  href: https://artifacts.apis.io/capepartners-fr/integrations/capepartners-fr-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/capepartners-fr-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/capepartners-fr/vendors/capepartners-fr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/capepartners-fr-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.capepartners.fr/privacy
- group: auth
  href: https://artifacts.apis.io/capepartners-fr/security/capepartners-fr-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/capepartners-fr-vulnerability-disclosure.yml
- group: other
  href: https://artifacts.apis.io/capepartners-fr/capabilities/capepartners-fr-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/capepartners-fr-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/capepartners-fr/overlays/capepartners-fr-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/capepartners-fr-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.capepartners.fr/
- group: docs
  title: ''
  type: Documentation
  url: https://www.capepartners.fr/llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://www.capepartners.fr/api
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.capepartners.fr/tos
- group: start
  title: ''
  type: SignUp
  url: https://www.capepartners.fr/new-workspace.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/capepartners/
- group: agent
  href: https://artifacts.apis.io/capepartners-fr/llms/capepartners-fr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/capepartners-fr-llms.txt
- group: agent
  href: https://artifacts.apis.io/capepartners-fr/well-known/capepartners-fr-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/capepartners-fr-well-known.yml
- group: other
  href: https://artifacts.apis.io/capepartners-fr/a2a/capepartners-fr-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/capepartners-fr-a2a.yml
- group: auth
  href: https://artifacts.apis.io/capepartners-fr/security/capepartners-fr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/capepartners-fr-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/capepartners-fr/authentication/capepartners-fr-authentication.yml
  title: ''
  type: Authentication
  url: authentication/capepartners-fr-authentication.yml
- group: design
  href: https://artifacts.apis.io/capepartners-fr/conventions/capepartners-fr-conventions.yml
  title: ''
  type: Conventions
  url: conventions/capepartners-fr-conventions.yml
- group: design
  href: https://artifacts.apis.io/capepartners-fr/conformance/capepartners-fr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/capepartners-fr-conformance.yml
- group: design
  href: https://artifacts.apis.io/capepartners-fr/lifecycle/capepartners-fr-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/capepartners-fr-lifecycle.yml
- group: commercial
  href: https://artifacts.apis.io/capepartners-fr/plans/capepartners-fr-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/capepartners-fr-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/capepartners-fr/rate-limits/capepartners-fr-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/capepartners-fr-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/capepartners-fr/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-19'
description: 'Cape Partners is an independent M&A advisory firm focused on technology, based in Le Chesnay, France (Cape Partners SAS, SIREN 833 208 960). It operates a deal-flow platform ("Sniffer") that sources and enriches European software companies, matches sellers to strategic and financial buyers with a deterministic-times-semantic fit score, produces preliminary valuations, and lets both sides manage pairings and deal phases in a session-scoped workspace. The platform is agent-first: an OpenAPI 3.1 contract at /openapi.json, a JSON capability index at /api, llms.txt, an AI-plugin discovery manifest, and an A2A 1.0 Agent Card whose SendMessage / GetTask / ListTasks operations are served live at /a2a. External agents take part through an "agent exchange" — publish a six-field manifest with no account or key, then poll for a grounded answer; a workspace UUID is issued only after a human-reviewed handshake, and the Terms of Service are signed by a human principal.'
image: https://www.capepartners.fr/logo.png
json_schemas:
- name: A2AJsonRpcRequest
  property_count: 4
  slug: capepartners-fr-a2-ajson-rpc-request
- name: A2ASendMessageRequest
  property_count: 4
  slug: capepartners-fr-a2-asend-message-request
- name: A2ATask
  property_count: 6
  slug: capepartners-fr-a2-atask
- name: ActivityResponse
  property_count: 3
  slug: capepartners-fr-activity-response
- name: DealFlowResponse
  property_count: 10
  slug: capepartners-fr-deal-flow-response
- name: DqEnqueueRequest
  property_count: 3
  slug: capepartners-fr-dq-enqueue-request
- name: DqEnqueueResponse
  property_count: 5
  slug: capepartners-fr-dq-enqueue-response
- name: EntityName
  property_count: 1
  slug: capepartners-fr-entity-name
- name: InfoMemo
  property_count: 1
  slug: capepartners-fr-info-memo
- name: InterestAckRequest
  property_count: 2
  slug: capepartners-fr-interest-ack-request
- name: InterestAckResponse
  property_count: 4
  slug: capepartners-fr-interest-ack-response
- name: InterestSignalsResponse
  property_count: 7
  slug: capepartners-fr-interest-signals-response
- name: Match
  property_count: 6
  slug: capepartners-fr-match
- name: MatchedNames
  property_count: 1
  slug: capepartners-fr-matched-names
- name: NdaSignRequest
  property_count: 6
  slug: capepartners-fr-nda-sign-request
- name: NdaSignResponse
  property_count: 3
  slug: capepartners-fr-nda-sign-response
- name: NdaTextResponse
  property_count: 2
  slug: capepartners-fr-nda-text-response
- name: PairingCreateRequest
  property_count: 4
  slug: capepartners-fr-pairing-create-request
- name: PairingCreateResponse
  property_count: 5
  slug: capepartners-fr-pairing-create-response
- name: PairingsResponse
  property_count: 7
  slug: capepartners-fr-pairings-response
- name: PhaseRequestDecisionResponse
  property_count: 6
  slug: capepartners-fr-phase-request-decision-response
- name: PhaseUpdateResponse
  property_count: 5
  slug: capepartners-fr-phase-update-response
- name: ProductAnalysis
  property_count: 14
  slug: capepartners-fr-product-analysis
- name: SearchResponse
  property_count: 4
  slug: capepartners-fr-search-response
- name: SessionIdentity
  property_count: 6
  slug: capepartners-fr-session-identity
- name: SubmitRequest
  property_count: 6
  slug: capepartners-fr-submit-request
- name: SubmitResponse
  property_count: 4
  slug: capepartners-fr-submit-response
- name: Valuation
  property_count: 7
  slug: capepartners-fr-valuation
- name: WatchlistRequest
  property_count: 5
  slug: capepartners-fr-watchlist-request
- name: WatchlistResponse
  property_count: 4
  slug: capepartners-fr-watchlist-response
- name: WorkspaceInfo
  property_count: 5
  slug: capepartners-fr-workspace-info
- name: WorkspaceJoinRequest
  property_count: 6
  slug: capepartners-fr-workspace-join-request
- name: WorkspaceJoinResponse
  property_count: 5
  slug: capepartners-fr-workspace-join-response
jsonld:
- class_count: 46
  name: Capepartners Fr Context
  property_count: 170
  slug: capepartners-fr-context
layout: provider
modified: '2026-09-19'
name: Cape Partners
nav: Providers
network: true
overview: 'Cape Partners publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Activity API, Confidentiality API, Data Quality API, and 13 more. Tagged areas include Mergers and Acquisitions, Deal Flow, Valuation, Investment, and Financial Services.


  The Cape Partners catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cape Partners'' developer surface includes documentation, API reference, signup flow, authentication, and 25 more developer resources.'
plans:
- name: Capepartners Fr Plans Pricing
  plan_count: 0
  slug: capepartners-fr-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Capepartners Fr Rate Limits
  slug: capepartners-fr-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Cape Partners API Rules
  rule_count: 12
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 2
  slug: capepartners-fr-rules
score:
  band: developing
  composite: 48.1
  coverage:
    artifact_dirs: 30
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.1
  facets:
    access_clarity: 28.9
    contract_governance: 35.6
    contract_quality: 62.6
    developer_ergonomics: 30.4
    discoverability: 73.2
    operational_transparency: 42.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 48.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 15
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/capepartners-fr/capepartners-fr-2026-10-11T102708.png
security:
- kind: authentication
  name: Capepartners Fr Authentication
  slug: capepartners-fr-authentication
  summary_line: apiKey · 6 schemes
- kind: domain-security
  name: Capepartners Fr Domain Security
  slug: capepartners-fr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Capepartners Fr Vulnerability Disclosure
  slug: capepartners-fr-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: a2a-send-and-read-tasks
  slug: capepartners-fr-a2a-send-and-read-tasks
- name: open-workspace-and-read-deal-flow
  slug: capepartners-fr-open-workspace-and-read-deal-flow
- name: Publish an agent manifest and poll for the answer (exchange tier 1)
  slug: capepartners-fr-publish-manifest-and-poll
slug: capepartners-fr
tags:
- Mergers and Acquisitions
- Deal Flow
- Valuation
- Investment
- Financial Services
- Agents
- A2A
- France
- Technology
- Software-as-a-Service
website: https://www.capepartners.fr/
---
