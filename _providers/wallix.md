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
  score: 14.4
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/wallix/refs/heads/main/llms/wallix-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wallix-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/wallix/refs/heads/main/well-known/wallix-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/wallix-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/wallix/refs/heads/main/hosts/wallix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wallix-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/wallix/refs/heads/main/packages/wallix-packages.yml
  title: ''
  type: SDKs
  url: packages/wallix-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/wallix/refs/heads/main/packages/wallix-packages.yml
  title: ''
  type: Packages
  url: packages/wallix-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wallix.com/legal-notice/
- group: operate
  title: ''
  type: Support
  url: https://www.wallix.com/support-services/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wallix.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wallix
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/wallix/refs/heads/main/security/wallix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wallix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wallix.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://partner.wallix.com/api/mcp
  reason: no-developer-program
  state: none
created: '2026-10-03'
description: WALLIX provides privileged access management, identity and access governance solutions for enterprises. The company focuses on securing privileged accounts, remote access, and zero‑trust architectures across on‑premises, cloud and OT environments. Founded in France, WALLIX serves global customers in finance, healthcare, critical infrastructure and other regulated sectors, offering products such as WALLIX PAM, Privileged Remote Access, and Web Session Manager. The platform integrates with major IAM solutions and supports compliance with standards like DORA, IEC 62443, and NIS2.
image: https://www.wallix.com/wp-content/uploads/2024/03/Preview-WALLIX-logo.png
layout: provider
modified: '2026-10-03'
name: WALLIX
nav: Providers
network: true
overview: 'WALLIX is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Privileged Access, Identity, Cybersecurity, and Enterprise.


  WALLIX''s developer surface includes support and 10 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 13.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 55.4
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Wallix Domain Security
  slug: wallix-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: wallix
tags:
- Company
- Privileged Access
- Identity
- Cybersecurity
- Enterprise
- Cloud
website: https://www.wallix.com
---
