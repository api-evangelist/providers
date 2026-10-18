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
- description: Civis Analytics provides an all‑in‑one analytics and AI platform for organizations to build data pipelines, perform advanced analytics, and generate actionable insights.
  name: Civis Analytics API
  slug: civis-analytics-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Security
  url: https://www.civisanalytics.com/legal-pages/security-center
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/civisanalytics/refs/heads/main/well-known/civisanalytics-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/civisanalytics-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/civisanalytics/refs/heads/main/well-known/civisanalytics-platform-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/civisanalytics-platform-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/civisanalytics/refs/heads/main/well-known/civisanalytics-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/civisanalytics-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/civisanalytics/refs/heads/main/hosts/civisanalytics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/civisanalytics-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/civisanalytics/refs/heads/main/vendors/civisanalytics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/civisanalytics-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.civisanalytics.com/legal-pages/terms-conditions
- group: operate
  title: ''
  type: Support
  url: https://support.civisanalytics.com/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://www.civisanalytics.com/register/taxonomer-release-webinar
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.civisanalytics.com/legal-pages/privacy-policy
- group: other
  title: ''
  type: Leadership
  url: https://www.civisanalytics.com/leadership
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CivisAnalytics
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/civisanalytics/refs/heads/main/security/civisanalytics-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/civisanalytics-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/civisanalytics/refs/heads/main/security/civisanalytics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/civisanalytics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.civisanalytics.com
coverage:
  checked: '2026-10-08'
  detail: API endpoints return 401 unauthorized and no OpenAPI spec is publicly available.
  evidence:
  - status: 401
    url: https://api.civisanalytics.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-08'
description: Civis Analytics provides an all‑in‑one analytics and AI platform for organizations to build data pipelines, perform advanced analytics, and generate actionable insights. Their solutions serve data engineers, scientists, decision makers, and IT teams across nonprofits, government, and enterprises, enabling unified reporting, data integration, and AI‑driven decision making.
layout: provider
modified: '2026-10-08'
name: Civisanalytics
nav: Providers
network: true
overview: 'Civisanalytics is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Analytics, Artificial Intelligence, Data Platform, Non-Profit, and Government.


  Civisanalytics'' developer surface includes support, signup flow, and 13 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 55.4
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 18.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Civisanalytics Domain Security
  slug: civisanalytics-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Civisanalytics Vulnerability Disclosure
  slug: civisanalytics-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: civisanalytics
tags:
- Analytics
- Artificial Intelligence
- Data Platform
- Non-Profit
- Government
website: https://www.civisanalytics.com
---
