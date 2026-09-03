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
  url: security/zeen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zeen.com
- group: start
  title: ''
  type: SignUp
  url: https://zeen.com/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zeen.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zeen.com/terms
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zeen-llms.txt
created: '2026-07-17'
description: Zeen is an AI-powered autonomous personal finance platform — a money copilot that connects to your financial accounts and uses background AI agents to manage money on your behalf. Its features include an interactive AI financial copilot that answers questions in real time, Guard (loss prevention that avoids overdraft fees and cancels unused subscriptions), Grow (yield optimization that moves idle balances to higher-interest accounts), and Guide (spending insights). As of mid-2026 Zeen is in pre-launch with a public waitlist. Zeen is backed by Cowboy Ventures and is tracked in the API Evangelist network as a company profile.
image: https://zeen.com/favicon/favicon.svg
layout: provider
modified: '2026-07-21'
name: Zeen
nav: Providers
network: true
overview: 'Zeen is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Fintech, Personal Finance, and Artificial Intelligence.


  Zeen''s developer surface includes signup flow and 5 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
security:
- kind: domain-security
  name: Zeen Domain Security
  slug: zeen-domain-security
  summary_line: TLSv1.3 · HSTS
slug: zeen
tags:
- Company
- Financial-Services
- Fintech
- Personal Finance
- Artificial Intelligence
- AI Agents
- Autonomous Finance
- Consumer
website: https://zeen.com
---
