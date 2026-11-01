---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Syvizo provides a low-code/no-code API platform enabling developers to design, build, test, and govern APIs and integrations without lock‑in.
  name: Syvizo API Platform
  slug: syvizo-api-platform
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/syvizo/authentication/syvizo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/syvizo-authentication.yml
- group: other
  href: https://artifacts.apis.io/syvizo/hosts/syvizo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/syvizo-hosts.yml
- group: start
  title: ''
  type: SignUp
  url: https://syvizo.com.au/contact/register
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Syvizo/
- group: docs
  title: ''
  type: Documentation
  url: https://syvizo.com.au/docs/Overview/Concepts.html
- group: company
  title: ''
  type: Blog
  url: https://syvizo.com.au/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://syvizo.com.au/docs/Getting_Started/Getting_Ready.html
- group: auth
  href: https://artifacts.apis.io/syvizo/security/syvizo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/syvizo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://syvizo.com.au/
coverage:
  checked: '2026-10-19'
  detail: The Syvizo documentation is publicly accessible but provides no machine‑readable OpenAPI, GraphQL, AsyncAPI, or other contract.
  evidence:
  - status: 200
    url: https://syvizo.com.au/docs/Overview/Concepts.html
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-19'
description: Syvizo provides a low-code/no-code API platform that enables developers to design, build, test, and govern APIs and integrations without lock‑in. Their Open Studio offers visual API creation, while Open Runtime runs open‑source projects. The NextGen API Gateway delivers advanced traffic management, security, and governance features. Syvizo aims to simplify API lifecycle management for enterprises and developers alike, emphasizing flexibility, open standards, and integration capabilities across cloud environments.
image: https://syvizo.com.au/logoLogoOne.svg
layout: provider
modified: '2026-10-19'
name: Syvizo
nav: Providers
network: true
overview: 'Syvizo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API Platform, Low-Code, No-Code, and Integration.


  Syvizo''s developer surface includes authentication, signup flow, documentation, engineering blog, getting-started guide, and 4 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Syvizo Authentication
  slug: syvizo-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Syvizo Domain Security
  slug: syvizo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: syvizo
tags:
- Company
- API Platform
- Low-Code
- No-Code
- Integration
website: https://syvizo.com.au/
---
