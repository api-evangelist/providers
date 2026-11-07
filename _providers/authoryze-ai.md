---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
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
  score: 21.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Authoryze MCP payment infrastructure, documented at https://authoryze.ai/docs
  name: Authoryze API
  slug: authoryze-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/authoryze-ai/well-known/authoryze-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/authoryze-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/authoryze-ai/hosts/authoryze-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/authoryze-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/authoryze-ai/vendors/authoryze-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/authoryze-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/authoryze-ai/security/authoryze-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/authoryze-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://authoryze.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://authoryze.ai/docs
- group: company
  title: ''
  type: Blog
  url: https://authoryze.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://authoryze.ai/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://authoryze.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://authoryze.ai/privacy
- group: start
  title: ''
  type: SignUp
  url: https://authoryze.ai/sign-up
- group: start
  title: ''
  type: Login
  url: https://authoryze.ai/sign-in
- group: start
  title: ''
  type: GettingStarted
  url: https://authoryze.ai/sign-up
coverage:
  checked: '2026-11-02'
  detail: Docs page renders via JavaScript, no machine‑readable spec found.
  evidence:
  - status: 200
    url: https://authoryze.ai/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: Authoryze provides MCP-native payment infrastructure that lets AI agents make purchases using single-use virtual cards. It offers spending limits, merchant approvals, audit trails, and team budgeting, supporting integrations with OpenAI, Claude, and other AI services. Plans start at $39.99/month for up to 100 transactions, with per-transaction pricing for higher volumes. The platform emphasizes security by never exposing real credit card details to agents.
image: https://authoryze.ai/opengraph-image?1d4ce8518cd66045
layout: provider
modified: '2026-11-02'
name: Authoryze
nav: Providers
network: true
overview: 'Authoryze is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Payments, Artificial Intelligence, Security, and Platform.


  Authoryze''s developer surface includes documentation, engineering blog, support, signup flow, getting-started guide, and 8 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.8
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 17.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 13.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Authoryze Ai Domain Security
  slug: authoryze-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: authoryze-ai
tags:
- Fintech
- Payments
- Artificial Intelligence
- Security
- Platform
website: https://authoryze.ai/
---
