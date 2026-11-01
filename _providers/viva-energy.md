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
    dynamic_client_registration: true
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
  score: 15.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/viva-energy/well-known/viva-energy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/viva-energy-well-known.yml
- group: other
  href: https://artifacts.apis.io/viva-energy/hosts/viva-energy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/viva-energy-hosts.yml
- group: other
  href: https://artifacts.apis.io/viva-energy/vendors/viva-energy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/viva-energy-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.vivaenergy.com.au/energy-hub/gas-terminal-project/register-for-project-updates-and-provide-feedback
- group: docs
  title: ''
  type: Documentation
  url: https://help.vivaenergy.com.au/
- group: auth
  href: https://artifacts.apis.io/viva-energy/security/viva-energy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/viva-energy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vivaenergy.com.au/
- group: company
  title: ''
  type: Blog
  url: https://www.vivaenergy.com.au/driven
- group: operate
  title: ''
  type: Support
  url: https://help.vivaenergy.com.au/MoveHelpAndSupport/s/
- group: operate
  title: ''
  type: Contact
  url: https://www.vivaenergy.com.au/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vivaenergy.com.au/contact/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vivaenergy.com.au/contact/privacy-policy
created: '2026-10-22'
description: Viva Energy Australia (vivaenergy.com.au) is an Australian energy company that says it supplies about a quarter of the fuel Australians need, through a network of Shell and Liberty service stations and business supply to aviation, marine, defence, mining, transport, bitumen, solvents and polymers customers. It operates the Geelong refinery in Victoria, fuel terminals and pipelines, and is developing a Geelong Energy Hub and gas terminal project. Its public web presence is a corporate site plus a Salesforce-hosted help centre for its Viva Energy Move service; no public developer API program was found during identity profiling.
image: https://www.vivaenergy.com.au/images/UserUploadedImages/11/viva-logo.svg
layout: provider
modified: '2026-10-22'
name: Viva Energy
nav: Providers
network: true
overview: 'Viva Energy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Fuel, Oil and Gas, and Refining.


  Viva Energy''s developer surface includes signup flow, documentation, engineering blog, support, and 8 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 15.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 15.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 16.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Viva Energy Domain Security
  slug: viva-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: viva-energy
tags:
- Company
- Energy
- Fuel
- Oil and Gas
- Refining
- Retail
- Australia
- Aviation
website: https://www.vivaenergy.com.au/
---
