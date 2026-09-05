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
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/rilla-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rilla-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: https://app.rilla.com/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/rilla-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rilla-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rilla-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.rilla.com
- group: start
  title: ''
  type: Login
  url: https://app.rilla.com/
- group: company
  title: ''
  type: Blog
  url: https://www.rilla.com/learn/rilla-labs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rillavoice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rilla.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rilla.com/terms-and-conditions
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.rilla.com/changelog
coverage:
  checked: '2026-08-14'
  detail: Rilla's production API is the private backend of its own apps — every path under https://api.rillavoice.com/api/v1/ returns HTTP 401 "Invalid Token" and requires an active tenant session — and Rilla publishes no developer portal, reference or spec anywhere on rilla.com to read instead.
  evidence:
  - status: 401
    url: https://api.rillavoice.com/api/v1/
  - status: 401
    url: https://api.rillavoice.com/api/v1/openapi.json
  - status: 403
    url: https://api.apirilla.com/openapi.json
  - status: 404
    url: https://www.rilla.com/llms.txt
  - status: 200
    url: https://app.rilla.com/.well-known/security.txt
  reason: customer-only-docs
  state: gated
created: '2026-07-17'
description: Rilla is an AI conversation-intelligence and coaching platform built for in-person and outside sales teams. Reps record their face-to-face customer conversations, and Rilla transcribes and analyzes them so managers can run virtual "ridealongs" and deliver targeted, data-driven coaching at scale. The platform surfaces talk patterns, objection handling, and outcome analytics across thousands of field conversations to help teams raise close rates, increase ticket size, and speed up rep ramp. Rilla is a GV (Google Ventures) portfolio company in the AI sector. Rilla runs a real production API — api.rillavoice.com/api/v1/, the private backend of its web and mobile apps, which answers every path with 401 Invalid Token — plus an AWS API Gateway webhook receiver its partner SPOTIO documents, but it publishes no developer portal, reference, SDK, or machine-readable specification of any kind, and its CRM integrations are delivered by consuming the Merge unified API rather than by exposing
  a contract. This record captures its public web identity, the RFC 9116 security.txt it serves from app.rilla.com, and live domain-security and well-known probes.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rilla.png
layout: provider
modified: '2026-08-14'
name: Rilla
nav: Providers
network: true
overview: 'Rilla is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Conversation Intelligence, Sales, and Coaching.


  Rilla''s developer surface includes engineering blog, changelog, and 11 more developer resources.'
plans:
- name: Rilla Plans Pricing
  plan_count: 0
  slug: rilla-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Rilla Rate Limits
  slug: rilla-rate-limits
score:
  band: emerging
  composite: 14.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 14.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rilla/refs/heads/main/screenshots/rilla-2026-09-02T153836.png
security:
- kind: domain-security
  name: Rilla Domain Security
  slug: rilla-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Rilla Vulnerability Disclosure
  slug: rilla-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: rilla
tags:
- Company
- Artificial Intelligence
- Conversation Intelligence
- Sales
- Coaching
- Sales Enablement
- Speech Analytics
- Machine-Learning
website: https://www.rilla.com
---
