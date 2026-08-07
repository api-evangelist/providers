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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: The US Commission on International Religious Freedom (USCIRF) is an independent, bipartisan federal government commission created by the International Religious Freedom Act of 1998 that monitors relig
  name: US Commission on International Religious Freedom
  slug: us-commission-on-international-religious-freedom
artifact_total: 29
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/us-commission-on-international-religious-freedom-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/us-commission-on-international-religious-freedom
- group: company
  title: ''
  type: Website
  url: https://www.uscirf.gov/
- group: docs
  title: Publications
  type: Documentation
  url: https://www.uscirf.gov/publications
- group: docs
  title: Annual Reports Archive
  type: Documentation
  url: https://www.uscirf.gov/annual-reports
- group: operate
  title: Contact USCIRF
  type: Contact
  url: https://www.uscirf.gov/about-uscirf/contact-us
- group: commercial
  title: Privacy Policy
  type: TermsOfService
  url: https://www.uscirf.gov/privacy-policy
- group: design
  title: USCIRF Vocabulary
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/us-commission-on-international-religious-freedom/refs/heads/main/vocabulary/us-commission-on-international-religious-freedom-vocabulary.yml
- group: design
  title: USCIRF JSON-LD Context
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/us-commission-on-international-religious-freedom/refs/heads/main/json-ld/us-commission-on-international-religious-freedom-context.jsonld
created: '2024-12-25'
description: The US Commission on International Religious Freedom (USCIRF) is an independent, bipartisan federal government commission created by the International Religious Freedom Act (IRFA) of 1998. USCIRF monitors the universal right to freedom of religion or belief abroad, reviews the facts and circumstances of violations of religious freedom internationally, and makes policy recommendations to the President, Secretary of State, and Congress. The Commission publishes an annual report designating Countries of Particular Concern (CPCs) and Special Watch List (SWL) countries, and recommends Entities of Particular Concern (EPCs) among non-state actors.
examples:
- key_count: 10
  name: Uscirf Annual Report Example
  slug: uscirf-annual-report-example
- key_count: 10
  name: Uscirf Country Assessment Example
  slug: uscirf-country-assessment-example
- key_count: 8
  name: Uscirf Policy Recommendation Example
  slug: uscirf-policy-recommendation-example
features:
- description: Comprehensive annual report documenting religious freedom conditions in countries worldwide, with CPC and SWL designations and policy recommendations to the U.S. government.
  name: Annual Report
- description: Formal designation recommendations for countries that engage in or tolerate particularly severe violations of religious freedom, used to guide U.S. foreign policy.
  name: Countries of Particular Concern Designations
- description: Countries that do not meet the CPC threshold but require close monitoring due to severe violations of religious freedom.
  name: Special Watch List
- description: Non-state actor designations for groups that engage in particularly severe violations of religious freedom abroad.
  name: Entities of Particular Concern
- description: Detailed country-by-country assessments of religious freedom conditions, minority group situations, and government treatment of religious communities.
  name: Country Reports and Fact Sheets
- description: Targeted policy recommendations on specific issues, countries, or legislation for the President, Secretary of State, and Congress.
  name: Policy Briefs and Recommendations
finops:
- name: Us Commission On International Religious Freedom Finops
  service_category: API
  slug: us-commission-on-international-religious-freedom-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/us-commission-on-international-religious-freedom.png
integrations:
- description: USCIRF works with the State Department's Office of International Religious Freedom, and State uses USCIRF recommendations for CPC and SWL designations.
  name: U.S. Department of State
- description: USCIRF reports directly to Congress, submitting annual and special reports with legislative recommendations.
  name: U.S. Congress
json_schemas:
- name: AnnualReport
  property_count: 10
  slug: uscirf-annual-report
- name: CountryAssessment
  property_count: 10
  slug: uscirf-country-assessment
- name: PolicyRecommendation
  property_count: 8
  slug: uscirf-policy-recommendation
json_structures:
- name: Uscirf Annual Report Structure
  property_count: 10
  slug: uscirf-annual-report-structure
- name: Uscirf Country Assessment Structure
  property_count: 10
  slug: uscirf-country-assessment-structure
- name: Uscirf Policy Recommendation Structure
  property_count: 8
  slug: uscirf-policy-recommendation-structure
jsonld:
- class_count: 3
  name: Us Commission On International Religious Freedom Context
  property_count: 25
  slug: us-commission-on-international-religious-freedom-context
layout: provider
modified: '2026-05-03'
name: US Commission on International Religious Freedom
nav: Providers
network: true
overview: 'US Commission on International Religious Freedom publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Federal Government, Religious Freedom, International Human Rights, and Foreign Policy.


  The US Commission on International Religious Freedom catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  US Commission on International Religious Freedom''s developer surface includes documentation and 8 more developer resources.'
plans:
- name: Us Commission On International Religious Freedom Plans Pricing
  plan_count: 3
  slug: us-commission-on-international-religious-freedom-plans-pricing
random_paper: 25
rate_limits:
- limit_count: 5
  name: Us Commission On International Religious Freedom Rate Limits
  slug: us-commission-on-international-religious-freedom-rate-limits
rules:
- name: US Commission on International Religious Freedom API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: us-commission-on-international-religious-freedom-jsonschema-spectral-rules
score:
  band: thin
  composite: 36.4
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 29.0
    developer_ergonomics: 8.7
    discoverability: 50.0
    governance: 68.8
    operational_transparency: 31.6
  previous_composite: 36.4
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/us-commission-on-international-religious-freedom/refs/heads/main/screenshots/us-commission-on-international-religious-freedom-2026-06-20T200619.png
security:
- kind: domain-security
  name: Us Commission On International Religious Freedom Domain Security
  slug: us-commission-on-international-religious-freedom-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: us-commission-on-international-religious-freedom
tags:
- Federal Government
- Religious Freedom
- International Human Rights
- Foreign Policy
use_cases:
- description: Using USCIRF designations and reports to understand U.S. government positions on international religious freedom and foreign policy priorities.
  name: Foreign Policy Analysis
- description: Assessing religious freedom risks in specific countries using CPC, SWL, and country report data for diplomatic, humanitarian, or business purposes.
  name: Country Risk Assessment
- description: Academic and advocacy research on international religious freedom conditions, trends, and the effectiveness of U.S. policy interventions.
  name: Human Rights Research
- description: Using USCIRF country assessments as supporting documentation for asylum claims and refugee status determinations involving religious persecution.
  name: Refugee and Asylum Applications
- description: Informing legislative advocacy and policy development using USCIRF recommendations and findings on specific countries or religious freedom issues.
  name: Congressional and Policy Advocacy
website: https://www.uscirf.gov/
---
