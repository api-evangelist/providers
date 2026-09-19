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
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-09-18'
api_count: 0
artifact_total: 5
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gartner/refs/heads/main/security/gartner-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/gartner-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gartner/refs/heads/main/security/gartner-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gartner-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gartner
- group: company
  title: ''
  type: Website
  url: https://www.gartner.com
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gartner/refs/heads/main/well-known/gartner-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gartner-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gartner/refs/heads/main/well-known/gartner-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/gartner-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gartner/refs/heads/main/security/gartner-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/gartner-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gartner/refs/heads/main/llms/gartner-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gartner-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/gartner/refs/heads/main/plans/gartner-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gartner-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/gartner/refs/heads/main/rate-limits/gartner-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gartner-rate-limits.yml
- group: operate
  title: ''
  type: Support
  url: https://gpivendorresources.gartner.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.gartner.com/en/insights
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gartner.com/en/about/policies/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gartner.com/en/about/policies/usage-policy
coverage:
  checked: '2026-09-12'
  detail: Gartner's only live first-party API host, gapi.gartner.com, is an AWS API Gateway that answers every anonymous request with 403 "Missing Authentication Token", and no reference, contract or auth guide for it is published outside the subscription-gated client platform and the login-walled Peer Insights vendor portal.
  evidence:
  - status: 403
    url: https://gapi.gartner.com/
  - status: 404
    url: https://api.gartner.com/openapi.json
  - status: 200
    url: https://gpivendorresources.gartner.com/llms.txt
  - status: 200
    url: https://www.gartner.com/.well-known/security.txt
  reason: customer-only-docs
  state: gated
created: '2026-03-24'
description: 'Gartner, Inc. (NYSE IT) is a global research and advisory firm selling syndicated research, analyst inquiry, benchmarking, peer communities and conferences to executives across IT, finance, HR, supply chain, marketing, sales, legal and customer service. Gartner publishes no public developer API, developer portal or machine-readable contract: the research library and the Peer Insights vendor portal are subscription-gated, and the one live first-party API host found by probe (gapi.gartner.com, an AWS API Gateway) rejects every anonymous request. Gartner sold its Digital Markets business - Capterra, GetApp and Software Advice, and the Buyer Discovery API that serves their intent data - to G2 in February 2026, so the only OpenAPI reachable on a gartner.com host belongs to G2. This repository tracks the company and any first-party technical artifact that surfaces over time.'
graphqls:
- description: '> **PROVENANCE WARNING — this is NOT a Gartner contract.** This schema was authored by'
  name: Gartner GraphQL Schema
  slug: gartner-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gartner.png
layout: provider
modified: '2026-09-12'
name: Gartner
nav: Providers
network: true
overview: 'Gartner is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Research, Advisory, Analyst, Enterprise, and Fortune 1000.


  Gartner''s developer surface includes support, engineering blog, and 12 more developer resources.'
plans:
- name: Gartner Plans Pricing
  plan_count: 0
  slug: gartner-plans-pricing
press:
- date: '2026-05-25'
  title: Gartner Says Autonomous Business and AI Layoffs May ...
  url: https://www.gartner.com/en/newsroom/press-releases/2026-05-05-gartner-says-autonomous-business-and-artificial-intelligence-layoffs-may-create-budget-room-but-do-not-deliver-returns
- date: '2026-05-25'
  title: Newsroom, Announcements and Media Contacts
  url: https://www.gartner.com/en/newsroom
- date: '2026-05-25'
  title: Gartner Survey Reveals 80% of CEOs Say AI Will Force ...
  url: https://www.gartner.com/en/newsroom/press-releases/2026-04-23-gartner-survey-reveals-80-percent-of-ceos-say-artificial-intelligence-will-force-operational-capability-overhauls
- date: '2026-05-25'
  title: Gartner Predicts 40% of Enterprise Apps Will Feature Task- ...
  url: https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025
- date: '2026-05-25'
  title: Gartner is the world authority on AI
  url: https://www.gartner.com/en/ai
random_paper: 7
rate_limits:
- limit_count: 0
  name: Gartner Rate Limits
  slug: gartner-rate-limits
score:
  band: emerging
  composite: 22.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 7.1
    discoverability: 57.4
    operational_transparency: 10.5
  previous_composite: 22.0
  schema_version: 0.22.0
  scored_at: '2026-09-18'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/gartner/refs/heads/main/screenshots/gartner-2026-07-25T215450.png
security:
- kind: domain-security
  name: Gartner Domain Security
  slug: gartner-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Gartner Vulnerability Disclosure
  slug: gartner-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: gartner
tags:
- Research
- Advisory
- Analyst
- Enterprise
- Fortune 1000
website: https://www.gartner.com
---
