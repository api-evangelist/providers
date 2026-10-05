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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://appstorys.com/security
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/appstorys/refs/heads/main/llms/appstorys-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/appstorys-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/appstorys/refs/heads/main/well-known/appstorys-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/appstorys-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appstorys/refs/heads/main/hosts/appstorys-hosts.yml
  title: ''
  type: Hosts
  url: hosts/appstorys-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appstorys/refs/heads/main/vendors/appstorys-vendors.yml
  title: ''
  type: Vendors
  url: vendors/appstorys-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://appstorys.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://appstorys.com/privacypolicy
- group: company
  title: ''
  type: Blog
  url: https://appstorys.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.appstorys.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/appstorys/refs/heads/main/security/appstorys-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/appstorys-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/appstorys/refs/heads/main/security/appstorys-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appstorys-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://appstorys.com
coverage:
  checked: 2026-09-25
  detail: Access to OpenAPI spec at https://api.appstorys.com/openapi.json returns HTTP 403, indicating a partner login wall.
  evidence:
  - status: 403
    url: https://api.appstorys.com/openapi.json
  reason: partner-login
  state: gated
created: '2026-09-25'
description: AppStorys is a leading in‑app engagement platform that helps brands increase user stickiness and drive growth through interactive stories, push notifications, email, SMS, and WhatsApp marketing. Founded to empower consumer products and fintech companies, AppStorys powers over 370+ apps worldwide, offering tools such as picture‑in‑picture videos, banners, quizzes, and analytics to boost feature adoption and user engagement. The company has raised $5 million to expand globally and continues to innovate in mobile and web user experiences.
image: https://appstorys.com/og-image.jpg
layout: provider
modified: '2026-09-25'
name: AppStorys
nav: Providers
network: true
overview: 'AppStorys is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, In-App Engagement, Mobile Marketing, User Analytics, and Fintech.


  AppStorys'' developer surface includes engineering blog, documentation, and 10 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 55.4
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Appstorys Domain Security
  slug: appstorys-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Appstorys Trust Center
  slug: appstorys-trust-center
  summary_line: SOC 2, GDPR
slug: appstorys
tags:
- Company
- In-App Engagement
- Mobile Marketing
- User Analytics
- Fintech
website: https://appstorys.com
---
