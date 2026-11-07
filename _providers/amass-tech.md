---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Amass Tech Agentic Access
  operation_count: 50
  slug: amass-tech-agentic-access
  summary_line: 50 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.amass.tech
  baseurl_source: declared
  description: The cores/biomedcore API from Amass — 4 operation(s) for cores/biomedcore.
  name: Amass Cores/biomedcore API
  slug: amass-tech-cores-biomedcore-api
- baseURL: https://api.amass.tech
  baseurl_source: declared
  description: The cores/drugcore API from Amass — 4 operation(s) for cores/drugcore.
  name: Amass Cores/drugcore API
  slug: amass-tech-cores-drugcore-api
- baseURL: https://api.amass.tech
  baseurl_source: declared
  description: The cores/genecore API from Amass — 4 operation(s) for cores/genecore.
  name: Amass Cores/genecore API
  slug: amass-tech-cores-genecore-api
- baseURL: https://api.amass.tech
  baseurl_source: declared
  description: The cores/patentcore API from Amass — 3 operation(s) for cores/patentcore.
  name: Amass Cores/patentcore API
  slug: amass-tech-cores-patentcore-api
- baseURL: https://api.amass.tech
  baseurl_source: declared
  description: The cores/regulatorycore API from Amass — 5 operation(s) for cores/regulatorycore.
  name: Amass Cores/regulatorycore API
  slug: amass-tech-cores-regulatorycore-api
- baseURL: https://api.amass.tech
  baseurl_source: declared
  description: The cores/trialcore API from Amass — 4 operation(s) for cores/trialcore.
  name: Amass Cores/trialcore API
  slug: amass-tech-cores-trialcore-api
- baseURL: https://api.amass.tech
  baseurl_source: declared
  description: The credits API from Amass — 1 operation(s) for credits.
  name: Amass Credits API
  slug: amass-tech-credits-api
artifact_total: 20
common:
- group: agent
  href: https://artifacts.apis.io/amass-tech/agentic-access/amass-tech-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/amass-tech-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/amass-tech/plans/amass-tech-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/amass-tech-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/amass-tech/rules/amass-tech-rules.yml
  title: ''
  type: Spectral
  url: rules/amass-tech-rules.yml
- group: design
  href: https://artifacts.apis.io/amass-tech/json-ld/amass-tech-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/amass-tech-context.jsonld
- group: design
  href: https://artifacts.apis.io/amass-tech/vocabulary/amass-tech-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/amass-tech-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/amass-tech/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/amass-tech/data-model/amass-tech-data-model.yml
  title: ''
  type: DataModel
  url: data-model/amass-tech-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://amass.tech/security
- group: design
  href: https://artifacts.apis.io/amass-tech/errors/amass-tech-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/amass-tech-problem-types.yml
- group: design
  href: https://artifacts.apis.io/amass-tech/conformance/amass-tech-conformance.yml
  title: ''
  type: Conformance
  url: conformance/amass-tech-conformance.yml
- group: agent
  href: https://artifacts.apis.io/amass-tech/llms/amass-tech-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/amass-tech-llms.txt
- group: agent
  href: https://artifacts.apis.io/amass-tech/well-known/amass-tech-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/amass-tech-well-known.yml
- group: other
  href: https://artifacts.apis.io/amass-tech/hosts/amass-tech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/amass-tech-hosts.yml
- group: other
  href: https://artifacts.apis.io/amass-tech/vendors/amass-tech-vendors.yml
  title: ''
  type: Vendors
  url: vendors/amass-tech-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://amass.tech/legal/terms-of-service
- group: auth
  title: ''
  type: Security
  url: https://amass.tech/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://amass.tech/legal/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://amass.tech/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/JungeAlexander
- group: docs
  title: ''
  type: Documentation
  url: https://platform.amass.tech/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://platform.amass.tech/documentation/getting-started/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://platform.amass.tech/llms.txt
- group: auth
  href: https://artifacts.apis.io/amass-tech/security/amass-tech-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/amass-tech-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/amass-tech/security/amass-tech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amass-tech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://amass.tech/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.amass.tech/openapi.json
  - status: 401
    url: https://api.amass.tech/mcp
  - status: 200
    url: https://amass.tech/
  reason: partner-login
  state: gated
created: '2026-11-01'
description: Amass provides scientific intelligence for life sciences, aggregating papers, trials, drugs, genes, patents, regulatory records and live web data. Their platform offers an API and MCP, delivering cited answers to support research and development in biotech and healthcare.
image: https://amass.tech/api/og?label=Scientific+intelligence+for+life+science&title=Scientific+intelligence+you+can+verify.&footer=amass.tech
json_schemas:
- name: BiomedCoreRecord
  property_count: 30
  slug: amass-tech-biomed-core-record
- name: GeneCoreLookupItem
  property_count: 0
  slug: amass-tech-gene-core-lookup-item
- name: PatentCoreRecord
  property_count: 34
  slug: amass-tech-patent-core-record
- name: RegulatoryCoreChangedRecord
  property_count: 5
  slug: amass-tech-regulatory-core-changed-record
- name: TrialCoreChangedRecord
  property_count: 4
  slug: amass-tech-trial-core-changed-record
- name: TrialCoreRecord
  property_count: 56
  slug: amass-tech-trial-core-record
jsonld:
- class_count: 19
  name: Amass Tech Context
  property_count: 133
  slug: amass-tech-context
layout: provider
modified: '2026-11-01'
name: Amass
nav: Providers
network: true
overview: 'Amass publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Cores/biomedcore API, Cores/drugcore API, Cores/genecore API, and 4 more. Tagged areas include Company, Life Sciences, Data Intelligence, and MCP.


  The Amass catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Amass'' developer surface includes pricing, documentation, getting-started guide, API reference, and 21 more developer resources.'
plans:
- name: Amass Tech Plans Pricing
  plan_count: 5
  slug: amass-tech-plans-pricing
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: Amass API Rules
  rule_count: 18
  severity_counts:
    error: 16
    hint: 0
    info: 1
    warn: 1
  slug: amass-tech-rules
score:
  band: developing
  composite: 40.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.5
  facets:
    access_clarity: 59.2
    contract_governance: 22.0
    contract_quality: 61.2
    developer_ergonomics: 16.1
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 50.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 18.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Amass Tech Domain Security
  slug: amass-tech-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Amass Tech Trust Center
  slug: amass-tech-trust-center
  summary_line: SOC 2, ISO 27001
skill_count: 1
skills:
- name: get-records
  slug: amass-tech-get-records
slug: amass-tech
tags:
- Company
- Life Sciences
- Data Intelligence
- MCP
website: https://amass.tech/
---
