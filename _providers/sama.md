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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sama/refs/heads/main/hosts/sama-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sama-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sama/refs/heads/main/vendors/sama-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sama-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/sama/refs/heads/main/packages/sama-packages.yml
  title: ''
  type: SDKs
  url: packages/sama-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/sama/refs/heads/main/packages/sama-packages.yml
  title: ''
  type: Packages
  url: packages/sama-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sama.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sama.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.sama.com/news
- group: company
  title: ''
  type: Blog
  url: https://www.sama.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sama/refs/heads/main/security/sama-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sama-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sama.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.sama.com/primary-services
- group: start
  title: ''
  type: GettingStarted
  url: https://www.sama.com/why-sama
- group: operate
  title: ''
  type: Support
  url: https://www.sama.com/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://www.sama.com/contact-us
coverage:
  checked: '2026-10-12'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract found on api.sama.com despite probing common spec locations.
  evidence:
  - status: 404
    url: https://api.sama.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Sama is a data annotation and labeling company that provides a platform for AI developers to create high‑quality training data. Offering services such as image, video, 3D lidar, and text annotation, Sama supports foundation model training, computer vision, autonomous vehicles, and other AI applications. The company is B Corp certified and publishes impact reports, emphasizing ethical AI data practices.
image: https://cdn.prod.website-files.com/65844ee8089ad9744a76677c/66ce3c21da39854ea3bcab6a_sama.com%20genai%20meta%20tag%20image.png
layout: provider
modified: '2026-10-12'
name: Sama
nav: Providers
network: true
overview: 'Sama is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data-Annotation, Artificial Intelligence, B-Corp, and Training-Data.


  Sama''s developer surface includes engineering blog, documentation, getting-started guide, support, signup flow, and 9 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Sama Domain Security
  slug: sama-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sama
tags:
- Company
- Data-Annotation
- Artificial Intelligence
- B-Corp
- Training-Data
website: https://sama.com/
---
