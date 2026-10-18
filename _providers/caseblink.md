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
- description: CaseBlink provides AI‑powered automation for immigration law firms via its platform.
  name: CaseBlink API
  slug: caseblink-api
artifact_total: 3
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/caseblink/refs/heads/main/vendors/caseblink-vendors.yml
  title: ''
  type: Vendors
  url: vendors/caseblink-vendors.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/caseblink/refs/heads/main/plans/caseblink-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/caseblink-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/caseblink/refs/heads/main/conformance/caseblink-conformance.yml
  title: ''
  type: Conformance
  url: conformance/caseblink-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/caseblink/refs/heads/main/llms/caseblink-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/caseblink-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/caseblink/refs/heads/main/well-known/caseblink-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/caseblink-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/caseblink/refs/heads/main/well-known/caseblink-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/caseblink-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/caseblink/refs/heads/main/hosts/caseblink-hosts.yml
  title: ''
  type: Hosts
  url: hosts/caseblink-hosts.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.caseblink.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.caseblink.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/caseblink/refs/heads/main/security/caseblink-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/caseblink-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.caseblink.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.caseblink.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.caseblink.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://www.caseblink.com/start-now
- group: operate
  title: ''
  type: Support
  url: https://www.caseblink.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.caseblink.com/resources/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.caseblink.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.caseblink.com/terms-of-service
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://www.caseblink.com/
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: CaseBlink provides AI-powered automation for immigration law firms, enabling faster case preparation, document organization, and form filing. Their platform offers tools like autopilot case assembly, AI research, and form auto‑completion, helping practitioners prepare petitions up to four times faster while reducing manual hours. The service includes a product suite, pricing plans, and resources for law firms seeking to modernize immigration case workflows.
image: https://storage.readdy-site.link/project_files/40d6c2db-2947-4b9f-b17f-ebc8352818fa/ec14c07d-d7a4-4644-9bae-f36f12894b20_Untitled-design-22.png?v=0c3c52dd917edcde7d31c2276d2124e1
layout: provider
modified: '2026-10-07'
name: CaseBlink
nav: Providers
network: true
overview: 'CaseBlink is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Immigration, Legal Tech, and Automation.


  CaseBlink''s developer surface includes documentation, pricing, getting-started guide, support, engineering blog, and 13 more developer resources.'
plans:
- name: Caseblink Plans Pricing
  plan_count: 4
  slug: caseblink-plans-pricing
random_paper: 16
score:
  band: thin
  composite: 31.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 71.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 64.3
    operational_transparency: 15.8
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Caseblink Domain Security
  slug: caseblink-domain-security
  summary_line: TLSv1.3 · DMARC
slug: caseblink
tags:
- Company
- Artificial Intelligence
- Immigration
- Legal Tech
- Automation
website: https://www.caseblink.com/
---
