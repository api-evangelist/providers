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
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/smud-org/refs/heads/main/security/smud-org-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/smud-org-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/smud-org/refs/heads/main/well-known/smud-org-myaccount-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/smud-org-myaccount-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/smud-org/refs/heads/main/well-known/smud-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/smud-org-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/smud-org/refs/heads/main/hosts/smud-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/smud-org-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.smud.org/Corporate/Privacy-policy/Terms-and-conditions
- group: start
  title: ''
  type: SignUp
  url: https://myaccount.smud.org/register
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.smud.org/Corporate/Privacy-policy
- group: start
  title: ''
  type: GettingStarted
  url: https://www.smud.org/Going-Green/Solar-for-Your-Home/Getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://www.smud.org/Rate-Information/Low-income-and-nonprofits/Documentation
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/smud-org/refs/heads/main/security/smud-org-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/smud-org-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/smud-org/refs/heads/main/security/smud-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/smud-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.smud.org
- group: start
  title: ''
  type: Portal
  url: https://myaccount.smud.org
- group: other
  title: ''
  type: Sitemap
  url: https://www.smud.org/sitemap.xml
coverage:
  checked: '2026-10-13'
  detail: Probed api, developer, data and opendata subdomains of smud.org (no DNS / no response); www.smud.org Green-Button and Open-data paths return a soft-404 shell; the 836-URL English sitemap lists no Green Button, developer, API or open-data page. Contract discovery found no OpenAPI, AsyncAPI, GraphQL or MCP. Customer energy data is reachable only through the myaccount.smud.org customer portal.
  evidence:
  - status: unresolved
    url: https://api.smud.org/
  - status: unresolved
    url: https://developer.smud.org/
  - status: 200
    url: https://www.smud.org/
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: Sacramento Municipal Utility District (SMUD) is the community-owned, not-for-profit electric utility serving Sacramento County, California. It publishes no public developer API, OpenAPI contract, open data portal, or Green Button Connect My Data developer program on its own domains as of 2026-10-13.
layout: provider
modified: '2026-10-13'
name: Sacramento Municipal Utility District (SMUD)
nav: Providers
network: true
overview: 'Sacramento Municipal Utility District (SMUD) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Utilities, and Electricity.


  Sacramento Municipal Utility District (SMUD)''s developer surface includes signup flow, getting-started guide, documentation, developer portal, and 10 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 18.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 35.7
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 16.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Smud Org Domain Security
  slug: smud-org-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Smud Org Vulnerability Disclosure
  slug: smud-org-vulnerability-disclosure
  summary_line: no policy recorded
slug: smud-org
tags:
- Company
- Energy
- Utilities
- Electricity
website: https://www.smud.org
---
