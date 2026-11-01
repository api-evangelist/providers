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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API documentation for GTM Helix guides and tools, as listed on the public guides page.
  name: GTM Helix Guides API
  slug: gtm-helix-guides-api
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/gtmhelix-com/security/gtmhelix-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/gtmhelix-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/gtmhelix-com/llms/gtmhelix-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gtmhelix-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/gtmhelix-com/well-known/gtmhelix-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/gtmhelix-com-security.txt
- group: agent
  href: https://artifacts.apis.io/gtmhelix-com/well-known/gtmhelix-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gtmhelix-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/gtmhelix-com/hosts/gtmhelix-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gtmhelix-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/gtmhelix-com/vendors/gtmhelix-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gtmhelix-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gtmhelix.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gtmhelix.com/privacy/
- group: auth
  href: https://artifacts.apis.io/gtmhelix-com/security/gtmhelix-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/gtmhelix-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/gtmhelix-com/security/gtmhelix-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gtmhelix-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gtmhelix.com/
- group: docs
  title: ''
  type: Documentation
  url: https://gtmhelix.com/guides/
- group: company
  title: ''
  type: About
  url: https://gtmhelix.com/about/
- group: company
  title: ''
  type: Blog
  url: https://gtmhelix.com/writing/
coverage:
  checked: '2026-10-29'
  detail: Guides page is a JavaScript‑rendered site with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://gtmhelix.com/guides/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Helix GTM Consulting, operating under the gtmhelix.com domain, offers a suite of free go‑to‑market tools and AI‑powered assistants for founders, marketers, and sales teams. Founded in 2022 in Bengaluru, the company leverages 24+ years of B2B experience to provide tools that run in Claude, ChatGPT, or a browser, alongside consulting services. The platform includes 81 tools, 33 skills, and multiple frameworks such as EPIC, IMPACT, and CRAFT, aiming to accelerate growth and improve GTM execution.
image: https://gtmhelix.com/og/agencies-sell-hours-we-ship-gtm-tools-v2.png
layout: provider
modified: '2026-10-29'
name: gtmhelix-com
nav: Providers
network: true
overview: 'gtmhelix-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include GTM, Consulting, AI, Tools, and B2B.


  gtmhelix-com''s developer surface includes documentation, engineering blog, and 12 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 14.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 10.5
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
  name: Gtmhelix Com Domain Security
  slug: gtmhelix-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Gtmhelix Com Vulnerability Disclosure
  slug: gtmhelix-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: gtmhelix-com
tags:
- GTM
- Consulting
- AI
- Tools
- B2B
website: https://gtmhelix.com/
---
