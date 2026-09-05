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
  band: agent-ready
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
    error_semantics: verified
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
  score: 35.4
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Abortion Policy Api Agentic Access
  operation_count: 12
  slug: abortion-policy-api-agentic-access
  summary_line: 12 operations
api_count: 4
apis:
- baseURL: https://api.abortionpolicyapi.com/v1
  baseurl_source: spec
  description: Endpoints for retrieving gestational limit abortion policies by state or zip code.
  name: Abortion Policy API Gestational Limits API
  slug: abortion-policy-api-gestational-limits-api
- baseURL: https://api.abortionpolicyapi.com/v1
  baseurl_source: spec
  description: Endpoints for retrieving abortion insurance coverage restrictions by state or zip code.
  name: Abortion Policy API Insurance Coverage API
  slug: abortion-policy-api-insurance-coverage-api
- baseURL: https://api.abortionpolicyapi.com/v1
  baseurl_source: spec
  description: Endpoints for retrieving abortion restrictions targeting minors by state or zip code.
  name: Abortion Policy API Minors API
  slug: abortion-policy-api-minors-api
- baseURL: https://api.abortionpolicyapi.com/v1
  baseurl_source: spec
  description: Endpoints for retrieving abortion waiting period restrictions by state or zip code.
  name: Abortion Policy API Waiting Periods API
  slug: abortion-policy-api-waiting-periods-api
artifact_total: 49
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Abortion Policy Gestational Limits API
  slug: open-abortion-policy-api-gestational-limits-api
- collection_type: open
  name: Abortion Policy Gestational Limits Insurance Coverage API
  slug: open-abortion-policy-api-insurance-coverage-api
- collection_type: open
  name: Abortion Policy Gestational Limits Minors API
  slug: open-abortion-policy-api-minors-api
- collection_type: open
  name: Abortion Policy Gestational Limits Waiting Periods API
  slug: open-abortion-policy-api-waiting-periods-api
- collection_type: open
  name: Abortion Policy API
  slug: open-abortion-policy-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/abortion-policy-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abortion-policy-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/abortion-policy-api-authentication.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://www.abortionpolicyapi.com/
- group: auth
  title: ''
  type: Authentication
  url: https://www.abortionpolicyapi.com/request-access
- group: docs
  title: ''
  type: APIReference
  url: https://www.abortionpolicyapi.com/field-references
- group: other
  title: ''
  type: CaseStudies
  url: https://www.abortionpolicyapi.com/case-studies
- group: operate
  title: ''
  type: Support
  url: https://www.abortionpolicyapi.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.abortionpolicyapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.abortionpolicyapi.com/privacy
- group: operate
  title: ''
  type: RateLimits
  url: ''
- group: design
  title: ''
  type: SpectralRules
  url: rules/abortion-policy-api-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/abortion-policy-api-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/abortion-policy-api-context.jsonld
created: '2025-01-07'
description: The Abortion Policy API provides up-to-date information on US state abortion policies that can be integrated into online abortion resources. The API consolidates abortion laws into one database across four data tables covering gestational limits, insurance coverage, minors restrictions, and waiting periods. Data is accessible by US state name or zip code. The project is co-led by Patient Forward and is fiscally sponsored by NEO Philanthropy.
examples:
- key_count: 6
  name: Gestational Limits Example
  slug: gestational-limits-example
- key_count: 18
  name: Insurance Coverage Example
  slug: insurance-coverage-example
- key_count: 7
  name: Minors Restrictions Example
  slug: minors-restrictions-example
- key_count: 6
  name: Waiting Periods Example
  slug: waiting-periods-example
features:
- description: State-by-state gestational limit policies including exceptions for life, health, fetal anomaly, and rape/incest.
  name: Gestational Limits Data
- description: Comprehensive insurance coverage restrictions covering Medicaid, private insurance, and ACA exchange plans by state.
  name: Insurance Coverage Data
- description: Parental consent, notification, and judicial bypass requirements for minors seeking abortion by state.
  name: Minors Restrictions Data
- description: State mandatory waiting period hours and counseling visit requirements between counseling and abortion care.
  name: Waiting Periods Data
- description: All policy data accessible by US state name or 5-digit zip code for integration flexibility.
  name: State and Zip Code Lookup
- description: Data collaboratively analyzed by reproductive rights experts from Guttmacher, Planned Parenthood, Power to Decide, CRR, and others.
  name: Expert-Curated Data
- description: API provided free without gatekeeping as a public good resource for reproductive health organizations.
  name: Free Public Good
finops:
- name: Abortion Policy Api Finops
  service_category: API
  slug: abortion-policy-api-finops
image: /assets/icons/abortion-policy-api.png
integrations:
- description: Used by Planned Parenthood for patient-facing abortion policy information.
  name: Planned Parenthood
- description: Powers policy data in the Abortion Finder patient resource tool.
  name: Abortion Finder
- description: Integrated into Charley the Chatbot for conversational abortion policy guidance.
  name: Charley the Chatbot
- description: Powers policy data for ineedana.com abortion access resource.
  name: Ineedana.com
- description: Available as an independent publisher connector for Power Apps, Power Automate, Logic Apps, and Copilot Studio.
  name: Microsoft Power Platform
json_schemas:
- name: GestationalLimits
  property_count: 6
  slug: gestational-limits
- name: InsuranceCoverage
  property_count: 18
  slug: insurance-coverage
- name: MinorsRestrictions
  property_count: 7
  slug: minors-restrictions
- name: WaitingPeriods
  property_count: 6
  slug: waiting-periods
json_structures:
- name: Gestational Limits Structure
  property_count: 6
  slug: gestational-limits-structure
- name: Insurance Coverage Structure
  property_count: 18
  slug: insurance-coverage-structure
- name: Minors Restrictions Structure
  property_count: 7
  slug: minors-restrictions-structure
- name: Waiting Periods Structure
  property_count: 6
  slug: waiting-periods-structure
jsonld:
- class_count: 4
  name: Abortion Policy Api Context
  property_count: 33
  slug: abortion-policy-api-context
layout: provider
modified: '2026-05-19'
name: Abortion Policy API
nav: Providers
network: true
overview: 'Abortion Policy API publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Gestational Limits API, Insurance Coverage API, Minors API, and 1 more. Tagged areas include Abortion, Policies, Healthcare, and Government.


  The Abortion Policy API catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Abortion Policy API''s developer surface includes authentication, getting-started guide, API reference, support, and 9 more developer resources.'
plans:
- name: Abortion Policy Api Plans Pricing
  plan_count: 3
  slug: abortion-policy-api-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Abortion Policy Api Rate Limits
  slug: abortion-policy-api-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Abortion Policy API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: abortion-policy-api-jsonschema-spectral-rules
- effective_rule_count: 79
  extends:
  - spectral:oas
  name: Abortion Policy API API Rules
  rule_count: 38
  severity_counts:
    error: 16
    hint: 0
    info: 2
    warn: 20
  slug: abortion-policy-api-spectral-rules
score:
  band: thin
  composite: 35.8
  coverage:
    artifact_dirs: 15
    catalog_earned: 66.5
    catalog_earned_first_party: 0.0
    catalog_gap: 48.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 28.8
    contract_quality: 29.9
    developer_ergonomics: 45.2
    discoverability: 55.6
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 35.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/abortion-policy-api/refs/heads/main/screenshots/abortion-policy-api-2026-06-20T161254.png
security:
- kind: authentication
  name: Abortion Policy Api Authentication
  slug: abortion-policy-api-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Abortion Policy Api Domain Security
  slug: abortion-policy-api-domain-security
  summary_line: TLSv1.3 · HSTS
slug: abortion-policy-api
tags:
- Abortion
- Policies
- Healthcare
- Government
use_cases:
- description: Integrate state abortion policy data into patient-facing tools that help people find abortion services.
  name: Abortion Finder Applications
- description: Embed policy data into clinical tools to help providers advise patients on state-specific access restrictions.
  name: Healthcare Provider Tools
- description: Access structured policy data for data journalism, academic research, and policy analysis.
  name: Journalism and Research
- description: Power public education tools and advocacy platforms with accurate, up-to-date abortion policy information.
  name: Advocacy and Education
- description: Provide abortion policy answers in conversational tools like Charley the Chatbot.
  name: Chatbot Integration
- description: Support legal aid organizations with accurate state law data for advising clients on abortion access.
  name: Legal Aid Resources
---
