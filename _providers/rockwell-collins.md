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
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.3
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 6
  human_in_the_loop: 1
  name: Rockwell Collins Agentic Access
  operation_count: 58
  slug: rockwell-collins-agentic-access
  summary_line: 58 operations · 6 acting · 1 human-in-the-loop
api_count: 8
apis:
- description: The Collins Digital Exchange is a developer portal operated by Collins Aerospace providing API products for aerospace integration. The portal provides quick-start guides and authenticated access to Co
  name: Collins Digital Exchange APIs
  slug: collins-digital-exchange-apis
- description: The airports API from Rockwell Collins — 17 operation(s) for airports.
  name: Rockwell Collins airports API
  slug: rockwell-collins-airports-api
- description: AeroAPI alerting can be used to configure and receive real-time alerts on key flight events. With customizable alerting offered by our alert endpoints, AeroAPI empowers users to selectively pick vario
  name: Rockwell Collins alerts API
  slug: rockwell-collins-alerts-api
- description: The flights API from Rockwell Collins — 11 operation(s) for flights.
  name: Rockwell Collins flights API
  slug: rockwell-collins-flights-api
- description: 'Foresight endpoints provide access to FlightAware''s Foresight predictive models and predictions for key events. Our advanced machine learning (ML) models identify key influencing factors for a flight '
  name: Rockwell Collins foresight API
  slug: rockwell-collins-foresight-api
- description: The history API from Rockwell Collins — 5 operation(s) for history.
  name: Rockwell Collins history API
  slug: rockwell-collins-history-api
- description: The miscellaneous API from Rockwell Collins — 6 operation(s) for miscellaneous.
  name: Rockwell Collins miscellaneous API
  slug: rockwell-collins-miscellaneous-api
- description: The operators API from Rockwell Collins — 8 operation(s) for operators.
  name: Rockwell Collins operators API
  slug: rockwell-collins-operators-api
artifact_total: 21
collections:
- collection_type: open
  name: AeroAPI
  slug: open-flightaware-aeroapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rockwell-collins-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rockwell-collins-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rockwell-collins-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rockwell-collins
- group: company
  title: ''
  type: Website
  url: https://www.rockwellcollins.com
- group: company
  title: ''
  type: Website
  url: https://www.rtx.com/collinsaerospace/
- group: start
  title: ''
  type: Portal
  url: https://developer.collins.com/api-products
- group: start
  title: ''
  type: Portal
  url: https://portal.rockwellcollins.com/
- group: start
  title: ''
  type: Portal
  url: https://customers.collinsaerospace.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.flightaware.com/commercial/aeroapi/
- group: operate
  title: ''
  type: Support
  url: https://www.rtx.com/collinsaerospace/what-we-do/service-and-support/support/support-lookup
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/flightaware-aeroapi-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/rockwell-collins-flight-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/rockwell-collins-flight-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/rockwell-collins-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/rockwell-collins-vocabulary.yml
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/rockwell-collins-rules.yml
created: '2026-03-24'
description: Rockwell Collins was a major American company providing avionics and information technology systems and services to government agencies and aircraft manufacturers. In 2018, Rockwell Collins was acquired by United Technologies and became part of Collins Aerospace, a subsidiary of RTX Corporation (formerly Raytheon Technologies). Collins Aerospace provides flight deck systems, cabin electronics, mission systems, communications, and advanced data services including FlightAware AeroAPI for aviation data. The Collins Digital Exchange offers API products for aerospace and defense integration.
examples:
- key_count: 5
  name: Aeroapi Get Flight Example
  slug: aeroapi-get-flight-example
finops:
- name: Rockwell Collins Finops
  service_category: API
  slug: rockwell-collins-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rockwell-collins.png
json_schemas:
- name: FlightAware AeroAPI Flight
  property_count: 29
  slug: rockwell-collins-flight
json_structures:
- name: Rockwell Collins Flight Structure
  property_count: 0
  slug: rockwell-collins-flight-structure
jsonld:
- class_count: 3
  name: Rockwell Collins Context
  property_count: 31
  slug: rockwell-collins-context
layout: provider
modified: '2026-05-19'
name: Rockwell Collins
nav: Providers
network: true
overview: 'Rockwell Collins publishes 7 APIs on the [APIs.io](https://apis.io/) network, including airports API, alerts API, flights API, and 4 more. Tagged areas include Avionics, Aerospace, Defense, Aviation, and Flight Deck.


  The Rockwell Collins catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Rockwell Collins'' developer surface includes authentication, developer portal, documentation, support, and 13 more developer resources.'
plans:
- name: Rockwell Collins Plans Pricing
  plan_count: 3
  slug: rockwell-collins-plans-pricing
press:
- date: '2026-05-25'
  title: Pradeep Ramalingam - Rockwell Collins
  url: https://sg.linkedin.com/in/pradeep-ramalingam-43246965
- date: '2026-05-25'
  title: United Technologies acquires Rockwell Collins for $30 ...
  url: https://www.therobotreport.com/united-technologies-acquires-rockwell-collins-30-billion/
- date: '2026-05-25'
  title: Digital Careers | Collins Aerospace
  url: https://www.rtx.com/collinsaerospace/careers/digital-careers
- date: '2026-05-25'
  title: United Technologies Announces Intention to Separate Into ...
  url: https://www.prnewswire.com/news-releases/united-technologies-announces-intention-to-separate-into-three-independent-companies-completes-acquisition-of-rockwell-collins-300755507.html
- date: '2026-05-25'
  title: Rockwell Collins Airport Solutions Enhance Operations at ...
  url: https://www.airport-technology.com/contractors/consult/arinc-airports/pressreleases/terminal-operations-noi-bai/
random_paper: 44
rate_limits:
- limit_count: 5
  name: Rockwell Collins Rate Limits
  slug: rockwell-collins-rate-limits
rules:
- name: Rockwell Collins API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: rockwell-collins-jsonschema-spectral-rules
- name: Rockwell Collins API Rules
  rule_count: 11
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 5
  slug: rockwell-collins-rules
score:
  band: developing
  composite: 51.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 69.0
    developer_ergonomics: 32.6
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 31.6
  previous_composite: 51.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rockwell-collins/refs/heads/main/screenshots/rockwell-collins-2026-06-20T193203.png
security:
- kind: authentication
  name: Rockwell Collins Authentication
  slug: rockwell-collins-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Rockwell Collins Domain Security
  slug: rockwell-collins-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: rockwell-collins
tags:
- Avionics
- Aerospace
- Defense
- Aviation
- Flight Deck
- Fortune 500
website: https://www.rockwellcollins.com
---
