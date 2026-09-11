---
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
  scored_at: '2026-09-10'
api_count: 1
apis:
- description: 'The first-party HTTP API behind the AdvisorCheck consumer web application, served from an AWS API Gateway custom domain at api.advisorcheck.com. It is an internal application backend, not a published '
  name: AdvisorCheck Platform API
  slug: advisorcheck-platform-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/advisorcheck-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.advisorcheck.com/
- group: company
  title: ''
  type: About
  url: https://www.advisorcheck.com/about-us
- group: operate
  title: ''
  type: Support
  url: https://help.advisorcheck.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.advisorcheck.com/
- group: company
  title: ''
  type: Blog
  url: https://www.advisorcheck.com/blog/what-does-a-financial-advisor-do
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.advisorcheck.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.advisorcheck.com/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/advisorcheck-llms.txt
- group: start
  title: ''
  type: GettingStarted
  url: https://help.advisorcheck.com/en/collections/7-getting-started-with-advisorchceck
- group: commercial
  title: ''
  type: Plans
  url: plans/advisorcheck-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/advisorcheck-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/advisorcheck-conformance.yml
coverage:
  checked: '2026-09-09'
  detail: 'AdvisorCheck ships a consumer web product only: api.advisorcheck.com is an AWS API Gateway custom domain serving the app''s own backend and answers 403 "Missing Authentication Token" on /openapi.json, /swagger.json, /api-docs, /graphql and /mcp alike, while the company''s complete public help-center index (help.advisorcheck.com/llms.txt, HTTP 200, 95 lines, 9 collections) contains no developer, API, SDK or integration topic at all — and the marketing host is separately unreadable behind a Vercel Security Checkpoint (x-vercel-mitigated: challenge) on every path.'
  evidence:
  - status: 403
    url: https://api.advisorcheck.com/openapi.json
  - status: 200
    url: https://api.advisorcheck.com/ping
  - status: 200
    url: https://help.advisorcheck.com/llms.txt
  - status: 429
    url: https://www.advisorcheck.com/
  reason: no-developer-program
  state: none
created: '2026-09-09'
description: AdvisorCheck is a consumer-first platform for researching, comparing and continuously monitoring US financial advisors and the firms they work for. It compiles verified public regulatory data — FINRA BrokerCheck, the SEC's Investment Adviser Public Disclosure (IAPD) system, court records and six industry certification bodies — into profiles covering roughly 380,000 investment adviser representatives and 620,000 registered representatives. A free tier covers search and basic advisor monitoring; the paid AdvisorCheck Premium membership adds Advanced Monitoring with firm-stability insights (AUM changes, advisor headcount and retention, client acquisition trends, leadership and ownership changes, new firm disclosures). AdvisorCheck was founded in 2019, is headquartered in Englewood Cliffs, New Jersey with an office in Los Angeles, and raised a $1.8M seed round in June 2023. The company operates an application API at api.advisorcheck.com but publishes no public developer program,
  API reference or machine-readable contract.
image: https://staticfiles.gleap.io/ghelpcenter_logos/jdvki1Q6KfvVYn6WJ5IbzFkAMI1HDBnm3wWzcecsDmKnxPzAOwQgpAeq64xEys7QLTIbrs9OKCX.png
layout: provider
modified: '2026-09-09'
name: AdvisorCheck
nav: Providers
network: true
overview: 'AdvisorCheck publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial Services, Fintech, Regulatory Data, and Background Checks.


  AdvisorCheck''s developer surface includes support, engineering blog, getting-started guide, and 10 more developer resources.'
plans:
- name: Advisorcheck Plans Pricing
  plan_count: 2
  slug: advisorcheck-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Advisorcheck Rate Limits
  slug: advisorcheck-rate-limits
score:
  band: emerging
  composite: 19.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  provenance:
    conformance: first-party
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Advisorcheck Domain Security
  slug: advisorcheck-domain-security
  summary_line: TLSv1.3 · DMARC
slug: advisorcheck
tags:
- Company
- Financial Services
- Fintech
- Regulatory Data
- Background Checks
- Investor Protection
- Financial Advisors
- Wealth Management
- Consumer Finance
- Compliance
website: https://www.advisorcheck.com/
---
