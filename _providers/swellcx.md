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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Swell provides an AI‑powered healthcare reputation management platform. The API documentation is not publicly available as a machine‑readable specification.
  name: Swell API
  slug: swell-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/swellcx/llms/swellcx-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/swellcx-llms.txt
- group: other
  href: https://artifacts.apis.io/swellcx/hosts/swellcx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/swellcx-hosts.yml
- group: other
  href: https://artifacts.apis.io/swellcx/vendors/swellcx-vendors.yml
  title: ''
  type: Vendors
  url: vendors/swellcx-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.swellcx.com/
- group: start
  title: ''
  type: Login
  url: https://platform.swellcx.com/auth/login
- group: auth
  href: https://artifacts.apis.io/swellcx/security/swellcx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/swellcx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://swellcx.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.swellcx.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.swellcx.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://support.swellcx.com/en/knowledge
- group: company
  title: ''
  type: Blog
  url: https://www.swellcx.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.swellcx.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.swellcx.com/legal/privacy-policy
coverage:
  checked: '2026-10-28'
  detail: The provider's documentation pages do not expose a machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec.
  evidence:
  - status: 404
    url: https://api.swellcx.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Swell provides an AI‑powered healthcare reputation management and patient experience platform for multi‑location healthcare groups. It centralizes operational visibility, automates review invitations, gathers patient and employee feedback, and offers AI‑generated, HIPAA‑compliant responses. The solution supports various specialties, integrates with major EHR/PMS systems, and includes tools for reputation monitoring, employee NPS, and analytics across clinics.
layout: provider
modified: '2026-10-28'
name: Swell
nav: Providers
network: true
overview: 'Swell is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Healthcare, Reputation, and PatientExperience.


  Swell''s developer surface includes documentation, pricing, support, engineering blog, and 9 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 19.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 14.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Swellcx Domain Security
  slug: swellcx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: swellcx
tags:
- Company
- AI
- Healthcare
- Reputation
- PatientExperience
website: https://swellcx.com/
---
