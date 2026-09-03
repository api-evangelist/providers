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
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: StudentAid.gov is the official consumer platform for U.S. federal student aid. Borrowers and students use the site to complete the FAFSA, manage federal loans, review repayment plans, and access aid r
  name: StudentAid.gov
  slug: studentaid-gov
- description: 'The College Scorecard API, operated by the U.S. Department of Education via api.data.gov, exposes institution-level data including federal aid participation, costs, completion rates, and post-college '
  name: College Scorecard API
  slug: college-scorecard
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/federal-student-aid-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/federalstudentaid
- group: company
  title: ''
  type: Website
  url: https://studentaid.gov
- group: company
  title: ''
  type: About
  url: https://studentaid.gov/about
- group: other
  title: ''
  type: FAFSA
  url: https://studentaid.gov/h/apply-for-aid/fafsa
- group: other
  title: ''
  type: Open Data
  url: https://www.ed.gov/about/news/data
created: '2024-12-03'
description: The Federal Student Aid (FSA) office of the U.S. Department of Education provides grants, loans, and work-study funds to eligible students enrolled in college or career school. FSA operates StudentAid.gov as the consumer portal for managing federal student loans, completing the FAFSA, and exploring repayment options. FSA does not currently publish a public, open developer API program; aggregate higher education and aid data is redistributed through the Department of Education's open data programs such as the College Scorecard API.
finops:
- name: Federal Student Aid Finops
  service_category: API
  slug: federal-student-aid-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/federal-student-aid.png
layout: provider
modified: '2026-04-28'
name: Federal Student Aid
nav: Providers
network: true
overview: Federal Student Aid publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Federal-Government, Financial Aid, Grants, and Loans.
plans:
- name: Federal Student Aid Plans Pricing
  plan_count: 3
  slug: federal-student-aid-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Federal Student Aid Rate Limits
  slug: federal-student-aid-rate-limits
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 5
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 10.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 11.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/federal-student-aid/refs/heads/main/screenshots/federal-student-aid-2026-06-20T181128.png
security:
- kind: domain-security
  name: Federal Student Aid Domain Security
  slug: federal-student-aid-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: federal-student-aid
tags:
- Education
- Federal-Government
- Financial Aid
- Grants
- Loans
- Student Aid
website: https://studentaid.gov
---
