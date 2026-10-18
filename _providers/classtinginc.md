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
api_count: 1
apis:
- description: Classting provides APIs for its education platform, enabling access to class data, assignments, and student progress.
  name: Classting API
  slug: classting-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/classtinginc/refs/heads/main/hosts/classtinginc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/classtinginc-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/classtinginc/refs/heads/main/vendors/classtinginc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/classtinginc-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://policies.classting.com/ko/terms
- group: operate
  title: ''
  type: Support
  url: https://support.classting.com/hc/ko
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.classting.com/ko/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.classting.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://blog.classting.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/classtinginc/refs/heads/main/security/classtinginc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/classtinginc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.classting.com
coverage:
  checked: '2026-10-08'
  detail: GraphQL endpoint https://www.classting.com/api/graphql returns only generic errors and no schema.
  evidence:
  - status: 200
    url: https://www.classting.com/api/graphql
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-08'
description: Classtinginc provides an AI‑driven personalized education platform for K‑12 schools, offering diagnostic assessments, adaptive learning recommendations, and real‑time student progress tracking. The service integrates AI models to predict learning gaps, suggest tailored content, and support teachers with data‑driven insights, aiming to improve engagement and outcomes across primary and secondary education.
layout: provider
modified: '2026-10-08'
name: Classtinginc
nav: Providers
network: true
overview: 'Classtinginc is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Artificial Intelligence, K-12, PersonalizedLearning, and EdTech.


  Classtinginc''s developer surface includes support, pricing, engineering blog, and 6 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 12.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 12.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Classtinginc Domain Security
  slug: classtinginc-domain-security
  summary_line: TLSv1.3 · DMARC
slug: classtinginc
tags:
- Education
- Artificial Intelligence
- K-12
- PersonalizedLearning
- EdTech
website: https://www.classting.com
---
