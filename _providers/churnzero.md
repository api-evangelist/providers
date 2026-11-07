---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/churnzero/vendors/churnzero-vendors.yml
  title: ''
  type: Vendors
  url: vendors/churnzero-vendors.yml
- group: auth
  title: ''
  type: Compliance
  url: https://compliance.churnzero.com:443/
- group: agent
  href: https://artifacts.apis.io/churnzero/well-known/churnzero-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/churnzero-well-known.yml
- group: other
  href: https://artifacts.apis.io/churnzero/hosts/churnzero-hosts.yml
  title: ''
  type: Hosts
  url: hosts/churnzero-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://support.churnzero.com/hc/en-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.churnzero.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://churnzero.com/privacy-center/
- group: start
  title: ''
  type: Login
  url: https://app.churnzero.com/Login
- group: company
  title: ''
  type: Blog
  url: https://churnzero.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://churnzero.com/solutions-onboarding/
- group: auth
  href: https://artifacts.apis.io/churnzero/security/churnzero-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/churnzero-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/churnzero/security/churnzero-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/churnzero-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://churnzero.com/
coverage:
  checked: '2026-10-26'
  detail: ChurnZero website renders documentation via JavaScript, preventing machine-readable access.
  evidence:
  - status: 200
    url: https://churnzero.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: ChurnZero provides AI‑powered customer success software that helps businesses grow revenue by reducing churn, improving onboarding, and increasing customer engagement. The platform offers digital customer success tools, AI agents, analytics, and integrations to enable teams to retain and expand accounts, automate workflows, and gain actionable insights across the customer lifecycle.
image: https://churnzero.com/wp-content/uploads/2025/01/ChurnZero-Newsroom-Logo-Feat.png
layout: provider
modified: '2026-10-26'
name: ChurnZero
nav: Providers
network: true
overview: 'ChurnZero is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Customer Success, Artificial Intelligence, Software-as-a-Service, and Analytics.


  ChurnZero''s developer surface includes support, engineering blog, getting-started guide, and 10 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.7
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 18.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/churnzero/churnzero-2026-11-03T124130.png
security:
- kind: domain-security
  name: Churnzero Domain Security
  slug: churnzero-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Churnzero Trust Center
  slug: churnzero-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: churnzero
tags:
- Company
- Customer Success
- Artificial Intelligence
- Software-as-a-Service
- Analytics
website: https://churnzero.com/
---
