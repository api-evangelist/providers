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
artifact_total: 2
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cbtnuggets/refs/heads/main/plans/cbtnuggets-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cbtnuggets-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cbtnuggets/refs/heads/main/hosts/cbtnuggets-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cbtnuggets-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cbtnuggets/refs/heads/main/vendors/cbtnuggets-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cbtnuggets-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cbtnuggets/refs/heads/main/packages/cbtnuggets-packages.yml
  title: ''
  type: SDKs
  url: packages/cbtnuggets-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cbtnuggets/refs/heads/main/packages/cbtnuggets-packages.yml
  title: ''
  type: Packages
  url: packages/cbtnuggets-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cbtnuggets.com/terms
- group: auth
  title: ''
  type: Security
  url: https://www.cbtnuggets.com/blog/technology/security/oscp-vs-ceh
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cbtnuggets.com/privacy
- group: start
  title: ''
  type: Login
  url: https://www.cbtnuggets.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.cbtnuggets.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.cbtnuggets.com/blog/certifications/cisco/ccnp-labs-what-is-the-best-setup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cbtnuggets
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cbtnuggets/refs/heads/main/security/cbtnuggets-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cbtnuggets-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cbtnuggets.com
coverage:
  checked: '2026-10-07'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on the provider's documentation pages.
  evidence:
  - status: 200
    url: https://www.cbtnuggets.com/signup
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: CBT Nuggets provides online IT training videos and certification preparation courses. Founded in 2006, it offers a subscription platform with thousands of video tutorials, practice labs, and quizzes for a wide range of technology certifications. The service aims to help professionals save time and reduce effort while advancing their careers.
image: https://images.ctfassets.net/aoyx73g9h2pg/7p0zSyvujcjMm76N0yrb1K/be173416f6a264bd85487739d50cf774/CBT_Nuggets_Logo_man_with_lanyard_and_laptop_OG.png?fm=jpg&w=1024
layout: provider
modified: '2026-10-07'
name: Cbtnuggets
nav: Providers
network: true
overview: 'Cbtnuggets is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, IT, Training, Video, and Certification.


  Cbtnuggets'' developer surface includes engineering blog, getting-started guide, and 12 more developer resources.'
plans:
- name: Cbtnuggets Plans Pricing
  plan_count: 2
  slug: cbtnuggets-plans-pricing
random_paper: 0
score:
  band: emerging
  composite: 21.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 48.2
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cbtnuggets Domain Security
  slug: cbtnuggets-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cbtnuggets
tags:
- Company
- IT
- Training
- Video
- Certification
- Education
website: https://www.cbtnuggets.com
---
