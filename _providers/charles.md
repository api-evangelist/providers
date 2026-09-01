---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Charles Agentic Access
  operation_count: 7
  slug: charles-agentic-access
  summary_line: 7 operations · 2 acting
api_count: 1
apis:
- description: The Charles University Digital Repository (Digitalni repozitar UK), a DSpace-based institutional repository, exposes a public OAI-PMH 2.0 endpoint for metadata harvesting of digitized collections incl
  name: CU Digital Repository OAI-PMH
  slug: digital-repository-oai
- description: The Charles University Research Publications Repository is a DSpace-based institutional archive where staff and students self-archive research outputs. It exposes a public OAI-PMH endpoint for metadat
  name: CU Research Publications Repository OAI-PMH
  slug: publications-repository-oai
- description: Public REST API for named-entity recognition and tokenization (NameTag) operated by the Institute of Formal and Applied Linguistics (UFAL) at Charles University via the LINDAT/CLARIAH-CZ infrastructur
  name: LINDAT NameTag API
  slug: lindat-nametag
- description: Operations with source and target languages
  name: Charles University languages API
  slug: charles-languages-api
- description: Operations related to translation models
  name: Charles University models API
  slug: charles-models-api
- description: Root resource for navigation to languages/models
  name: Charles University root API
  slug: charles-root-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LINDAT Translation languages API
  slug: open-charles-languages-api
- collection_type: open
  name: LINDAT Translation languages models API
  slug: open-charles-models-api
- collection_type: open
  name: LINDAT Translation languages root API
  slug: open-charles-root-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/charles-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/charles-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/charles-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cuni.cz/UKEN-1.html
- group: build
  title: ''
  type: GitHub
  url: https://github.com/UKUK-Repository-Dept
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/univerzita-karlova/
- group: auth
  title: ''
  type: Authentication
  url: https://uvt.cuni.cz/UVTEN-37.html
- group: commercial
  title: ''
  type: Plans
  url: plans/charles-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/charles-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/charles-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Charles University (Univerzita Karlova), founded in 1348 in Prague, is the largest and oldest university in Czechia and is ranked #246 in the QS World University Rankings 2025. Its public developer/API footprint is limited and primarily academic-infrastructure oriented: institutional DSpace repositories expose standards-based OAI-PMH metadata-harvesting endpoints, and the Institute of Formal and Applied Linguistics (UFAL, Faculty of Mathematics and Physics) operates the LINDAT/CLARIAH-CZ platform which publishes documented public REST web services for natural-language processing. Core student-facing systems such as the Study Information System (SIS) and single sign-on are gated behind eduID.cz / Shibboleth (SAML) authentication and do not publish an open API.'
examples:
- key_count: 4
  name: Charles Get Language Collection Example
  slug: charles-get-language-collection-example
- key_count: 4
  name: Charles Get Model Collection Example
  slug: charles-get-model-collection-example
- key_count: 4
  name: Charles Post Model Item Example
  slug: charles-post-model-item-example
finops:
- name: Charles Finops
  service_category: Education
  slug: charles-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/charles.png
json_schemas:
- name: LanguageResource
  property_count: 3
  slug: charles-language
- name: ModelResource
  property_count: 6
  slug: charles-model
json_structures:
- name: Charles Language Structure
  property_count: 2
  slug: charles-language-structure
- name: Charles Model Structure
  property_count: 5
  slug: charles-model-structure
jsonld:
- class_count: 8
  name: Charles Context
  property_count: 3
  slug: charles-context
layout: provider
modified: '2026-06-03'
name: Charles University
nav: Providers
network: true
overview: 'Charles University publishes 3 APIs on the [APIs.io](https://apis.io/) network: languages API, models API, and root API. Tagged areas include Education, Higher Education, University, Research, and Open Data.


  The Charles University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Charles University''s developer surface includes GitHub presence, authentication, and 9 more developer resources.'
plans:
- name: Charles Plans Pricing
  plan_count: 2
  slug: charles-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Charles Rate Limits
  slug: charles-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Charles University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: charles-jsonschema-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Charles University API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 3
  slug: charles-rules
score:
  band: thin
  composite: 35.7
  coverage:
    artifact_dirs: 14
    catalog_gap: 47.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 47.8
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 35.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 42.6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/charles/refs/heads/main/screenshots/charles-2026-06-20T174227.png
security:
- kind: domain-security
  name: Charles Domain Security
  slug: charles-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Charles Vulnerability Disclosure
  slug: charles-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: charles
tags:
- Education
- Higher Education
- University
- Research
- Open Data
- Repository
- OAI-PMH
- Natural Language Processing
- Czechia
- Europe
website: https://www.cuni.cz/UKEN-1.html
---
