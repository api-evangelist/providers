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
apis:
- description: API documentation not publicly available; platform details are described on the website.
  name: Intrepid Labs API
  slug: intrepid-labs-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/intrepid-labs/hosts/intrepid-labs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/intrepid-labs-hosts.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.intrepidlabs.tech/
- group: company
  title: ''
  type: Newsroom
  url: https://www.intrepidlabs.tech/news
- group: start
  title: ''
  type: GettingStarted
  url: https://www.intrepidlabs.tech/articles/getting-started
- group: auth
  href: https://artifacts.apis.io/intrepid-labs/security/intrepid-labs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/intrepid-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.intrepidlabs.tech
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.intrepidlabs.tech/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.intrepidlabs.tech/privacy-policy
- group: operate
  title: ''
  type: Contact
  url: https://www.intrepidlabs.tech/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/intrepid-labs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.intrepidlabs.tech/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.intrepidlabs.tech/privacy-policy
- group: operate
  title: ''
  type: Contact
  url: https://www.intrepidlabs.tech/contact-us
coverage:
  detail: Platform page renders via Framer with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://www.intrepidlabs.tech/platform
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Intrepid Labs is an AI‑driven drug formulation platform that accelerates therapeutic development by combining artificial intelligence, automation, and deep pharmaceutical expertise. The company’s mission is to make drug development faster, more predictive, and patient‑centered, offering capabilities such as molecule selection, AI‑guided formulation design, and manufacturable formulation delivery for pharma partners worldwide.
image: https://framerusercontent.com/images/oLzype3QKbRgjcVBvMm2zUp5090.png
layout: provider
modified: '2026-10-29'
name: Intrepid Labs
nav: Providers
network: true
overview: 'Intrepid Labs is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Drug-Formulation, Pharma, and Platform.


  Intrepid Labs'' developer surface includes getting-started guide and 12 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 15.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 58.9
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 14.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Intrepid Labs Domain Security
  slug: intrepid-labs-domain-security
  summary_line: TLSv1.3 · HSTS
slug: intrepid-labs
tags:
- Company
- AI
- Drug-Formulation
- Pharma
- Platform
- Startup
website: https://www.intrepidlabs.tech
---
