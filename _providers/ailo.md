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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/ailo/plans/ailo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ailo-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/ailo/changelog/ailo-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ailo-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://ailo.io/security
- group: auth
  href: https://artifacts.apis.io/ailo/well-known/ailo-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ailo-security.txt
- group: agent
  href: https://artifacts.apis.io/ailo/well-known/ailo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ailo-well-known.yml
- group: other
  href: https://artifacts.apis.io/ailo/hosts/ailo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ailo-hosts.yml
- group: other
  href: https://artifacts.apis.io/ailo/vendors/ailo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ailo-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://ailo.io/register-mecca-event
- group: other
  title: ''
  type: Leadership
  url: https://ailo.io/team/benjamin-ling
- group: start
  title: ''
  type: GettingStarted
  url: https://ailo.io/handbook-training-onboarding
- group: docs
  title: ''
  type: Documentation
  url: https://help.ailo.io/
- group: company
  title: ''
  type: Website
  url: https://ailo.io/
- group: auth
  href: https://artifacts.apis.io/ailo/security/ailo-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/ailo-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/ailo/security/ailo-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ailo-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ailo/security/ailo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ailo-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://ailo.io/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://ailo.io/whats-new
- group: operate
  title: ''
  type: Support
  url: https://help.ailo.io/hc/en-au
- group: company
  title: ''
  type: AboutUs
  url: https://ailo.io/about-us
- group: operate
  title: ''
  type: Contact
  url: https://ailo.io/contact
- group: company
  title: ''
  type: Careers
  url: https://ailo.io/careers
- group: auth
  title: ''
  type: Security
  url: https://ailo.io/security
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ailo.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ailo.io/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ailo/
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/ailohq/
created: '2026-10-22'
description: Ailo is an Australian property management platform, co-founded in 2017, that connects the people, work and money involved in property management. Renters, property managers, property investors (owners) and tradespeople use the Ailo Platform and mobile app to see rent, payments, inspections, repair requests and messages in one place, with Ailo handling the financial transactions between them. Surfaced via the API Evangelist harvest backlog (australia-apidays-2026); no public developer API was identified in the identity pass.
image: https://ailo.io/images/default-social-image-preview.png
layout: provider
modified: '2026-10-22'
name: Ailo
nav: Providers
network: true
overview: 'Ailo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Property Management, Real Estate, PropTech, and Rent Payments.


  Ailo''s developer surface includes changelog, signup flow, getting-started guide, documentation, engineering blog, support, and 20 more developer resources.'
plans:
- name: Ailo Plans Pricing
  plan_count: 3
  slug: ailo-plans-pricing
random_paper: 13
score:
  band: thin
  composite: 30.9
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 81.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 50.0
    operational_transparency: 26.3
  previous_composite: 30.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 22.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ailo Domain Security
  slug: ailo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ailo Vulnerability Disclosure
  slug: ailo-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Ailo Trust Center
  slug: ailo-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: ailo
tags:
- Company
- Property Management
- Real Estate
- PropTech
- Rent Payments
- Payments
- Australia
website: https://ailo.io/
---
