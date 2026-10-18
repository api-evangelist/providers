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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://trust.sitoo.com/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sitoo/refs/heads/main/conformance/sitoo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sitoo-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sitoo/refs/heads/main/llms/sitoo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sitoo-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sitoo/refs/heads/main/well-known/sitoo-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sitoo-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sitoo/refs/heads/main/well-known/sitoo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sitoo-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sitoo/refs/heads/main/hosts/sitoo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sitoo-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sitoo/refs/heads/main/vendors/sitoo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sitoo-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://sitoo.com/about/release-notes
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sitoo
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sitoo/refs/heads/main/security/sitoo-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/sitoo-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sitoo/refs/heads/main/security/sitoo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sitoo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sitoo.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.sitoo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.sitoo.com/api-reference/overview
- group: docs
  title: ''
  type: APIReference
  url: https://developer.sitoo.com/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.sitoo.com/sign-up
- group: operate
  title: ''
  type: Support
  url: https://sitoo.com/contact
- group: company
  title: ''
  type: Blog
  url: https://sitoo.com/articles
- group: commercial
  title: ''
  type: Pricing
  url: https://sitoo.com/solution/pos?hsLang=en
- group: start
  title: ''
  type: SignUp
  url: https://developer.sitoo.com/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sitoo.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sitoo.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sitoo.com/
coverage:
  checked: '2026-10-15'
  detail: Developer documentation pages are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://developer.sitoo.com/api-reference/overview
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-15'
description: Sitoo provides a Retail POS and Unified Commerce Platform, delivering point‑of‑sale solutions for Android and iOS, composable technology, inventory management, self‑checkout, and RFID capabilities. The company serves retailers across fashion, beauty, accessories, furniture, jewelry, luxury, sports, and more, offering integrated commerce experiences and partner ecosystems. Sitoo’s platform is MACH‑certified, enabling flexible, API‑first integrations for modern retail operations.
image: https://sitoo.com/hubfs/01%20Website%20pages/01%20Images/02%20Heros%20and%20Backgrounds/light-bg-woman-yellow-hoodie-tablet.webp
layout: provider
modified: '2026-10-15'
name: Sitoo
nav: Providers
network: true
overview: 'Sitoo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Retail, Point-of-Sale, Commerce, Platform, and Company.


  Sitoo''s developer surface includes changelog, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 16 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 35.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 55.4
    operational_transparency: 36.8
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Sitoo Domain Security
  slug: sitoo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Sitoo Trust Center
  slug: sitoo-trust-center
  summary_line: ISO 27001
slug: sitoo
tags:
- Retail
- Point-of-Sale
- Commerce
- Platform
- Company
website: https://sitoo.com/
---
