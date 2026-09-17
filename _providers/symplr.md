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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-16'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.symplr.com
- group: company
  title: ''
  type: Blog
  url: https://www.symplr.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.symplr.com/feed
- group: operate
  title: ''
  type: Support
  url: https://www.symplr.com/customer-support
- group: start
  title: ''
  type: Login
  url: https://www.symplr.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.symplr.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.symplr.com/privacy-policy
- group: company
  title: ''
  type: Partners
  url: https://www.symplr.com/partnerships
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/symplr/
- group: other
  title: ''
  type: X
  url: https://x.com/symplr
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/symplr/refs/heads/main/security/symplr-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/symplr-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/symplr/refs/heads/main/security/symplr-trust-center.yml
  title: ''
  type: Compliance
  url: security/symplr-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/symplr/refs/heads/main/security/symplr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/symplr-domain-security.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/symplr/refs/heads/main/packages/symplr-packages.yml
  title: ''
  type: Packages
  url: packages/symplr-packages.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/symplr/refs/heads/main/plans/symplr-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/symplr-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/symplr/refs/heads/main/rate-limits/symplr-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/symplr-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/symplr/refs/heads/main/llms/symplr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/symplr-llms.txt
coverage:
  checked: '2026-09-16'
  detail: symplr markets an "open API and secure webhook framework" for Contingent Talent Management and a partner API behind "Request a demo", but the one public reference it ever ran, apidoc.symplr.com (a FHIR-shaped Portfolio API using client_id/client_secret headers, per search-index snippets), no longer resolves, and no OpenAPI, SDK, developer portal or well-known document is served on any symplr host.
  evidence:
  - note: DNS NOERROR with no A record from 8.8.8.8, 1.1.1.1 and symplr's UltraDNS nameserver
    status: 0
    url: https://apidoc.symplr.com/
  - status: 200
    url: https://www.symplr.com/products/contingent-talent-management/integrations
  - status: 0
    url: https://developer.symplr.com/
  - status: 403
    url: https://www.symplr.com/openapi.json
  - status: 404
    url: https://www.symplr.com/.well-known/api-catalog
  - status: 403
    url: https://integrations.symplr.com/
  reason: sales-gate
  state: gated
created: '2026-09-16'
description: 'symplr (symplr software LLC, Houston) sells healthcare operations software to hospitals, health systems and payers: provider data management and credentialing (symplr Provider, Directory, CVO, Payer), workforce and talent management (Smart Square, symplr Workforce, formerly API Healthcare), quality and safety (Midas), clinical communications, spend, access, contract and compliance management, unified as the symplr Operations Platform. It markets APIs, webhooks and a certified partner program, but publishes no public API reference or machine-readable contract.'
image: https://www.symplr.com/wp-content/uploads/2025/02/Generic-symplr2.jpg
layout: provider
modified: '2026-09-16'
name: symplr
nav: Providers
network: true
overview: 'symplr is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Healthcare Operations, Provider Data Management, and Credentialing.


  symplr''s developer surface includes engineering blog, support, and 15 more developer resources.'
plans:
- name: Symplr Plans Pricing
  plan_count: 0
  slug: symplr-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Symplr Rate Limits
  slug: symplr-rate-limits
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.8
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Symplr Domain Security
  slug: symplr-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Symplr Trust Center
  slug: symplr-trust-center
  summary_line: ISO 27001:2022, HITRUST, SOC 2 Type II, SOC 1 Type II, HIPAA, NIST
slug: symplr
tags:
- Company
- Healthcare
- Healthcare Operations
- Provider Data Management
- Credentialing
- Workforce Management
- Compliance
- Supply Chain
website: https://www.symplr.com
---
