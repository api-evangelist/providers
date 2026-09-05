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
- description: 'JSON:API compliant REST API for managing candidates, jobs, applications, users, departments, and recruitment workflows in Teamtailor. Available in EU (api.teamtailor.com), NA (api.na.teamtailor.com), '
  name: Teamtailor API
  slug: rest-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/teamtailor-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/teamtailor-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Teamtailor
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/teamtailor
- group: company
  title: ''
  type: Website
  url: https://www.teamtailor.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.teamtailor.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.teamtailor.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://app.teamtailor.com/users/sign_up
created: '2026-05-11'
description: Teamtailor is an applicant tracking system (ATS) and employer branding platform that helps companies attract, engage, and hire candidates with customizable career sites, recruitment workflows, candidate communications, and analytics. The platform supports collaborative hiring, GDPR compliance, and a marketplace of integrations. Teamtailor's API follows the JSON:API specification with regional base URLs and uses token-based authentication with Public, Internal, and Admin key permission levels.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/teamtailor.png
layout: provider
modified: '2026-05-11'
name: Teamtailor
nav: Providers
network: true
overview: 'Teamtailor publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include ATS, Applicant Tracking, Recruiting, HR, and Hiring.


  Teamtailor''s developer surface includes documentation, pricing, signup flow, and 5 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 15.4
  coverage:
    artifact_dirs: 2
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 15.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/teamtailor/refs/heads/main/screenshots/teamtailor-2026-06-20T194958.png
security:
- kind: domain-security
  name: Teamtailor Domain Security
  slug: teamtailor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Teamtailor Trust Center
  slug: teamtailor-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: teamtailor
tags:
- ATS
- Applicant Tracking
- Recruiting
- HR
- Hiring
- Employer Branding
website: https://www.teamtailor.com
---
