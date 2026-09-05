---
access_model:
  confidence: medium
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
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
api_count: 4
apis:
- description: Retrieve the assessments available to an employer - both content the employer has authored and items selected from Vervoe's public Assessment Library - so an external system such as an ATS can display
  name: Vervoe Assessments API
  slug: vervoe-assessments-api
- description: Invite a candidate (email, first name, last name) to complete a specific assessment and monitor their progress. Per documented Example Scenario 2, the integration issues a "POST Invite candidate to co
  name: Vervoe Candidates API
  slug: vervoe-candidates-api
- description: 'Retrieve a candidate''s assessment results and scores so an external system can load and display them. Per documented Example Scenario 3, the integration issues a "GET Get candidate assessment report" '
  name: Vervoe Candidate Reports API
  slug: vervoe-reports-api
- description: An employer can configure a reporting webhook to which Vervoe sends an Assessment Report. Fourteen documented events fire updates - including candidate started, candidate completed, first AI grade, AI
  name: Vervoe Report Notification Webhook
  slug: vervoe-report-notification-webhook
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vervoe-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vervoe
- group: company
  title: ''
  type: Website
  url: https://vervoe.com
- group: docs
  title: ''
  type: Documentation
  url: https://vervoe.stoplight.io/docs/api-docs/ZG9jOjQ4ODIx-introduction
- group: other
  title: ''
  type: APILandingPage
  url: https://vervoe.com/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/vervoe-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vervoe-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/vervoe-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://vervoe.com/blog/
created: '2026-07-10'
description: Vervoe is an AI-powered skills assessment and skills-based hiring platform. Employers build their own assessment content or select from a public Assessment Library - assessments can include video, spreadsheets, presentations, and code challenges that simulate real work - then invite candidates and let Vervoe's AI grade and rank them by predicted on-the-job performance in "Talent Trials". The Vervoe API is a partner/integration REST API, accessed over HTTPS, that lets an external system (typically an ATS or internal hiring dashboard) list an employer's assessments, invite candidates to complete an assessment, retrieve candidate assessment reports and scores, and receive real-time report notifications through a signed webhook. API access is provisioned by Vervoe - partners contact sales to set up credentials. Detailed REST endpoint paths are not published in the public documentation, so the logical APIs below are modeled from Vervoe's documented Example Scenarios and webhook reference.
finops:
- name: Vervoe Finops
  service_category: Human Resources and Recruitment
  slug: vervoe-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vervoe.png
layout: provider
modified: '2026-07-10'
name: Vervoe
nav: Providers
network: true
overview: 'Vervoe publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Hiring, Recruitment, Skills Assessment, Talent, and HR Tech.


  Vervoe''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Vervoe Plans Pricing
  plan_count: 2
  slug: vervoe-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 3
  name: Vervoe Rate Limits
  slug: vervoe-rate-limits
score:
  band: emerging
  composite: 21.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 63.0
    catalog_earned_first_party: 0.0
    catalog_gap: 52.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 21.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vervoe/refs/heads/main/screenshots/vervoe-2026-09-02T165822.png
security:
- kind: domain-security
  name: Vervoe Domain Security
  slug: vervoe-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: vervoe
tags:
- Hiring
- Recruitment
- Skills Assessment
- Talent
- HR Tech
- AI Grading
- ATS Integration
website: https://vervoe.com
---
