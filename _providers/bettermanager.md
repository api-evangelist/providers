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
- description: API documentation for Bettermanager
  name: Bettermanager API
  slug: bettermanager-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bettermanager/refs/heads/main/hosts/bettermanager-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bettermanager-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bettermanager/refs/heads/main/vendors/bettermanager-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bettermanager-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bettermanager.us/terms-of-service
- group: start
  title: ''
  type: Login
  url: https://www.bettermanager.us/remote-teams-hq/login
- group: other
  title: ''
  type: Leadership
  url: https://www.bettermanager.us/category/leadership
- group: docs
  title: ''
  type: Documentation
  url: https://www.bettermanager.us/training/docs
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bettermanager/refs/heads/main/security/bettermanager-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bettermanager-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bettermanager.us
- group: company
  title: ''
  type: Blog
  url: https://www.bettermanager.us/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bettermanager.us/privacy-policy
coverage:
  checked: '2026-09-28'
  detail: Documentation pages are rendered via JavaScript and no OpenAPI spec is discoverable.
  evidence:
  - status: 200
    url: https://www.bettermanager.us/training/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-28'
description: BetterManager provides leadership coaching and development programs that increase collaboration, engagement, and performance across your entire management team. It offers a range of programs for managers, higher education, and organizations, delivering personalized coaching, workshops, and resources to help leaders grow and drive business impact.
image: https://global-uploads.webflow.com/5c622fe1b51ea042f603663b/5d648a816ed3ee6fde9f1e46_BetterManager-Home-2019.jpg
layout: provider
modified: '2026-09-28'
name: Bettermanager
nav: Providers
network: true
overview: 'Bettermanager publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Leadership, Coaching, Development, and Management.


  Bettermanager''s developer surface includes documentation, engineering blog, and 8 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 14.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 58.9
    operational_transparency: 0.0
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
  name: Bettermanager Domain Security
  slug: bettermanager-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bettermanager
tags:
- Company
- Leadership
- Coaching
- Development
- Management
website: https://www.bettermanager.us
---
