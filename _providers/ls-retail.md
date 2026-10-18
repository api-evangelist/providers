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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 13.7
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Developer portal for LS Retail services
  name: LS Retail API
  slug: ls-retail-api
artifact_total: 2
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ls-retail/refs/heads/main/conformance/ls-retail-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ls-retail-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ls-retail/refs/heads/main/wsdl/omniwrapper.wsdl
  title: ''
  type: WSDL
  url: wsdl/omniwrapper.wsdl
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ls-retail/refs/heads/main/llms/ls-retail-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ls-retail-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ls-retail/refs/heads/main/well-known/ls-retail-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ls-retail-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ls-retail/refs/heads/main/hosts/ls-retail-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ls-retail-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ls-retail/refs/heads/main/vendors/ls-retail-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ls-retail-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lsretail.com/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://help.lsretail.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lsretail.com/privacy-policy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.lsretail.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lsretail
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ls-retail/refs/heads/main/security/ls-retail-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ls-retail-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lsretail.com
- group: company
  title: ''
  type: Blog
  url: https://www.lsretail.com/resources
- group: docs
  title: ''
  type: Documentation
  url: https://www.lsretail.com/resources
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://www.lsretail.com/mcp
  - status: 200
    url: https://www.lsretail.com
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: LS Retail provides modular point‑of‑sale (POS) and business management software solutions for retail, hospitality, and other industries. Their flagship LS Central platform integrates POS, inventory, e‑commerce, and analytics, enabling seamless operations across stores, restaurants, hotels, pharmacies, and forecourts. LS Retail serves global brands with cloud‑enabled, Microsoft Dynamics‑based solutions, offering extensive customization, scalability, and support for omnichannel experiences.
image: https://www.lsretail.com/hubfs/SEO-hompage-ls-retail.jpg
layout: provider
modified: '2026-10-13'
name: LS Retail
nav: Providers
network: true
overview: 'LS Retail is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Retail, Point-of-Sale, Business Management, Microsoft Dynamics, and Omnichannel.


  LS Retail''s developer surface includes support, engineering blog, documentation, and 12 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 20.2
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
    developer_ergonomics: 26.2
    discoverability: 64.3
    operational_transparency: 5.3
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ls Retail Domain Security
  slug: ls-retail-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ls-retail
tags:
- Retail
- Point-of-Sale
- Business Management
- Microsoft Dynamics
- Omnichannel
- Software
website: https://www.lsretail.com
---
