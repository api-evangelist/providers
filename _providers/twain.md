---
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
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/twain/plans/twain-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/twain-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/twain/security/twain-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/twain-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/twain/authentication/twain-authentication.yml
  title: ''
  type: Authentication
  url: authentication/twain-authentication.yml
- group: design
  href: https://artifacts.apis.io/twain/conformance/twain-conformance.yml
  title: ''
  type: Conformance
  url: conformance/twain-conformance.yml
- group: agent
  href: https://artifacts.apis.io/twain/llms/twain-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/twain-llms.txt
- group: auth
  href: https://artifacts.apis.io/twain/well-known/twain-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/twain-security.txt
- group: auth
  href: https://artifacts.apis.io/twain/well-known/twain-intercom-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/twain-intercom-security.txt
- group: auth
  href: https://artifacts.apis.io/twain/well-known/twain-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/twain-api-security.txt
- group: agent
  href: https://artifacts.apis.io/twain/well-known/twain-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/twain-well-known.yml
- group: other
  href: https://artifacts.apis.io/twain/hosts/twain-hosts.yml
  title: ''
  type: Hosts
  url: hosts/twain-hosts.yml
- group: auth
  href: https://artifacts.apis.io/twain/security/twain-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/twain-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/twain/security/twain-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/twain-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.twain.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.twain.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.twain.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://www.twain.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.twain.ai/onboarding
- group: operate
  title: ''
  type: Support
  url: https://intercom.help/usetwain/
- group: company
  title: ''
  type: Blog
  url: https://www.twain.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.twain.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.twain.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.twain.ai/privacy
- group: start
  title: ''
  type: SignUp
  url: https://www.twain.ai/onboarding?authMode=sign-up
coverage:
  checked: '2026-10-24'
  detail: Homepage loads a JavaScript SPA with no machine‑readable OpenAPI spec discovered.
  evidence:
  - status: 200
    url: https://www.twain.ai/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-23'
description: Twain provides an AI‑powered outreach platform that helps sales and marketing teams craft highly personalized cold‑email campaigns at scale. By combining contextual research with natural‑language generation, Twain creates unique, human‑like messages for each prospect, boosting reply rates and reducing campaign preparation time. The service includes features such as automated prospect research, email drafting, A/B testing, and performance analytics, aiming to improve outbound outreach efficiency and effectiveness for B2B companies.
image: https://www.twain.ai/opengraph/default.png?v=20260724
layout: provider
modified: '2026-10-23'
name: Twain
nav: Providers
network: true
overview: 'Twain is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Outreach, Sales, and Marketing.


  Twain''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 16 more developer resources.'
plans:
- name: Twain Plans Pricing
  plan_count: 7
  slug: twain-plans-pricing
random_paper: 19
score:
  band: thin
  composite: 37.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Twain Authentication
  slug: twain-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Twain Domain Security
  slug: twain-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Twain Vulnerability Disclosure
  slug: twain-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: twain
tags:
- Company
- AI
- Outreach
- Sales
- Marketing
website: https://www.twain.ai/
---
