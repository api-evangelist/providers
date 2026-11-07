---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://wodan.ai/responsible-disclosure
- group: agent
  href: https://artifacts.apis.io/wodan-ai/llms/wodan-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wodan-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/wodan-ai/well-known/wodan-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/wodan-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/wodan-ai/well-known/wodan-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/wodan-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/wodan-ai/hosts/wodan-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wodan-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/wodan-ai/vendors/wodan-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/wodan-ai-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://wodan.ai/trust/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.wodan.ai/
- group: auth
  href: https://artifacts.apis.io/wodan-ai/security/wodan-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/wodan-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/wodan-ai/security/wodan-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wodan-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wodan.ai
- group: docs
  title: ''
  type: Documentation
  url: https://wodan.ai/about/
- group: company
  title: ''
  type: Blog
  url: https://wodan.ai/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wodan.ai/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wodan.ai/legal-advice/
coverage:
  checked: '2026-10-25'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, or other machine-readable contracts were found.
  evidence:
  - status: 200
    url: https://dev.wodan.ai/
  - status: 200
    url: https://docs.wodan.ai/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-25'
description: Wodan AI provides zero‑trust AI solutions that run machine‑learning models on encrypted data without ever decrypting it. By leveraging advanced cryptographic techniques, the platform enables enterprises to extract insights from sensitive information while preserving privacy and complying with regulations such as GDPR and the EU AI Act. Their services target identity verification, financial services, industrial IP protection, and broader AI‑driven analytics, offering a secure, collaborative environment for data‑intensive workloads.
layout: provider
modified: '2026-10-25'
name: Wodan AI
nav: Providers
network: true
overview: 'Wodan AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Zero Trust, Encryption, and Privacy.


  Wodan AI''s developer surface includes documentation, engineering blog, and 13 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.5
  facets:
    access_clarity: 14.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 51.8
    operational_transparency: 5.3
  previous_composite: 17.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/wodan-ai/wodan-ai-2026-11-03T150223.png
security:
- kind: domain-security
  name: Wodan Ai Domain Security
  slug: wodan-ai-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Wodan Ai Vulnerability Disclosure
  slug: wodan-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: wodan-ai
tags:
- Company
- Artificial Intelligence
- Zero Trust
- Encryption
- Privacy
- Financial Services
website: https://wodan.ai
---
