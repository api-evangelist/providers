---
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 35.4
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Axuall Agentic Access
  operation_count: 43
  slug: axuall-agentic-access
  summary_line: 43 operations · 14 acting
api_count: 1
apis:
- baseURL: https://api.axuall.net
  baseurl_source: declared
  description: The Actor API from Axuall — 1 operation(s) for actor.
  name: Axuall Actor API
  slug: axuall-actor-api
- baseURL: https://api.axuall.net
  baseurl_source: declared
  description: The Address Deduplications API from Axuall — 2 operation(s) for address deduplications.
  name: Axuall Address Deduplications API
  slug: axuall-address-deduplications-api
- baseURL: https://api.axuall.net
  baseurl_source: declared
  description: The Agent API from Axuall — 6 operation(s) for agent.
  name: Axuall Agent API
  slug: axuall-agent-api
- baseURL: https://api.axuall.net
  baseurl_source: declared
  description: The Authentication API from Axuall — 2 operation(s) for authentication.
  name: Axuall Authentication API
  slug: axuall-authentication-api
- baseURL: https://api.axuall.net
  baseurl_source: declared
  description: The Case Log Artifact API from Axuall — 1 operation(s) for case log artifact.
  name: Axuall Case Log Artifact API
  slug: axuall-case-log-artifact-api
- baseURL: https://api.axuall.net
  baseurl_source: declared
  description: The Documents API from Axuall — 1 operation(s) for documents.
  name: Axuall Documents API
  slug: axuall-documents-api
- baseURL: https://api.axuall.net
  baseurl_source: declared
  description: The Email API from Axuall — 2 operation(s) for email.
  name: Axuall Email API
  slug: axuall-email-api
- baseURL: https://api.axuall.net
  baseurl_source: declared
  description: The Facilities API from Axuall — 1 operation(s) for facilities.
  name: Axuall Facilities API
  slug: axuall-facilities-api
- baseURL: https://api.axuall.net
  baseurl_source: declared
  description: The FSMB Artifact API from Axuall — 1 operation(s) for fsmb artifact.
  name: Axuall FSMB Artifact API
  slug: axuall-fsmb-artifact-api
- baseURL: https://api.axuall.net
  baseurl_source: declared
  description: The Invite API from Axuall — 2 operation(s) for invite.
  name: Axuall Invite API
  slug: axuall-invite-api
- baseURL: https://api.axuall.net
  baseurl_source: declared
  description: The Monitoring reports API from Axuall — 5 operation(s) for monitoring reports.
  name: Axuall Monitoring reports API
  slug: axuall-monitoring-reports-api
- baseURL: https://api.axuall.net
  baseurl_source: declared
  description: The Provider Preview API from Axuall — 2 operation(s) for provider preview.
  name: Axuall Provider Preview API
  slug: axuall-provider-preview-api
- baseURL: https://api.axuall.net
  baseurl_source: declared
  description: The Providers API from Axuall — 13 operation(s) for providers.
  name: Axuall Providers API
  slug: axuall-providers-api
- baseURL: https://api.axuall.net
  baseurl_source: declared
  description: The Recipes API from Axuall — 1 operation(s) for recipes.
  name: Axuall Recipes API
  slug: axuall-recipes-api
- baseURL: https://api.axuall.net
  baseurl_source: declared
  description: The Tasks API from Axuall — 3 operation(s) for tasks.
  name: Axuall Tasks API
  slug: axuall-tasks-api
artifact_total: 28
asyncapis:
- description: ''
  name: Axuall Webhooks
  slug: axuall-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/axuall/refs/heads/main/agentic-access/axuall-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/axuall-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/axuall/refs/heads/main/plans/axuall-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/axuall-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axuall/refs/heads/main/rules/axuall-rules.yml
  title: ''
  type: Spectral
  url: rules/axuall-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axuall/refs/heads/main/json-ld/axuall-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/axuall-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axuall/refs/heads/main/vocabulary/axuall-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/axuall-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/axuall/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axuall/refs/heads/main/asyncapi/axuall-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/axuall-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axuall/refs/heads/main/data-model/axuall-data-model.yml
  title: ''
  type: DataModel
  url: data-model/axuall-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/axuall/refs/heads/main/cli/axuall-cli.yml
  title: ''
  type: CLI
  url: cli/axuall-cli.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/axuall/refs/heads/main/authentication/axuall-authentication.yml
  title: ''
  type: Authentication
  url: authentication/axuall-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axuall/refs/heads/main/errors/axuall-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/axuall-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axuall/refs/heads/main/conformance/axuall-conformance.yml
  title: ''
  type: Conformance
  url: conformance/axuall-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/axuall/refs/heads/main/well-known/axuall-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/axuall-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/axuall/refs/heads/main/well-known/axuall-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/axuall-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/axuall/refs/heads/main/hosts/axuall-hosts.yml
  title: ''
  type: Hosts
  url: hosts/axuall-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/axuall/refs/heads/main/vendors/axuall-vendors.yml
  title: ''
  type: Vendors
  url: vendors/axuall-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.axuall.com/
- group: other
  title: ''
  type: Leadership
  url: https://axuall.com/about-axuall/team
- group: operate
  title: ''
  type: ChangeLog
  url: https://axuall.com/post/whats-new
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/axuall/refs/heads/main/security/axuall-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/axuall-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://axuall.com
- group: docs
  title: ''
  type: Documentation
  url: https://axuall.readme.io
- group: docs
  title: ''
  type: APIReference
  url: https://axuall.readme.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://axuall.readme.io/docs/welcome-to-axuall
- group: operate
  title: ''
  type: Support
  url: https://help.axuall.net/en
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://axuall.com/utility/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://axuall.com/utility/termsofuse
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://axuall.readme.io/mcp
  - status: 403
    url: https://equityzen.com/company/axuall
  reason: partner-login
  state: gated
created: '2026-09-27'
description: Axuall provides a healthcare data network that empowers credentialing teams with AI‑assisted insights. Their platform integrates with enterprise systems to streamline verification of clinicians, reduce administrative workload, and improve patient access. Axuall offers solutions for exploring, confirming, and syncing credential data, targeting hospitals, health systems, and insurers.
json_schemas:
- name: AgentChatRequestSchema
  property_count: 8
  slug: axuall-agent-chat-request-schema
- name: ProviderFile
  property_count: 9
  slug: axuall-provider-file
- name: ProviderProfile
  property_count: 7
  slug: axuall-provider-profile
- name: ProviderRegistrationRequestSchema
  property_count: 27
  slug: axuall-provider-registration-request-schema
- name: ProviderSearchResult
  property_count: 17
  slug: axuall-provider-search-result
- name: SendInviteRequestSchema
  property_count: 21
  slug: axuall-send-invite-request-schema
jsonld:
- class_count: 120
  name: Axuall Context
  property_count: 452
  slug: axuall-context
layout: provider
modified: '2026-09-27'
name: Axuall
nav: Providers
network: true
overview: 'Axuall publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Actor API, Address Deduplications API, Agent API, and 12 more. Tagged areas include Company, Healthcare, Data, Credentialing, and Artificial Intelligence.


  The Axuall catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Axuall''s developer surface includes CLI, authentication, changelog, documentation, API reference, getting-started guide, support, and 20 more developer resources.'
plans:
- name: Axuall Plans Pricing
  plan_count: 3
  slug: axuall-plans-pricing
random_paper: 9
rules:
- effective_rule_count: 55
  extends:
  - spectral:oas
  name: Axuall API Rules
  rule_count: 14
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 2
  slug: axuall-rules
score:
  band: strong
  composite: 57.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 72.8
    catalog_earned_first_party: 12.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 35.6
    contract_quality: 70.6
    developer_ergonomics: 54.2
    discoverability: 64.3
    operational_transparency: 23.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 22.1
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: true
    score: 27.8
security:
- kind: authentication
  name: Axuall Authentication
  slug: axuall-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Axuall Domain Security
  slug: axuall-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: axuall
tags:
- Company
- Healthcare
- Data
- Credentialing
- Artificial Intelligence
website: https://axuall.com
---
