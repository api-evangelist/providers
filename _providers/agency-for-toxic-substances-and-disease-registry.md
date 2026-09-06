---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Agency For Toxic Substances And Disease Registry Agentic Access
  operation_count: 4
  slug: agency-for-toxic-substances-and-disease-registry-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- baseURL: https://data.cdc.gov/resource
  baseurl_source: declared
  description: The Exposure Investigations API from Agency for Toxic Substances and Disease Registry — 1 operation(s) for exposure investigations.
  name: Agency for Toxic Substances and Disease Registry Exposure Investigations API
  slug: agency-for-toxic-substances-and-disease-registry-exposure-investigations-api
- baseURL: https://data.cdc.gov/resource
  baseurl_source: declared
  description: The Minimum Risk Levels API from Agency for Toxic Substances and Disease Registry — 1 operation(s) for minimum risk levels.
  name: Agency for Toxic Substances and Disease Registry Minimum Risk Levels API
  slug: agency-for-toxic-substances-and-disease-registry-minimum-risk-levels-api
- baseURL: https://data.cdc.gov/resource
  baseurl_source: declared
  description: The Substance Priority List API from Agency for Toxic Substances and Disease Registry — 1 operation(s) for substance priority list.
  name: Agency for Toxic Substances and Disease Registry Substance Priority List API
  slug: agency-for-toxic-substances-and-disease-registry-substance-priority-list-api
- baseURL: https://data.cdc.gov/resource
  baseurl_source: declared
  description: The Toxicological Profiles API from Agency for Toxic Substances and Disease Registry — 1 operation(s) for toxicological profiles.
  name: Agency for Toxic Substances and Disease Registry Toxicological Profiles API
  slug: agency-for-toxic-substances-and-disease-registry-toxicological-profiles-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ATSDR Toxic Substance Profiles Exposure Investigations API
  slug: open-agency-for-toxic-substances-and-disease-registry-exposure-investigations-api
- collection_type: open
  name: ATSDR Toxic Substance Profiles Exposure Investigations Minimum Risk Levels API
  slug: open-agency-for-toxic-substances-and-disease-registry-minimum-risk-levels-api
- collection_type: open
  name: ATSDR Toxic Substance Profiles Exposure Investigations Substance Priority List API
  slug: open-agency-for-toxic-substances-and-disease-registry-substance-priority-list-api
- collection_type: open
  name: ATSDR Toxic Substance Profiles Exposure Investigations Toxicological Profiles API
  slug: open-agency-for-toxic-substances-and-disease-registry-toxicological-profiles-api
- collection_type: open
  name: ATSDR Toxic Substance Profiles API
  slug: open-atsdr-toxic-substance-profiles
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/agency-for-toxic-substances-and-disease-registry-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agency-for-toxic-substances-and-disease-registry-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/agency-for-toxic-substances-and-disease-registry
- group: company
  title: ''
  type: Website
  url: https://www.atsdr.cdc.gov/
- group: start
  title: ''
  type: Portal
  url: https://www.atsdr.cdc.gov/api
- group: start
  title: ''
  type: DataPortal
  url: https://data.cdc.gov/browse?category=Environmental+Health
- group: start
  title: ''
  type: GettingStarted
  url: https://www.atsdr.cdc.gov/substances/index.asp
- group: docs
  title: ''
  type: Documentation
  url: https://www.atsdr.cdc.gov/mrls/index.asp
- group: docs
  title: ''
  type: Documentation
  url: https://www.atsdr.cdc.gov/spl/index.html
- group: other
  title: ''
  type: FOIA
  url: https://www.hhs.gov/foia/index.html
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/agency-for-toxic-substances-and-disease-registry/refs/heads/main/rules/atsdr-spectral-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/agency-for-toxic-substances-and-disease-registry/refs/heads/main/json-schema/atsdr-tox-profile-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/agency-for-toxic-substances-and-disease-registry/refs/heads/main/json-schema/atsdr-mrl-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/agency-for-toxic-substances-and-disease-registry/refs/heads/main/json-ld/atsdr-toxicology-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/agency-for-toxic-substances-and-disease-registry/refs/heads/main/vocabulary/atsdr-vocabulary.yaml
created: '2024-11-21'
description: ATSDR protects communities from harmful health effects related to exposure to natural and man-made hazardous substances. It is a federal public health agency within the U.S. Department of Health and Human Services. ATSDR provides toxicological profiles, minimum risk levels, substance priority rankings, and exposure investigation data for hazardous chemicals.
examples:
- key_count: 7
  name: Atsdr Toxic Substance Profiles Exposure Investigation Example
  slug: atsdr-toxic-substance-profiles-exposure-investigation-example
- key_count: 7
  name: Atsdr Toxic Substance Profiles Minimum Risk Level Example
  slug: atsdr-toxic-substance-profiles-minimum-risk-level-example
- key_count: 7
  name: Atsdr Toxic Substance Profiles Substance Priority Example
  slug: atsdr-toxic-substance-profiles-substance-priority-example
- key_count: 7
  name: Atsdr Toxic Substance Profiles Tox Profile Example
  slug: atsdr-toxic-substance-profiles-tox-profile-example
finops:
- name: Agency For Toxic Substances And Disease Registry Finops
  service_category: API
  slug: agency-for-toxic-substances-and-disease-registry-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/agency-for-toxic-substances-and-disease-registry.png
json_schemas:
- name: ExposureInvestigation
  property_count: 7
  slug: atsdr-toxic-substance-profiles-exposure-investigation
- name: MinimumRiskLevel
  property_count: 7
  slug: atsdr-toxic-substance-profiles-minimum-risk-level
- name: SubstancePriority
  property_count: 7
  slug: atsdr-toxic-substance-profiles-substance-priority
- name: ToxProfile
  property_count: 7
  slug: atsdr-toxic-substance-profiles-tox-profile
json_structures:
- name: Atsdr Toxic Substance Profiles Exposure Investigation Structure
  property_count: 7
  slug: atsdr-toxic-substance-profiles-exposure-investigation-structure
- name: Atsdr Toxic Substance Profiles Minimum Risk Level Structure
  property_count: 7
  slug: atsdr-toxic-substance-profiles-minimum-risk-level-structure
- name: Atsdr Toxic Substance Profiles Substance Priority Structure
  property_count: 7
  slug: atsdr-toxic-substance-profiles-substance-priority-structure
- name: Atsdr Toxic Substance Profiles Tox Profile Structure
  property_count: 7
  slug: atsdr-toxic-substance-profiles-tox-profile-structure
jsonld:
- class_count: 4
  name: Agency For Toxic Substances And Disease Registry Atsdr Context
  property_count: 23
  slug: agency-for-toxic-substances-and-disease-registry-atsdr-context
layout: provider
modified: '2026-05-19'
name: Agency for Toxic Substances and Disease Registry
nav: Providers
network: true
overview: 'Agency for Toxic Substances and Disease Registry publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Exposure Investigations API, Minimum Risk Levels API, Substance Priority List API, and 1 more. Tagged areas include Diseases, Federal-Government, Public Health, Toxic Substances, and Environmental Health.


  The Agency for Toxic Substances and Disease Registry catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Agency for Toxic Substances and Disease Registry''s developer surface includes developer portal, getting-started guide, documentation, and 12 more developer resources.'
plans:
- name: Agency For Toxic Substances And Disease Registry Plans Pricing
  plan_count: 3
  slug: agency-for-toxic-substances-and-disease-registry-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Agency For Toxic Substances And Disease Registry Rate Limits
  slug: agency-for-toxic-substances-and-disease-registry-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Agency for Toxic Substances and Disease Registry API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: agency-for-toxic-substances-and-disease-registry-jsonschema-spectral-rules
- effective_rule_count: 68
  extends:
  - spectral:oas
  name: Agency for Toxic Substances and Disease Registry API Rules
  rule_count: 27
  severity_counts:
    error: 14
    hint: 0
    info: 0
    warn: 13
  slug: agency-for-toxic-substances-and-disease-registry-spectral-rules
score:
  band: thin
  composite: 29.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 57.5
    catalog_earned_first_party: 0.0
    catalog_gap: 42.5
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 28.8
    contract_quality: 57.8
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 29.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agency-for-toxic-substances-and-disease-registry/refs/heads/main/screenshots/agency-for-toxic-substances-and-disease-registry-2026-06-20T165830.png
security:
- kind: domain-security
  name: Agency For Toxic Substances And Disease Registry Domain Security
  slug: agency-for-toxic-substances-and-disease-registry-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: agency-for-toxic-substances-and-disease-registry
tags:
- Diseases
- Federal-Government
- Public Health
- Toxic Substances
- Environmental Health
- Hazardous Materials
website: https://www.atsdr.cdc.gov/
---
