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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: The US Commission on Civil Rights is an independent, bipartisan federal agency established in 1957 that investigates, reports on, and issues public service announcements about discrimination or denial
  name: US Commission on Civil Rights
  slug: us-commission-on-civil-rights
artifact_total: 26
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/us-commission-on-civil-rights-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/us-commission-on-civil-rights-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usccrgov
- group: company
  title: ''
  type: Website
  url: https://www.usccr.gov/
- group: docs
  title: Reports and Publications
  type: Documentation
  url: https://www.usccr.gov/reports
- group: operate
  title: Frequently Asked Questions
  type: FAQ
  url: https://www.usccr.gov/about/faq
- group: commercial
  title: Privacy Policy
  type: TermsOfService
  url: https://www.usccr.gov/about/privacy-policy
- group: operate
  title: Contact Us
  type: Contact
  url: https://www.usccr.gov/about/contact
- group: design
  title: US Commission on Civil Rights Vocabulary
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/us-commission-on-civil-rights/refs/heads/main/vocabulary/us-commission-on-civil-rights-vocabulary.yml
- group: design
  title: US Commission on Civil Rights JSON-LD Context
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/us-commission-on-civil-rights/refs/heads/main/json-ld/us-commission-on-civil-rights-context.jsonld
created: '2024-12-25'
description: The US Commission on Civil Rights is an independent, bipartisan federal agency that investigates, reports on, and issues public service announcements about discrimination or denials of equal protection based on race, color, religion, sex, age, disability, national origin, or in the electoral process. The Commission informs the development of national civil rights policy and laws through factual research, advisory committees in all 50 states, and public reporting to the President and Congress.
examples:
- key_count: 10
  name: Us Commission On Civil Rights Complaint Example
  slug: us-commission-on-civil-rights-complaint-example
- key_count: 8
  name: Us Commission On Civil Rights No Fear Act Example
  slug: us-commission-on-civil-rights-no-fear-act-example
- key_count: 11
  name: Us Commission On Civil Rights Report Example
  slug: us-commission-on-civil-rights-report-example
features:
- description: Interactive map and datasets of civil rights complaints filed with federal agencies, organized by state and subject matter.
  name: Civil Rights Complaints Data
- description: Annual comprehensive data inventory maintained per the Foundations for Evidence-Based Policymaking Act of 2018, with a designated Chief Data Officer.
  name: Data Inventory Program
- description: Federal employee discrimination complaint statistics required under the Notification and Federal Employee Antidiscrimination and Retaliation Act.
  name: No FEAR Act Statistics
- description: Reports from 51 state and local advisory committees covering civil rights conditions across all 50 states and the District of Columbia.
  name: Advisory Committee Reports
- description: Congressional and Presidential reports on federal agency civil rights enforcement activities and compliance.
  name: Statutory Enforcement Reports
finops:
- name: Us Commission On Civil Rights Finops
  service_category: API
  slug: us-commission-on-civil-rights-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/us-commission-on-civil-rights.png
json_schemas:
- name: CivilRightsComplaint
  property_count: 10
  slug: us-commission-on-civil-rights-complaint
- name: NoFearActStatistic
  property_count: 8
  slug: us-commission-on-civil-rights-no-fear-act
- name: CivilRightsReport
  property_count: 11
  slug: us-commission-on-civil-rights-report
json_structures:
- name: Us Commission On Civil Rights Complaint Structure
  property_count: 10
  slug: us-commission-on-civil-rights-complaint-structure
- name: Us Commission On Civil Rights No Fear Act Structure
  property_count: 8
  slug: us-commission-on-civil-rights-no-fear-act-structure
- name: Us Commission On Civil Rights Report Structure
  property_count: 11
  slug: us-commission-on-civil-rights-report-structure
jsonld:
- class_count: 4
  name: Us Commission On Civil Rights Context
  property_count: 26
  slug: us-commission-on-civil-rights-context
layout: provider
modified: '2026-05-03'
name: US Commission on Civil Rights
nav: Providers
network: true
overview: 'US Commission on Civil Rights publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Civil Rights, Federal-Government, Equal Protection, and Discrimination.


  The US Commission on Civil Rights catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  US Commission on Civil Rights'' developer surface includes documentation, FAQ, and 8 more developer resources.'
plans:
- name: Us Commission On Civil Rights Plans Pricing
  plan_count: 3
  slug: us-commission-on-civil-rights-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Us Commission On Civil Rights Rate Limits
  slug: us-commission-on-civil-rights-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: US Commission on Civil Rights API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: us-commission-on-civil-rights-jsonschema-spectral-rules
score:
  band: emerging
  composite: 21.6
  coverage:
    artifact_dirs: 12
    catalog_earned: 62.3
    catalog_earned_first_party: 0.0
    catalog_gap: 52.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 24.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 25.0
    operational_transparency: 7.9
  previous_composite: 21.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/us-commission-on-civil-rights/refs/heads/main/screenshots/us-commission-on-civil-rights-2026-06-20T200608.png
security:
- kind: domain-security
  name: Us Commission On Civil Rights Domain Security
  slug: us-commission-on-civil-rights-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Us Commission On Civil Rights Vulnerability Disclosure
  slug: us-commission-on-civil-rights-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: us-commission-on-civil-rights
tags:
- Civil Rights
- Federal-Government
- Equal Protection
- Discrimination
use_cases:
- description: Accessing Commission reports, briefing papers, and findings to inform civil rights policy development and legislative analysis.
  name: Civil Rights Policy Research
- description: Analyzing civil rights complaint data by state, subject, and federal agency to understand discrimination patterns and trends.
  name: Discrimination Complaint Analysis
- description: Reviewing No FEAR Act statistics and statutory enforcement data to assess federal agency compliance with civil rights laws.
  name: Federal Agency Compliance Monitoring
- description: Using Commission datasets and reports for academic research on civil rights, equal opportunity, and discrimination in the United States.
  name: Academic Research
website: https://www.usccr.gov/
---
