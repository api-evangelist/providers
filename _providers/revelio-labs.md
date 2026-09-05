---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: REST API for programmatic access to Revelio Labs' workforce intelligence datasets — workforce dynamics, job postings (COSMOS), sentiment, layoffs, and individual-level files — returning standardized c
  name: Revelio Labs Data API
  slug: revelio-labs-data-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/revelio-labs-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/revelio-labs-llms.txt
- group: company
  title: ''
  type: Website
  url: https://reveliolabs.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.data-dictionary.reveliolabs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.data-dictionary.reveliolabs.com/
- group: company
  title: ''
  type: Blog
  url: https://www.reveliolabs.com/blog/
- group: start
  title: ''
  type: SignUp
  url: https://account.reveliolabs.com/signup
- group: start
  title: ''
  type: Login
  url: https://account.reveliolabs.com/login
- group: operate
  title: ''
  type: Support
  url: https://www.reveliolabs.com/demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.reveliolabs.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.reveliolabs.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/reveliolabs
created: '2026-07-17'
description: Revelio Labs is a workforce intelligence company that builds a universal HR database from public professional profiles, job postings, employee reviews, and WARN layoff notices. It maps more than 1.1 billion profiles across 20 million+ companies and 5,000+ skills into standardized datasets covering workforce dynamics (headcount, hiring and attrition flows, transitions), job postings (the COSMOS dataset), sentiment, layoffs, and individual-level user, position, education, and skill files. The data is delivered through a REST API, bulk data feeds, and an interactive dashboard, letting investors, corporations, and researchers analyze companies, labor markets, and talent trends in near real time.
image: https://www.reveliolabs.com/static/rl-logo-meta-image-96544d38919e52c97a23480ba1080d38.png
layout: provider
modified: '2026-07-20'
name: Revelio Labs
nav: Providers
network: true
overview: 'Revelio Labs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Workforce Intelligence, Labor Market Data, HR Analytics, and Talent Analytics.


  Revelio Labs'' developer surface includes documentation, engineering blog, signup flow, support, and 8 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 18.7
  coverage:
    artifact_dirs: 4
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 18.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/revelio-labs/refs/heads/main/screenshots/revelio-labs-2026-09-02T153655.png
security:
- kind: domain-security
  name: Revelio Labs Domain Security
  slug: revelio-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: revelio-labs
tags:
- Company
- Workforce Intelligence
- Labor Market Data
- HR Analytics
- Talent Analytics
- People Analytics
- Data
website: https://reveliolabs.com/
---
