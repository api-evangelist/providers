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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/qognify-com/llms/qognify-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/qognify-com-llms.txt
- group: other
  href: https://artifacts.apis.io/qognify-com/hosts/qognify-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/qognify-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/qognify-com/vendors/qognify-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/qognify-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.octave.com/industries/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.octave.com/about/newsroom
- group: other
  title: ''
  type: Leadership
  url: https://www.octave.com/about/leadership
- group: auth
  href: https://artifacts.apis.io/qognify-com/security/qognify-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/qognify-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.qognify.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.qognify.com/
- group: operate
  title: ''
  type: Support
  url: https://www.octave.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.octave.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.octave.com/legal/privacy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.qognify.com/mcp
coverage:
  checked: '2026-10-29'
  detail: No public API documentation or machine‑readable spec was found; attempts to fetch common OpenAPI endpoints returned 404 or redirects.
  evidence:
  - status: 301
    url: https://www.qognify.com/openapi.json
  - status: 0
    url: https://api.qognify.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Qognify provides public‑safety and physical‑security software solutions, including video analytics and AI‑driven incident response tools. After being acquired by Octave, its web presence redirects to Octave’s Coda product page. The company maintains a status page, support portal, privacy policy, terms of service, and leadership information hosted on Octave’s domain. Qognify’s offerings target enterprise security operations, integrating with existing surveillance infrastructure.
image: https://www.octave.com/_og/d/c_Default,title_Octave+Coda+Physical+Security+Software,description_~Q29kYSBhZHZhbmNlZCBwaHlzaWNhbCBzZWN1cml0eSBzb2Z0d2FyZSBlbXBvd2VycyBlbnRlcnByaXNlIG9yZ2FuaXphdGlvbnMgdG8gZGV0ZWN0LCBjb21tYW5kLCBjb250cm9sIGFuZCBjb2xsYWJvcmF0ZS4,q_eyJ1dG1fZWFzeXJlZGlyIjoid3d3LnFvZ25pZnkuY29tIn0,p_Ii9wcm9kdWN0cy9wdWJsaWMtc2FmZXR5LXBoeXNpY2FsLXNlY3VyaXR5L2NvZGEi.png?_query=%7B%22utm_easyredir%22:%22www.qognify.com%22%7D
layout: provider
modified: '2026-10-29'
name: Qognify
nav: Providers
network: true
overview: 'Qognify is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include PublicSafety, PhysicalSecurity, VideoAnalytics, AI, and Enterprise.


  Qognify''s developer surface includes support and 12 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 15.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 51.8
    operational_transparency: 26.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Qognify Com Domain Security
  slug: qognify-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: qognify-com
tags:
- PublicSafety
- PhysicalSecurity
- VideoAnalytics
- AI
- Enterprise
website: https://www.qognify.com/
---
