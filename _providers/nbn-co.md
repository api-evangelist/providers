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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'B2B Access under the Wholesale Broadband Agreement Platform Interfacing Service: contracted retail service providers integrate their RSP B2B Applications with an API gateway hosted by nbn, using digit'
  name: nbn Platform Interfacing Service (B2B Access)
  slug: nbn-platform-interfacing-service-b2b-access
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/nbn-co/plans/nbn-co-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nbn-co-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/nbn-co/authentication/nbn-co-authentication.yml
  title: ''
  type: Authentication
  url: authentication/nbn-co-authentication.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://www.nbnco.com.au/support/network-status
- group: design
  href: https://artifacts.apis.io/nbn-co/lifecycle/nbn-co-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/nbn-co-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/nbn-co/hosts/nbn-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nbn-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/nbn-co/vendors/nbn-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nbn-co-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.nbnco.com.au/register
- group: auth
  href: https://artifacts.apis.io/nbn-co/security/nbn-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nbn-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nbnco.com.au/
- group: company
  title: ''
  type: Blog
  url: https://www.nbnco.com.au/blog
- group: company
  title: ''
  type: Newsroom
  url: https://www.nbnco.com.au/corporate-information/about-nbn-co/newsroom
- group: operate
  title: ''
  type: Support
  url: https://www.nbnco.com.au/support
- group: operate
  title: ''
  type: NetworkStatus
  url: https://www.nbnco.com.au/support/network-status
- group: commercial
  title: ''
  type: Plans
  url: https://www.nbnco.com.au/business/small-business/plans
- group: company
  title: ''
  type: Careers
  url: https://www.nbnco.com.au/corporate-information/careers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nbnco.com.au/utility/terms-and-conditions-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nbnco.com.au/utility/privacy-policy
- group: commercial
  title: ''
  type: PlatformInterfacingServiceTerms
  url: https://www.nbnco.com.au/content/dam/nbn/documents/sell/wba/2024/sfaa-wba-nbn-platform-interfacing-service-service-terms-20241003.pdf.coredownload.pdf
created: '2026-10-22'
description: 'NBN Co (styled "nbn") is the Australian Government-owned wholesale operator of the National Broadband Network, building and running the fixed-line, fixed wireless and satellite access network that retail service providers (RSPs) resell to homes and businesses across Australia. Its website describes the mission as "evolving Australia''s digital backbone to meet the ever-changing needs of people across the country." NBN Co does not publish a public developer API; its Wholesale Broadband Agreement Platform Interfacing Service terms describe B2B Access for contracted RSPs through an API gateway hosted by nbn and an nbn Developer Portal, both gated to wholesale customers. Surfaced via the API Evangelist harvest backlog (source: australia-apidays-2026).'
image: https://www.nbnco.com.au/content/config/website-footer/_jcr_content/root/container/website_footer_new/imageLogo.coreimg.png/1687751244726/nbn-logo.png
layout: provider
modified: '2026-10-22'
name: NBN Co
nav: Providers
network: true
overview: 'NBN Co is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Telecommunications, Broadband, Wholesale, and Australia.


  NBN Co''s developer surface includes authentication, signup flow, engineering blog, support, and 14 more developer resources.'
plans:
- name: Nbn Co Plans Pricing
  plan_count: 5
  slug: nbn-co-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Nbn Co Rate Limits
  slug: nbn-co-rate-limits
score:
  band: thin
  composite: 26.3
  coverage:
    artifact_dirs: 12
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 58.9
    operational_transparency: 15.8
  previous_composite: 26.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Nbn Co Authentication
  slug: nbn-co-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Nbn Co Domain Security
  slug: nbn-co-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: nbn-co
tags:
- Company
- Telecommunications
- Broadband
- Wholesale
- Australia
- Network Infrastructure
- B2B
website: https://www.nbnco.com.au/
---
