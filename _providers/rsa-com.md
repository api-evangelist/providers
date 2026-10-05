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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.1
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: The Users API from RSA — 1 operation(s) for users.
  name: RSA Users API
  slug: rsa-com-users-api
artifact_total: 3
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rsa-com/refs/heads/main/rules/rsa-com-rules.yml
  title: ''
  type: Spectral
  url: rules/rsa-com-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rsa-com/refs/heads/main/conformance/rsa-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rsa-com-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rsa-com/refs/heads/main/llms/rsa-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rsa-com-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rsa-com/refs/heads/main/well-known/rsa-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rsa-com-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/rsa-com/refs/heads/main/hosts/rsa-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rsa-com-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/rsa-com/refs/heads/main/vendors/rsa-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rsa-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rsa.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rsa.com/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.rsa.com/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rsa-com/refs/heads/main/security/rsa-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rsa-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rsa.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.rsa.com/resources
- group: operate
  title: ''
  type: Support
  url: https://www.rsa.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.rsa.com/resources/blog
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://community.rsa.com/mcp/v1
  reason: no-developer-program
  state: none
created: '2026-10-03'
description: RSA provides identity and access management solutions, including multi-factor authentication, passwordless authentication, and security governance. Their platform helps organizations protect digital assets, streamline compliance, and defend against advanced threats through AI‑driven security and robust authentication services.
image: https://www.rsa.com/wp-content/uploads/rsa-og-image-2026.png
layout: provider
modified: '2026-10-03'
name: RSA
nav: Providers
network: true
overview: 'RSA publishes 1 API on the [APIs.io](https://apis.io/) network: Users API. Tagged areas include Identity Management, Multi-Factor Authentication, Passwordless, Identity Governance, and Cloud IAM.


  The RSA catalog on APIs.io includes 1 Spectral governance ruleset.


  RSA''s developer surface includes documentation, support, engineering blog, and 11 more developer resources.'
random_paper: 8
rules:
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: RSA API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: rsa-com-rules
score:
  band: emerging
  composite: 19.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 9.4
    developer_ergonomics: 16.7
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 24.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Rsa Com Domain Security
  slug: rsa-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rsa-com
tags:
- Identity Management
- Multi-Factor Authentication
- Passwordless
- Identity Governance
- Cloud IAM
- Government
- Financial Services
website: https://www.rsa.com
---
