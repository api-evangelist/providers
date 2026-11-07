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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for managing healthcare staffing and shift scheduling.
  name: Clipboard Health API
  slug: clipboard-health-api
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/clipboardhealth-com/security/clipboardhealth-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/clipboardhealth-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/clipboardhealth-com/well-known/clipboardhealth-com-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clipboardhealth-com-www-security.txt
- group: agent
  href: https://artifacts.apis.io/clipboardhealth-com/well-known/clipboardhealth-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clipboardhealth-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/clipboardhealth-com/hosts/clipboardhealth-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clipboardhealth-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/clipboardhealth-com/vendors/clipboardhealth-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clipboardhealth-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clipboard.com/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://www.clipboard.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clipboard.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.clipboard.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.clipboard.com/press
- group: company
  title: ''
  type: Blog
  url: https://www.clipboard.com/resources/blog
- group: auth
  href: https://artifacts.apis.io/clipboardhealth-com/security/clipboardhealth-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/clipboardhealth-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/clipboardhealth-com/security/clipboardhealth-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clipboardhealth-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://clipboardhealth.com
coverage:
  checked: '2026-10-26'
  detail: Documentation site renders via JavaScript, preventing machine-readable contract discovery.
  evidence:
  - status: 200
    url: https://www.clipboard.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-25'
description: Clipboard Health provides an on-demand staffing platform that connects healthcare facilities with qualified professionals such as nurses, therapists, and support staff. The service enables facilities to post shifts quickly, offering hourly rates without fees for posting or canceling, and ensures rapid coverage with most shifts filled within an hour. Clipboard Health verifies background checks, licenses, and certifications of its workforce, and offers tools for facilities to manage staffing, view credentials, and export audit records. The platform emphasizes flexibility, allowing last‑minute coverage and supporting a wide range of roles across regions.
image: https://www.clipboard.com/og-link-preview.webp
layout: provider
modified: '2026-10-25'
name: Clipboard Health
nav: Providers
network: true
overview: 'Clipboard Health is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Staffing, On-Demand, Platform, and Workforce.


  Clipboard Health''s developer surface includes support, pricing, engineering blog, and 11 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 58.0
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 15.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/clipboardhealth-com/clipboardhealth-com-2026-11-03T124441.png
security:
- kind: domain-security
  name: Clipboardhealth Com Domain Security
  slug: clipboardhealth-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Clipboardhealth Com Vulnerability Disclosure
  slug: clipboardhealth-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: clipboardhealth-com
tags:
- Healthcare
- Staffing
- On-Demand
- Platform
- Workforce
website: http://clipboardhealth.com
---
