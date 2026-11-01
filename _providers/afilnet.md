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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/afilnet/hosts/afilnet-hosts.yml
  title: ''
  type: Hosts
  url: hosts/afilnet-hosts.yml
- group: build
  href: https://artifacts.apis.io/afilnet/packages/afilnet-packages.yml
  title: ''
  type: SDKs
  url: packages/afilnet-packages.yml
- group: build
  href: https://artifacts.apis.io/afilnet/packages/afilnet-packages.yml
  title: ''
  type: Packages
  url: packages/afilnet-packages.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.afilnet.com/en/client/register/
- group: auth
  title: ''
  type: Security
  url: https://www.afilnet.com/en/solutions/security/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Afilnet
- group: auth
  href: https://artifacts.apis.io/afilnet/security/afilnet-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/afilnet-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.afilnet.com/en/
- group: docs
  title: ''
  type: Documentation
  url: https://www.afilnet.com/en/api/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.afilnet.com/en/bulk-sms/price/
- group: operate
  title: ''
  type: Support
  url: https://www.afilnet.com/en/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.afilnet.com/en/privacy-policy/
coverage:
  checked: '2026-10-19'
  detail: API documentation pages are rendered with JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://www.afilnet.com/es/sms-api/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-19'
description: Afilnet provides a cloud communications platform that enables businesses to send bulk SMS, automated voice calls, certified email and SMS, and manage two‑factor authentication via a RESTful API. The service includes pricing plans, a developer portal with API documentation, and tools for creating contracts and digital signatures. It targets enterprises needing reliable messaging, compliance‑grade certifications, and integration with web chat, WhatsApp Business, and email marketing.
layout: provider
modified: '2026-10-19'
name: Afilnet
nav: Providers
network: true
overview: 'Afilnet is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Communications, SMS, Voice, and Email.


  Afilnet''s developer surface includes signup flow, documentation, pricing, support, and 8 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 44.6
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Afilnet Domain Security
  slug: afilnet-domain-security
  summary_line: TLSv1.3 · DMARC
slug: afilnet
tags:
- Company
- Communications
- SMS
- Voice
- Email
- Two Factor
website: https://www.afilnet.com/en/
---
