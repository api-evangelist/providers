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
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bravely/refs/heads/main/hosts/bravely-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bravely-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dev.workbravely.com/terms-of-service
- group: start
  title: ''
  type: SignUp
  url: https://api.workbravely.com/sign-up
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dev.workbravely.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://workbravely.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.workbravely.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WorkBravely
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bravely/refs/heads/main/security/bravely-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bravely-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://workbravely.com
coverage:
  checked: '2026-10-03'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL files were found on any discovered host.
  evidence:
  - status: 404
    url: https://api.workbravely.com/openapi.json
  - status: 404
    url: https://api.workbravely.com/openapi.yaml
  - status: 404
    url: https://api.workbravely.com/v1/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-03'
description: Bravely provides a coaching and training platform for employees, offering products such as Bravely Advance, Boost, Exec, Workshops, and AI-driven Bravely Bea. The platform helps develop critical talent, leadership skills, and on-demand coaching for individuals and executives, with resources like blogs, education, and a demo request. It serves organizations seeking to enhance employee growth and performance through personalized coaching solutions.
layout: provider
modified: '2026-10-03'
name: Bravely
nav: Providers
network: true
overview: 'Bravely is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Coaching, Employee Development, Training Platform, Leadership, and Artificial Intelligence.


  Bravely''s developer surface includes signup flow, engineering blog, documentation, and 6 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 13.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 44.6
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bravely Domain Security
  slug: bravely-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bravely
tags:
- Coaching
- Employee Development
- Training Platform
- Leadership
- Artificial Intelligence
website: https://workbravely.com
---
