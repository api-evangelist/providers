---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Deploy HTML or a built site to a live HTTPS URL via the aft.page platform.
  name: aft.page API
  slug: aft-page-api
- baseURL: https://api.aft.page
  baseurl_source: declared
  description: Deploy HTML or a built site to a live HTTPS URL. Cloud for small software — no account, no cloud setup.
  name: aft.page API API
  slug: aft-page-api-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/aft-page/rules/aft-page-rules.yml
  title: ''
  type: Spectral
  url: rules/aft-page-rules.yml
- group: design
  href: https://artifacts.apis.io/aft-page/vocabulary/aft-page-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aft-page-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/aft-page/conformance/aft-page-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aft-page-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/aft-page/plans/aft-page-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aft-page-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/aft-page/cli/aft-page-cli.yml
  title: ''
  type: CLI
  url: cli/aft-page-cli.yml
- group: operate
  href: https://artifacts.apis.io/aft-page/changelog/aft-page-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aft-page-changelog.yml
- group: auth
  href: https://artifacts.apis.io/aft-page/security/aft-page-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/aft-page-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/aft-page/errors/aft-page-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aft-page-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/aft-page/llms/aft-page-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aft-page-llms.txt
- group: auth
  href: https://artifacts.apis.io/aft-page/well-known/aft-page-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aft-page-security.txt
- group: agent
  href: https://artifacts.apis.io/aft-page/well-known/aft-page-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aft-page-well-known.yml
- group: other
  href: https://artifacts.apis.io/aft-page/hosts/aft-page-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aft-page-hosts.yml
- group: other
  href: https://artifacts.apis.io/aft-page/vendors/aft-page-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aft-page-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aft.page
- group: start
  title: ''
  type: Login
  url: https://aft.page/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://aft.page/changelog
- group: company
  title: ''
  type: Blog
  url: https://aft.page/blog/deploy-static-site-without-vercel-netlify-or-cloudflare-pages/
- group: docs
  title: ''
  type: APIReference
  url: https://aft.page/llms.txt
- group: auth
  href: https://artifacts.apis.io/aft-page/security/aft-page-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aft-page-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aft-page/security/aft-page-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aft-page-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aft.page/
- group: docs
  title: ''
  type: Documentation
  url: https://aft.page/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://aft.page/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aft.page/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aft.page/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aft.page/acceptable-use/
created: '2026-10-31'
description: aft.page is a platform that lets users create live, shareable URLs for AI‑generated projects with a single command. It offers a CLI to deploy folders or zip files, integrates with popular AI tools like Claude, Codex, Cursor, and Replit, and provides free hosting with custom domain support. The service emphasizes zero‑account deployment, instant sharing, and versioned updates, targeting developers and AI‑assisted creators looking for quick, low‑friction web publishing.
image: https://aft.page/og.png
layout: provider
modified: '2026-10-31'
name: aft.page
nav: Providers
network: true
overview: 'aft.page publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API API, and 1 more. Tagged areas include Artificial Intelligence, Hosting, CLI, Deployment, and Low‑friction.


  The aft.page catalog on APIs.io includes 1 Spectral governance ruleset.


  aft.page''s developer surface includes CLI, changelog, engineering blog, API reference, documentation, pricing, support, and 19 more developer resources.'
plans:
- name: Aft Page Plans Pricing
  plan_count: 3
  slug: aft-page-plans-pricing
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: aft.page API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: aft-page-rules
score:
  band: thin
  composite: 36.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.5
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 35.5
    developer_ergonomics: 19.0
    discoverability: 66.1
    operational_transparency: 26.3
  previous_composite: 46.2
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aft Page Domain Security
  slug: aft-page-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aft Page Vulnerability Disclosure
  slug: aft-page-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: aft-page
tags:
- Artificial Intelligence
- Hosting
- CLI
- Deployment
- Low‑friction
website: https://aft.page/
---
