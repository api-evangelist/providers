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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for accessing Forage's virtual job simulations and career resources.
  name: Forage API
  slug: forage-api
artifact_total: 3
common:
- group: other
  href: https://artifacts.apis.io/theforage-com/hosts/theforage-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/theforage-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/theforage-com/vendors/theforage-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/theforage-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.theforage.com/terms
- group: auth
  title: ''
  type: Security
  url: https://www.theforage.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.theforage.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/theforage
- group: auth
  href: https://artifacts.apis.io/theforage-com/security/theforage-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/theforage-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/theforage-com/security/theforage-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/theforage-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://theforage.com/
- group: company
  title: ''
  type: Blog
  url: https://www.theforage.com/blog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://enterprise.theforage.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.theforage.com/student-signup
- group: start
  title: ''
  type: SignUp
  url: https://www.theforage.com/student-signup
coverage:
  checked: '2026-10-29'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://www.theforage.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Forage provides free virtual job simulations and career preparation resources, partnering with top employers to offer hands‑on experience across industries such as finance, engineering, consulting, and cybersecurity. Users can explore simulations, build skills, and showcase their work to potential employers, while enterprises and educators access tailored programs for talent development and recruitment.
image: https://cdn-assets.theforage.com/images/meta-image-homepage.png
layout: provider
modified: '2026-10-29'
name: Forage
nav: Providers
network: true
overview: 'Forage is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, Career, Simulations, and Talent.


  Forage''s developer surface includes engineering blog, getting-started guide, signup flow, and 10 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 19.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Theforage Com Domain Security
  slug: theforage-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Theforage Com Vulnerability Disclosure
  slug: theforage-com-vulnerability-disclosure
  summary_line: no policy recorded
slug: theforage-com
tags:
- Company
- Education
- Career
- Simulations
- Talent
website: https://theforage.com/
---
