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
api_count: 1
apis:
- description: API for Custosa runtime data‑control plane
  name: Custosa API
  slug: custosa-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: Security
  url: https://custosa.com/security-policy
- group: auth
  title: ''
  type: Compliance
  url: https://custosa.com/trust.html
- group: design
  href: https://artifacts.apis.io/custosa-com/conformance/custosa-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/custosa-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/custosa-com/llms/custosa-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/custosa-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/custosa-com/well-known/custosa-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/custosa-com-security.txt
- group: agent
  href: https://artifacts.apis.io/custosa-com/well-known/custosa-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/custosa-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/custosa-com/hosts/custosa-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/custosa-com-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://custosa.com/login
- group: auth
  href: https://artifacts.apis.io/custosa-com/security/custosa-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/custosa-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/custosa-com/security/custosa-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/custosa-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/custosa-com/security/custosa-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/custosa-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://custosa.com/
- group: docs
  title: ''
  type: Documentation
  url: https://custosa.com/docs.html
- group: start
  title: ''
  type: GettingStarted
  url: https://custosa.com/learn.html
- group: operate
  title: ''
  type: Support
  url: https://custosa.com/contact.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://custosa.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://custosa.com/privacy.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Custosa-Inc
coverage:
  checked: '2026-11-04'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract found on discovered hosts.
  evidence:
  - status: 0
    url: https://api.custosa.com/openapi.json
  - status: 0
    url: https://api.custosa.com/openapi.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Custosa provides a runtime data‑control plane for enterprise AI, inspecting every record before it reaches the model, redacting by role, and sealing each decision as verifiable evidence. It supports HIPAA‑compliant AI, financial‑services safeguards, and permission‑aware retrieval, helping organisations govern AI data securely and transparently.
image: https://custosa.com/og-default.png
layout: provider
modified: '2026-11-04'
name: Custosa
nav: Providers
network: true
overview: 'Custosa is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Data Governance, Security, Healthcare, and Finance.


  Custosa''s developer surface includes documentation, getting-started guide, support, and 15 more developer resources.'
random_paper: 6
score:
  band: thin
  composite: 26.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 22.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Custosa Com Domain Security
  slug: custosa-com-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Custosa Com Vulnerability Disclosure
  slug: custosa-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Custosa Com Trust Center
  slug: custosa-com-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, FedRAMP
slug: custosa-com
tags:
- Artificial Intelligence
- Data Governance
- Security
- Healthcare
- Finance
website: https://custosa.com/
---
