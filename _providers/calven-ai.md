---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
common:
- group: other
  href: https://artifacts.apis.io/calven-ai/vendors/calven-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/calven-ai-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/calven-ai/plans/calven-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/calven-ai-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://calven.ai/security
- group: agent
  href: https://artifacts.apis.io/calven-ai/llms/calven-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/calven-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/calven-ai/well-known/calven-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/calven-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/calven-ai/well-known/calven-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/calven-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/calven-ai/hosts/calven-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/calven-ai-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://calven.ai/terms
- group: operate
  title: ''
  type: Support
  url: https://calven.ai/support
- group: start
  title: ''
  type: SignUp
  url: https://app.calven.ai/sign-up
- group: auth
  title: ''
  type: Security
  url: https://calven.ai/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://calven.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://calven.ai/pricing
- group: other
  title: ''
  type: Leadership
  url: https://calven.ai/solutions/leadership
- group: auth
  href: https://artifacts.apis.io/calven-ai/security/calven-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/calven-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/calven-ai/security/calven-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/calven-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/calven-ai/security/calven-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/calven-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://calven.ai/
coverage:
  checked: '2026-11-04'
  detail: No OpenAPI, GraphQL, AsyncAPI, or other machine-readable contract was found; only HTML docs are available.
  evidence:
  - status: 401
    url: https://api.calven.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Calven AI is an AI product marketing platform for B2B teams. It offers nine autonomous agents that perform market research, competitive intelligence, win/loss analysis, ICP and persona development, positioning, and messaging. Users own the strategy while the agents handle execution, enabling efficient product marketing at scale.
image: https://calven.ai/images/brand/logo.svg
layout: provider
modified: '2026-11-04'
name: Calven AI
nav: Providers
network: true
overview: 'Calven AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Marketing, Platform, B2B, and Automation.


  Calven AI''s developer surface includes support, signup flow, pricing, and 15 more developer resources.'
plans:
- name: Calven Ai Plans Pricing
  plan_count: 3
  slug: calven-ai-plans-pricing
random_paper: 16
score:
  band: emerging
  composite: 20.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 49.1
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Calven Ai Domain Security
  slug: calven-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Calven Ai Vulnerability Disclosure
  slug: calven-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Calven Ai Trust Center
  slug: calven-ai-trust-center
  summary_line: SOC 2, GDPR
slug: calven-ai
tags:
- Artificial Intelligence
- Marketing
- Platform
- B2B
- Automation
website: https://calven.ai/
---
