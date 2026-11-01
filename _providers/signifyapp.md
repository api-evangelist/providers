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
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/signifyapp/plans/signifyapp-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/signifyapp-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://signifyapp.com/en/security
- group: agent
  href: https://artifacts.apis.io/signifyapp/llms/signifyapp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/signifyapp-llms.txt
- group: other
  href: https://artifacts.apis.io/signifyapp/hosts/signifyapp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/signifyapp-hosts.yml
- group: other
  href: https://artifacts.apis.io/signifyapp/vendors/signifyapp-vendors.yml
  title: ''
  type: Vendors
  url: vendors/signifyapp-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://signifyapp.com/en/security
- group: auth
  href: https://artifacts.apis.io/signifyapp/security/signifyapp-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/signifyapp-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/signifyapp/security/signifyapp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/signifyapp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://signifyapp.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.signifyapp.com/api-documentation
- group: docs
  title: ''
  type: Documentation
  url: https://portal.signifyapp.com/api-documentation/docs/overview
- group: company
  title: ''
  type: Blog
  url: https://signifyapp.com/en/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://signifyapp.com/en/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://signifyapp.com/en/policies/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://signifyapp.com/en/policies/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://support.signifyapp.com/hc/en
created: '2026-10-21'
description: Signify provides a comprehensive contract management platform that digitizes the entire workflow for sales, procurement, HR, finance, and front office operations. Users can create, manage, and store legally binding electronic contracts, automate approvals, and integrate with existing enterprise systems. The solution emphasizes security, compliance, and a seamless user experience across web and mobile, supporting digital signatures, document storage, and analytics to streamline business processes.
image: https://cdn.signifyapp.com/all_your_agreements_managed_in_one_place_9eef9c50ac.png
layout: provider
modified: '2026-10-21'
name: Signify
nav: Providers
network: true
overview: 'Signify is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Contract Management, Digital Signature, Enterprise Software, and Software-as-a-Service.


  Signify''s developer surface includes documentation, engineering blog, pricing, support, and 12 more developer resources.'
plans:
- name: Signifyapp Plans Pricing
  plan_count: 4
  slug: signifyapp-plans-pricing
random_paper: 2
score:
  band: thin
  composite: 27.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Signifyapp Domain Security
  slug: signifyapp-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Signifyapp Trust Center
  slug: signifyapp-trust-center
  summary_line: ISO 27001, ISO 27018, GDPR
slug: signifyapp
tags:
- Company
- Contract Management
- Digital Signature
- Enterprise Software
- Software-as-a-Service
website: https://signifyapp.com/
---
