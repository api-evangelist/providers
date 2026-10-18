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
api_count: 1
apis:
- description: Censinet RiskOps API for healthcare vendors and partners
  name: Censinet API
  slug: censinet-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/censinet/refs/heads/main/llms/censinet-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/censinet-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/censinet/refs/heads/main/well-known/censinet-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/censinet-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/censinet/refs/heads/main/well-known/censinet-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/censinet-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/censinet/refs/heads/main/hosts/censinet-hosts.yml
  title: ''
  type: Hosts
  url: hosts/censinet-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/censinet/refs/heads/main/vendors/censinet-vendors.yml
  title: ''
  type: Vendors
  url: vendors/censinet-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.censinet.com/en/
- group: company
  title: ''
  type: Newsroom
  url: https://www.censinet.com/company/news
- group: other
  title: ''
  type: Leadership
  url: https://www.censinet.com/company/leadership
- group: start
  title: ''
  type: GettingStarted
  url: https://help.censinet.com/en/articles/8166619-getting-started-with-censinet-for-vendors-affiliates-and-partners
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Censinet
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/censinet/refs/heads/main/security/censinet-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/censinet-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.censinet.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.censinet.com/resources
- group: company
  title: ''
  type: Blog
  url: https://www.censinet.com/resources/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.censinet.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.censinet.com/privacy-policy
coverage:
  checked: '2026-10-08'
  detail: API documentation requires login and is rendered via JavaScript, preventing automated discovery.
  evidence:
  - status: 200
    url: https://help.censinet.com/en/articles/8166619-getting-started-with-censinet-for-vendors-affiliates-and-partners.md
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-07'
description: Censinet provides purpose‑built solutions to reduce risk in healthcare organizations. Their platform offers third‑party risk management, enterprise risk oversight, systemic risk remediation, AI governance, and peer benchmarking to help healthcare providers secure data, comply with regulations, and improve cybersecurity maturity across the ecosystem.
image: https://cdn.prod.website-files.com/63bc855e7cb1897eeb806ea7/64999d7e628c4483a79a913d_Censinet%20Open%20Graph%203.jpg
layout: provider
modified: '2026-10-07'
name: Censinet
nav: Providers
network: true
overview: 'Censinet is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Risk Management, Cybersecurity, and AI Governance.


  Censinet''s developer surface includes support, getting-started guide, documentation, engineering blog, and 12 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 67.9
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Censinet Domain Security
  slug: censinet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: censinet
tags:
- Company
- Healthcare
- Risk Management
- Cybersecurity
- AI Governance
website: https://www.censinet.com/
---
