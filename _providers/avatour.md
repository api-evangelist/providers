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
- description: Avatour provides API endpoints for its 360° video collaboration platform. Documentation pages were found but no machine‑readable contract could be retrieved.
  name: Avatour API
  slug: avatour-api
artifact_total: 4
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/avatour/refs/heads/main/plans/avatour-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/avatour-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/avatour/refs/heads/main/conformance/avatour-conformance.yml
  title: ''
  type: Conformance
  url: conformance/avatour-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avatour/refs/heads/main/hosts/avatour-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avatour-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avatour/refs/heads/main/vendors/avatour-vendors.yml
  title: ''
  type: Vendors
  url: vendors/avatour-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://avatour.com/legal/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://avatour.com/support
- group: auth
  title: ''
  type: Security
  url: https://avatour.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://avatour.com/legal/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://avatour.com/webshop/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://avatour.com/support-category/release-notes
- group: start
  title: ''
  type: GettingStarted
  url: https://avatour.com/quickstart
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avatour/refs/heads/main/security/avatour-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/avatour-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avatour/refs/heads/main/security/avatour-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avatour-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://avatour.com/
created: '2026-09-26'
description: Avatour provides a 360° video collaboration platform that enables teams to conduct remote inspections, virtual tours, training, and continuous improvement without travel. Their solution offers live 360° walkthroughs, recorded site reviews, AI‑powered reports, and integrates hardware kits for various industries such as construction, manufacturing, logistics, retail, and real estate. The platform aims to improve safety, efficiency, and cost savings by delivering immersive, real‑time visual collaboration.
image: https://cdn.prod.website-files.com/6578f6bdfadb289687b7a7ad/658c81c577289556c2da3815_avatour-logo-dark.svg
layout: provider
modified: '2026-09-26'
name: AVATOUR
nav: Providers
network: true
overview: 'AVATOUR publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, VideoCollaboration, RemoteInspection, Virtual Tours, and Artificial Intelligence.


  AVATOUR''s developer surface includes support, pricing, changelog, getting-started guide, and 10 more developer resources.'
plans:
- name: Avatour Plans Pricing
  plan_count: 8
  slug: avatour-plans-pricing
random_paper: 0
score:
  band: thin
  composite: 28.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 26.3
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
    score: 22.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Avatour Domain Security
  slug: avatour-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Avatour Vulnerability Disclosure
  slug: avatour-vulnerability-disclosure
  summary_line: disclosure policy published
slug: avatour
tags:
- Company
- VideoCollaboration
- RemoteInspection
- Virtual Tours
- Artificial Intelligence
website: https://avatour.com/
---
