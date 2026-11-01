---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 69
  human_in_the_loop: 16
  name: Ozonetel Agentic Access
  operation_count: 97
  slug: ozonetel-agentic-access
  summary_line: 97 operations · 69 acting · 16 human-in-the-loop
api_count: 93
apis:
- baseURL_template: https://{domainname}/
  baseurl_source: spec_template
  description: The Agent API from Ozonetel — 3 operation(s) for agent.
  name: Ozonetel Agent API
  slug: ozonetel-agent-api
- baseURL_template: https://{domainname}/
  baseurl_source: spec_template
  description: The AHT API from Ozonetel — 1 operation(s) for aht.
  name: Ozonetel AHT API
  slug: ozonetel-aht-api
- baseURL_template: https://{domainname}/
  baseurl_source: spec_template
  description: The Campaign API from Ozonetel — 4 operation(s) for campaign.
  name: Ozonetel Campaign API
  slug: ozonetel-campaign-api
- baseURL_template: https://{domainname}/
  baseurl_source: spec_template
  description: The Campaign Reports API from Ozonetel — 1 operation(s) for campaign reports.
  name: Ozonetel Campaign Reports API
  slug: ozonetel-campaign-reports-api
- baseURL_template: https://{domainname}/
  baseurl_source: spec_template
  description: The Chat Campaign API from Ozonetel — 1 operation(s) for chat campaign.
  name: Ozonetel Chat Campaign API
  slug: ozonetel-chat-campaign-api
- baseURL_template: https://{domainname}/
  baseurl_source: spec_template
  description: The default API from Ozonetel — 36 operation(s) for default.
  name: Ozonetel Default API
  slug: ozonetel-default-api
- baseURL_template: https://{domainname}/
  baseurl_source: spec_template
  description: The Disposition API from Ozonetel — 1 operation(s) for disposition.
  name: Ozonetel Disposition API
  slug: ozonetel-disposition-api
- baseURL_template: https://{domainname}/
  baseurl_source: spec_template
  description: The Reports API from Ozonetel — 1 operation(s) for reports.
  name: Ozonetel Reports API
  slug: ozonetel-reports-api
- baseURL: https://smsapi1.ozonetel.com/
  baseurl_source: declared
  description: The SMS API from Ozonetel — 1 operation(s) for sms.
  name: Ozonetel SMS API
  slug: ozonetel-sms-api
artifact_total: 13
common:
- group: other
  href: https://artifacts.apis.io/ozonetel/vendors/ozonetel-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ozonetel-vendors.yml
- group: agent
  href: https://artifacts.apis.io/ozonetel/agentic-access/ozonetel-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ozonetel-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/ozonetel/rules/ozonetel-rules.yml
  title: ''
  type: Spectral
  url: rules/ozonetel-rules.yml
- group: design
  href: https://artifacts.apis.io/ozonetel/vocabulary/ozonetel-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ozonetel-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ozonetel/errors/ozonetel-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ozonetel-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ozonetel/conformance/ozonetel-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ozonetel-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ozonetel/llms/ozonetel-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ozonetel-llms.txt
- group: other
  href: https://artifacts.apis.io/ozonetel/hosts/ozonetel-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ozonetel-hosts.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://ozonetel.com/trust/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ozonetel.com/terms-conditions/
- group: operate
  title: ''
  type: Support
  url: https://ozonetel.com/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ozonetel.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ozonetel.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://ozonetel.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.ozonetel.com/
- group: auth
  href: https://artifacts.apis.io/ozonetel/authentication/ozonetel-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ozonetel-authentication.yml
- group: auth
  href: https://artifacts.apis.io/ozonetel/security/ozonetel-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ozonetel-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ozonetel.com/
coverage:
  checked: '2026-10-28'
  detail: Provider documentation does not expose a machine‑readable OpenAPI/GraphQL/AsyncAPI spec.
  evidence:
  - status: 200
    url: https://docs.ozonetel.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Ozonetel provides a unified customer experience (CX) platform that powers over 300,000 agents to handle more than 7 billion customer interactions each year across voice, messaging, email, and social channels. Trusted by 3,500+ customers, the cloud‑based solution offers omnichannel routing, AI‑driven analytics, and scalable contact‑center capabilities for enterprises worldwide.
image: https://ozonetel.com/wp-content/uploads/2025/05/Picture8.png
layout: provider
modified: '2026-10-28'
name: Ozonetel
nav: Providers
network: true
overview: 'Ozonetel publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent API, AHT API, Campaign API, and 6 more. Tagged areas include Company, CX Platform, Cloud Communications, Contact Center, and API.


  The Ozonetel catalog on APIs.io includes 1 Spectral governance ruleset.


  Ozonetel''s developer surface includes support, engineering blog, documentation, authentication, and 14 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Ozonetel API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: ozonetel-rules
score:
  band: thin
  composite: 34.3
  coverage:
    artifact_dirs: 14
    catalog_earned: 35.8
    catalog_earned_first_party: 0.0
    catalog_gap: 79.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    contract_governance: 22.0
    contract_quality: 42.6
    developer_ergonomics: 28.6
    discoverability: 53.6
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 9
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ozonetel Authentication
  slug: ozonetel-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Ozonetel Domain Security
  slug: ozonetel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ozonetel
tags:
- Company
- CX Platform
- Cloud Communications
- Contact Center
- API
website: https://ozonetel.com/
---
