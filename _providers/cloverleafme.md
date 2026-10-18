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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cloverleafme/refs/heads/main/changelog/cloverleafme-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cloverleafme-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.cloverleaf.me/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloverleafme/refs/heads/main/conformance/cloverleafme-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cloverleafme-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloverleafme/refs/heads/main/llms/cloverleafme-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cloverleafme-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloverleafme/refs/heads/main/well-known/cloverleafme-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cloverleafme-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloverleafme/refs/heads/main/well-known/cloverleafme-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cloverleafme-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloverleafme/refs/heads/main/hosts/cloverleafme-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloverleafme-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloverleafme/refs/heads/main/vendors/cloverleafme-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cloverleafme-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloverleaf.me/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cloverleaf.me/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://cloverleaf.me/pricing
- group: other
  title: ''
  type: Leadership
  url: https://cloverleaf.me/about/team/
- group: start
  title: ''
  type: GettingStarted
  url: http://help.cloverleaf.me/en/articles/9212013-enterprise-plan-organization-admin-getting-started-guide
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloverleafme/refs/heads/main/security/cloverleafme-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cloverleafme-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloverleafme/refs/heads/main/security/cloverleafme-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloverleafme-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cloverleaf.me
- group: docs
  title: ''
  type: Documentation
  url: https://help.cloverleaf.me/en/
- group: company
  title: ''
  type: Blog
  url: https://cloverleaf.me/blog/
coverage:
  checked: '2026-10-09'
  detail: OpenAPI endpoints on api.cloverleaf.me return 404, and the help center provides no machine‑readable contract.
  evidence:
  - status: 404
    url: https://api.cloverleaf.me/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-09'
description: Cloverleaf is a team performance platform that provides AI‑driven coaching, behavioral assessments, and analytics for people teams. Founded in 2017, it serves over 45,000 teams worldwide, offering integrations across workplace tools and patented technology to improve collaboration and leadership development.
image: https://cloverleaf.me/wp-content/uploads/2026/09/Cloverleaf_Feature-Image.jpg
layout: provider
modified: '2026-10-09'
name: Cloverleafme
nav: Providers
network: true
overview: 'Cloverleafme is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Team Performance, AI Coaching, Behavioral Assessment, Workplace Integration, and Leadership Development.


  Cloverleafme''s developer surface includes changelog, pricing, getting-started guide, documentation, engineering blog, and 13 more developer resources.'
random_paper: 15
score:
  band: thin
  composite: 26.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
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
  name: Cloverleafme Domain Security
  slug: cloverleafme-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cloverleafme Trust Center
  slug: cloverleafme-trust-center
  summary_line: SOC 2, ISO 27001
slug: cloverleafme
tags:
- Team Performance
- AI Coaching
- Behavioral Assessment
- Workplace Integration
- Leadership Development
- Company
website: https://cloverleaf.me
---
