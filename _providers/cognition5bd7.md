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
- description: API reference not publicly available; site renders a JavaScript shell with no machine‑readable docs.
  name: Cognition API
  slug: cognition-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: Compliance
  url: https://cognition.com/legal/security
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cognition5bd7/refs/heads/main/llms/cognition5bd7-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cognition5bd7-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cognition5bd7/refs/heads/main/hosts/cognition5bd7-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cognition5bd7-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cognition5bd7/refs/heads/main/vendors/cognition5bd7-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cognition5bd7-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://cognition.com/legal/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cognition.com/legal/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://cognition.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cognition5bd7/refs/heads/main/security/cognition5bd7-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cognition5bd7-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cognition5bd7/refs/heads/main/security/cognition5bd7-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cognition5bd7-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cognition5bd7/refs/heads/main/security/cognition5bd7-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cognition5bd7-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cognition.com
coverage:
  checked: '2026-10-09'
  detail: The Cognition website returns a JavaScript shell with no machine‑readable API documentation.
  evidence:
  - status: 200
    url: https://cognition.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-09'
description: Cognition5bd7 is an emerging AI-driven analytics platform that provides advanced data processing, machine learning models, and real-time insights for enterprises. The company focuses on delivering scalable solutions for data integration, predictive analytics, and decision support across various industries, aiming to empower businesses with actionable intelligence and automated workflows.
image: https://cognition.com/opengraph-image.jpg?opengraph-image.0mzhc99j4lsox.jpg
layout: provider
modified: '2026-10-09'
name: Cognition5bd7
nav: Providers
network: true
overview: 'Cognition5bd7 is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Data, Analytics, Platform, and Cognition.


  Cognition5bd7''s developer surface includes engineering blog and 10 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 14.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 64.3
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cognition5Bd7 Domain Security
  slug: cognition5bd7-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cognition5Bd7 Vulnerability Disclosure
  slug: cognition5bd7-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Cognition5Bd7 Trust Center
  slug: cognition5bd7-trust-center
  summary_line: SOC 2, ISO 27001
slug: cognition5bd7
tags:
- Artificial Intelligence
- Data
- Analytics
- Platform
- Cognition
website: https://cognition.com
---
