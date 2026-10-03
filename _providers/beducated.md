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
api_count: 1
apis:
- description: API for Beducated platform offering course data and user management.
  name: Beducated API
  slug: beducated-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beducated/refs/heads/main/vendors/beducated-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beducated-vendors.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/beducated/refs/heads/main/conformance/beducated-conformance.yml
  title: ''
  type: Conformance
  url: conformance/beducated-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beducated/refs/heads/main/hosts/beducated-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beducated-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://support.beducated.com/
- group: company
  title: ''
  type: Newsroom
  url: https://beducated.com/press
- group: start
  title: ''
  type: Login
  url: https://my.beducated.com/login/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beducated/refs/heads/main/security/beducated-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beducated-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://beducated.com
- group: docs
  title: ''
  type: Documentation
  url: https://beducated.com/about
- group: start
  title: ''
  type: GettingStarted
  url: https://beducated.com/get-started
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://beducated.com/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://beducated.com/legal/terms
- group: other
  title: ''
  type: Imprint
  url: https://beducated.com/legal/imprint
coverage:
  checked: '2026-09-27'
  detail: Main site redirects to my.beducated.com and provides no machine‑readable API spec.
  evidence:
  - status: 200
    url: https://app.beducated.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: Beducated is an online platform offering 150+ courses on sex and relationships, providing safe, inclusive education for adults of all orientations and genders. It aims to improve sexual skills and confidence through expert-led video tutorials and interactive exercises, fostering better intimacy and personal growth.
image: https://beducated.com/social_images/og-default.jpg
layout: provider
modified: '2026-09-27'
name: Beducated
nav: Providers
network: true
overview: 'Beducated publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Sexual Health, Online Learning, Courses, and AdultEducation.


  Beducated''s developer surface includes support, documentation, getting-started guide, and 10 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 18.6
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Beducated Domain Security
  slug: beducated-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: beducated
tags:
- Education
- Sexual Health
- Online Learning
- Courses
- AdultEducation
website: https://beducated.com
---
