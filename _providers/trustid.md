---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trustid-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/trustid-llms.txt
- group: company
  title: ''
  type: Website
  url: https://trustid.com
created: '2026-07-17'
description: TRUSTID was a Portland, Oregon telephone caller-authentication and call-center anti-fraud company led by CEO Patrick Cox, authenticating inbound callers pre-answer without knowledge-based interrogation of the caller. Surfaced as a portfolio company of Norwest Venture Partners and Trinity Ventures, TRUSTID was acquired by Neustar (closed January 2019), and Neustar was itself acquired by TransUnion in December 2021, where the caller-authentication capability lives on in Trusted Call Solutions. TRUSTID no longer operates independently and publishes no public API surface — trustid.com is unresponsive and www.trustid.com returns HTTP 503 from Neustar redirect infrastructure.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trustid.png
layout: provider
modified: '2026-07-21'
name: Trustid
nav: Providers
network: true
overview: Trustid is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Caller Authentication, Identity, Fraud Prevention, and Call Centers.
random_paper: 6
score:
  band: minimal
  composite: 2.6
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 2.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Trustid Domain Security
  slug: trustid-domain-security
  summary_line: DMARC
slug: trustid
tags:
- Company
- Caller Authentication
- Identity
- Fraud Prevention
- Call Centers
- Telecommunications
- Acquired
website: https://trustid.com
---
