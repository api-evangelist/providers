---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/spocont-com/well-known/spocont-com-ifrcoworker-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/spocont-com-ifrcoworker-security.txt
- group: auth
  title: ''
  type: Security
  url: https://ifrcoworker.app/terms
- group: agent
  href: https://artifacts.apis.io/spocont-com/llms/spocont-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/spocont-com-llms.txt
- group: other
  href: https://artifacts.apis.io/spocont-com/a2a/spocont-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/spocont-com-a2a.yml
- group: auth
  href: https://artifacts.apis.io/spocont-com/well-known/spocont-com-vida-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/spocont-com-vida-security.txt
- group: auth
  href: https://artifacts.apis.io/spocont-com/well-known/spocont-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/spocont-com-security.txt
- group: auth
  href: https://artifacts.apis.io/spocont-com/well-known/spocont-com-esign-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/spocont-com-esign-security.txt
- group: auth
  href: https://artifacts.apis.io/spocont-com/well-known/spocont-com-docu-scan-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/spocont-com-docu-scan-security.txt
- group: agent
  href: https://artifacts.apis.io/spocont-com/well-known/spocont-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/spocont-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/spocont-com/hosts/spocont-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/spocont-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/spocont-com/security/spocont-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/spocont-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/spocont-com/security/spocont-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/spocont-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://spocont.com/
coverage:
  checked: '2026-10-30'
  detail: OpenAPI spec URLs returned redirects with no spec content.
  evidence:
  - status: 302
    url: https://spocont.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Spocont.com is a technology company that provides a platform for managing and automating contact center operations. The service offers tools for integrating communication channels, routing interactions, and analyzing performance metrics to improve customer service efficiency. It targets enterprises seeking scalable, cloud‑based contact center solutions with robust API access for custom workflows and third‑party integrations.
image: https://reservoprix.com/spocontLogo.png
layout: provider
modified: '2026-10-30'
name: spocont-com
nav: Providers
network: true
overview: spocont-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, ContactCenter, Automation, CloudPlatform, and API.
random_paper: 10
score:
  band: minimal
  composite: 6.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
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
    score: 17.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Spocont Com Domain Security
  slug: spocont-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Spocont Com Vulnerability Disclosure
  slug: spocont-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: spocont-com
tags:
- Company
- ContactCenter
- Automation
- CloudPlatform
- API
website: https://spocont.com/
---
