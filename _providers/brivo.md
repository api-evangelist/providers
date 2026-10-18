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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Brivo API provides capabilities to build physical security applications for access control, video surveillance, and visitor management.
  name: Brivo API
  slug: brivo-api
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brivo/refs/heads/main/well-known/brivo-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/brivo-status-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brivo/refs/heads/main/security/brivo-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/brivo-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/brivo/refs/heads/main/llms/brivo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brivo-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brivo/refs/heads/main/well-known/brivo-careers-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/brivo-careers-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/brivo/refs/heads/main/well-known/brivo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brivo-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brivo/refs/heads/main/hosts/brivo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brivo-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brivo/refs/heads/main/vendors/brivo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brivo-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://explore.brivo.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://support.brivo.com/s/?language=en_US
- group: operate
  title: ''
  type: StatusPage
  url: https://status.brivo.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brivo.com/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://explore.brivo.com/about/news/
- group: start
  title: ''
  type: Login
  url: https://explore.brivo.com/login/
- group: company
  title: ''
  type: Blog
  url: https://www.brivo.com/resources/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.brivo.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.brivolabs.com/files/favicon.png
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/brivo
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brivo/refs/heads/main/security/brivo-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/brivo-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brivo/refs/heads/main/security/brivo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brivo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.brivo.com/
coverage:
  checked: '2026-10-06'
  detail: Access to OpenAPI spec at apidocs.brivo.com is blocked with HTTP 403, indicating a partner login requirement.
  evidence:
  - status: 403
    url: https://apidocs.brivo.com/openapi.json
  reason: partner-login
  state: gated
created: '2026-10-06'
description: Brivo provides cloud‑based physical security solutions, including access control, video surveillance, visitor management, and intrusion detection. Their platform integrates with various hardware and software, offering unified management for commercial and multifamily properties. Brivo’s services focus on secure, scalable, and remote‑managed security infrastructure for enterprises.
image: https://www.brivo.com/wp-content/uploads/2026/07/Brivo-Twitter-1280x720-px-1.jpg
layout: provider
modified: '2026-10-06'
name: Brivo
nav: Providers
network: true
overview: 'Brivo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Access Control, VideoSurveillance, and Cloud.


  Brivo''s developer surface includes support, engineering blog, documentation, and 17 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 24.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 66.1
    operational_transparency: 31.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brivo Domain Security
  slug: brivo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Brivo Vulnerability Disclosure
  slug: brivo-vulnerability-disclosure
  summary_line: no policy recorded
slug: brivo
tags:
- Company
- Security
- Access Control
- VideoSurveillance
- Cloud
website: https://www.brivo.com/
---
