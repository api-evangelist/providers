---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 4.5
  scored_at: '2026-08-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/legal-and-general-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/legal-and-general-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/Legal-and-General/canopy/blob/master/docs/SECURITY.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/legal-and-general-packages.yml
- group: design
  title: ''
  type: Components
  url: components/legal-and-general-components.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/legal-and-general-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/legal-and-general-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://github.com/Legal-and-General/canopy/blob/master/docs/BREAKING_CHANGES.md
- group: design
  title: ''
  type: Conformance
  url: conformance/legal-and-general-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/legal-and-general-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.legalandgeneral.com/
- group: company
  title: ''
  type: CorporateWebsite
  url: https://group.legalandgeneral.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Legal-and-General
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Legal-and-General/canopy
- group: company
  title: ''
  type: Blog
  url: https://group.legalandgeneral.com/en/newsroom/press-releases
- group: start
  title: ''
  type: Login
  url: https://www.legalandgeneral.com/log-in/
- group: operate
  title: ''
  type: Support
  url: https://www.legalandgeneral.com/contact-us/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.legalandgeneral.com/help/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.legalandgeneral.com/privacy-notice/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.legalandgeneral.com/legal-information/
- group: other
  title: ''
  type: Accessibility
  url: https://www.legalandgeneral.com/accessibility/
created: '2026-07-25'
description: 'Legal & General Group plc is a FTSE 100 United Kingdom life insurer, retirement and institutional asset manager headquartered in London and regulated by the FCA and PRA. Its lines of business are life and protection insurance (term life, critical illness, income protection), workplace and individual pensions, annuities and bulk-purchase annuity/pension risk transfer, equity release through Legal & General Home Finance, and asset management through Legal & General Investment Management. It is a life and health carrier rather than a general insurer, and it distributes almost entirely through regulated intermediaries — financial advisers, mortgage brokers and employee-benefit consultants — rather than direct-to-developer. Its API posture reflects that distribution model honestly: Legal & General publishes NO public, self-serve developer portal, no public API reference, and no downloadable OpenAPI or Swagger definition. No developer.legalandgeneral.com, developers, docs, or api
  subdomain resolves in DNS, and /developers, /api, /developer, /partners and /integrations all return HTTP 404 on the primary site. Every documented Legal & General API is a bilateral, partner-gated integration announced by the counterparty rather than published by Legal & General — real-time equity release quotation, KFI and application APIs wired into Iress "The Exchange", Air Sourcing and the Advise Wise platform, a Mortgage Club integration with Kensington Mortgages, and adviser-facing protection quote-and-apply through OLP Connect. Adviser identity and messaging run on the UK''s Origo rails — Unipass digital certificates, Unipass Letter of Authority and Origo Track My Apps — which is the UK life and pensions analogue of ACORD; no ACORD, AL3, ACORD XML or NGDS reference appears anywhere in Legal & General''s public surface. The only public Legal & General code is the Canopy design system on GitHub — an Apache-2.0 Angular component library shipped through GitHub Packages, with dated
  semver release notes, a published breaking-change policy, a repository security policy, and 84 installable agent skills (69 component best-practice skills and 15 per-major migration skills) that work with GitHub Copilot, Claude Code and Cursor. That makes Legal & General agent-native on the front end and completely closed on the API. This record exists to measure that split accurately: a large carrier whose integration surface is entirely intermediary-gated and invisible from outside a login wall.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Legal & General
nav: Providers
network: true
overview: 'Legal & General is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, United Kingdom, Life Insurance, Health Insurance, and Employee Benefits.


  Legal & General''s developer surface includes changelog, engineering blog, support, and 19 more developer resources.'
random_paper: 66
score:
  band: emerging
  composite: 25.2
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 13.0
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 39.5
  previous_composite: 25.2
  provenance:
    conformance: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/legal-and-general/refs/heads/main/screenshots/legal-and-general-2026-07-25T224825.png
security:
- kind: domain-security
  name: Legal And General Domain Security
  slug: legal-and-general-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Legal And General Vulnerability Disclosure
  slug: legal-and-general-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: legal-and-general
tags:
- Insurance
- United Kingdom
- Life Insurance
- Health Insurance
- Employee Benefits
- Pensions
- Annuities
- Asset Management
- Underwriting
- Carrier
- Broker
- Partner Gated
- No Public API
- Design System
- Agent Skills
- Open Source
website: https://www.legalandgeneral.com/
---
