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
  href: https://raw.githubusercontent.com/api-evangelist/biofourmispteltd/refs/heads/main/hosts/biofourmispteltd-hosts.yml
  title: ''
  type: Hosts
  url: hosts/biofourmispteltd-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://biofourmis.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://biofourmis.com/privacy-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/biofourmispteltd/refs/heads/main/security/biofourmispteltd-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/biofourmispteltd-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://biofourmis.com
coverage:
  checked: '2026-09-28'
  detail: No developer program or API documentation is publicly available.
  evidence:
  - status: 200
    url: https://biofourmis.com
  reason: no-developer-program
  state: none
created: '2026-09-28'
description: Biofourmis is a digital health company that leverages AI and advanced analytics to deliver personalized, real‑time care solutions. It provides a platform for remote patient monitoring, predictive health insights, and in‑home care services, helping healthcare providers improve outcomes and reduce costs. The company focuses on integrating wearable data, clinical data, and AI models to enable proactive health management across chronic disease, post‑acute care, and wellness programs.
image: https://cdn.prod.website-files.com/6410ded0f8074bcf431541cf/641dcbd86f41fde1b426a0ce_BF_home_header_01.webp
layout: provider
modified: '2026-09-28'
name: Biofourmispteltd
nav: Providers
network: true
overview: Biofourmispteltd is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Digital Health, Artificial Intelligence, Remote Monitoring, Healthcare, and Platform.
random_paper: 2
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.3
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Biofourmispteltd Domain Security
  slug: biofourmispteltd-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: biofourmispteltd
tags:
- Digital Health
- Artificial Intelligence
- Remote Monitoring
- Healthcare
- Platform
website: https://biofourmis.com
---
