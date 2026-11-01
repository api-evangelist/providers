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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 13.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/memberspace/llms/memberspace-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/memberspace-llms.txt
- group: auth
  href: https://artifacts.apis.io/memberspace/well-known/memberspace-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/memberspace-status-security.txt
- group: agent
  href: https://artifacts.apis.io/memberspace/well-known/memberspace-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/memberspace-well-known.yml
- group: other
  href: https://artifacts.apis.io/memberspace/hosts/memberspace-hosts.yml
  title: ''
  type: Hosts
  url: hosts/memberspace-hosts.yml
- group: other
  href: https://artifacts.apis.io/memberspace/vendors/memberspace-vendors.yml
  title: ''
  type: Vendors
  url: vendors/memberspace-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.memberspace.com/terms-and-conditions/
- group: operate
  title: ''
  type: Support
  url: https://help.memberspace.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.memberspace.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.memberspace.com/signup/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.memberspace.com/privacy-policy/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.memberspace.com/getting-started/install-code
- group: docs
  title: ''
  type: Documentation
  url: https://developers.memberspace.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/memberspace
- group: auth
  href: https://artifacts.apis.io/memberspace/security/memberspace-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/memberspace-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://memberspace.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.memberspace.com/pricing
coverage:
  checked: '2026-10-28'
  detail: Developer documentation pages are rendered via JavaScript and no machine‑readable spec was found.
  evidence:
  - status: 200
    url: https://developers.memberspace.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: MemberSpace provides a membership site platform that enables website owners to add paid memberships, subscription plans, and community features to any website. It supports integrations with platforms like Squarespace, Wix, WordPress, and custom sites, offering tools for managing members, content libraries, forums, and online courses. The service includes flexible pricing, free trials, manual approvals, and supports Apple Pay, Google Pay, and Google login.
image: https://www.memberspace.com/wp-content/uploads/2025/04/memberspace-open-graph.webp
layout: provider
modified: '2026-10-27'
name: MemberSpace
nav: Providers
network: true
overview: 'MemberSpace is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include SaaS, Membership, Payments, Community, and Integration.


  MemberSpace''s developer surface includes support, signup flow, getting-started guide, documentation, pricing, and 11 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 22.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 48.2
    operational_transparency: 31.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Memberspace Domain Security
  slug: memberspace-domain-security
  summary_line: TLSv1.3 · DMARC
slug: memberspace
tags:
- SaaS
- Membership
- Payments
- Community
- Integration
- Company
website: https://memberspace.com/
---
