---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API reference not publicly documented; no machine-readable contract discovered.
  name: AI Interview Agents API
  slug: ai-interview-agents-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/aiinterviewagents-com/plans/aiinterviewagents-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aiinterviewagents-com-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.aiinterviewagents.com/security
- group: agent
  href: https://artifacts.apis.io/aiinterviewagents-com/llms/aiinterviewagents-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aiinterviewagents-com-llms.txt
- group: other
  href: https://artifacts.apis.io/aiinterviewagents-com/hosts/aiinterviewagents-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aiinterviewagents-com-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://www.aiinterviewagents.com/security
- group: other
  title: ''
  type: Leadership
  url: https://www.aiinterviewagents.com/interview-questions/leadership
- group: auth
  href: https://artifacts.apis.io/aiinterviewagents-com/security/aiinterviewagents-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/aiinterviewagents-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/aiinterviewagents-com/security/aiinterviewagents-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiinterviewagents-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aiinterviewagents.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aiinterviewagents.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aiinterviewagents.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aiinterviewagents.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.aiinterviewagents.com/blog
coverage:
  checked: '2026-11-01'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, or other contract was found.
  evidence:
  - status: 200
    url: https://www.aiinterviewagents.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AI Interview Agents provides AI-powered interview tools for recruiters and small agencies, including AI interviewers, video interview software, resume screening, candidate location checks, and career page builders. Their platform helps automate applicant qualification, interview highlights, and resume analysis, offering free and paid plans for scaling hiring needs.
image: https://www.aiinterviewagents.com/og-image.jpg
layout: provider
modified: '2026-11-01'
name: AI Interview Agents
nav: Providers
network: true
overview: 'AI Interview Agents is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Interviews, Recruiter Tools, Candidate Screening, and Video Interview.


  AI Interview Agents'' developer surface includes pricing, engineering blog, and 11 more developer resources.'
plans:
- name: Aiinterviewagents Com Plans Pricing
  plan_count: 2
  slug: aiinterviewagents-com-plans-pricing
random_paper: 13
score:
  band: emerging
  composite: 15.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 48.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 49.1
    operational_transparency: 5.3
  previous_composite: 21.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aiinterviewagents Com Domain Security
  slug: aiinterviewagents-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Aiinterviewagents Com Trust Center
  slug: aiinterviewagents-com-trust-center
  summary_line: SOC 2, ISO 27001
slug: aiinterviewagents-com
tags:
- AI Interviews
- Recruiter Tools
- Candidate Screening
- Video Interview
website: https://www.aiinterviewagents.com/
---
