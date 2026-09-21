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
  try_now: true
agent_readiness:
  band: agent-aware
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.4
  scored_at: '2026-09-20'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Cdisc Agentic Access
  operation_count: 59
  slug: cdisc-agentic-access
  summary_line: 59 operations · 14 acting
api_count: 1
apis:
- description: CDISC CORE (Checks and Rules Engine) is an open-source rules engine for validating clinical data against CDISC conformance rules. It enables automated validation of SDTM, ADaM, and other study data ar
  name: CDISC CORE (Checks and Rules Engine) API
  slug: cdisc-core-api
- baseURL: https://library.cdisc.org/api
  baseurl_source: declared
  description: Analysis Data Model standards
  name: cdisc ADaM API
  slug: cdisc-adam-api
- baseURL: https://library.cdisc.org/api
  baseurl_source: declared
  description: CDISC Biomedical Concepts (COSMOS)
  name: cdisc Biomedical Concepts API
  slug: cdisc-biomedical-concepts-api
- baseURL: https://library.cdisc.org/api
  baseurl_source: declared
  description: Clinical Data Acquisition Standards Harmonization
  name: cdisc CDASH API
  slug: cdisc-cdash-api
- baseURL: https://library.cdisc.org/api
  baseurl_source: declared
  description: CDISC standards product catalog
  name: cdisc Products API
  slug: cdisc-products-api
- baseURL: https://library.cdisc.org/api
  baseurl_source: declared
  description: Study Data Tabulation Model standards
  name: cdisc SDTM API
  slug: cdisc-sdtm-api
- baseURL: https://library.cdisc.org/api
  baseurl_source: declared
  description: CDISC controlled terminology
  name: cdisc Terminology API
  slug: cdisc-terminology-api
- baseURL: https://library.cdisc.org/api
  baseurl_source: declared
  description: 'The Analysis Results Standard surface of the CDISC Library API — 17 read operations that expose published ARS packages and their reporting events: planned analyses, analysis sets, data subsets, groupi'
  name: CDISC Analysis Results Standard (ARS) API
  slug: cdisc-analysis-results-api
- description: 'CDISC-authored OpenAPI 3.1 specification for the Dataset-JSON API — studies, snapshots, datasets (including an NDJSON streaming representation and an $export operation) and Define-XML documents. This '
  name: CDISC Dataset-JSON API (standard specification)
  slug: cdisc-dataset-json-api
- description: CDISC-published OpenAPI for the USDM (Unified Study Definitions Model) study-definitions interface from the Digital Data Flow programme — create, update, read and version a study definition and search
  name: CDISC USDM (DDF) Study Definitions API
  slug: cdisc-usdm-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CDISC Library ADaM API
  slug: open-cdisc-adam-api
- collection_type: open
  name: CDISC Library ADaM Biomedical Concepts API
  slug: open-cdisc-biomedical-concepts-api
- collection_type: open
  name: CDISC Library ADaM CDASH API
  slug: open-cdisc-cdash-api
- collection_type: open
  name: CDISC Library API
  slug: open-cdisc-library
- collection_type: open
  name: CDISC Library ADaM Products API
  slug: open-cdisc-products-api
- collection_type: open
  name: CDISC Library ADaM SDTM API
  slug: open-cdisc-sdtm-api
- collection_type: open
  name: CDISC Library ADaM Terminology API
  slug: open-cdisc-terminology-api
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cdisc/refs/heads/main/agentic-access/cdisc-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cdisc-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cdisc/refs/heads/main/security/cdisc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cdisc-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cdisc/refs/heads/main/authentication/cdisc-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cdisc-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cdisc-org
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cdisc
- group: company
  title: ''
  type: Website
  url: https://www.cdisc.org/
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/cdisc/refs/heads/main/json-schema/cdisc-dataset-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/cdisc/refs/heads/main/json-ld/cdisc-context.jsonld
- group: start
  title: ''
  type: Portal
  url: https://www.cdisc.org/cdisc-library
- group: start
  title: ''
  type: GettingStarted
  url: https://www.cdisc.org/cdisc-library/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://www.cdisc.org/cdisc-library/api-documentation
- group: auth
  title: ''
  type: Authentication
  url: https://api.developer.library.cdisc.org/
- group: operate
  title: ''
  type: Support
  url: https://jira.cdisc.org/servicedesk/customer/portal/2
- group: operate
  title: ''
  type: ChangeLog
  url: https://wiki.cdisc.org/display/LIBSUPRT/Release+Notes
- group: start
  title: ''
  type: Signup
  url: https://www.cdisc.org/cdisc-library/api-account-request
- group: company
  title: ''
  type: Blog
  url: https://www.cdisc.org/news/whats-new
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cdisc/refs/heads/main/packages/cdisc-packages.yml
  title: ''
  type: Packages
  url: packages/cdisc-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cdisc/refs/heads/main/packages/cdisc-packages.yml
  title: ''
  type: SDKs
  url: packages/cdisc-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cdisc/refs/heads/main/cli/cdisc-cli.yml
  title: ''
  type: CLI
  url: cli/cdisc-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cdisc/refs/heads/main/conventions/cdisc-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cdisc-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cdisc/refs/heads/main/errors/cdisc-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cdisc-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cdisc/refs/heads/main/lifecycle/cdisc-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cdisc-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://cdisc.statuspage.io
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cdisc/refs/heads/main/changelog/cdisc-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cdisc-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cdisc/refs/heads/main/conformance/cdisc-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cdisc-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cdisc/refs/heads/main/data-model/cdisc-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cdisc-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cdisc/refs/heads/main/llms/cdisc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cdisc-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cdisc/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cdisc/refs/heads/main/plans/cdisc-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cdisc-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cdisc/refs/heads/main/rate-limits/cdisc-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cdisc-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cdisc/refs/heads/main/finops/cdisc-finops.yml
  title: ''
  type: FinOps
  url: finops/cdisc-finops.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cdisc/refs/heads/main/rules/cdisc-jsonschema-spectral-rules.yml
  title: ''
  type: Rules
  url: rules/cdisc-jsonschema-spectral-rules.yml
- group: operate
  title: ''
  type: Roadmap
  url: https://www.cdisc.org/cdisc-roadmap
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cdisc.org/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cdisc.org/privacy-policy
created: '2026-04-07'
description: CDISC Library uses linked data and a REST API to deliver CDISC standards metadata to software applications that automate standards-based processes. CDISC Library provides access to new relationships between standards as well as a substantially increased number of versioned CDISC standards and controlled terminology packages.
finops:
- name: Cdisc Finops
  service_category: API
  slug: cdisc-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cdisc.png
json_schemas:
- name: CDISC Dataset (Domain)
  property_count: 9
  slug: cdisc-dataset
jsonld:
- class_count: 6
  name: Cdisc Context
  property_count: 16
  slug: cdisc-context
layout: provider
modified: '2026-09-17'
name: Cdisc
nav: Providers
network: true
overview: 'Cdisc publishes 9 APIs on the [APIs.io](https://apis.io/) network, including ADaM API, Biomedical Concepts API, CDASH API, and 6 more. Tagged areas include Clinical Trials, Standards, Life Sciences, Pharma, and Healthcare.


  The Cdisc catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cdisc''s developer surface includes authentication, developer portal, getting-started guide, documentation, support, changelog, signup flow, and 28 more developer resources.'
plans:
- name: Cdisc Plans Pricing
  plan_count: 0
  slug: cdisc-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Cdisc Rate Limits
  slug: cdisc-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Cdisc API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: cdisc-jsonschema-spectral-rules
score:
  band: developing
  composite: 52.9
  coverage:
    artifact_dirs: 27
    catalog_earned: 49.3
    catalog_earned_first_party: 0.0
    catalog_gap: 65.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 14.4
    contract_quality: 63.6
    developer_ergonomics: 68.5
    discoverability: 59.3
    operational_transparency: 39.5
  previous_composite: 52.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 77.8
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/cdisc/refs/heads/main/screenshots/cdisc-2026-06-20T174105.png
security:
- kind: authentication
  name: Cdisc Authentication
  slug: cdisc-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Cdisc Domain Security
  slug: cdisc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cdisc
tags:
- Clinical Trials
- Standards
- Life Sciences
- Pharma
- Healthcare
- Metadata
- Controlled Terminology
- Data Exchange
- Non-Profit
website: https://www.cdisc.org/
---
