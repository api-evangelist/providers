---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/cipherome/plans/cipherome-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cipherome-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/cipherome/hosts/cipherome-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cipherome-hosts.yml
- group: other
  href: https://artifacts.apis.io/cipherome/vendors/cipherome-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cipherome-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cipherome.com/terms-and-condition
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cipherome.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cipherome.com/pricing
- group: start
  title: ''
  type: Login
  url: https://www.cipherome.com/log-in
- group: other
  title: ''
  type: Leadership
  url: https://www.cipherome.com/team/priyanka
- group: docs
  title: ''
  type: Documentation
  url: https://www.cipherome.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.cipherome.com/docs-categories/getting-started-d627a
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cipherome
- group: auth
  href: https://artifacts.apis.io/cipherome/security/cipherome-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cipherome-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cipherome.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.cipherome.com/
  - status: 403
    url: https://equityzen.com/company/cipherome
  reason: no-developer-program
  state: none
created: '2026-10-08'
description: Cipherome provides the COMPASS data analysis platform for healthcare and life‑science research. It transforms raw clinical, genomic and biobank data into clean, structured datasets, enables cohort definition, statistical analysis, AI model training and automated reporting, all through an intuitive no‑code GUI. The platform accelerates research by handling data extraction, transformation, exploration and visualization, letting scientists focus on insights rather than data wrangling.
layout: provider
modified: '2026-10-08'
name: Cipherome
nav: Providers
network: true
overview: 'Cipherome is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare Data Analysis, Clinical Research, Genomic Analysis, AI Model Training, and Data Transformation.


  Cipherome''s developer surface includes pricing, documentation, getting-started guide, and 10 more developer resources.'
plans:
- name: Cipherome Plans Pricing
  plan_count: 6
  slug: cipherome-plans-pricing
random_paper: 20
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.5
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 45.5
    operational_transparency: 2.6
  previous_composite: 24.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cipherome/cipherome-2026-11-03T124157.png
security:
- kind: domain-security
  name: Cipherome Domain Security
  slug: cipherome-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cipherome
tags:
- Healthcare Data Analysis
- Clinical Research
- Genomic Analysis
- AI Model Training
- Data Transformation
website: https://www.cipherome.com/
---
