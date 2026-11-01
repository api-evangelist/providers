---
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
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for Relume Publish, documented at the Relume Resources docs. Provides endpoints for managing sites, content, and publishing workflows.
  name: Relume Publish API
  slug: relume-publish-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/relume/plans/relume-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/relume-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/relume/security/relume-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/relume-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/relume/llms/relume-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/relume-llms.txt
- group: auth
  href: https://artifacts.apis.io/relume/well-known/relume-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/relume-security.txt
- group: auth
  href: https://artifacts.apis.io/relume/well-known/relume-relume-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/relume-relume-security.txt
- group: auth
  href: https://artifacts.apis.io/relume/well-known/relume-community-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/relume-community-security.txt
- group: agent
  href: https://artifacts.apis.io/relume/well-known/relume-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/relume-well-known.yml
- group: other
  href: https://artifacts.apis.io/relume/hosts/relume-hosts.yml
  title: ''
  type: Hosts
  url: hosts/relume-hosts.yml
- group: other
  href: https://artifacts.apis.io/relume/vendors/relume-vendors.yml
  title: ''
  type: Vendors
  url: vendors/relume-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.relume.ai/legal/terms
- group: operate
  title: ''
  type: Support
  url: https://www.relume.ai/support
- group: build
  title: ''
  type: SDKs
  url: https://www.relume.ai/libraries
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.relume.ai/legal/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.relume.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://www.relume.ai/app/login
- group: docs
  title: ''
  type: Documentation
  url: https://www.relume.ai/resources/publish/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.relume.ai/whats-new
- group: start
  title: ''
  type: GettingStarted
  url: https://www.relume.ai/resources/publish/doc/getting-started-with-relume-publish
- group: auth
  href: https://artifacts.apis.io/relume/security/relume-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/relume-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/relume/security/relume-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/relume-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://relume.ai/
coverage:
  checked: '2026-10-28'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable spec was found.
  evidence:
  - status: 200
    url: https://www.relume.ai/resources/publish/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: Relume is an AI-powered website builder focused on marketing sites. It leverages a component library used across over 2 million websites, allowing users to generate, customize, and publish professional sites via Relume or export them to Webflow, Figma, and React. The platform offers a free tier and paid plans starting at $14/month, emphasizing rapid AI-driven site creation, responsive design, and SEO-friendly content.
image: https://cdn.prod.website-files.com/6177739448baa66404ce1d9c/6a8660a8897b488119f6ed90_og-default-v1.png
layout: provider
modified: '2026-10-28'
name: Relume
nav: Providers
network: true
overview: 'Relume is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Website Builder, Marketing, and No-code.


  Relume''s developer surface includes support, pricing, documentation, changelog, getting-started guide, and 16 more developer resources.'
plans:
- name: Relume Plans Pricing
  plan_count: 5
  slug: relume-plans-pricing
random_paper: 2
score:
  band: thin
  composite: 31.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 57.1
    operational_transparency: 26.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Relume Domain Security
  slug: relume-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Relume Vulnerability Disclosure
  slug: relume-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: relume
tags:
- Company
- AI
- Website Builder
- Marketing
- No-code
website: https://relume.ai/
---
