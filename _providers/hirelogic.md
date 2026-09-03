---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hirelogic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hirelogic.com/
- group: company
  title: ''
  type: Blog
  url: https://hirelogic.com/insights/
- group: company
  title: ''
  type: BlogRSS
  url: https://hirelogic.com/feed/
- group: start
  title: ''
  type: SignUp
  url: https://app.hirelogic.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.hirelogic.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hirelogic.com/info/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hirelogic.com/info/privacy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hirelogic-co/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/hirelogicnow
- group: operate
  title: ''
  type: Support
  url: https://support.hirelogic.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.hirelogic.com/
- group: auth
  title: ''
  type: Compliance
  url: conformance/hirelogic-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hirelogic-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hirelogic-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/hirelogic-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hirelogic-rate-limits.yml
coverage:
  checked: '2026-08-22'
  detail: 'HireLogic, Inc. sells AI interview intelligence purely as an end-user SaaS app: /developers, /api and /docs all 404 on hirelogic.com, its only API host api.hirelogic.com is a private AWS API Gateway that 403s every anonymous request, and its ATS connectivity is consumed from the Merge unified API rather than exposed as one.'
  evidence:
  - status: 404
    url: https://hirelogic.com/developers
  - status: 404
    url: https://hirelogic.com/api
  - status: 403
    url: https://api.hirelogic.com/openapi.json
  - status: 404
    url: https://hirelogic.com/llms.txt
  - status: 200
    url: https://support.hirelogic.com/integrations
  reason: no-developer-program
  state: none
created: '2026-08-22'
description: 'HireLogic, Inc. is a US (Great Falls, Virginia) HR-technology company building an AI interview intelligence platform for staffing, recruiting and in-house talent teams. Its AI joins video, phone and in-person interviews to produce automated interview notes, transcripts, structured candidate summaries, topic highlights and hiring-signal analytics, so recruiters stop hand-writing notes and hiring managers can compare candidates on evidence rather than recall. The product surface includes instant interview insights, an interview chatbot for querying past interviews, intake-call insights, smart resume analysis and ranking, automated AI interviews, recruiting-team analytics, and a mobile companion app for in-person interviews. It integrates with Zoom, Microsoft Teams and Google Meet, and connects to applicant tracking systems through the Merge unified API as a consumer of that service. HireLogic raised a $4M seed round in 2022. It is delivered strictly as an end-user SaaS product:
  as of this profile the company publishes no public API, developer portal, SDK, or machine-readable contract.'
image: https://hirelogic.com/wp-content/uploads/Hirelogic_icon.png
layout: provider
modified: '2026-08-22'
name: HireLogic
nav: Providers
network: true
overview: 'HireLogic is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Human Resources, HR Tech, Recruiting, and Talent Acquisition.


  HireLogic''s developer surface includes engineering blog, signup flow, support, and 14 more developer resources.'
plans:
- name: Hirelogic Plans Pricing
  plan_count: 0
  slug: hirelogic-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Hirelogic Rate Limits
  slug: hirelogic-rate-limits
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 9
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 15.7
  provenance:
    conformance: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hirelogic/refs/heads/main/screenshots/hirelogic-2026-09-02T145737.png
security:
- kind: domain-security
  name: Hirelogic Domain Security
  slug: hirelogic-domain-security
  summary_line: TLSv1.3 · DMARC
slug: hirelogic
tags:
- Company
- Human Resources
- HR Tech
- Recruiting
- Talent Acquisition
- Interview Intelligence
- Artificial Intelligence
- Transcription
- Staffing
- Conversation Intelligence
website: https://hirelogic.com/
---
