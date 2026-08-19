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
    dry_run_mode: na
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Shovels Agentic Access
  operation_count: 21
  slug: shovels-agentic-access
  summary_line: 21 operations
api_count: 6
apis:
- description: The Addresses API from Shovels — 4 operation(s) for addresses.
  name: Shovels Addresses API
  slug: shovels-addresses-api
- description: The Contractors API from Shovels — 5 operation(s) for contractors.
  name: Shovels Contractors API
  slug: shovels-contractors-api
- description: The Geography API from Shovels — 7 operation(s) for geography.
  name: Shovels Geography API
  slug: shovels-geography-api
- description: The Lists API from Shovels — 1 operation(s) for lists.
  name: Shovels Lists API
  slug: shovels-lists-api
- description: The Meta API from Shovels — 2 operation(s) for meta.
  name: Shovels Meta API
  slug: shovels-meta-api
- description: The Permits API from Shovels — 2 operation(s) for permits.
  name: Shovels Permits API
  slug: shovels-permits-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Shovels Addresses API
  slug: open-shovels-addresses-api
- collection_type: open
  name: Shovels Addresses Contractors API
  slug: open-shovels-contractors-api
- collection_type: open
  name: Shovels Addresses Geography API
  slug: open-shovels-geography-api
- collection_type: open
  name: Shovels Addresses Lists API
  slug: open-shovels-lists-api
- collection_type: open
  name: Shovels Addresses Meta API
  slug: open-shovels-meta-api
- collection_type: open
  name: Shovels Addresses Permits API
  slug: open-shovels-permits-api
- collection_type: open
  name: Shovels API
  slug: open-shovels
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shovels-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/shovels-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shovels-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shovels-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shovels
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.shovels.ai/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.shovels.ai/feeds/all.atom.xml
created: '2026-05-02'
description: Shovels is the intelligence layer for the built world, providing building permit data and contractor intelligence aggregated from 1,800+ jurisdictions across the United States. The platform offers 130M+ building permits, 2.3M+ contractor profiles, property details, resident information, and geographic market metrics. Shovels helps materials suppliers, construction tech companies, energy and climate firms, home services companies, real estate professionals, and telecommunications providers identify qualified contractors, understand work history, and power sales and marketing with rich permit data.
examples:
- key_count: 4
  name: Shovels Search Contractors Example
  slug: shovels-search-contractors-example
- key_count: 4
  name: Shovels Search Permits Example
  slug: shovels-search-permits-example
finops:
- name: Shovels Finops
  service_category: API
  slug: shovels-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shovels.png
json_schemas:
- name: Shovels Contractor
  property_count: 15
  slug: shovels-contractor
- name: Shovels Permit
  property_count: 12
  slug: shovels-permit
json_structures:
- name: Shovels Permit Structure
  property_count: 0
  slug: shovels-permit-structure
jsonld:
- class_count: 22
  name: Shovels Context
  property_count: 13
  slug: shovels-context
layout: provider
modified: '2026-05-19'
name: Shovels
nav: Providers
network: true
overview: 'Shovels publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Addresses API, Contractors API, Geography API, and 3 more. Tagged areas include Construction, Building Permits, Contractors, Real Estate, and Property Data.


  The Shovels catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Shovels'' developer surface includes authentication, engineering blog, and 5 more developer resources.'
plans:
- name: Shovels Plans Pricing
  plan_count: 3
  slug: shovels-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 5
  name: Shovels Rate Limits
  slug: shovels-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Shovels API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: shovels-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Shovels API Rules
  rule_count: 10
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 5
  slug: shovels-rules
score:
  band: thin
  composite: 36.0
  delta: -6.5
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 9.8
    contract_quality: 72.1
    developer_ergonomics: 14.3
    discoverability: 81.5
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 42.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/shovels/refs/heads/main/screenshots/shovels-2026-06-20T193844.png
security:
- kind: authentication
  name: Shovels Authentication
  slug: shovels-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Shovels Domain Security
  slug: shovels-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Shovels Trust Center
  slug: shovels-trust-center
  summary_line: SOC 2
slug: shovels
tags:
- Construction
- Building Permits
- Contractors
- Real Estate
- Property Data
- Market Intelligence
---
