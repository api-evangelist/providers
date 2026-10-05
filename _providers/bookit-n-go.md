---
agent_readiness:
  band: agent-native
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
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.0
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 21
  human_in_the_loop: 1
  name: Bookit N Go Agentic Access
  operation_count: 37
  slug: bookit-n-go-agentic-access
  summary_line: 37 operations · 21 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://developers.bookitngo.com
  baseurl_source: declared
  description: Supplier-neutral, consent-bound agent actions and receipts
  name: Bookit N Go Agent API
  slug: bookit-n-go-agent-api
- baseURL: https://developers.bookitngo.com
  baseurl_source: declared
  description: Sandbox flight search, validation, fare, and booking operations
  name: Bookit N Go Flights API
  slug: bookit-n-go-flights-api
- baseURL: https://developers.bookitngo.com
  baseurl_source: declared
  description: Sandbox hotel search, validation, and booking operations
  name: Bookit N Go Hotels API
  slug: bookit-n-go-hotels-api
- baseURL: https://developers.bookitngo.com
  baseurl_source: declared
  description: App-scoped traveler profiles, preferences, constraints, and consent
  name: Bookit N Go Travelers API
  slug: bookit-n-go-travelers-api
- baseURL: https://developers.bookitngo.com
  baseurl_source: declared
  description: Sandbox trip grouping and hotel servicing workflows
  name: Bookit N Go Trips API
  slug: bookit-n-go-trips-api
- baseURL: https://developers.bookitngo.com
  baseurl_source: declared
  description: App-scoped webhook endpoint configuration and delivery history
  name: Bookit N Go Webhooks API
  slug: bookit-n-go-webhooks-api
artifact_total: 18
asyncapis:
- description: ''
  name: Bookit N Go Webhooks
  slug: bookit-n-go-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bookit-n-go/refs/heads/main/agentic-access/bookit-n-go-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bookit-n-go-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bookit-n-go/refs/heads/main/rules/bookit-n-go-rules.yml
  title: ''
  type: Spectral
  url: rules/bookit-n-go-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bookit-n-go/refs/heads/main/json-ld/bookit-n-go-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bookit-n-go-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bookit-n-go/refs/heads/main/vocabulary/bookit-n-go-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bookit-n-go-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bookit-n-go/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bookit-n-go/refs/heads/main/asyncapi/bookit-n-go-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/bookit-n-go-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bookit-n-go/refs/heads/main/data-model/bookit-n-go-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bookit-n-go-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bookit-n-go/refs/heads/main/conventions/bookit-n-go-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/bookit-n-go-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bookit-n-go/refs/heads/main/conventions/bookit-n-go-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bookit-n-go-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bookit-n-go/refs/heads/main/errors/bookit-n-go-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bookit-n-go-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bookit-n-go/refs/heads/main/conformance/bookit-n-go-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bookit-n-go-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bookit-n-go/refs/heads/main/overlays/bookit-n-go-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bookit-n-go-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bookit-n-go/refs/heads/main/llms/bookit-n-go-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bookit-n-go-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bookit-n-go/refs/heads/main/hosts/bookit-n-go-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bookit-n-go-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bookit-n-go/refs/heads/main/vendors/bookit-n-go-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bookit-n-go-vendors.yml
- group: docs
  title: ''
  type: APIReference
  url: https://developers.bookitngo.com/llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bookit-n-go/refs/heads/main/authentication/bookit-n-go-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bookit-n-go-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bookit-n-go/refs/heads/main/security/bookit-n-go-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bookit-n-go-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bookitngo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bookitngo.com/about
- group: start
  title: ''
  type: DeveloperPortal
  url: https://start.bookitngo.com/
- group: company
  title: ''
  type: Blog
  url: https://www.bookitngo.com/blog
created: '2026-10-02'
description: Bookit N Go is an AI‑powered travel technology SaaS platform that provides white‑labeled solutions for OTAs, corporate travel managers, TMCs, distributors and startups. Their suite includes the Zoe AI engine for conversational booking, the Nevo corporate travel platform, Trava consumer portal, and Nexel B2B partner platform, enabling rapid launch of branded travel services with full data control and AI‑driven personalization.
image: https://framerusercontent.com/assets/Y4bHVpvh3wTsSQ15KjZon2JhwE8.png
json_schemas:
- name: FlightBookingInput
  property_count: 4
  slug: bookit-n-go-flight-booking-input
- name: FlightSearch
  property_count: 10
  slug: bookit-n-go-flight-search
- name: HotelBookingInput
  property_count: 5
  slug: bookit-n-go-hotel-booking-input
- name: HotelSearch
  property_count: 9
  slug: bookit-n-go-hotel-search
- name: PreferenceInput
  property_count: 9
  slug: bookit-n-go-preference-input
- name: RecommendationResponse
  property_count: 1
  slug: bookit-n-go-recommendation-response
jsonld:
- class_count: 59
  name: Bookit N Go Context
  property_count: 105
  slug: bookit-n-go-context
layout: provider
modified: '2026-10-02'
name: Bookit N Go
nav: Providers
network: true
overview: 'Bookit N Go publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Agent API, Flights API, Hotels API, and 3 more. Tagged areas include Travel, Software-as-a-Service, Artificial Intelligence, White Label, and B2B.


  The Bookit N Go catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Bookit N Go''s developer surface includes API reference, authentication, documentation, engineering blog, and 18 more developer resources.'
random_paper: 6
rules:
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: Bookit N Go API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: bookit-n-go-rules
score:
  band: thin
  composite: 34.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 64.0
    developer_ergonomics: 42.3
    discoverability: 73.2
    operational_transparency: 7.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Bookit N Go Authentication
  slug: bookit-n-go-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bookit N Go Domain Security
  slug: bookit-n-go-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bookit-n-go
tags:
- Travel
- Software-as-a-Service
- Artificial Intelligence
- White Label
- B2B
website: https://www.bookitngo.com/
---
