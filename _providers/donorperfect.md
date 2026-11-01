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
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: operate
  href: https://artifacts.apis.io/donorperfect/changelog/donorperfect-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/donorperfect-changelog.yml
- group: agent
  href: https://artifacts.apis.io/donorperfect/llms/donorperfect-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/donorperfect-llms.txt
- group: auth
  href: https://artifacts.apis.io/donorperfect/well-known/donorperfect-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/donorperfect-status-security.txt
- group: agent
  href: https://artifacts.apis.io/donorperfect/well-known/donorperfect-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/donorperfect-well-known.yml
- group: other
  href: https://artifacts.apis.io/donorperfect/hosts/donorperfect-hosts.yml
  title: ''
  type: Hosts
  url: hosts/donorperfect-hosts.yml
- group: other
  href: https://artifacts.apis.io/donorperfect/vendors/donorperfect-vendors.yml
  title: ''
  type: Vendors
  url: vendors/donorperfect-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.donorperfect.com:443/company/terms-of-service/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.donorperfect.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.donorperfect.com/integrations/volunteer-management/signup/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.donorperfect.com:443/company/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.donorperfect.com:443/fundraising-software/pricing-guide/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.donorperfect.com:443/clients/release-notes/
- group: company
  title: ''
  type: Blog
  url: https://www.donorperfect.com/blog/vote-for-the-winner-of-the-donorperfect-community-impact-award/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.donorperfect.com:443/client-services/system-implementation/
- group: auth
  href: https://artifacts.apis.io/donorperfect/security/donorperfect-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/donorperfect-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://donorperfect.com/
coverage:
  checked: '2026-10-27'
  detail: The DonorPerfect API documentation page provides only HTML details without a machine‑readable OpenAPI/GraphQL/AsyncAPI spec.
  evidence:
  - status: 200
    url: https://www.donorperfect.com/factsheets/api-access-feature
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: DonorPerfect provides fundraising software and a public XML API for nonprofit donor management. The platform offers tools for donation forms, event management, donor CRM, marketing, analytics, and integrations, helping organizations streamline fundraising operations and improve donor engagement.
image: https://uploads.donorperfect.com/images/new-template-home-facebook-1.png
layout: provider
modified: '2026-10-27'
name: DonorPerfect
nav: Providers
network: true
overview: 'DonorPerfect is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fundraising, Nonprofit, CRM, and API.


  DonorPerfect''s developer surface includes changelog, signup flow, pricing, engineering blog, getting-started guide, and 11 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 21.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 48.2
    operational_transparency: 42.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Donorperfect Domain Security
  slug: donorperfect-domain-security
  summary_line: TLSv1.3 · DMARC
slug: donorperfect
tags:
- Company
- Fundraising
- Nonprofit
- CRM
- API
- Software
website: https://donorperfect.com/
---
