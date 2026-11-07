---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
  score: 18.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Remote shell and long‑running job execution API as described in the OpenAPI spec.
  name: AI Commander Remote Shell API
  slug: ai-commander-remote-shell-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/aicommander-dev/plans/aicommander-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aicommander-dev-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/aicommander-dev/changelog/aicommander-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aicommander-dev-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://aicommander.dev/security/#reporting
- group: auth
  href: https://artifacts.apis.io/aicommander-dev/authentication/aicommander-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aicommander-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/aicommander-dev/conformance/aicommander-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aicommander-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aicommander-dev/llms/aicommander-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aicommander-dev-llms.txt
- group: auth
  href: https://artifacts.apis.io/aicommander-dev/well-known/aicommander-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aicommander-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/aicommander-dev/well-known/aicommander-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aicommander-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/aicommander-dev/hosts/aicommander-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aicommander-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/aicommander-dev/vendors/aicommander-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aicommander-dev-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aicommander.dev/privacy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://aicommander.dev/changelog/
- group: auth
  href: https://artifacts.apis.io/aicommander-dev/security/aicommander-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aicommander-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aicommander-dev/security/aicommander-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aicommander-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aicommander.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://aicommander.dev/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://aicommander.dev/pricing/
- group: start
  title: ''
  type: GettingStarted
  url: https://aicommander.dev/start.md
- group: operate
  title: ''
  type: Support
  url: https://aicommander.dev/security/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://aicommander.dev/openapi.json
  - status: 401
    url: https://aicommander.dev/mcp
  - status: 200
    url: https://aicommander.dev/
  reason: partner-login
  state: gated
created: '2026-11-01'
description: AI Commander provides remote shell and long‑running job execution for AI agents on user‑owned machines. It supports Claude, ChatGPT, Codex, Grok and other models, offering outbound‑only connections, encrypted traffic, and file transfer capabilities. Users can install agents on macOS, Windows or Linux, obtain a session code, and let the AI run commands, scripts, or training jobs without exposing inbound ports. Free tier supports up to 10 machines; paid plans add more machines and file transfer.
image: https://aicommander.dev/og-image.png
layout: provider
modified: '2026-11-01'
name: AI Commander
nav: Providers
network: true
overview: 'AI Commander is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, RemoteShell, Machine Learning, Automation, and Cloud.


  AI Commander''s developer surface includes changelog, authentication, documentation, pricing, getting-started guide, support, and 13 more developer resources.'
plans:
- name: Aicommander Dev Plans Pricing
  plan_count: 2
  slug: aicommander-dev-plans-pricing
random_paper: 4
score:
  band: emerging
  composite: 21.3
  coverage:
    artifact_dirs: 12
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.7
  facets:
    access_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 25.0
    discoverability: 66.1
    operational_transparency: 13.2
  previous_composite: 28.0
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aicommander Dev Authentication
  slug: aicommander-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Aicommander Dev Domain Security
  slug: aicommander-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Aicommander Dev Vulnerability Disclosure
  slug: aicommander-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: aicommander-dev
tags:
- Artificial Intelligence
- RemoteShell
- Machine Learning
- Automation
- Cloud
website: https://aicommander.dev/
---
