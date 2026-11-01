---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 42.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 5
asyncapis:
- description: ''
  name: Lettermint Webhooks
  slug: lettermint-webhooks
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lettermint.co/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lettermint.co/privacy-policy
- group: commercial
  href: https://artifacts.apis.io/lettermint/plans/lettermint-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lettermint-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/lettermint/asyncapi/lettermint-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/lettermint-webhooks.yml
- group: operate
  href: https://artifacts.apis.io/lettermint/changelog/lettermint-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/lettermint-changelog.yml
- group: design
  href: https://artifacts.apis.io/lettermint/conventions/lettermint-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/lettermint-conventions.yml
- group: design
  href: https://artifacts.apis.io/lettermint/conventions/lettermint-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lettermint-conventions.yml
- group: start
  href: https://artifacts.apis.io/lettermint/sandbox/lettermint-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/lettermint-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/lettermint/security/lettermint-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/lettermint-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/lettermint/authentication/lettermint-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lettermint-authentication.yml
- group: agent
  href: https://artifacts.apis.io/lettermint/llms/lettermint-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lettermint-llms.txt
- group: auth
  href: https://artifacts.apis.io/lettermint/well-known/lettermint-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/lettermint-security.txt
- group: auth
  href: https://artifacts.apis.io/lettermint/well-known/lettermint-emailexpert-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/lettermint-emailexpert-security.txt
- group: auth
  href: https://artifacts.apis.io/lettermint/well-known/lettermint-bsky-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/lettermint-bsky-security.txt
- group: auth
  href: https://artifacts.apis.io/lettermint/well-known/lettermint-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/lettermint-app-security.txt
- group: agent
  href: https://artifacts.apis.io/lettermint/well-known/lettermint-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lettermint-well-known.yml
- group: other
  href: https://artifacts.apis.io/lettermint/hosts/lettermint-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lettermint-hosts.yml
- group: other
  href: https://artifacts.apis.io/lettermint/vendors/lettermint-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lettermint-vendors.yml
- group: build
  href: https://artifacts.apis.io/lettermint/packages/lettermint-packages.yml
  title: ''
  type: SDKs
  url: packages/lettermint-packages.yml
- group: build
  href: https://artifacts.apis.io/lettermint/packages/lettermint-packages.yml
  title: ''
  type: Packages
  url: packages/lettermint-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lettermint.co/
- group: start
  title: ''
  type: Sandbox
  url: https://lettermint.co/roadmap/sandbox
- group: operate
  title: ''
  type: Roadmap
  url: https://lettermint.co/roadmap
- group: start
  title: ''
  type: DeveloperPortal
  url: https://lettermint.co/for/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://lettermint.co/changelog
- group: auth
  href: https://artifacts.apis.io/lettermint/security/lettermint-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/lettermint-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/lettermint/security/lettermint-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lettermint-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lettermint.co/
- group: docs
  title: ''
  type: Documentation
  url: https://lettermint.co/docs
- group: docs
  title: ''
  type: APIReference
  url: https://lettermint.co/docs/api-reference/sending
- group: start
  title: ''
  type: GettingStarted
  url: https://lettermint.co/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://lettermint.co/knowledge-base
- group: company
  title: ''
  type: Blog
  url: https://lettermint.co/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://lettermint.co/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.lettermint.co/register
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/lettermint/workspace
created: '2026-10-26'
description: Lettermint is a European partner providing transactional email services, offering reliable delivery of transactional, broadcast, and inbound emails. Their platform includes SDKs for multiple languages, a CLI, and an MCP server for AI assistants. Lettermint is ISO/IEC 27001:2022 certified and GDPR compliant, ensuring secure and privacy‑focused email communications for developers and businesses across Europe.
image: https://lettermint.co/open-graph.jpg
layout: provider
modified: '2026-10-26'
name: Lettermint
nav: Providers
network: true
overview: 'Lettermint is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Email, Transactional, API, and European.


  The Lettermint catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Lettermint''s developer surface includes changelog, sandbox, authentication, documentation, API reference, getting-started guide, support, and 29 more developer resources.'
plans:
- name: Lettermint Plans Pricing
  plan_count: 25
  slug: lettermint-plans-pricing
random_paper: 16
score:
  band: developing
  composite: 53.8
  coverage:
    artifact_dirs: 13
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 76.2
    discoverability: 48.2
    operational_transparency: 55.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Lettermint Authentication
  slug: lettermint-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Lettermint Domain Security
  slug: lettermint-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Lettermint Vulnerability Disclosure
  slug: lettermint-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: lettermint
tags:
- Company
- Email
- Transactional
- API
- European
website: https://lettermint.co/
---
