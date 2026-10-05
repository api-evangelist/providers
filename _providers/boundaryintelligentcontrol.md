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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.boundarycontrol.com/trust
- group: auth
  title: ''
  type: Security
  url: https://www.boundarycontrol.com/trust#responsible-disclosure
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boundaryintelligentcontrol/refs/heads/main/well-known/boundaryintelligentcontrol-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/boundaryintelligentcontrol-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/boundaryintelligentcontrol/refs/heads/main/well-known/boundaryintelligentcontrol-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/boundaryintelligentcontrol-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/boundaryintelligentcontrol/refs/heads/main/hosts/boundaryintelligentcontrol-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boundaryintelligentcontrol-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/boundaryintelligentcontrol/refs/heads/main/vendors/boundaryintelligentcontrol-vendors.yml
  title: ''
  type: Vendors
  url: vendors/boundaryintelligentcontrol-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.boundarycontrol.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.boundarycontrol.com/privacy
- group: start
  title: ''
  type: Login
  url: https://www.boundarycontrol.com/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boundaryintelligentcontrol/refs/heads/main/security/boundaryintelligentcontrol-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/boundaryintelligentcontrol-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boundaryintelligentcontrol/refs/heads/main/security/boundaryintelligentcontrol-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/boundaryintelligentcontrol-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boundaryintelligentcontrol/refs/heads/main/security/boundaryintelligentcontrol-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boundaryintelligentcontrol-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.boundarycontrol.com
coverage:
  checked: '2026-10-03'
  detail: OpenAPI spec endpoints on api.boundarycontrol.com and www.boundarycontrol.com all return HTTP 403, providing no machine‑readable contract.
  evidence:
  - status: 403
    url: https://api.boundarycontrol.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-03'
description: Boundary provides runtime context governance for enterprise AI, enabling organizations to control what business context AI systems can access before sensitive data reaches the model. Their platform offers field-level classification, fail-closed design, and integrates with various enterprise tools to ensure data privacy and compliance across AI deployments.
image: https://boundarycontrol.com/og-image.png
layout: provider
modified: '2026-10-03'
name: Boundaryintelligentcontrol
nav: Providers
network: true
overview: Boundaryintelligentcontrol is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Governance, Privacy, Enterprise, and Platform.
random_paper: 4
score:
  band: emerging
  composite: 17.3
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
    developer_ergonomics: 0.0
    discoverability: 48.2
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
  name: Boundaryintelligentcontrol Domain Security
  slug: boundaryintelligentcontrol-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Boundaryintelligentcontrol Vulnerability Disclosure
  slug: boundaryintelligentcontrol-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Boundaryintelligentcontrol Trust Center
  slug: boundaryintelligentcontrol-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: boundaryintelligentcontrol
tags:
- Artificial Intelligence
- Governance
- Privacy
- Enterprise
- Platform
website: https://www.boundarycontrol.com
---
