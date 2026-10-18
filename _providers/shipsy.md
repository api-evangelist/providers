---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.3
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Shipsy Agentic Access
  operation_count: 1
  slug: shipsy-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://www.shipsy.ai
  baseurl_source: declared
  description: AI assistant endpoints for the shipsy.ai website. Not the logistics platform API.
  name: Shipsy Website AI API
  slug: shipsy-website-ai-api
artifact_total: 7
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.shipsy.ai/terms-and-conditions
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/shipsy/refs/heads/main/agentic-access/shipsy-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/shipsy-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shipsy/refs/heads/main/rules/shipsy-rules.yml
  title: ''
  type: Spectral
  url: rules/shipsy-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shipsy/refs/heads/main/json-ld/shipsy-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/shipsy-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shipsy/refs/heads/main/vocabulary/shipsy-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/shipsy-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/shipsy/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shipsy/refs/heads/main/data-model/shipsy-data-model.yml
  title: ''
  type: DataModel
  url: data-model/shipsy-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.shipsy.io/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/shipsy/refs/heads/main/authentication/shipsy-authentication.yml
  title: ''
  type: Authentication
  url: authentication/shipsy-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shipsy/refs/heads/main/errors/shipsy-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/shipsy-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shipsy/refs/heads/main/conformance/shipsy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/shipsy-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/shipsy/refs/heads/main/llms/shipsy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/shipsy-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/shipsy/refs/heads/main/hosts/shipsy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/shipsy-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/shipsy/refs/heads/main/vendors/shipsy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/shipsy-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.shipsy.ai/news
- group: start
  title: ''
  type: GettingStarted
  url: https://knowledge.shipsy.ai/help/core-platform/how-to-enable-and-disable-app-user--xcgbwdmu
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/shipsy/refs/heads/main/security/shipsy-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/shipsy-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/shipsy/refs/heads/main/security/shipsy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shipsy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.shipsy.io
- group: docs
  title: ''
  type: Documentation
  url: https://knowledge.shipsy.ai/help
- group: start
  title: ''
  type: DeveloperPortal
  url: https://knowledge.shipsy.ai/help
- group: start
  title: ''
  type: SignUp
  url: https://www.shipsy.ai/request-a-demo
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.shipsy.ai/privacy-policy
created: '2026-10-13'
description: Shipsy provides an AI‑native logistics platform offering Transportation Management System (TMS) and Warehouse Management System (WMS) capabilities. The cloud‑based solution automates shipment planning, carrier selection, real‑time tracking, route optimization, and inventory accuracy for enterprises worldwide. Recognized in the 2026 Gartner Magic Quadrant for TMS, Shipsy serves over 150 global customers across 30+ countries, delivering AI‑driven insights and end‑to‑end visibility across the supply chain.
image: https://www.shipsy.ai/og-image.png
jsonld:
- class_count: 1
  name: Shipsy Context
  property_count: 1
  slug: shipsy-context
layout: provider
modified: '2026-10-13'
name: Shipsy
nav: Providers
network: true
overview: 'Shipsy publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Website AI API. Tagged areas include Logistics, Artificial Intelligence, Transportation, Warehouse, and Software-as-a-Service.


  The Shipsy catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Shipsy''s developer surface includes authentication, getting-started guide, documentation, signup flow, and 19 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Shipsy API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: shipsy-rules
score:
  band: developing
  composite: 44.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 47.8
    catalog_earned_first_party: 0.0
    catalog_gap: 67.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.0
    contract_governance: 22.0
    contract_quality: 51.8
    developer_ergonomics: 49.3
    discoverability: 75.0
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Shipsy Authentication
  slug: shipsy-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Shipsy Domain Security
  slug: shipsy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Shipsy Trust Center
  slug: shipsy-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: shipsy
tags:
- Logistics
- Artificial Intelligence
- Transportation
- Warehouse
- Software-as-a-Service
- Company
website: https://www.shipsy.io
---
