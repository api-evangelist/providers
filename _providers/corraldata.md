---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: unknown
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.4
  scored_at: '2026-10-17'
api_count: 2
apis:
- description: API platform for CorralData providing data analytics services.
  name: CorralData API
  slug: corraldata-api-2
- description: The Kb API from CorralData — 3 operation(s) for kb.
  name: CorralData Kb API
  slug: corraldata-kb-api
artifact_total: 6
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/corraldata/refs/heads/main/plans/corraldata-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/corraldata-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/corraldata/refs/heads/main/rules/corraldata-rules.yml
  title: ''
  type: Spectral
  url: rules/corraldata-rules.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/corraldata/refs/heads/main/authentication/corraldata-authentication.yml
  title: ''
  type: Authentication
  url: authentication/corraldata-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/corraldata/refs/heads/main/conformance/corraldata-conformance.yml
  title: ''
  type: Conformance
  url: conformance/corraldata-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/corraldata/refs/heads/main/llms/corraldata-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/corraldata-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/corraldata/refs/heads/main/well-known/corraldata-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/corraldata-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/corraldata/refs/heads/main/hosts/corraldata-hosts.yml
  title: ''
  type: Hosts
  url: hosts/corraldata-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/corraldata/refs/heads/main/vendors/corraldata-vendors.yml
  title: ''
  type: Vendors
  url: vendors/corraldata-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://corraldata.com/integrations/webhooks/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://corraldata.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://corraldata.com/privacy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://corraldata.com/changelog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CorralData
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/corraldata/refs/heads/main/security/corraldata-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/corraldata-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://corraldata.com/
- group: company
  title: ''
  type: Blog
  url: https://corraldata.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://corraldata.com/pricing/
- group: docs
  title: ''
  type: Documentation
  url: https://corraldata.com/platform/
- group: operate
  title: ''
  type: Support
  url: https://corraldata.com/guided-onboarding/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/corraldata/refs/heads/main/security/corraldata-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/corraldata-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://corraldata.com/
- group: company
  title: ''
  type: Blog
  url: https://corraldata.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://corraldata.com/pricing/
- group: docs
  title: ''
  type: Documentation
  url: https://corraldata.com/platform/
- group: operate
  title: ''
  type: Support
  url: https://corraldata.com/guided-onboarding/
coverage:
  checked: '2026-10-11'
  detail: API host https://api.corraldata.com returned 404 for all OpenAPI discovery URLs
  evidence:
  - status: 404
    url: https://api.corraldata.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-11'
description: CorralData provides AI‑powered analytics platforms for healthcare brands, enabling unified data modeling, governance, and actionable insights across a wide range of reporting needs. Their solutions include data apps, reverse ETL, and integration with AI assistants like Claude, helping organizations turn raw data into strategic decisions while maintaining security and compliance.
image: https://corraldata.com/wp-content/uploads/2025/02/Facebook-Link-Share-Image-2.1-ratio-@2x.png
layout: provider
modified: '2026-10-11'
name: CorralData
nav: Providers
network: true
overview: 'CorralData is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including Kb API, and 1 more. Tagged areas include Company, Data, Analytics, Healthcare, and Artificial Intelligence.


  The CorralData catalog on APIs.io includes 1 Spectral governance ruleset.


  CorralData''s developer surface includes authentication, changelog, engineering blog, pricing, documentation, support, and 19 more developer resources.'
plans:
- name: Corraldata Plans Pricing
  plan_count: 5
  slug: corraldata-plans-pricing
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: CorralData API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: corraldata-rules
score:
  band: thin
  composite: 35.6
  coverage:
    artifact_dirs: 12
    catalog_earned: 48.5
    catalog_earned_first_party: 12.0
    catalog_gap: 66.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 31.8
    contract_quality: 9.2
    developer_ergonomics: 28.6
    discoverability: 64.3
    operational_transparency: 28.9
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 18.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Corraldata Authentication
  slug: corraldata-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Corraldata Domain Security
  slug: corraldata-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: corraldata
tags:
- Company
- Data
- Analytics
- Healthcare
- Artificial Intelligence
- Platform
website: https://corraldata.com/
---
