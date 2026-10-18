---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.9
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 10
  human_in_the_loop: 2
  name: Esendex Agentic Access
  operation_count: 16
  slug: esendex-agentic-access
  summary_line: 16 operations · 10 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.esendex.com
  baseurl_source: declared
  description: The Credential Management API from Esendex — 6 operation(s) for credential management.
  name: Esendex Credential Management API
  slug: esendex-credential-management-api
- baseURL: https://api.esendex.com
  baseurl_source: declared
  description: The Message Dispatcher API from Esendex — 2 operation(s) for message dispatcher.
  name: Esendex Message Dispatcher API
  slug: esendex-message-dispatcher-api
- baseURL: https://api.esendex.com
  baseurl_source: declared
  description: The Message Headers API from Esendex — 3 operation(s) for message headers.
  name: Esendex Message Headers API
  slug: esendex-message-headers-api
artifact_total: 14
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/esendex/refs/heads/main/agentic-access/esendex-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/esendex-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/esendex/refs/heads/main/rules/esendex-rules.yml
  title: ''
  type: Spectral
  url: rules/esendex-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/esendex/refs/heads/main/json-ld/esendex-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/esendex-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/esendex/refs/heads/main/vocabulary/esendex-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/esendex-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/esendex/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/esendex/refs/heads/main/data-model/esendex-data-model.yml
  title: ''
  type: DataModel
  url: data-model/esendex-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/esendex/refs/heads/main/errors/esendex-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/esendex-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/esendex/refs/heads/main/conformance/esendex-conformance.yml
  title: ''
  type: Conformance
  url: conformance/esendex-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/esendex/refs/heads/main/hosts/esendex-hosts.yml
  title: ''
  type: Hosts
  url: hosts/esendex-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/esendex/refs/heads/main/vendors/esendex-vendors.yml
  title: ''
  type: Vendors
  url: vendors/esendex-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/esendex/refs/heads/main/packages/esendex-packages.yml
  title: ''
  type: SDKs
  url: packages/esendex-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/esendex/refs/heads/main/packages/esendex-packages.yml
  title: ''
  type: Packages
  url: packages/esendex-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.esendex.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/esendex/refs/heads/main/authentication/esendex-authentication.yml
  title: ''
  type: Authentication
  url: authentication/esendex-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/esendex/refs/heads/main/security/esendex-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/esendex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.esendex.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.esendex.co.uk/developers/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.esendex.co.uk/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://www.esendex.co.uk/developers/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.esendex.co.uk/developers/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.esendex.co.uk/pricing/
- group: operate
  title: ''
  type: Support
  url: https://www.esendex.co.uk/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.esendex.co.uk/blog/
created: '2026-10-13'
description: Esendex provides global business SMS and multichannel messaging services, offering APIs for SMS, WhatsApp, RCS, Email, Voice and more. It serves enterprises across multiple countries, enabling messaging, notifications, two‑factor authentication, digital letters and chatbot integration through a unified platform.
json_schemas:
- name: ApiResponseOfCreateCredentialResponse
  property_count: 0
  slug: esendex-api-response-of-create-credential-response
- name: ApiResponseOfGetCredentialsResponse
  property_count: 0
  slug: esendex-api-response-of-get-credentials-response
- name: ApiResponseOfGetSessionsResponse
  property_count: 0
  slug: esendex-api-response-of-get-sessions-response
- name: ApiResponseOfUserCredential
  property_count: 0
  slug: esendex-api-response-of-user-credential
- name: CreateCredentialRequest
  property_count: 8
  slug: esendex-create-credential-request
- name: messages
  property_count: 9
  slug: esendex-messages
jsonld:
- class_count: 14
  name: Esendex Context
  property_count: 27
  slug: esendex-context
layout: provider
modified: '2026-10-13'
name: Esendex
nav: Providers
network: true
overview: 'Esendex publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Credential Management API, Message Dispatcher API, and Message Headers API. Tagged areas include SMS, Messaging, Communications, and Business.


  The Esendex catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Esendex''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, support, engineering blog, and 16 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Esendex API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: esendex-rules
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 55.8
    catalog_earned_first_party: 0.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 59.9
    developer_ergonomics: 66.1
    discoverability: 53.6
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 14.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Esendex Authentication
  slug: esendex-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Esendex Domain Security
  slug: esendex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: esendex
tags:
- SMS
- Messaging
- Communications
- Business
website: https://www.esendex.com
---
