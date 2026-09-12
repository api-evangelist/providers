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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-12'
api_count: 2
apis:
- description: StudentAid.gov is the official consumer platform for U.S. federal student aid. Borrowers and students use the site to complete the FAFSA, manage federal loans, review repayment plans, and access aid r
  name: StudentAid.gov
  slug: studentaid-gov
- description: 'The College Scorecard API, operated by the U.S. Department of Education via api.data.gov, exposes institution-level data including federal aid participation, costs, completion rates, and post-college '
  name: College Scorecard API
  slug: college-scorecard
artifact_total: 8
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
  url: https://data.ed.gov/
- group: operate
  title: ''
  type: Support
  url: https://studentaid.gov/help-center
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://studentaid.gov/help/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/federal-student-aid-authentication.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/federal-student-aid-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/federal-student-aid-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/federal-student-aid-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/federal-student-aid-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/federal-student-aid-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/federal-student-aid-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/federal-student-aid-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/federal-student-aid-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/federal-student-aid-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/federal-student-aid-rate-limits.yml
- group: auth
  title: ''
  type: Security
  url: security/federal-student-aid-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/federal-student-aid-vulnerability-disclosure.yml
created: '2024-12-03'
description: The Federal Student Aid (FSA) office of the U.S. Department of Education provides grants, loans, and work-study funds to eligible students enrolled in college or career school. FSA operates StudentAid.gov as the consumer portal for managing federal student loans, completing the FAFSA, and exploring repayment options. FSA does not currently publish a public, open developer API program; aggregate higher education and aid data is redistributed through the Department of Education's open data programs such as the College Scorecard API.
finops:
- name: Federal Student Aid Finops
  service_category: API
  slug: federal-student-aid-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/federal-student-aid.png
layout: provider
modified: '2026-09-09'
name: Federal Student Aid
nav: Providers
network: true
overview: 'Federal Student Aid publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Federal-Government, Financial Aid, Grants, and Loans.


  Federal Student Aid''s developer surface includes support, authentication, changelog, and 18 more developer resources.'
plans:
- name: Federal Student Aid Plans Pricing
  plan_count: 0
  slug: federal-student-aid-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 3
  name: Federal Student Aid Rate Limits
  slug: federal-student-aid-rate-limits
score:
  band: thin
  composite: 31.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 47.0
    catalog_earned_first_party: 12.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 66.7
    operational_transparency: 63.2
  previous_composite: 31.3
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/federal-student-aid/refs/heads/main/screenshots/federal-student-aid-2026-06-20T181128.png
security:
- kind: authentication
  name: Federal Student Aid Authentication
  slug: federal-student-aid-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Federal Student Aid Domain Security
  slug: federal-student-aid-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Federal Student Aid Vulnerability Disclosure
  slug: federal-student-aid-vulnerability-disclosure
  summary_line: Hackerone
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
