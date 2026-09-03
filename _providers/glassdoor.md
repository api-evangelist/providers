---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
- description: Historical REST API that exposed job listings, employer reviews, salary reports, and company metadata to approved partners. Required a partner ID and partner key as query parameters. The program stopp
  name: Glassdoor Partner API (Legacy)
  slug: partner-api-legacy
- description: Enterprise channel for distributing job postings from applicant tracking systems and programmatic recruitment platforms into Glassdoor. Access is contracted directly with Glassdoor / Indeed sales rath
  name: Glassdoor Job Distribution / ATS Integrations
  slug: job-distribution
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/glassdoor-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/glassdoor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.glassdoor.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.glassdoor.com/developer/index.htm
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/glassdoor.com
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Glassdoor
created: '2026-05-23'
description: Glassdoor is an online platform for company reviews, salary reports, and job listings, now part of Recruit Holdings (alongside Indeed) and tightly integrated with the broader Workday talent ecosystem. Historically Glassdoor offered a public Partner Job Search / Employer Reviews API (api.glassdoor.com/api/api.htm), but the program was closed to new applications in 2021 and active integrations require an existing partner relationship. Current API access is enterprise sales-led for ATS, programmatic recruitment, and employer-brand partners. No self-serve developer portal is active today.
finops:
- name: Glassdoor Finops
  service_category: API
  slug: glassdoor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/glassdoor.png
layout: provider
modified: '2026-05-23'
name: Glassdoor
nav: Providers
network: true
overview: 'Glassdoor publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Employer Reviews, Job Search, Salaries, Recruitment, and Employer Branding.


  Glassdoor''s developer surface includes documentation and 5 more developer resources.'
plans:
- name: Glassdoor Plans Pricing
  plan_count: 1
  slug: glassdoor-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 2
  name: Glassdoor Rate Limits
  slug: glassdoor-rate-limits
score:
  band: emerging
  composite: 17.3
  coverage:
    artifact_dirs: 6
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 17.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/glassdoor/refs/heads/main/screenshots/glassdoor-2026-06-20T181902.png
security:
- kind: domain-security
  name: Glassdoor Domain Security
  slug: glassdoor-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Glassdoor Vulnerability Disclosure
  slug: glassdoor-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: glassdoor
tags:
- Employer Reviews
- Job Search
- Salaries
- Recruitment
- Employer Branding
website: https://www.glassdoor.com/
---
