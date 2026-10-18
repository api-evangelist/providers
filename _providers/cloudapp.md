---
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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API documentation and developer resources for Zight (formerly CloudApp).
  name: Zight API
  slug: zight-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cloudapp/refs/heads/main/plans/cloudapp-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cloudapp-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cloudapp/refs/heads/main/changelog/cloudapp-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cloudapp-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudapp/refs/heads/main/conformance/cloudapp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cloudapp-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudapp/refs/heads/main/llms/cloudapp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cloudapp-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudapp/refs/heads/main/well-known/cloudapp-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cloudapp-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudapp/refs/heads/main/well-known/cloudapp-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cloudapp-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudapp/refs/heads/main/hosts/cloudapp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloudapp-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudapp/refs/heads/main/vendors/cloudapp-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cloudapp-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.zight.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zight.com/legal/terms-of-service/
- group: operate
  title: ''
  type: Support
  url: https://support.zight.com/hc/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zight.com
- group: build
  title: ''
  type: SDKs
  url: https://zight.com/sdk/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zight.com/legal/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://zight.com/plans/
- group: company
  title: ''
  type: Newsroom
  url: https://zight.com/press
- group: start
  title: ''
  type: Login
  url: https://share.zight.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://zight.com/resource-type/guides/
- group: operate
  title: ''
  type: ChangeLog
  url: https://zight.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://zight.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://zight.com/use-cases/training-onboarding
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudapp/refs/heads/main/security/cloudapp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudapp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zight.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://zight.com/mcp
  - status: 403
    url: https://status.zight.com/mcp
  - status: 401
    url: https://support.zight.com/mcp
  - status: 200
    url: https://zight.com/
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-10-09'
description: CloudApp, now operating as Zight, provides a visual communication platform that enables teams to capture screenshots, screen recordings, and AI‑generated guides, then share them instantly via secure links. The service focuses on improving productivity, reducing meetings, and enhancing asynchronous collaboration for businesses of all sizes. Zight’s suite includes screen recorder, screenshot tool, AI‑assisted SOP generation, and integrations that streamline support, sales, and internal workflows.
image: https://zight.com/_astro/og-default.CDKHFpew_25xOdj.jpeg
layout: provider
modified: '2026-10-09'
name: CloudApp
nav: Providers
network: true
overview: 'CloudApp is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  CloudApp''s developer surface includes changelog, support, pricing, documentation, engineering blog, getting-started guide, and 17 more developer resources.'
plans:
- name: Cloudapp Plans Pricing
  plan_count: 4
  slug: cloudapp-plans-pricing
random_paper: 20
score:
  band: thin
  composite: 37.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 57.1
    operational_transparency: 31.6
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cloudapp Domain Security
  slug: cloudapp-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: cloudapp
tags:
- Company
website: https://zight.com/
---
