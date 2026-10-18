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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API documentation for CEIPAL ATS V2, covering authentication, endpoints, and webhook events.
  name: CEIPAL ATS API V2
  slug: ceipal-ats-api-v2
artifact_total: 4
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.ceipal.com/legal/security
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ceipal/refs/heads/main/conformance/ceipal-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ceipal-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ceipal/refs/heads/main/hosts/ceipal-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ceipal-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ceipal/refs/heads/main/vendors/ceipal-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ceipal-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://www.ceipal.com/support
- group: start
  title: ''
  type: SignUp
  url: https://www.ceipal.com/register
- group: auth
  title: ''
  type: Security
  url: https://www.ceipal.com/legal/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ceipal.com/legal/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.ceipal.com/news/whats-new
- group: start
  title: ''
  type: GettingStarted
  url: https://www.ceipal.com/staffing-agency-software/applicant-tracking-system/onboarding-software
- group: docs
  title: ''
  type: Documentation
  url: https://developer.ceipal.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ceipal/refs/heads/main/security/ceipal-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/ceipal-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ceipal/refs/heads/main/security/ceipal-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ceipal-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ceipal/refs/heads/main/security/ceipal-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ceipal-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ceipal.com/
coverage:
  checked: '2026-10-07'
  detail: Developer portal pages render via JavaScript and do not expose a machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://developer.ceipal.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-07'
description: Ceipal provides a unified talent platform that combines applicant tracking, vendor management, and workforce management with AI-driven sourcing, matching, and engagement. The solution serves staffing agencies, corporate recruiting teams, healthcare organizations, and global capability centers, offering modules for credentialing, invoicing, workflow automation, and analytics to accelerate hiring and improve talent lifecycle efficiency.
image: https://cdn.prod.website-files.com/673b1fe857bafc67dccfe030/68cbe0c791e1f0cbbf346194_Thumb_Homepage.webp
layout: provider
modified: '2026-10-07'
name: CEIPAL
nav: Providers
network: true
overview: 'CEIPAL is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Staffing, Recruiting, Software-as-a-Service, and Artificial Intelligence.


  CEIPAL''s developer surface includes support, signup flow, changelog, getting-started guide, documentation, and 10 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 25.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 39.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 26.3
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ceipal Domain Security
  slug: ceipal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ceipal Vulnerability Disclosure
  slug: ceipal-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Ceipal Trust Center
  slug: ceipal-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: ceipal
tags:
- Company
- Staffing
- Recruiting
- Software-as-a-Service
- Artificial Intelligence
website: https://www.ceipal.com/
---
