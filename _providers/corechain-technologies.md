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
artifact_total: 1
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/corechain-technologies/refs/heads/main/conformance/corechain-technologies-conformance.yml
  title: ''
  type: Conformance
  url: conformance/corechain-technologies-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/corechain-technologies/refs/heads/main/hosts/corechain-technologies-hosts.yml
  title: ''
  type: Hosts
  url: hosts/corechain-technologies-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/corechain-technologies/refs/heads/main/security/corechain-technologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/corechain-technologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://corechain.tech
- group: docs
  title: ''
  type: Documentation
  url: https://corechain.tech/solutions
- group: company
  title: ''
  type: Partners
  url: https://corechain.tech/partners
- group: other
  title: ''
  type: Company
  url: https://corechain.tech/company
- group: company
  title: ''
  type: Careers
  url: https://corechain.tech/careers
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://corechain.tech/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://corechain.tech/legal/terms-of-service
coverage:
  checked: '2026-10-11'
  detail: The site provides marketing pages but no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://corechain.tech/solutions
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-10'
description: CoreChain Technologies provides a scalable, secure B2B payments network and supply chain finance solutions. With over $1 billion in payments processed, the platform integrates with major ERPs, offers working‑capital lines, and is SOC‑2 compliant, targeting enterprises seeking to reduce fraud, lower operating costs, and automate vendor payments.
image: https://corechain.tech/_next/static/media/ogLogo.6c7df144.png
layout: provider
modified: '2026-10-10'
name: CoreChain Technologies
nav: Providers
network: true
overview: 'CoreChain Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Fintech, B2B, and Supply Chain.


  CoreChain Technologies'' developer surface includes documentation and 9 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.0
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Corechain Technologies Domain Security
  slug: corechain-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: corechain-technologies
tags:
- Company
- Payments
- Fintech
- B2B
- Supply Chain
website: https://corechain.tech
---
