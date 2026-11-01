---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 5.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/unchained-capital-com/plans/unchained-capital-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/unchained-capital-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/unchained-capital-com/authentication/unchained-capital-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/unchained-capital-com-authentication.yml
- group: agent
  href: https://artifacts.apis.io/unchained-capital-com/llms/unchained-capital-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/unchained-capital-com-llms.txt
- group: other
  href: https://artifacts.apis.io/unchained-capital-com/hosts/unchained-capital-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/unchained-capital-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/unchained-capital-com/vendors/unchained-capital-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/unchained-capital-com-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.unchained.com/trust
- group: auth
  title: ''
  type: Security
  url: https://www.unchained.com/blog-tag/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unchained-capital
- group: start
  title: ''
  type: GettingStarted
  url: https://help.unchained.com/what-can-i-expect-from-my-concierge-onboarding
- group: docs
  title: ''
  type: Documentation
  url: https://help.unchained.com/
- group: auth
  href: https://artifacts.apis.io/unchained-capital-com/security/unchained-capital-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/unchained-capital-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://unchained-capital.com
- group: company
  title: ''
  type: Blog
  url: https://www.unchained.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.unchained.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.unchained.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.unchained.com/privacy
coverage:
  checked: '2026-10-29'
  detail: Docs at https://help.unchained.com render via JavaScript and provide no machine‑readable spec.
  evidence:
  - status: 200
    url: https://help.unchained.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Unchained Capital provides Bitcoin financial services, offering collaborative custody, vaults, trust services, and investment products for individuals and institutions. Their platform includes personal vaults, signature premium services, Bitcoin IRA, loans, donor‑advised funds, and wealth advisory, aiming to make secure Bitcoin ownership accessible and manageable for families and fiduciaries.
layout: provider
modified: '2026-10-29'
name: Unchained Capital
nav: Providers
network: true
overview: 'Unchained Capital is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Bitcoin, Financial Services, Custody, Investment, and Trust.


  Unchained Capital''s developer surface includes authentication, getting-started guide, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Unchained Capital Com Plans Pricing
  plan_count: 13
  slug: unchained-capital-com-plans-pricing
random_paper: 22
score:
  band: thin
  composite: 29.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 71.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 44.6
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Unchained Capital Com Authentication
  slug: unchained-capital-com-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Unchained Capital Com Domain Security
  slug: unchained-capital-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: unchained-capital-com
tags:
- Bitcoin
- Financial Services
- Custody
- Investment
- Trust
website: https://unchained-capital.com
---
