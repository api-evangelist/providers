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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Navis Agentic Access
  operation_count: 8
  slug: navis-agentic-access
  summary_line: 8 operations
api_count: 1
apis:
- baseURL_template: https://{terminal}.navis.example.com/apex/n4/api/v2
  baseurl_source: spec_template
  description: Truck gate transactions
  name: Navis (Kaleris) Gate API
  slug: navis-gate-api
- baseURL_template: https://{terminal}.navis.example.com/apex/n4/api/v2
  baseurl_source: spec_template
  description: Container hold management
  name: Navis (Kaleris) Holds API
  slug: navis-holds-api
- baseURL_template: https://{terminal}.navis.example.com/apex/n4/api/v2
  baseurl_source: spec_template
  description: Work queues and crane operations
  name: Navis (Kaleris) Operations API
  slug: navis-operations-api
- baseURL_template: https://{terminal}.navis.example.com/apex/n4/api/v2
  baseurl_source: spec_template
  description: Container and cargo unit tracking
  name: Navis (Kaleris) Units API
  slug: navis-units-api
- baseURL_template: https://{terminal}.navis.example.com/apex/n4/api/v2
  baseurl_source: spec_template
  description: Vessel port call management and planning
  name: Navis (Kaleris) Vessel Visits API
  slug: navis-vessel-visits-api
artifact_total: 27
collections:
- collection_type: postman
  name: Navis N4 Terminal Operating System REST Gate API
  slug: postman-navis-gate-api
- collection_type: postman
  name: Navis N4 Terminal Operating System REST Gate Holds API
  slug: postman-navis-holds-api
- collection_type: postman
  name: Navis N4 Terminal Operating System REST Gate Operations API
  slug: postman-navis-operations-api
- collection_type: postman
  name: Navis N4 Terminal Operating System REST Gate Units API
  slug: postman-navis-units-api
- collection_type: postman
  name: Navis N4 Terminal Operating System REST Gate Vessel Visits API
  slug: postman-navis-vessel-visits-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Navis N4 Terminal Operating System REST Gate API
  slug: open-navis-gate-api
- collection_type: open
  name: Navis N4 Terminal Operating System REST Gate Holds API
  slug: open-navis-holds-api
- collection_type: open
  name: Navis N4 Terminal Operating System REST API
  slug: open-navis-n4
- collection_type: open
  name: Navis N4 Terminal Operating System REST Gate Operations API
  slug: open-navis-operations-api
- collection_type: open
  name: Navis N4 Terminal Operating System REST Gate Units API
  slug: open-navis-units-api
- collection_type: open
  name: Navis N4 Terminal Operating System REST Gate Vessel Visits API
  slug: open-navis-vessel-visits-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/navis-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/navis-kaleris/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/navis-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/navis-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/navis-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/navis-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/navis
- group: start
  title: ''
  type: Portal
  url: https://kaleris.com/
- group: company
  title: ''
  type: Website
  url: https://kaleris.com/
- group: operate
  title: ''
  type: Support
  url: https://kaleris.com/support/
- group: operate
  title: ''
  type: Support
  url: https://kaleriscommunity.force.com/
- group: company
  title: ''
  type: Blog
  url: https://kaleris.com/resources/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kaleris.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kaleris.com/terms-and-conditions/
- group: operate
  title: ''
  type: StatusPage
  url: https://trust.kaleris.com/
created: '2026-03-18'
description: Navis (now operated by Kaleris) provides terminal operating systems and supply chain software for the maritime and intermodal industries. The flagship N4 product offers APIs for container tracking, vessel planning, berth scheduling, yard management, and gate operations, serving 650+ organizations across 95+ countries.
finops:
- name: Navis Finops
  service_category: API
  slug: navis-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/navis.png
json_schemas:
- name: Navis N4 Container Unit
  property_count: 18
  slug: navis-unit
jsonld:
- class_count: 9
  name: Navis Context
  property_count: 13
  slug: navis-context
layout: provider
modified: '2026-05-19'
name: Navis (Kaleris)
nav: Providers
network: true
overview: 'Navis (Kaleris) publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Gate API, Holds API, Operations API, and 2 more. Tagged areas include Maritime, Port, Terminal, Container, and Logistics.


  The Navis (Kaleris) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Navis (Kaleris)''s developer surface includes authentication, developer portal, support, engineering blog, and 11 more developer resources.'
plans:
- name: Navis Plans Pricing
  plan_count: 3
  slug: navis-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Navis Rate Limits
  slug: navis-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Navis (Kaleris) API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: navis-jsonschema-spectral-rules
score:
  band: developing
  composite: 43.7
  coverage:
    artifact_dirs: 15
    catalog_gap: 53.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 9.8
    contract_quality: 63.9
    developer_ergonomics: 42.9
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 23.7
  previous_composite: 43.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/navis/refs/heads/main/screenshots/navis-2026-06-20T190102.png
security:
- kind: authentication
  name: Navis Authentication
  slug: navis-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Navis Domain Security
  slug: navis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Navis Trust Center
  slug: navis-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: navis
tags:
- Maritime
- Port
- Terminal
- Container
- Logistics
website: https://kaleris.com/
---
