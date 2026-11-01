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
  score: 16.8
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/getviktor-com/plans/getviktor-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/getviktor-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/getviktor-com/changelog/getviktor-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/getviktor-com-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://viktor.com/security
- group: design
  href: https://artifacts.apis.io/getviktor-com/conformance/getviktor-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/getviktor-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/getviktor-com/llms/getviktor-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getviktor-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/getviktor-com/well-known/getviktor-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/getviktor-com-security.txt
- group: auth
  href: https://artifacts.apis.io/getviktor-com/well-known/getviktor-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/getviktor-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/getviktor-com/well-known/getviktor-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/getviktor-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/getviktor-com/hosts/getviktor-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getviktor-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/getviktor-com/vendors/getviktor-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/getviktor-com-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://viktor.com/help
- group: auth
  title: ''
  type: Security
  url: https://viktor.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://viktor.com/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://viktor.com/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://viktor.com/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://viktor.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://viktor.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://viktor.com/docs/getting-started
- group: auth
  href: https://artifacts.apis.io/getviktor-com/security/getviktor-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/getviktor-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/getviktor-com/security/getviktor-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/getviktor-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/getviktor-com/security/getviktor-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getviktor-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://viktor.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://api.viktor.com/mcp
  - status: 200
    url: https://getviktor.com/
  reason: partner-login
  state: gated
created: '2026-10-21'
description: Viktor is an AI employee that works in Slack and Microsoft Teams, helping teams automate reports, dashboards, spreadsheets, research, code, campaign changes and internal apps. It connects to over 9,800 tools and serves founders, operations, marketing, sales, finance, agencies, ecommerce and professional services firms. No per‑seat charges, approved by a human for sensitive actions.
image: https://viktor.com/assets/og/home-ai-employee.png
layout: provider
modified: '2026-10-21'
name: Viktor
nav: Providers
network: true
overview: 'Viktor is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Automation, Slack, and Microsoft Teams.


  Viktor''s developer surface includes changelog, support, pricing, documentation, engineering blog, getting-started guide, and 16 more developer resources.'
plans:
- name: Getviktor Com Plans Pricing
  plan_count: 34
  slug: getviktor-com-plans-pricing
random_paper: 11
score:
  band: thin
  composite: 31.9
  coverage:
    artifact_dirs: 12
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 68.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 48.2
    operational_transparency: 26.3
  provenance:
    conformance: first-party
    mcp: unknown
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
    score: 29.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Getviktor Com Domain Security
  slug: getviktor-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Getviktor Com Vulnerability Disclosure
  slug: getviktor-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Getviktor Com Trust Center
  slug: getviktor-com-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: getviktor-com
tags:
- Company
- AI
- Automation
- Slack
- Microsoft Teams
website: https://viktor.com/
---
