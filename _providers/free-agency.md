---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
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
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.freeagency.com/
- group: company
  title: ''
  type: Blog
  url: https://intent.freeagency.com
- group: company
  title: ''
  type: BlogRSS
  url: https://intent.freeagency.com/feed
- group: start
  title: ''
  type: SignUp
  url: https://tally.so/r/Bz7QYQ
- group: operate
  title: ''
  type: Contact
  url: https://tally.so/r/kdKARZ
- group: company
  title: ''
  type: Careers
  url: https://jobs.ashbyhq.com/freeagency
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/join-free-agency
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/free-agency
- group: auth
  title: ''
  type: DomainSecurity
  url: security/free-agency-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/free-agency-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/free-agency-llms.txt
coverage:
  checked: '2026-08-13'
  detail: Free Agency's entire public surface is one Next.js waitlist page — /pricing, /docs, /api, /developers and every /.well-known/ path return HTTP 404, api./app./docs./ developer.freeagency.com do not resolve in DNS, and the github.com/free-agency org holds only two forked third-party utility repos, so there is no developer program to read.
  evidence:
  - status: 404
    url: https://www.freeagency.com/openapi.json
  - status: 404
    url: https://www.freeagency.com/.well-known/agent-card.json
  - status: 404
    url: https://www.freeagency.com/developers
  - status: 200
    url: https://www.freeagency.com/
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Free Agency is a careers company and talent marketplace that pairs technology professionals with an AI-powered Talent Agent which proactively surfaces relevant work — full-time roles and short project engagements with defined deliverables, duration, and compensation. Founded by Sherveen Mashayekhi and backed by Bloomberg Beta, the company has raised a $10M Series A and counts talent placed at companies such as OpenAI, Stripe, and Figma. It also publishes Intent, a newsletter for careerists, and runs CareerMakers, a cohort course hosted on Maven. As of August 2026 the entire public surface is a single waitlist landing page with two Tally intake forms — one for individual talent and one "For AI companies" — plus the Intent newsletter and an Ashby-hosted job board. Free Agency exposes no public API, SDK, developer portal, or machine-readable contract of any kind; this profile tracks it in the API Evangelist network as a company stub with a probed, verified absence rather than an
  unexamined gap.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/free-agency.png
layout: provider
modified: '2026-08-13'
name: Free Agency
nav: Providers
network: true
overview: 'Free Agency is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Careers, Talent, Recruiting, and Marketplace.


  Free Agency''s developer surface includes engineering blog, signup flow, and 9 more developer resources.'
plans:
- name: Free Agency Plans Pricing
  plan_count: 0
  slug: free-agency-plans-pricing
random_paper: 2
score:
  band: minimal
  composite: 9.2
  delta: -0.3
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 9.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/free-agency/refs/heads/main/screenshots/free-agency-2026-07-25T215123.png
security:
- kind: domain-security
  name: Free Agency Domain Security
  slug: free-agency-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: free-agency
tags:
- Company
- Careers
- Talent
- Recruiting
- Marketplace
- Jobs
- AI
- Newsletter
website: https://www.freeagency.com/
---
