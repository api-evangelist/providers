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
    consent_identity: true
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
  score: 4.7
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chasi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chasi.ai
- group: company
  title: ''
  type: About
  url: https://chasi.ai/about-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chasi.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chasi.ai/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Chasi-AI
- group: auth
  title: ''
  type: TrustCenter
  url: https://chasi-ai.trust.site/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chasi-ai/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/chasi-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.chasi.ai/
- group: build
  title: ''
  type: Packages
  url: packages/chasi-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/chasi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/chasi-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/chasi-conformance.yml
- group: other
  title: ''
  type: ContentSignal
  url: well-known/chasi-robots.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/chasi-llms.txt
- group: company
  title: ''
  type: Careers
  url: https://app.dover.com/jobs/chasi
- group: start
  title: ''
  type: Demo
  url: https://demo.chasi.co
- group: other
  title: ''
  type: iOSApp
  url: https://apps.apple.com/us/app/chasi-ai/id6761392628
coverage:
  checked: '2026-08-13'
  detail: 'Chasi ships real software — a Clerk-authenticated tenant app at app.chasi.ai, an iOS app (v1.6.0, 2026-07-27) and a Rootly status page — but runs no developer program: every spec path 404s on chasi.ai, api.chasi.ai and mcp.chasi.ai do not resolve (and chasi.ai has no wildcard DNS), the Chasi-AI GitHub org has 0 public repos, and the only docs-shaped subdomain, docs.chasi.ai, is mispointed at Cap''s (cap.so) documentation — its OpenAPI self-identifies as "Cap HTTP API", so it was rejected under the ownership check and nothing was derived from it.'
  evidence:
  - status: 404
    url: https://chasi.ai/openapi.json
  - status: 404
    url: https://chasi.ai/llms.txt
  - status: 404
    url: https://chasi.ai/.well-known/agent-card.json
  - status: 200
    url: https://docs.chasi.ai/api
  - status: 200
    url: https://api.github.com/orgs/Chasi-AI/repos
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Chasi (Chasi AI) is a Y Combinator Winter 2026 company building an AI revenue engine for the equipment industry — sales, rental, and service. Chasi deploys AI agents that plug into an equipment dealer or rental company's existing stack and work around the clock to handle lead intake, quoting, CRM updates, follow-ups, and booking coordination, so teams respond faster, sell more, and maximize fleet utilization without adding headcount. Founded in 2025 by Akash Pavan and Sarman Aulakh, the company targets an industry where fleet utilization often sits below 60% and reps lose hours each day to email, voicemail, and manual data entry. Chasi ships a Clerk-authenticated tenant application at app.chasi.ai, a first-party iOS app, an interactive demo, a Rootly-hosted status page, and a trust center, and is live with equipment businesses in the US and Europe — but as of August 2026 it publishes no public developer API, OpenAPI, GraphQL, MCP server, agent card, or SDK, and its go-to-market
  is sales-led through a booked demo and a 90-day pilot.
image: https://framerusercontent.com/assets/GT39i2nj6q4IM9EL9nYFxG6psDA.png
layout: provider
modified: '2026-08-13'
name: Chasi
nav: Providers
network: true
overview: Chasi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Agents, Equipment, and Equipment Rental.
plans:
- name: Chasi Plans Pricing
  plan_count: 0
  slug: chasi-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Chasi Rate Limits
  slug: chasi-rate-limits
score:
  band: emerging
  composite: 13.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 13.2
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chasi/refs/heads/main/screenshots/chasi-2026-07-25T205115.png
security:
- kind: domain-security
  name: Chasi Domain Security
  slug: chasi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Chasi Trust Center
  slug: chasi-trust-center
  summary_line: SOC 2
slug: chasi
tags:
- Company
- Artificial Intelligence
- AI Agents
- Equipment
- Equipment Rental
- Equipment Dealers
- Sales Automation
- Vertical AI
- CRM
website: https://chasi.ai
---
