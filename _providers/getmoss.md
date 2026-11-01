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
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.getmoss.com/security
- group: agent
  href: https://artifacts.apis.io/getmoss/llms/getmoss-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getmoss-llms.txt
- group: auth
  href: https://artifacts.apis.io/getmoss/well-known/getmoss-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/getmoss-help-security.txt
- group: agent
  href: https://artifacts.apis.io/getmoss/well-known/getmoss-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/getmoss-well-known.yml
- group: other
  href: https://artifacts.apis.io/getmoss/hosts/getmoss-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getmoss-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://help.getmoss.com/en/?origin-page=en-us
- group: auth
  title: ''
  type: Security
  url: https://www.getmoss.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getmoss.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getmoss.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.getmoss.com/press
- group: start
  title: ''
  type: Login
  url: https://www.getmoss.com/welcome/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.getmoss.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://help.getmoss.com/nl/articles/11384907-kyc-onboarding-bij-moss
- group: docs
  title: ''
  type: Documentation
  url: https://developers.getmoss.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.getmoss.com/changelog/
- group: auth
  href: https://artifacts.apis.io/getmoss/security/getmoss-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/getmoss-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/getmoss/security/getmoss-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/getmoss-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/getmoss/security/getmoss-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getmoss-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getmoss.com/
coverage:
  checked: '2026-10-27'
  detail: The website returns HTML shells and 404 for OpenAPI endpoints, indicating docs are rendered via JavaScript without a machine‑readable spec.
  evidence:
  - status: 200
    url: https://www.getmoss.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: Moss provides a finance automation platform for European businesses, offering corporate cards, expense management, invoicing, and accounting integration. Their AI‑driven solution streamlines approvals, budgeting, and ERP synchronization, aiming to reduce invoice processing time and improve financial visibility across the organization.
image: https://images.prismic.io/mosswebsite/7ruXd5LwQJ3q01H2_HomeopengraphEU.png?auto=format,compress
layout: provider
modified: '2026-10-26'
name: Moss
nav: Providers
network: true
overview: 'Moss is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Automation, AI, and European.


  Moss'' developer surface includes support, pricing, changelog, getting-started guide, documentation, API reference, and 13 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 26.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 50.0
    operational_transparency: 26.3
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
- kind: domain-security
  name: Getmoss Domain Security
  slug: getmoss-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Getmoss Vulnerability Disclosure
  slug: getmoss-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Getmoss Trust Center
  slug: getmoss-trust-center
  summary_line: ISO 27001, GDPR
slug: getmoss
tags:
- Company
- Finance
- Automation
- AI
- European
website: https://www.getmoss.com/
---
