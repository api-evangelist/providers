---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 1
artifact_total: 3
common:
- group: other
  href: https://artifacts.apis.io/qolapps-org/hosts/qolapps-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/qolapps-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/qolapps-org/vendors/qolapps-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/qolapps-org-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://qolapps.org/terms/
- group: auth
  href: https://artifacts.apis.io/qolapps-org/security/qolapps-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/qolapps-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://qolapps.org/
- group: company
  title: ''
  type: Blog
  url: https://qolapps.org/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://qolapps.org/privacy/
- group: operate
  title: ''
  type: Support
  url: https://qolapps.org/contact/
coverage:
  checked: '2026-10-31'
  detail: The site provides only app listings and no developer documentation or API endpoints.
  evidence:
  - status: 200
    url: https://qolapps.org/
  reason: no-developer-program
  state: none
created: '2026-10-31'
description: QOL Apps is the brand of independent iOS developer Lav Chaudhary, who builds small, privacy‑first mobile applications. The portfolio includes iOS apps on the App Store and Android versions on Google Play, all released under the QOL Apps name. The site also hosts an AI tech blog, free web tools, and comprehensive privacy policies for each product, emphasizing on‑device processing and minimal data collection.
image: https://qolapps.org/assets/qol-apps-logo.jpg
layout: provider
modified: '2026-10-31'
name: qolapps-org
nav: Providers
network: true
overview: 'qolapps-org publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include iOS, Android, Privacy, Developer, and Apps.


  qolapps-org''s developer surface includes engineering blog, support, and 6 more developer resources.'
random_paper: 13
scopes:
- name: Qolapps Org Scopes
  scope_count: 0
  slug: qolapps-org-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Qolapps Org Authentication
  slug: qolapps-org-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Qolapps Org Domain Security
  slug: qolapps-org-domain-security
  summary_line: TLSv1.3
slug: qolapps-org
tags:
- iOS
- Android
- Privacy
- Developer
- Apps
website: https://qolapps.org/
---
