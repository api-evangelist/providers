---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Teetra Com Agentic Access
  operation_count: 3
  slug: teetra-com-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- description: Teetra API — 149 operations.
  name: Teetra API
  slug: teetra-api
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/teetra-com/agentic-access/teetra-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/teetra-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/teetra-com/plans/teetra-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/teetra-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/teetra-com/rules/teetra-com-rules.yml
  title: ''
  type: Spectral
  url: rules/teetra-com-rules.yml
- group: design
  href: https://artifacts.apis.io/teetra-com/vocabulary/teetra-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/teetra-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/teetra-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/teetra-com/security/teetra-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/teetra-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/teetra-com/authentication/teetra-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/teetra-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/teetra-com/errors/teetra-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/teetra-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/teetra-com/conformance/teetra-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/teetra-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/teetra-com/llms/teetra-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/teetra-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/teetra-com/well-known/teetra-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/teetra-com-security.txt
- group: agent
  href: https://artifacts.apis.io/teetra-com/well-known/teetra-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/teetra-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/teetra-com/hosts/teetra-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/teetra-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/teetra-com/vendors/teetra-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/teetra-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/teetra-com/packages/teetra-com-packages.yml
  title: ''
  type: SDKs
  url: packages/teetra-com-packages.yml
- group: build
  href: https://artifacts.apis.io/teetra-com/packages/teetra-com-packages.yml
  title: ''
  type: Packages
  url: packages/teetra-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.teetra.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.teetra.com/privacy
- group: auth
  href: https://artifacts.apis.io/teetra-com/security/teetra-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/teetra-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/teetra-com/security/teetra-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/teetra-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://teetra.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.teetra.com/
- group: operate
  title: ''
  type: Support
  url: https://teetra.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://app.teetra.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.teetra.com/enroll
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://app.teetra.com/openapi.json
  - status: 401
    url: https://app.teetra.com/mcp
  - status: 200
    url: https://teetra.com/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: Teetra is a studio of AI‑first applications that enables API providers to monetize usage by AI assistants. Builders can list their APIs, set free trial budgets, and convert AI‑driven calls into paying customers, with all transactions routed through Teetra. The platform requires no code changes, no middleware, and offers secure key management, allowing providers to retain full control over their data while earning revenue only when paid. Teetra’s ecosystem includes properties such as Neemio, Didactum, Embryx, and Truant, and integrates with major AI assistants like Claude, ChatGPT, Gemini, and Copilot.
image: https://teetra.com/og-image.png
layout: provider
modified: '2026-10-31'
name: teetra-com
nav: Providers
network: true
overview: 'teetra-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Payments, API-Monetization, and Marketplace.


  The teetra-com catalog on APIs.io includes 1 Spectral governance ruleset.


  teetra-com''s developer surface includes authentication, support, pricing, signup flow, and 21 more developer resources.'
plans:
- name: Teetra Com Plans Pricing
  plan_count: 3
  slug: teetra-com-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Teetra Com Rate Limits
  slug: teetra-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: teetra-com API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: teetra-com-rules
score:
  band: developing
  composite: 41.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 68.5
    catalog_earned_first_party: 0.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 0.0
    developer_ergonomics: 39.8
    discoverability: 66.1
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 25.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Teetra Com Authentication
  slug: teetra-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Teetra Com Domain Security
  slug: teetra-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Teetra Com Vulnerability Disclosure
  slug: teetra-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: health-check
  slug: teetra-com-health-check
slug: teetra-com
tags:
- Company
- AI
- Payments
- API-Monetization
- Marketplace
- DeveloperTools
website: https://teetra.com/
---
