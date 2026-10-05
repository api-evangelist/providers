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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blended-technologies/refs/heads/main/hosts/blended-technologies-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blended-technologies-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blended-technologies/refs/heads/main/vendors/blended-technologies-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blended-technologies-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blended-technologies/refs/heads/main/security/blended-technologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blended-technologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.blendedtech.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blendedtech.com/
- group: company
  title: ''
  type: Blog
  url: https://www.blendedtech.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blendedtech.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blendedtech.com/terms-of-service
coverage:
  checked: '2026-09-29'
  detail: Documentation redirects to a JavaScript-rendered site with no machine-readable spec.
  evidence:
  - status: 307
    url: https://docs.blendedtech.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-29'
description: Blended Technologies provides modern winery management software that streamlines production, inventory, compliance, finance, and case goods for winemakers. Their platform automates repetitive tasks, offers real‑time insights, and integrates the entire winemaking process—from grape intake to bottling—into a single cloud‑based system, helping wineries improve efficiency and data‑driven decision making.
image: https://cdn.prod.website-files.com/671fbe17abadacf3dc0bf0dc/67239cd13e2d137d6da3dfdd_Blended%20OG%20image%20(1).jpg
layout: provider
modified: '2026-09-29'
name: Blended Technologies
nav: Providers
network: true
overview: 'Blended Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Winery, Software, Software-as-a-Service, and Production.


  Blended Technologies'' developer surface includes documentation, engineering blog, and 6 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blended Technologies Domain Security
  slug: blended-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: blended-technologies
tags:
- Company
- Winery
- Software
- Software-as-a-Service
- Production
website: https://www.blendedtech.com/
---
