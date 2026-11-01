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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.goodweek.com/en/security
- group: auth
  href: https://artifacts.apis.io/goodweek/well-known/goodweek-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/goodweek-help-security.txt
- group: agent
  href: https://artifacts.apis.io/goodweek/well-known/goodweek-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/goodweek-well-known.yml
- group: other
  href: https://artifacts.apis.io/goodweek/hosts/goodweek-hosts.yml
  title: ''
  type: Hosts
  url: hosts/goodweek-hosts.yml
- group: other
  href: https://artifacts.apis.io/goodweek/vendors/goodweek-vendors.yml
  title: ''
  type: Vendors
  url: vendors/goodweek-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.goodweek.com/en/terms
- group: operate
  title: ''
  type: Support
  url: https://help.goodweek.com/en/
- group: auth
  title: ''
  type: Security
  url: https://www.goodweek.com/en/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.goodweek.com/en/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.goodweek.com/en/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://help.goodweek.com/en/collections/19728702-getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://help.goodweek.com/
- group: auth
  href: https://artifacts.apis.io/goodweek/security/goodweek-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/goodweek-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/goodweek/security/goodweek-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/goodweek-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/goodweek/security/goodweek-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/goodweek-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://goodweek.com
coverage:
  checked: '2026-10-24'
  detail: The provider's documentation is a JavaScript‑rendered site with no machine‑readable API spec discovered.
  evidence:
  - status: 200
    url: https://www.goodweek.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-24'
description: Goodweek provides an AI management platform that enables enterprises to securely deploy, monitor, and govern AI models across their organization. The platform offers centralized model storage, usage analytics, policy enforcement, and integration capabilities, helping teams work faster, smarter, and safer with AI. It serves various use cases from inbox filtering to financial forecasting, emphasizing visibility, control, and compliance for AI deployments.
image: https://www.goodweek.com/en/opengraph-image?a435c65ffadf7868
layout: provider
modified: '2026-10-24'
name: Goodweek
nav: Providers
network: true
overview: 'Goodweek is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Platform, Governance, and Enterprise.


  Goodweek''s developer surface includes support, engineering blog, getting-started guide, documentation, and 12 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 20.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Goodweek Domain Security
  slug: goodweek-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Goodweek Vulnerability Disclosure
  slug: goodweek-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Goodweek Trust Center
  slug: goodweek-trust-center
  summary_line: SOC 2, GDPR
slug: goodweek
tags:
- Company
- AI
- Platform
- Governance
- Enterprise
website: https://goodweek.com
---
