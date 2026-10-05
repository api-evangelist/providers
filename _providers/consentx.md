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
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: ConsentX provides a JavaScript embed API for consent banners; no REST endpoints or OpenAPI spec were found.
  name: ConsentX API
  slug: consentx-api
artifact_total: 5
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/consentx/refs/heads/main/plans/consentx-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/consentx-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.consentx.io/trust
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/consentx/refs/heads/main/conformance/consentx-conformance.yml
  title: ''
  type: Conformance
  url: conformance/consentx-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/consentx/refs/heads/main/llms/consentx-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/consentx-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/consentx/refs/heads/main/well-known/consentx-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/consentx-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/consentx/refs/heads/main/well-known/consentx-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/consentx-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/consentx/refs/heads/main/hosts/consentx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/consentx-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/consentx/refs/heads/main/vendors/consentx-vendors.yml
  title: ''
  type: Vendors
  url: vendors/consentx-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.consentx.io/terms
- group: auth
  title: ''
  type: Security
  url: https://www.consentx.io/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.consentx.io/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.consentx.io/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.consentx.io/solutions/media
- group: start
  title: ''
  type: Login
  url: https://app.consentx.io/auth/login
- group: company
  title: ''
  type: Blog
  url: https://www.consentx.io/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/consentx/refs/heads/main/security/consentx-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/consentx-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/consentx/refs/heads/main/security/consentx-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/consentx-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/consentx/refs/heads/main/security/consentx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/consentx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.consentx.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.consentx.io/integrations
coverage:
  detail: Documentation pages are JavaScript-rendered and provide only an embed script, no machine‑readable API spec.
  evidence:
  - status: 200
    url: https://www.consentx.io/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-02'
description: ConsentX provides a consent management platform (CMP) that helps websites comply with privacy regulations such as GDPR, CCPA, DPDPA, LGPD, and others. It offers cookie consent banners, prior‑script blocking, consent records, audit evidence, region‑rule engine, and integrations with Google Consent Mode, Global Privacy Control, and AI‑driven privacy scanning. The platform includes tools for data residency, DSAR handling, and a suite of compliance features across multiple jurisdictions.
image: https://www.consentx.io/api/og?title=ConsentX%3A+consent+management+platform+for+GDPR%2C+CCPA+and+DPDPA
layout: provider
modified: '2026-10-02'
name: ConsentX
nav: Providers
network: true
overview: 'ConsentX publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, CMP, GDPR, CCPA, and Privacy.


  ConsentX''s developer surface includes pricing, engineering blog, documentation, and 17 more developer resources.'
plans:
- name: Consentx Plans Pricing
  plan_count: 4
  slug: consentx-plans-pricing
random_paper: 2
score:
  band: thin
  composite: 33.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 66.1
    operational_transparency: 10.5
  provenance:
    conformance: first-party
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
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Consentx Domain Security
  slug: consentx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Consentx Vulnerability Disclosure
  slug: consentx-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Consentx Trust Center
  slug: consentx-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: consentx
tags:
- Company
- CMP
- GDPR
- CCPA
- Privacy
- Consent Management
website: https://www.consentx.io/
---
