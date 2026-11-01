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
api_count: 0
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/double-the-donation/plans/double-the-donation-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/double-the-donation-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.doublethedonation.com/
- group: agent
  href: https://artifacts.apis.io/double-the-donation/llms/double-the-donation-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/double-the-donation-llms.txt
- group: agent
  href: https://artifacts.apis.io/double-the-donation/well-known/double-the-donation-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/double-the-donation-well-known.yml
- group: other
  href: https://artifacts.apis.io/double-the-donation/hosts/double-the-donation-hosts.yml
  title: ''
  type: Hosts
  url: hosts/double-the-donation-hosts.yml
- group: other
  href: https://artifacts.apis.io/double-the-donation/vendors/double-the-donation-vendors.yml
  title: ''
  type: Vendors
  url: vendors/double-the-donation-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://doublethedonation.com/members/login/
- group: other
  title: ''
  type: Leadership
  url: https://doublethedonation.com/team/
- group: auth
  href: https://artifacts.apis.io/double-the-donation/security/double-the-donation-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/double-the-donation-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/double-the-donation/security/double-the-donation-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/double-the-donation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://doublethedonation.com/
- group: docs
  title: ''
  type: Documentation
  url: https://doublethedonation.com/resources/
- group: company
  title: ''
  type: Blog
  url: https://doublethedonation.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://doublethedonation.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://support.doublethedonation.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://doublethedonation.com/privacy-policy-2/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://doublethedonation.com/master-terms-and-conditions/
- group: start
  title: ''
  type: GettingStarted
  url: https://doublethedonation.com/get-a-demo/
coverage:
  checked: '2026-10-27'
  detail: The provider's documented developer portal URL returns 404, indicating no accessible API program.
  evidence:
  - status: 404
    url: https://integrations.doublethedonation.com/
  reason: no-developer-program
  state: none
created: '2026-10-27'
description: Double the Donation provides a platform that simplifies corporate matching gifts, volunteer grants, and payroll giving for nonprofits. Their service automates the collection, verification, and submission of matching gift requests, helping organizations increase donor contributions and streamline compliance. The company offers integrations with major fundraising and CRM tools, a searchable matching gift database, and resources such as guides, webinars, and case studies to educate nonprofits on maximizing corporate giving opportunities.
image: https://doublethedonation.com/wp-content/uploads/2022/06/double-the-donation-logo-500x300-1.png
layout: provider
modified: '2026-10-27'
name: Double the Donation
nav: Providers
network: true
overview: 'Double the Donation is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Nonprofit, Fundraising, Matching Gifts, and SaaS.


  Double the Donation''s developer surface includes documentation, engineering blog, pricing, support, getting-started guide, and 13 more developer resources.'
plans:
- name: Double The  Donation Plans Pricing
  plan_count: 0
  slug: double-the- donation-plans-pricing
- name: Double The Donation Plans Pricing
  plan_count: 3
  slug: double-the-donation-plans-pricing
random_paper: 10
score:
  band: emerging
  composite: 24.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 50.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Double The Donation Domain Security
  slug: double-the-donation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Double The Donation Trust Center
  slug: double-the-donation-trust-center
  summary_line: SOC 2
slug: double-the-donation
tags:
- Company
- Nonprofit
- Fundraising
- Matching Gifts
- SaaS
website: https://doublethedonation.com/
---
