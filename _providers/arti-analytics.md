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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arti-analytics/refs/heads/main/hosts/arti-analytics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arti-analytics-hosts.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.artianalytics.com/company/trust-center
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arti-analytics/refs/heads/main/security/arti-analytics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arti-analytics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.artianalytics.com/
- group: company
  title: ''
  type: AboutUs
  url: https://www.artianalytics.com/company/about-us
- group: company
  title: ''
  type: Careers
  url: https://www.artianalytics.com/company/careers
- group: company
  title: ''
  type: Investors
  url: https://www.artianalytics.com/company/investors
- group: company
  title: ''
  type: Newsroom
  url: https://www.artianalytics.com/company/newsroom
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.artianalytics.com/company/privacy-policy
coverage:
  checked: 2026-09-26
  detail: No OpenAPI or other machine-readable spec found; attempts to fetch common spec URLs returned 404.
  evidence:
  - status: 404
    url: https://api.artianalytics.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: ARTI Analytics provides an enterprise AI platform offering solutions such as AI security & governance, DSML model development, and AI applications. Their flagship product ARTI Dominion acts as a control layer to enforce policy across models, agents, and tools in real time, delivering audit‑proof records. The company also delivers custom AI models, data science pipelines, and consulting services to help enterprises adopt trustworthy AI at scale.
image: https://artianalytics.com/assets/social/arti-social-preview-v1.jpg
layout: provider
modified: '2026-09-26'
name: ARTI Analytics
nav: Providers
network: true
overview: ARTI Analytics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Enterprise, Platform, and Security.
random_paper: 15
score:
  band: minimal
  composite: 8.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Arti Analytics Domain Security
  slug: arti-analytics-domain-security
  summary_line: TLSv1.3 · HSTS
slug: arti-analytics
tags:
- Company
- Artificial Intelligence
- Enterprise
- Platform
- Security
website: https://www.artianalytics.com/
---
