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
- description: CreativeX provides a marketing analytics API (no public contract discovered).
  name: CreativeX API
  slug: creativex-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://trust.creativex.com/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/creativex/refs/heads/main/hosts/creativex-hosts.yml
  title: ''
  type: Hosts
  url: hosts/creativex-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/creativex/refs/heads/main/vendors/creativex-vendors.yml
  title: ''
  type: Vendors
  url: vendors/creativex-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.creativex.com/legal/terms
- group: operate
  title: ''
  type: Support
  url: https://support.creativex.com/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.creativex.com/legal/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.creativex.com/resources/press
- group: start
  title: ''
  type: Login
  url: https://www.creativex.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.creativex.com/resources/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/creativex/refs/heads/main/security/creativex-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/creativex-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/creativex/refs/heads/main/security/creativex-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/creativex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.creativex.com/
coverage:
  checked: '2026-10-11'
  detail: No public OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract found on the provider's hosts.
  evidence:
  - status: 404
    url: https://api.creativex.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-11'
description: CreativeX provides the foundation for data‑powered creative decisions, giving marketers a single source of truth to measure, optimize, and scale creative excellence. The platform unifies creative, content and media measurement, offering tools for creative quality, salience, lifecycle, and inclusive representation, helping brands improve ROI across channels.
image: https://cdn.prod.website-files.com/621d36527fa01265102ea2a5/680024684f793250dd020422_Slide%2016_9%20-%204-1.png
layout: provider
modified: '2026-10-11'
name: CreativeX
nav: Providers
network: true
overview: 'CreativeX is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Analytics, Creative, and Media.


  CreativeX''s developer surface includes support, engineering blog, and 10 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 17.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Creativex Domain Security
  slug: creativex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Creativex Trust Center
  slug: creativex-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR
slug: creativex
tags:
- Company
- Marketing
- Analytics
- Creative
- Media
website: https://www.creativex.com/
---
