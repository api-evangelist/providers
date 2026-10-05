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
artifact_total: 2
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/brainscape/refs/heads/main/plans/brainscape-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/brainscape-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/brainscape/refs/heads/main/conformance/brainscape-conformance.yml
  title: ''
  type: Conformance
  url: conformance/brainscape-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brainscape/refs/heads/main/hosts/brainscape-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brainscape-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.brainscape.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brainscape.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.brainscape.com/pricing?paywall=upgrade
- group: company
  title: ''
  type: Newsroom
  url: https://www.brainscape.com/academy/news/
- group: start
  title: ''
  type: Login
  url: https://www.brainscape.com/log-in
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brainscape/refs/heads/main/security/brainscape-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brainscape-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.brainscape.com
coverage:
  checked: '2026-10-03'
  detail: Brainscape provides no public developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.brainscape.com
  reason: no-developer-program
  state: none
created: '2026-10-03'
description: Brainscape provides a flashcard-based learning platform that helps students and professionals study more efficiently. Users can create, share, and discover millions of flashcards across subjects such as entrance exams, professional certifications, languages, medical, science, and more. The service leverages spaced repetition and cognitive science to improve retention, offering tools for educators, schools, and individual learners to customize study experiences.
image: https://www.brainscape.com/assets/bsc-share-icon.png
layout: provider
modified: '2026-10-03'
name: Brainscape
nav: Providers
network: true
overview: 'Brainscape is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Flashcards, Learning, Study Tools, and Mobile App.


  Brainscape''s developer surface includes pricing and 9 more developer resources.'
plans:
- name: Brainscape Plans Pricing
  plan_count: 3
  slug: brainscape-plans-pricing
random_paper: 14
score:
  band: emerging
  composite: 22.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 18.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brainscape Domain Security
  slug: brainscape-domain-security
  summary_line: TLSv1.2 · DMARC
slug: brainscape
tags:
- Education
- Flashcards
- Learning
- Study Tools
- Mobile App
website: https://www.brainscape.com
---
