---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Our guides cover a wide range of topics; from legislation to software specific advice, there's something to benefit every business.
  name: Guides
  slug: guides
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/iris-software/llms/iris-software-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/iris-software-llms.txt
- group: agent
  href: https://artifacts.apis.io/iris-software/well-known/iris-software-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/iris-software-well-known.yml
- group: other
  href: https://artifacts.apis.io/iris-software/hosts/iris-software-hosts.yml
  title: ''
  type: Hosts
  url: hosts/iris-software-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.iris.co.uk/news/
- group: docs
  title: ''
  type: Documentation
  url: https://www.iris.co.uk/guides/
- group: auth
  href: https://artifacts.apis.io/iris-software/security/iris-software-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/iris-software-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.iris.co.uk/
- group: company
  title: ''
  type: Blog
  url: https://www.iris.co.uk/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.iris.co.uk/legal/privacy-statement/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.iris.co.uk/legal/website-terms-conditions/
- group: operate
  title: ''
  type: Support
  url: https://www.iris.co.uk/
coverage:
  checked: '2026-10-28'
  detail: Public documentation pages exist (e.g., Guides) but no OpenAPI, AsyncAPI, GraphQL SDL, or other machine‑readable spec was found.
  evidence:
  - status: 200
    url: https://api.co.uk/openapi.json
  - status: 404
    url: https://www.iris.co.uk/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: IRIS Software Group provides business software solutions for mission‑critical tasks across accounting, payroll, HR, education, financials and more. Their AI‑powered platforms help organisations manage finance, human resources, payroll and education operations efficiently, serving customers worldwide.
image: https://www.iris.co.uk/wp-content/uploads/2021/05/IRIS-logo.png
layout: provider
modified: '2026-10-28'
name: IRIS Software Group
nav: Providers
network: true
overview: 'IRIS Software Group is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software, Accounting, Payroll, and HR.


  IRIS Software Group''s developer surface includes documentation, engineering blog, support, and 8 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
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
  name: Iris Software Domain Security
  slug: iris-software-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: iris-software
tags:
- Company
- Software
- Accounting
- Payroll
- HR
- Education
website: https://www.iris.co.uk/
---
