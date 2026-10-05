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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: Identity and access management API (no machine-readable spec found)
  name: Avatier API
  slug: avatier-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: Compliance
  url: https://trust.avatier.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avatier/refs/heads/main/security/avatier-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/avatier-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avatier/refs/heads/main/llms/avatier-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/avatier-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avatier/refs/heads/main/well-known/avatier-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/avatier-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avatier/refs/heads/main/well-known/avatier-identitychallengecard-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/avatier-identitychallengecard-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avatier/refs/heads/main/well-known/avatier-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/avatier-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avatier/refs/heads/main/hosts/avatier-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avatier-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avatier/refs/heads/main/vendors/avatier-vendors.yml
  title: ''
  type: Vendors
  url: vendors/avatier-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.avatier.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://www.avatier.com/support/
- group: start
  title: ''
  type: SignUp
  url: https://community.avatier.com/auth/v3/register?brand_id=87209&return_to=https%253A%252F%252Fcommunity.avatier.com%252Fhc%252Fen-us%253Fbrand_id%253D87209&locale=en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.avatier.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.avatier.com/products/identity-container/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://www.avatier.com/news/
- group: other
  title: ''
  type: Leadership
  url: https://www.avatier.com/leadership/
- group: company
  title: ''
  type: Blog
  url: https://www.avatier.com/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avatier/refs/heads/main/security/avatier-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/avatier-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avatier/refs/heads/main/security/avatier-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/avatier-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avatier/refs/heads/main/security/avatier-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avatier-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.avatier.com
coverage:
  checked: 2026-09-26
  detail: Documentation pages are behind JavaScript challenges and no OpenAPI spec is accessible.
  evidence:
  - status: 0
    url: https://api.avatier.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Avatier provides AI‑powered identity and access management solutions, offering self‑service password reset, lifecycle automation, access governance, SSO, and AI‑driven security workflows. Their platform supports cloud‑hosted and non‑hosted deployments across major clouds and integrates with MFA providers. Avatier targets enterprises seeking scalable, low‑code identity security with customizable APIs.
image: https://www.avatier.com/images/og.png
layout: provider
modified: '2026-09-26'
name: Avatier
nav: Providers
network: true
overview: 'Avatier publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Identity, Access Management, Artificial Intelligence, Cloud, and Enterprise.


  Avatier''s developer surface includes support, signup flow, pricing, engineering blog, and 16 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 22.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 67.9
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Avatier Domain Security
  slug: avatier-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Avatier Vulnerability Disclosure
  slug: avatier-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Avatier Trust Center
  slug: avatier-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR, CSA STAR
slug: avatier
tags:
- Identity
- Access Management
- Artificial Intelligence
- Cloud
- Enterprise
website: https://www.avatier.com
---
