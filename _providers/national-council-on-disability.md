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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 4.7
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: FOIA-accessible data from the National Council on Disability including performance and results act reports, congressional budget justification reports, financial audit reports, strategic plans, bylaws
  name: National Council on Disability FOIA Data
  slug: ncd-foia-data
- description: Comprehensive archive of NCD policy reports dating back to 1984 covering disability civil rights, healthcare, transportation, employment, housing, financial assistance, and emergency management. Repor
  name: National Council on Disability Policy Reports
  slug: ncd-policy-reports
- description: 'Performance, accountability, and budget data from the National Council on Disability. Includes Annual Performance Reports, Congressional Budget Justification Reports, financial audits, and EEO policy '
  name: National Council on Disability Accountability Reports
  slug: ncd-accountability-data
artifact_total: 41
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/national-council-on-disability-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ncdgov
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/ncd-vocabulary.yaml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/ncd-policy-report-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/ncd-foia-record-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/ncd-accountability-report-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/ncd-testimony-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/ncd-stakeholder-letter-schema.json
- group: company
  title: ''
  type: Website
  url: https://www.ncd.gov
- group: docs
  title: ''
  type: Documentation
  url: https://www.ncd.gov/reports/
- group: other
  title: ''
  type: DataAPI
  url: https://www.ncd.gov/foia/
- group: operate
  title: ''
  type: Contact
  url: https://www.ncd.gov/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ncd.gov/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.ncd.gov/newsroom/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/ncd-context.jsonld
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/ncd-policy-report-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/ncd-foia-record-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/ncd-accountability-report-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/ncd-testimony-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/ncd-stakeholder-letter-structure.json
- group: build
  title: ''
  type: Examples
  url: examples/ncd-policy-report-example.json
- group: build
  title: ''
  type: Examples
  url: examples/ncd-foia-record-example.json
- group: build
  title: ''
  type: Examples
  url: examples/ncd-accountability-report-example.json
- group: build
  title: ''
  type: Examples
  url: examples/ncd-testimony-example.json
- group: build
  title: ''
  type: Examples
  url: examples/ncd-stakeholder-letter-example.json
- group: company
  title: ''
  type: Blog
  url: https://www.ncd.gov/newsroom/
created: '2024-12-03'
description: The National Council on Disability (NCD) is an independent federal agency that advises the President, Congress, and other federal agencies on disability policy and programs. Established in 1978, the NCD promotes equal opportunity, economic self-sufficiency, independent living, and full participation in all areas of society for individuals with disabilities. The agency conducts research, gathers information, and provides recommendations to improve policies, programs, and services. NCD publishes policy reports spanning civil rights, healthcare, transportation, employment, housing, and emergency management for people with disabilities.
examples:
- key_count: 8
  name: Ncd Accountability Report Example
  slug: ncd-accountability-report-example
- key_count: 7
  name: Ncd Foia Record Example
  slug: ncd-foia-record-example
- key_count: 8
  name: Ncd Policy Report Example
  slug: ncd-policy-report-example
- key_count: 7
  name: Ncd Stakeholder Letter Example
  slug: ncd-stakeholder-letter-example
- key_count: 7
  name: Ncd Testimony Example
  slug: ncd-testimony-example
features:
- description: Comprehensive archive of NCD policy reports dating back to 1984 covering all areas of disability policy including civil rights, healthcare, employment, housing, and transportation.
  name: Policy Reports Archive
- description: Proactively published collection of NCD documents including bylaws, performance reports, budget justifications, financial audits, and strategic plans available for public download.
  name: FOIA e-Library
- description: Archive of NCD testimony before Congress on disability policy issues, providing insight into legislative advocacy and policy recommendations over time.
  name: Congressional Testimony Archive
- description: Practical toolkits and fact sheets on disability rights and policy topics to help individuals, advocates, and policymakers understand and implement disability-inclusive practices.
  name: Disability Policy Toolkits
- description: Press releases, newsroom updates, and letters to federal agency stakeholders documenting NCD's ongoing policy engagement and recommendations.
  name: Newsroom and Stakeholder Letters
finops:
- name: National Council On Disability Finops
  service_category: API
  slug: national-council-on-disability-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/national-council-on-disability.png
integrations:
- description: NCD's work intersects with the Americans with Disabilities Act guidance provided through ADA.gov maintained by the Department of Justice.
  name: ADA.gov
- description: NCD recommendations inform resources available through federal disability information portals providing access to government benefits and services.
  name: Disability.gov
- description: Federal government open data portal where related disability datasets from agencies like SSA, HHS, and DOL are cataloged and made available for download.
  name: data.gov
- description: NCD federal spending data is publicly accessible through USASpending.gov as part of federal transparency requirements.
  name: USASpending.gov
json_schemas:
- name: NCD Accountability Report
  property_count: 8
  slug: ncd-accountability-report
- name: NCD FOIA Record
  property_count: 7
  slug: ncd-foia-record
- name: NCD Policy Report
  property_count: 8
  slug: ncd-policy-report
- name: NCD Stakeholder Letter
  property_count: 7
  slug: ncd-stakeholder-letter
- name: NCD Congressional Testimony
  property_count: 7
  slug: ncd-testimony
json_structures:
- name: Ncd Accountability Report Structure
  property_count: 8
  slug: ncd-accountability-report-structure
- name: Ncd Foia Record Structure
  property_count: 7
  slug: ncd-foia-record-structure
- name: Ncd Policy Report Structure
  property_count: 8
  slug: ncd-policy-report-structure
- name: Ncd Stakeholder Letter Structure
  property_count: 7
  slug: ncd-stakeholder-letter-structure
- name: Ncd Testimony Structure
  property_count: 7
  slug: ncd-testimony-structure
jsonld:
- class_count: 3
  name: Ncd Context
  property_count: 6
  slug: ncd-context
layout: provider
modified: '2026-04-19'
name: National Council on Disability
nav: Providers
network: true
overview: 'National Council on Disability publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Disability, Federal Government, Policy, Civil Rights, and Healthcare.


  The National Council on Disability catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  National Council on Disability''s developer surface includes documentation, code examples, engineering blog, and 23 more developer resources.'
plans:
- name: National Council On Disability Plans Pricing
  plan_count: 3
  slug: national-council-on-disability-plans-pricing
random_paper: 32
rate_limits:
- limit_count: 5
  name: National Council On Disability Rate Limits
  slug: national-council-on-disability-rate-limits
rules:
- name: National Council on Disability API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: national-council-on-disability-jsonschema-spectral-rules
score:
  band: thin
  composite: 32.3
  delta: -5.8
  facets:
    commercial_clarity: 50.0
    contract_quality: 8.1
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 31.6
  previous_composite: 38.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 22.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/national-council-on-disability/refs/heads/main/screenshots/national-council-on-disability-2026-06-20T190008.png
security:
- kind: domain-security
  name: National Council On Disability Domain Security
  slug: national-council-on-disability-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: national-council-on-disability
solutions:
- description: NCD provides independent policy analysis and recommendations to the three branches of government on all matters affecting people with disabilities.
  name: Disability Policy Leadership
- description: NCD monitors federal agency compliance with disability rights laws and makes recommendations for program improvements and new legislation.
  name: Federal Agency Accountability
- description: NCD publishes toolkits, fact sheets, and reports to educate the public and policymakers about disability rights and best practices for inclusion.
  name: Public Education
tags:
- Disability
- Federal Government
- Policy
- Civil Rights
- Healthcare
- Independent Agency
use_cases:
- description: Access NCD's comprehensive reports to research disability policy history, current recommendations, and policy gaps across federal programs and agencies.
  name: Disability Policy Research
- description: Submit FOIA requests or access the FOIA e-Library to retrieve agency financial, performance, and operational documents.
  name: FOIA Document Retrieval
- description: Use NCD testimony archives and policy letters as reference material for disability rights advocacy and legislative engagement.
  name: Legislative Advocacy
- description: Access NCD recommendations to understand federal agency obligations under disability rights laws including the ADA, Rehabilitation Act, and other statutes.
  name: Federal Agency Compliance
- description: Download NCD policy reports, progress reports, and data for academic research on disability policy, independent living, and civil rights.
  name: Academic Research
website: https://www.ncd.gov
---
