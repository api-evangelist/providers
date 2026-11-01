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
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Elvex provides an API for its AI agent platform
  name: Elvex API
  slug: elvex-api
artifact_total: 4
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.elvex.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.elvex.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.elvex.com/security
- group: agent
  href: https://artifacts.apis.io/elvex/llms/elvex-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/elvex-llms.txt
- group: agent
  href: https://artifacts.apis.io/elvex/well-known/elvex-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/elvex-well-known.yml
- group: other
  href: https://artifacts.apis.io/elvex/hosts/elvex-hosts.yml
  title: ''
  type: Hosts
  url: hosts/elvex-hosts.yml
- group: other
  href: https://artifacts.apis.io/elvex/vendors/elvex-vendors.yml
  title: ''
  type: Vendors
  url: vendors/elvex-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.elvex.com/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.elvex.com/solutions/industry/media
- group: docs
  title: ''
  type: APIReference
  url: https://elvex.readme.io/reference/generate_text_response_v0_apps__assistant_id__versions__version__text_generate_post
- group: auth
  href: https://artifacts.apis.io/elvex/security/elvex-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/elvex-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/elvex/security/elvex-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/elvex-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/elvex/security/elvex-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/elvex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.elvex.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.elvex.com/platform
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.elvex.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://www.elvex.com/platform/guide
- group: operate
  title: ''
  type: Support
  url: https://www.elvex.com/resources
- group: company
  title: ''
  type: Blog
  url: https://www.elvex.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.elvex.com/pricing
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/elvex/workspace
coverage:
  checked: '2026-10-20'
  detail: Developer portal redirects to a JavaScript‑rendered site with no OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://www.elvex.com/developers
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-20'
description: Elvex provides an enterprise AI agent platform that enables teams across various functions—such as IT, HR, operations, marketing, and sales—to build, share, and control AI-driven agents. The platform offers a library of pre‑built agents, customizable integrations, security controls, and tools for rapid deployment, allowing organizations to automate workflows, enhance decision‑making, and improve productivity. Elvex’s solutions cater to industries including technology, publishing, insurance, consulting, legal, financial services, healthcare, and media, delivering a comprehensive AI‑powered experience for modern enterprises.
image: https://cdn.prod.website-files.com/6866a8f63ad698a595db92cc/6866b2c539c8e6ea08447bc2_B41yc2htQqZ8lJtAO0qPho76ZG0.png
layout: provider
modified: '2026-10-20'
name: elvex
nav: Providers
network: true
overview: 'elvex is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Enterprise, Platform, Automation, and Integration.


  elvex''s developer surface includes API reference, documentation, getting-started guide, support, engineering blog, pricing, and 15 more developer resources.'
random_paper: 20
score:
  band: thin
  composite: 28.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 58.9
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
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
- kind: domain-security
  name: Elvex Domain Security
  slug: elvex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Elvex Vulnerability Disclosure
  slug: elvex-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Elvex Trust Center
  slug: elvex-trust-center
  summary_line: SOC 2, HIPAA
slug: elvex
tags:
- AI
- Enterprise
- Platform
- Automation
- Integration
- Company
website: https://www.elvex.com/
---
