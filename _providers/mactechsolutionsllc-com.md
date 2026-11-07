---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Client portal provides deliverables, milestones, and compliance status for MacTech engagements.
  name: Client Portal
  slug: client-portal
artifact_total: 7
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.mactechsolutionsllc.com/trust
- group: other
  href: https://artifacts.apis.io/mactechsolutionsllc-com/hosts/mactechsolutionsllc-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mactechsolutionsllc-com-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://www.mactechsolutionsllc.com/auth/signin
- group: other
  title: ''
  type: Leadership
  url: https://www.mactechsolutionsllc.com/leadership
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.mactechsolutionsllc.com/
- group: auth
  href: https://artifacts.apis.io/mactechsolutionsllc-com/security/mactechsolutionsllc-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/mactechsolutionsllc-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/mactechsolutionsllc-com/security/mactechsolutionsllc-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mactechsolutionsllc-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mactechsolutionsllc.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mactechsolutionsllc.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mactechsolutionsllc.com/privacy
coverage:
  checked: '2026-10-29'
  detail: The API reference is behind a client portal login requiring authentication.
  evidence:
  - status: 200
    url: https://portal.mactechsolutionsllc.com/
  reason: customer-only-docs
  state: gated
created: '2026-10-29'
description: MacTech Solutions LLC is a veteran‑owned Small Disadvantaged Business (SDVOSB) specializing in federal cybersecurity and compliance services. It helps DoD primes and subcontractors achieve CMMC 2.0, NIST SP 800‑171, DFARS 252.204‑7012, and RMF readiness, offering expertise in Controlled Unclassified Information (CUI) protection, STIG compliance, and supply‑chain cyber risk management. Founded in 2024, the company provides consulting, assessment, and implementation services to secure mission‑critical programs and maintain authorization to operate (ATO) for defense industrial base contractors.
image: https://www.mactechsolutionsllc.com/mactech.png
layout: provider
modified: '2026-10-29'
name: mactechsolutionsllc-com
nav: Providers
network: true
overview: mactechsolutionsllc-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cybersecurity, CMMC, NIST 800-171, DFARS, and SDVOSB.
plans:
- name: Mactechsolutionsllc Com Plans Pricing
  plan_count: 0
  slug: mactechsolutionsllc-com-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Mactechsolutionsllc Com Rate Limits
  slug: mactechsolutionsllc-com-rate-limits
scopes:
- name: Mactechsolutionsllc Com Scopes
  scope_count: 0
  slug: mactechsolutionsllc-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.2
  facets:
    access_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 58.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 19.8
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/mactechsolutionsllc-com/mactechsolutionsllc-com-2026-11-03T135210.png
security:
- kind: authentication
  name: Mactechsolutionsllc Com Authentication
  slug: mactechsolutionsllc-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Mactechsolutionsllc Com Domain Security
  slug: mactechsolutionsllc-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Mactechsolutionsllc Com Trust Center
  slug: mactechsolutionsllc-com-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP, FIPS 140
slug: mactechsolutionsllc-com
tags:
- Cybersecurity
- CMMC
- NIST 800-171
- DFARS
- SDVOSB
- Compliance
website: https://mactechsolutionsllc.com/
---
