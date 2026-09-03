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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ripplematch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ripplematch.com
- group: company
  title: ''
  type: Blog
  url: https://ripplematch.com/career-advice
- group: start
  title: ''
  type: SignUp
  url: https://app.ripplematch.com/v2/login/register
- group: start
  title: ''
  type: Login
  url: https://app.ripplematch.com/v2/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.ripplematch.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.ripplematch.com/v2/public/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:support@ripplematch.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ripplematch-llms.txt
created: '2026-07-17'
description: RippleMatch is an AI-powered early-career recruiting platform that matches college students and recent graduates with internships and entry-level jobs based on their background, skills, and career goals rather than mass applications. For employers it offers "Campus OS", an all-in-one recruiting operating system for sourcing, skills validation, and campus event management, and it transfers matched candidates into most major applicant tracking systems (Greenhouse, Workday, Lever, SmartRecruiters, BambooHR). RippleMatch was surfaced as a portfolio company of Bullpen Capital and profiled in the API Evangelist network. As of this enrichment pass the company publishes no public developer portal, API reference, OpenAPI specification, SDKs, or webhook/event surface; its integrations are one-way ATS data transfers rather than an openly documented API.
image: https://8139278.fs1.hubspotusercontent-na1.net/hubfs/8139278/RippleMatch%20Logo%20Square%20-%202024%20Onwards.png
layout: provider
modified: '2026-07-21'
name: RippleMatch
nav: Providers
network: true
overview: 'RippleMatch is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Recruiting, Hiring, Early Career, and Job Matching.


  RippleMatch''s developer surface includes engineering blog, signup flow, support, and 6 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ripplematch/refs/heads/main/screenshots/ripplematch-2026-09-02T153849.png
security:
- kind: domain-security
  name: Ripplematch Domain Security
  slug: ripplematch-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ripplematch
tags:
- Company
- Recruiting
- Hiring
- Early Career
- Job Matching
- Campus Recruiting
- Talent Acquisition
- HR Tech
website: https://ripplematch.com
---
