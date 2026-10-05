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
  url: https://www.arconnet.com/compliance
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arconnet/refs/heads/main/security/arconnet-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/arconnet-vulnerability-disclosure.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arconnet/refs/heads/main/hosts/arconnet-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arconnet-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arconnet/refs/heads/main/vendors/arconnet-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arconnet-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.arconnet.com/portal/en/home
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arconnet/refs/heads/main/security/arconnet-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/arconnet-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arconnet/refs/heads/main/security/arconnet-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/arconnet-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arconnet/refs/heads/main/security/arconnet-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arconnet-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.arconnet.com
created: '2026-10-03'
description: ARCON provides runtime privilege security solutions that enforce just‑in‑time and just‑enough access for users, machines, and AI agents. Their platform evaluates identity, context, policy, and risk in real time to grant minimum necessary privileges, monitor usage, and automatically revoke access. ARCON serves enterprises across banking, telecom, utilities, government, healthcare, and education, helping reduce identity risk, accelerate compliance, and simplify governance through dynamic privilege lifecycle management.
image: https://cms.arconnet.com/wp-content/uploads/2026/08/Vertical_Logo_Full_JPEG.jpg
layout: provider
modified: '2026-10-03'
name: ARCON
nav: Providers
network: true
overview: 'ARCON is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Identity, Access Control, and Enterprise.


  ARCON''s developer surface includes support and 8 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Arconnet Domain Security
  slug: arconnet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Arconnet Vulnerability Disclosure
  slug: arconnet-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Arconnet Trust Center
  slug: arconnet-trust-center
  summary_line: SOC 2, PCI DSS, HIPAA, GDPR
slug: arconnet
tags:
- Company
- Security
- Identity
- Access Control
- Enterprise
website: https://www.arconnet.com
---
