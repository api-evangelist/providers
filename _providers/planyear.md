---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 8.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: PlanYear developer portal providing API information, but the API reference is gated.
  name: PlanYear API
  slug: planyear-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/planyear/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/planyear/components/planyear-components.yml
  title: ''
  type: Components
  url: components/planyear-components.yml
- group: design
  href: https://artifacts.apis.io/planyear/conformance/planyear-conformance.yml
  title: ''
  type: Conformance
  url: conformance/planyear-conformance.yml
- group: other
  href: https://artifacts.apis.io/planyear/hosts/planyear-hosts.yml
  title: ''
  type: Hosts
  url: hosts/planyear-hosts.yml
- group: other
  href: https://artifacts.apis.io/planyear/vendors/planyear-vendors.yml
  title: ''
  type: Vendors
  url: vendors/planyear-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://planyear.ai/terms-of-service
- group: auth
  title: ''
  type: Security
  url: https://planyear.ai/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://planyear.ai/privacy-policy
- group: auth
  href: https://artifacts.apis.io/planyear/security/planyear-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/planyear-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://planyear.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.planyear.com
- group: operate
  title: ''
  type: Support
  url: https://planyear.com/contact
coverage:
  checked: '2026-10-29'
  detail: Access to the API reference is blocked by a 403 partner portal login at https://portal.planyear.com/mcp.
  evidence:
  - status: 403
    url: https://portal.planyear.com/mcp
  reason: partner-login
  state: gated
created: '2026-10-29'
description: PlanYear provides an AI‑native platform for the benefits industry, offering the BEACON platform for benefits consultants and the RAPID solution for insurance carriers. Built by benefits professionals, the platform reads, cleans, and formats census files, plan documents, RFPs, and renewals, enabling consultants to focus on strategic guidance and carriers to quote efficiently. The service combines deep industry knowledge with modern AI to return time to relationships and growth.
image: https://cdn.prod.website-files.com/68889aefbde1e55ca71a9944/6adb5ea932e169e23330c029_home-og-image.jpg
layout: provider
modified: '2026-10-29'
name: PlanYear
nav: Providers
network: true
overview: 'PlanYear is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Benefits, Insurance, Platform, and Consulting.


  PlanYear''s developer surface includes support and 11 more developer resources.'
random_paper: 20
rate_limits:
- limit_count: 0
  name: Planyear Rate Limits
  slug: planyear-rate-limits
scopes:
- name: Planyear Scopes
  scope_count: 0
  slug: planyear-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 20.7
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 29.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Planyear Authentication
  slug: planyear-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Planyear Domain Security
  slug: planyear-domain-security
  summary_line: TLSv1.3 · DMARC
slug: planyear
tags:
- AI
- Benefits
- Insurance
- Platform
- Consulting
website: https://planyear.com
---
