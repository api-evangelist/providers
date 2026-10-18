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
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.9
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Brightidea Developer Portal provides API documentation for the Brightidea innovation management platform.
  name: Brightidea API
  slug: brightidea-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.brightidea.com/security/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brightidea/refs/heads/main/well-known/brightidea-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/brightidea-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/brightidea/refs/heads/main/well-known/brightidea-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brightidea-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brightidea/refs/heads/main/hosts/brightidea-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brightidea-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brightidea/refs/heads/main/vendors/brightidea-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brightidea-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.brightidea.com/integrations/webhooks/
- group: operate
  title: ''
  type: StatusPage
  url: http://status.brightidea.com/
- group: auth
  title: ''
  type: Security
  url: https://www.brightidea.com/security/
- group: company
  title: ''
  type: Newsroom
  url: https://www.brightidea.com/news/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.brightidea.com/_documentation
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brightidea/refs/heads/main/security/brightidea-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/brightidea-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brightidea/refs/heads/main/security/brightidea-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/brightidea-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brightidea/refs/heads/main/security/brightidea-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brightidea-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.brightidea.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.brightidea.com/resources/
- group: company
  title: ''
  type: Blog
  url: https://www.brightidea.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.brightidea.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.brightidea.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brightidea.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.brightidea.com/pricing/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.brightidea.com/guide/idea-management/what-is-idea-management/
coverage:
  checked: '2026-10-06'
  detail: Developer portal redirects to a login page requiring partner credentials.
  evidence:
  - status: 200
    url: https://developer.brightidea.com
  reason: partner-login
  state: gated
created: '2026-10-06'
description: Brightidea provides an innovation management software platform that helps organizations capture ideas, run crowdsourcing challenges, manage hackathons, and drive company‑wide transformation. Their solutions enable collaborative innovation, idea evaluation, and portfolio management for enterprises seeking to foster a culture of continuous improvement and measurable outcomes.
layout: provider
modified: '2026-10-06'
name: Brightidea
nav: Providers
network: true
overview: 'Brightidea is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Innovation, Software, Collaboration, and Enterprise.


  Brightidea''s developer surface includes documentation, engineering blog, support, pricing, getting-started guide, and 16 more developer resources.'
random_paper: 9
score:
  band: thin
  composite: 28.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 55.4
    operational_transparency: 34.2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brightidea Domain Security
  slug: brightidea-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Brightidea Vulnerability Disclosure
  slug: brightidea-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Brightidea Trust Center
  slug: brightidea-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017
slug: brightidea
tags:
- Company
- Innovation
- Software
- Collaboration
- Enterprise
website: https://www.brightidea.com
---
