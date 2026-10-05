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
api_count: 1
apis:
- description: API for BrandYourself services
  name: BrandYourself API
  slug: brandyourself-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brandyourself/refs/heads/main/hosts/brandyourself-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brandyourself-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brandyourself/refs/heads/main/vendors/brandyourself-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brandyourself-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://brandyourself.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brandyourself.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://brandyourself.com/press
- group: start
  title: ''
  type: Login
  url: https://brandyourself.com/login
- group: other
  title: ''
  type: Leadership
  url: https://brandyourself.com/team
- group: company
  title: ''
  type: Blog
  url: https://blog.brandyourself.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.brandyourself.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BrandYourself
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brandyourself/refs/heads/main/security/brandyourself-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brandyourself-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brandyourself.com
coverage:
  checked: '2026-10-03'
  detail: Developers site provides documentation but no OpenAPI spec was found at common endpoints.
  evidence:
  - status: 404
    url: https://api.brandyourself.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-03'
description: BrandYourself provides reputation management and online privacy services for individuals and businesses. Their platform offers tools to clean up negative Google results, remove personal data from data brokers, scan the dark web, and build personal branding. Over a million users rely on their software to protect their online presence and privacy.
layout: provider
modified: '2026-10-03'
name: Brandyourself
nav: Providers
network: true
overview: 'Brandyourself publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Reputation, Privacy, Online-Tools, Software-as-a-Service, and BrandYourself.


  Brandyourself''s developer surface includes engineering blog, documentation, and 10 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 15.3
  coverage:
    artifact_dirs: 4
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 5.3
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
  name: Brandyourself Domain Security
  slug: brandyourself-domain-security
  summary_line: TLSv1.3 · DMARC
slug: brandyourself
tags:
- Reputation
- Privacy
- Online-Tools
- Software-as-a-Service
- BrandYourself
website: https://brandyourself.com
---
