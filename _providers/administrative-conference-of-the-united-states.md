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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-08-30'
api_count: 3
apis:
- description: 'ACUS maintains an online database of Equal Access to Justice Act (EAJA) awards, tracking awards of attorney''s fees and other costs against the United States government. ACUS collects and reports this '
  name: Equal Access to Justice Act (EAJA) Database
  slug: eaja-database
- description: 'A joint project between ACUS and Stanford Law School, the Federal Administrative Adjudication Database provides comprehensive data on federal agency adjudication processes across the U.S. government. '
  name: Federal Administrative Adjudication Database
  slug: federal-administrative-adjudication-database
- description: 'The Federal Administrative Procedure Sourcebook is ACUS''s reference wiki covering the core statutes of U.S. federal administrative procedure — the Administrative Procedure Act, FOIA, the Privacy Act, '
  name: Federal Administrative Procedure Sourcebook API
  slug: federal-administrative-procedure-sourcebook
artifact_total: 20
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/administrative-conference-of-the-united-states-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/administrative-conference-of-the-united-states-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/administrative-conference-of-the-united-states-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/administrative-conference-of-the-united-states-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/administrative-conference-of-the-united-states-lifecycle.yml
- group: build
  title: ''
  type: Examples
  url: examples/administrative-conference-of-the-united-states-sourcebook-api-examples.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/administrative-conference-of-the-united-states-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/administrative-conference-of-the-united-states-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/administrative-conference-of-the-united-states-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/administrative-conference-of-the-united-states-rate-limits.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/administrative-conference-of-the-united-states-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.acus.gov/vulnerability-disclosure-policy
- group: docs
  title: ''
  type: APIReference
  url: https://sourcebook.acus.gov/api.php
- group: docs
  title: ''
  type: Documentation
  url: https://www.acus.gov/page/resources
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acus.gov/document/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.acus.gov/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.acus.gov/rss.xml
- group: operate
  title: ''
  type: Support
  url: https://www.acus.gov/about-acus
- group: auth
  title: ''
  type: DomainSecurity
  url: security/administrative-conference-of-the-united-states-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/administrative-conference-of-the-united-states
- group: company
  title: ''
  type: Website
  url: https://www.acus.gov/
- group: start
  title: ''
  type: Portal
  url: https://www.acus.gov/
- group: other
  title: ''
  type: Resources
  url: https://www.acus.gov/page/resources
- group: operate
  title: ''
  type: Contact
  url: https://www.acus.gov/about-acus
created: '2024-11-20'
description: The Administrative Conference of the United States (ACUS) is an independent federal agency within the executive branch whose statutory mission is to identify ways to improve the procedures by which federal agencies administer regulatory, benefit, and other government programs. ACUS issues approximately a dozen recommendations per year to agencies, Congress, the President, and the Judicial Conference, aimed at enhancing efficiency and fairness in administrative procedures. The agency maintains the Federal Administrative Adjudication Database (with Stanford Law School), the Equal Access to Justice Act (EAJA) online database, and various open data resources under the Foundations for Evidence-Based Policymaking Act of 2018.
features:
- description: Issues approximately a dozen formal recommendations per year to federal agencies, Congress, the President, and the Judicial Conference aimed at improving the efficiency, fairness, and transparency of administrative procedures and regulatory programs.
  name: Regulatory Reform Recommendations
- description: Joint project with Stanford Law School providing comprehensive data on federal agency adjudication processes, administrative law judges, and hearing statistics across all federal agencies.
  name: Federal Administrative Adjudication Database
- description: Annual reporting to Congress on awards of attorney's fees and costs against the United States under EAJA, with an online database of all EAJA awards accessible to the public.
  name: Equal Access To Justice Act (EAJA) Reporting
- description: Comprehensive reference resource documenting the structure, authority, and programs of all U.S. executive agencies, updated periodically to reflect organizational changes.
  name: Sourcebook Of US Executive Agencies
- description: ACUS consultants and staff prepare research reports, model rules, and periodic summaries of administrative law reform bills on topics related to administrative procedure and government efficiency.
  name: Administrative Law Research And Publications
- description: ACUS maintains open data resources and has designated a Chief Data Officer in compliance with the Foundations for Evidence-Based Policymaking Act of 2018.
  name: Open Government Data Initiative
finops:
- name: Administrative Conference Of The United States Finops
  service_category: API
  slug: administrative-conference-of-the-united-states-finops
image: /assets/icons/administrative-conference-of-the-united-states.png
layout: provider
modified: '2026-08-30'
name: Administrative Conference of the United States
nav: Providers
network: true
overview: 'Administrative Conference of the United States publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Federal-Government, Regulatory Reform, Administrative Law, Government Efficiency, and Open Data.


  Administrative Conference of the United States'' developer surface includes authentication, code examples, API reference, documentation, engineering blog, support, developer portal, and 17 more developer resources.'
plans:
- name: Administrative Conference Of The United States Plans Pricing
  plan_count: 0
  slug: administrative-conference-of-the-united-states-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Administrative Conference Of The United States Rate Limits
  slug: administrative-conference-of-the-united-states-rate-limits
score:
  band: thin
  composite: 28.7
  coverage:
    artifact_dirs: 16
    catalog_gap: 77.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 16.4
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 6.7
    developer_ergonomics: 45.2
    discoverability: 64.8
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 12.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 50.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: rising
security:
- kind: authentication
  name: Administrative Conference Of The United States Authentication
  slug: administrative-conference-of-the-united-states-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Administrative Conference Of The United States Domain Security
  slug: administrative-conference-of-the-united-states-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Administrative Conference Of The United States Vulnerability Disclosure
  slug: administrative-conference-of-the-united-states-vulnerability-disclosure
  summary_line: contact published
slug: administrative-conference-of-the-united-states
tags:
- Federal-Government
- Regulatory Reform
- Administrative Law
- Government Efficiency
- Open Data
- Policy Research
use_cases:
- description: Legal researchers, law schools, and practitioners can access ACUS recommendations, reports, and the adjudication database to study trends in federal administrative law and regulatory practice.
  name: Administrative Law Research
- description: Federal agencies can use ACUS recommendations and research to benchmark their regulatory and adjudicative procedures against best practices and ACUS-recommended reforms.
  name: Regulatory Process Benchmarking
- description: Researchers and policymakers can use the EAJA database to analyze government litigation costs, identify agencies with high fee award rates, and evaluate the effectiveness of EAJA in providing access to justice.
  name: EAJA Litigation Cost Analysis
- description: Congressional staff and agency officials can draw on ACUS reports and model rules for guidance on improving rulemaking procedures, notice-and-comment processes, and public participation.
  name: Rulemaking Process Reform
- description: Public interest organizations and policy researchers can use ACUS data and publications to analyze opportunities for improving government administrative processes and reducing regulatory burdens.
  name: Government Efficiency Analysis
website: https://www.acus.gov/
---
