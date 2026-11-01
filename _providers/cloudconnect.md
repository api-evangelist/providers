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
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/cloudconnect/llms/cloudconnect-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cloudconnect-llms.txt
- group: agent
  href: https://artifacts.apis.io/cloudconnect/well-known/cloudconnect-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cloudconnect-well-known.yml
- group: other
  href: https://artifacts.apis.io/cloudconnect/hosts/cloudconnect-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloudconnect-hosts.yml
- group: other
  href: https://artifacts.apis.io/cloudconnect/vendors/cloudconnect-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cloudconnect-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.salesforce.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.salesforce.com/company/legal/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.salesforce.com/slack/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://www.salesforce.com/news/
- group: start
  title: ''
  type: Login
  url: https://iis.digital.salesforce.com/services/auth/login
- group: other
  title: ''
  type: Leadership
  url: https://www.salesforce.com/company/leadership/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.salesforce.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.salesforce.com/products/innovation/releases/
- group: company
  title: ''
  type: Blog
  url: https://www.salesforce.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.salesforce.com/blog/onboard-employees-customer-journey/
- group: docs
  title: ''
  type: Documentation
  url: https://help.salesforce.com/
- group: auth
  href: https://artifacts.apis.io/cloudconnect/security/cloudconnect-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudconnect-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cloudconnect.com
coverage:
  checked: '2026-10-30'
  detail: CloudConnect redirects to Salesforce and provides no public API documentation on its own domain.
  evidence:
  - status: 301
    url: https://www.cloudconnect.com
  reason: not-a-software-company
  state: none
created: '2026-10-29'
description: 'CloudConnect is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by heavybit) and added to the network as a stub for full-pipeline profiling.'
image: https://images.ctfassets.net/ct4bxoykjwgb/62APtIxMy9L1S8YnUi00Lm/2f6e3f8ccbe2d3cbb1b633895176968a/salesforce-logo.jpg
layout: provider
modified: '2026-10-29'
name: CloudConnect
nav: Providers
network: true
overview: 'CloudConnect is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  CloudConnect''s developer surface includes pricing, changelog, engineering blog, getting-started guide, documentation, and 12 more developer resources.'
plans:
- name: Cloudconnect Plans Pricing
  plan_count: 19
  slug: cloudconnect-plans-pricing
random_paper: 9
score:
  band: thin
  composite: 29.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 29.0
    catalog_earned_first_party: 12.0
    catalog_gap: 86.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 33.9
    operational_transparency: 15.8
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cloudconnect Domain Security
  slug: cloudconnect-domain-security
  summary_line: TLSv1.3 · HSTS
slug: cloudconnect
tags:
- Company
website: https://www.cloudconnect.com
---
