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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Customer-authorized energy usage data sharing in the Green Button Connect My Data standard (XML or JSON API, CSV/XML downloads). Third parties register with National Grid; customers authorize them fro
  name: National Grid Green Button Connect My Data
  slug: green-button-connect
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/nationalgridus-com/refs/heads/main/hosts/nationalgridus-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nationalgridus-com-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/nationalgridus-com/refs/heads/main/vendors/nationalgridus-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nationalgridus-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nationalgridus.com/Our-Company/Terms-Conditions
- group: start
  title: ''
  type: SignUp
  url: https://www.nationalgridus.com/uwp_b2c/pages/register-account.json
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nationalgridus.com/Our-Company/Privacy-Notice
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nationalgridus.com/News/2022/03/Price-of-Electricity-Coming-Down-for-National-Grid-Customers-in-Rhode-Island-
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nationalgridus-com/refs/heads/main/security/nationalgridus-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nationalgridus-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nationalgridus.com
- group: start
  title: ''
  type: Portal
  url: https://greenbuttonconnect.nationalgrid.com
coverage:
  checked: '2026-10-13'
  detail: Green Button Connect My Data program exists (third-party registration and customer self-API access at greenbuttonconnect.nationalgrid.com). No OpenAPI, AsyncAPI, GraphQL, MCP, developer portal, or public API reference found; /docs and /api/docs 404; www.nationalgridus.com /developer and /greenbutton resolve to 404.aspx. Contract discovery on api/www/online/www1 hosts found nothing.
  evidence:
  - status: 200
    url: https://greenbuttonconnect.nationalgrid.com/
  - status: 302
    url: https://www.nationalgridus.com/developer
  reason: customer-only-docs
  state: gated
created: '2026-10-13'
description: 'National Grid US is the US arm of National Grid plc, delivering electricity and natural gas in New York and Massachusetts. Its developer-facing data surface is Green Button Connect My Data: customers authorize registered third parties to receive their energy usage data, and customers can get API access (XML or JSON) to their own data, via the greenbuttonconnect.nationalgrid.com portal.'
layout: provider
modified: '2026-10-13'
name: National Grid US
nav: Providers
network: true
overview: 'National Grid US is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Utilities, Green Button, and Energy Data.


  National Grid US''s developer surface includes signup flow, pricing, developer portal, and 6 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 17.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 53.6
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 11.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Nationalgridus Com Domain Security
  slug: nationalgridus-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nationalgridus-com
tags:
- Company
- Energy
- Utilities
- Green Button
- Energy Data
website: https://www.nationalgridus.com
---
