---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bound
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.8
  scored_at: '2026-10-04'
api_count: 1
apis:
- baseURL: https://business.example.com/usp/v1
  baseurl_source: spec
  description: 'Availability query and optional hold operations. Hold and release endpoints require the business to advertise holds: true in the dev.usp-protocol.services.availability capability.'
  name: AlloyX Availability API
  slug: alloyx-availability-api
- baseURL: https://business.example.com/usp/v1
  baseurl_source: spec
  description: Booking lifecycle operations
  name: AlloyX Bookings API
  slug: alloyx-bookings-api
- baseURL: https://business.example.com/usp/v1
  baseurl_source: spec
  description: The Discovery API from AlloyX — 1 operation(s) for discovery.
  name: AlloyX Discovery API
  slug: alloyx-discovery-api
- baseURL: https://business.example.com/usp/v1
  baseurl_source: spec
  description: Discovery registry operations (optional)
  name: AlloyX Registry API
  slug: alloyx-registry-api
- baseURL: https://business.example.com/usp/v1
  baseurl_source: spec
  description: Service catalog operations
  name: AlloyX Services API
  slug: alloyx-services-api
- baseURL: https://business.example.com/usp/v1
  baseurl_source: spec
  description: The Universal Scheduling Protocol (USP) REST API API from AlloyX — 0 operation(s) for universal scheduling protocol (usp) rest api.
  name: AlloyX Universal Scheduling Protocol (USP) REST API
  slug: alloyx-universal-scheduling-protocol-usp-rest-api-api
- baseURL: https://business.example.com/usp/v1
  baseurl_source: spec
  description: Waitlist management operations
  name: AlloyX Waitlist API
  slug: alloyx-waitlist-api
artifact_total: 10
asyncapis:
- description: ''
  name: Alloyx Webhooks
  slug: alloyx-webhooks
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/alloyx/refs/heads/main/rules/alloyx-rules.yml
  title: ''
  type: Spectral
  url: rules/alloyx-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/alloyx/refs/heads/main/vocabulary/alloyx-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/alloyx-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/alloyx/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/alloyx/refs/heads/main/asyncapi/alloyx-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/alloyx-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/alloyx/refs/heads/main/conventions/alloyx-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/alloyx-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/alloyx/refs/heads/main/conventions/alloyx-conventions.yml
  title: ''
  type: Conventions
  url: conventions/alloyx-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/alloyx/refs/heads/main/errors/alloyx-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/alloyx-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/alloyx/refs/heads/main/conformance/alloyx-conformance.yml
  title: ''
  type: Conformance
  url: conformance/alloyx-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/alloyx/refs/heads/main/llms/alloyx-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alloyx-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/alloyx/refs/heads/main/hosts/alloyx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alloyx-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/alloyx/refs/heads/main/vendors/alloyx-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alloyx-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alloyx.com/privacypolicy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/alloyx/refs/heads/main/security/alloyx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alloyx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.alloyx.com/
created: '2026-09-24'
description: 'AlloyX is a company surfaced via the API Evangelist harvest backlog (source: secondary-market) and added to the network as a stub for full-pipeline profiling.'
image: https://static.wixstatic.com/media/4d72bb_4be080e66b164688acc268f19e3b338e~mv2.png/v1/fill/w_580,h_569,al_c/4d72bb_4be080e66b164688acc268f19e3b338e~mv2.png
layout: provider
modified: '2026-09-24'
name: AlloyX
nav: Providers
network: true
overview: 'AlloyX publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Availability API, Bookings API, Discovery API, and 4 more. Tagged areas include Stablecoins, Digital Tokens, Compliance, Blockchain, and Regulated Finance.


  The AlloyX catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.'
random_paper: 5
rules:
- effective_rule_count: 57
  extends:
  - spectral:oas
  name: AlloyX API Rules
  rule_count: 16
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 5
  slug: alloyx-rules
score:
  band: emerging
  composite: 23.5
  coverage:
    artifact_dirs: 14
    catalog_earned: 27.8
    catalog_earned_first_party: 0.0
    catalog_gap: 87.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 54.3
    developer_ergonomics: 1.8
    discoverability: 46.4
    operational_transparency: 7.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Alloyx Domain Security
  slug: alloyx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alloyx
tags:
- Stablecoins
- Digital Tokens
- Compliance
- Blockchain
- Regulated Finance
website: https://www.alloyx.com/
---
