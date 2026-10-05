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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/breadcrumbs/refs/heads/main/llms/breadcrumbs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/breadcrumbs-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/breadcrumbs/refs/heads/main/well-known/breadcrumbs-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/breadcrumbs-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/breadcrumbs/refs/heads/main/hosts/breadcrumbs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/breadcrumbs-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/breadcrumbs/refs/heads/main/vendors/breadcrumbs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/breadcrumbs-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://breadcrumbs.io/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://breadcrumbs.io/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://breadcrumbs.io/pricing/
- group: docs
  title: ''
  type: Documentation
  url: https://breadcrumbs.io/guides/
- group: company
  title: ''
  type: Blog
  url: https://breadcrumbs.io/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/breadcrumbs/refs/heads/main/security/breadcrumbs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/breadcrumbs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://breadcrumbs.io/
coverage:
  checked: '2026-10-03'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on the provider's hosts.
  evidence:
  - status: 0
    url: https://api.breadcrumbs.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-03'
description: Breadcrumbs provides an enterprise‑grade lead scoring and revenue acceleration platform that uses AI to analyze data across marketing and sales funnels, offering tools like email verification, lead scoring, and a copilot to help users build scoring models quickly.
image: https://breadcrumbs.io/wp-content/uploads/2023/05/home3d-feat-share-fig.png
layout: provider
modified: '2026-10-03'
name: Breadcrumbs
nav: Providers
network: true
overview: 'Breadcrumbs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Lead Scoring, Revenue Acceleration, Marketing Automation, Sales Enablement, and Artificial Intelligence.


  Breadcrumbs'' developer surface includes pricing, documentation, engineering blog, and 8 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 14.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Breadcrumbs Domain Security
  slug: breadcrumbs-domain-security
  summary_line: TLSv1.3
slug: breadcrumbs
tags:
- Lead Scoring
- Revenue Acceleration
- Marketing Automation
- Sales Enablement
- Artificial Intelligence
- Software-as-a-Service
website: https://breadcrumbs.io/
---
