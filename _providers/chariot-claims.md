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
  href: https://raw.githubusercontent.com/api-evangelist/chariot-claims/refs/heads/main/security/chariot-claims-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/chariot-claims-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chariot-claims/refs/heads/main/well-known/chariot-claims-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/chariot-claims-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chariot-claims/refs/heads/main/well-known/chariot-claims-chariotclaims-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/chariot-claims-chariotclaims-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chariot-claims/refs/heads/main/well-known/chariot-claims-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/chariot-claims-app-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chariot-claims/refs/heads/main/well-known/chariot-claims-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chariot-claims-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chariot-claims/refs/heads/main/hosts/chariot-claims-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chariot-claims-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.chariotclaims.com/terms
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chariot-claims/refs/heads/main/security/chariot-claims-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/chariot-claims-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chariot-claims/refs/heads/main/security/chariot-claims-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chariot-claims-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.chariotclaims.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chariotclaims.com/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://app.chariotclaims.com/sign-in
coverage:
  checked: '2026-10-08'
  detail: No public developer program or API documentation is offered; attempts to fetch OpenAPI spec at https://api.chariotclaims.com/openapi.json returned 404.
  evidence:
  - status: 404
    url: https://api.chariotclaims.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-08'
description: Chariot Claims provides a platform that helps consumers discover, file, and receive compensation for claims against corporations. It connects users with vetted law firms, offers a no‑upfront‑cost model, and aims to make justice accessible through a simple online process.
image: https://framerusercontent.com/assets/xzu1WKxjBkOLCiSnhgQslpLTcno.png
layout: provider
modified: '2026-10-08'
name: Chariot Claims
nav: Providers
network: true
overview: 'Chariot Claims is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Legal Tech, Claims, and ConsumerProtection.


  Chariot Claims'' developer surface includes signup flow and 11 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 13.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 17.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chariot Claims Domain Security
  slug: chariot-claims-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Chariot Claims Vulnerability Disclosure
  slug: chariot-claims-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: chariot-claims
tags:
- Company
- Insurance
- Legal Tech
- Claims
- ConsumerProtection
website: https://www.chariotclaims.com/
---
