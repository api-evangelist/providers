---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Meddra Agentic Access
  operation_count: 7
  slug: meddra-agentic-access
  summary_line: 7 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.meddra.example.com
  baseurl_source: declared
  description: MedDRA hierarchy navigation (SOC → HLGT → HLT → PT → LLT)
  name: meddra Hierarchy API
  slug: meddra-hierarchy-api
- baseURL: https://api.meddra.example.com
  baseurl_source: declared
  description: MedDRA term search and retrieval
  name: meddra Terms API
  slug: meddra-terms-api
- baseURL: https://api.meddra.example.com
  baseurl_source: declared
  description: Code validation for regulatory submissions
  name: meddra Validation API
  slug: meddra-validation-api
- baseURL: https://api.meddra.example.com
  baseurl_source: declared
  description: Dictionary version management
  name: meddra Versions API
  slug: meddra-versions-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: MedDRA Medical Dictionary for Regulatory Activities Hierarchy API
  slug: open-meddra-hierarchy-api
- collection_type: open
  name: MedDRA Medical Dictionary for Regulatory Activities API
  slug: open-meddra-terminology
- collection_type: open
  name: MedDRA Medical Dictionary for Regulatory Activities Hierarchy Terms API
  slug: open-meddra-terms-api
- collection_type: open
  name: MedDRA Medical Dictionary for Regulatory Activities Hierarchy Validation API
  slug: open-meddra-validation-api
- collection_type: open
  name: MedDRA Medical Dictionary for Regulatory Activities Hierarchy Versions API
  slug: open-meddra-versions-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/meddra-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/meddra-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/meddra-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/meddra-msso
- group: start
  title: ''
  type: Portal
  url: https://www.meddra.org/
- group: company
  title: ''
  type: Website
  url: https://www.meddra.org/
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/meddra/refs/heads/main/openapi/meddra-terminology-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/meddra/refs/heads/main/json-schema/meddra-term-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/meddra/refs/heads/main/json-ld/meddra-context.jsonld
description: MedDRA (Medical Dictionary for Regulatory Activities) is a clinically validated international medical terminology dictionary used by regulatory authorities and the regulated biopharmaceutical industry.
finops:
- name: Meddra Finops
  service_category: API
  slug: meddra-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/meddra.png
json_schemas:
- name: MedDRA Term
  property_count: 9
  slug: meddra-term
jsonld:
- class_count: 2
  name: Meddra Context
  property_count: 13
  slug: meddra-context
layout: provider
modified: '2026-05-19'
name: Meddra
nav: Providers
network: true
overview: 'Meddra publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Hierarchy API, Terms API, Validation API, and 1 more.


  The Meddra catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Meddra''s developer surface includes authentication, developer portal, and 7 more developer resources.'
plans:
- name: Meddra Plans Pricing
  plan_count: 3
  slug: meddra-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Meddra Rate Limits
  slug: meddra-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Meddra API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: meddra-jsonschema-spectral-rules
score:
  band: thin
  composite: 30.3
  coverage:
    artifact_dirs: 13
    catalog_earned: 55.3
    catalog_earned_first_party: 0.0
    catalog_gap: 59.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 61.2
    developer_ergonomics: 21.4
    discoverability: 53.7
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 30.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    note: provider declares no identity tags; regime could not be determined
    undetermined: true
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/meddra/refs/heads/main/screenshots/meddra-2026-06-20T185114.png
security:
- kind: authentication
  name: Meddra Authentication
  slug: meddra-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Meddra Domain Security
  slug: meddra-domain-security
  summary_line: TLSv1.3
slug: meddra
website: https://www.meddra.org/
---
