---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The Wonolo API V2 is a RESTful, JSON-only integration API for the Wonolo on-demand staffing platform. It performs CRUD operations against platform resources — Users (both Workers/Wonoloers and Employe
  name: Wonolo API V2
  slug: wonolo-api-v2
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.wonolo.com/
- group: company
  title: ''
  type: Blog
  url: https://www.wonolo.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Wonolo
- group: operate
  title: ''
  type: Support
  url: https://support-business.wonolo.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support-worker.wonolo.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://info.wonolo.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://info.wonolo.com/privacy/
- group: start
  title: ''
  type: Login
  url: https://api.wonolo.com/users/sign_in
- group: agent
  title: ''
  type: WellKnown
  url: well-known/wonolo-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wonolo-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wonolo-llms.txt
coverage:
  checked: '2026-08-05'
  detail: Wonolo's API is live — https://api.wonolo.com/api_v2/info answers 200 anonymously — but its public reference at wonolo.readme.io now returns a hard 404 and the Developer Center at developer.wonolo.com is a dangling Netlify custom domain (cert covers only *.netlify.app, origin 404s), so the api_v2 contract is reachable today only by customers Wonolo has issued an api_key/secret_key to.
  evidence:
  - status: 200
    url: https://api.wonolo.com/api_v2/info
  - status: 404
    url: https://wonolo.readme.io/docs/getting-started
  - status: 404
    url: https://wonolo-developer-center.netlify.app/
  - status: 404
    url: https://api.wonolo.com/openapi.json
  reason: customer-only-docs
  state: gated
created: '2026-08-05'
description: Wonolo is an on-demand staffing marketplace, founded in 2013 and headquartered in San Francisco, that connects businesses needing flexible frontline labor with a pool of vetted independent workers ("Wonoloers") for warehousing, manufacturing, food production, retail, hospitality and general labor jobs. Businesses post job requests and are matched to available workers in real time without resumes or interviews, for one-off, ongoing and temp-to-hire needs. Wonolo operates a REST integration API (V2) on api.wonolo.com that lets customers create and manage job requests, jobs, workers and users programmatically and receive webhook callbacks, so scheduling, timekeeping, HR and CRM systems can be wired directly into the staffing platform.
image: https://framerusercontent.com/assets/PBgIa3TL1hQKy1ZdIQ2vbm12CE.png
layout: provider
modified: '2026-08-05'
name: Wonolo
nav: Providers
network: true
overview: 'Wonolo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Staffing, Workforce, Human Resources, and Marketplace.


  Wonolo''s developer surface includes engineering blog, support, and 9 more developer resources.'
random_paper: 74
score:
  band: emerging
  composite: 18.2
  delta: -0.8
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 19.0
  provenance:
    conformance: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Wonolo Authentication
  slug: wonolo-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Wonolo Domain Security
  slug: wonolo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wonolo
tags:
- Company
- Staffing
- Workforce
- Human Resources
- Marketplace
- Gig Economy
- Recruiting
- Labor
- On-Demand
website: https://www.wonolo.com/
---
