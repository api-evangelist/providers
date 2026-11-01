---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://uk.api.atto.co
  baseurl_source: declared
  description: 'The ID API as documented publicly: 36 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: The ID API
  slug: theidco-api
artifact_total: 9
asyncapis:
- description: ''
  name: Theidco Webhooks
  slug: theidco-webhooks
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.atto.co/content/docs/guides/introduction/apis/getting-started
- group: operate
  href: https://artifacts.apis.io/theidco/rate-limits/theidco-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/theidco-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/theidco/rules/theidco-rules.yml
  title: ''
  type: Spectral
  url: rules/theidco-rules.yml
- group: design
  href: https://artifacts.apis.io/theidco/json-ld/theidco-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/theidco-context.jsonld
- group: design
  href: https://artifacts.apis.io/theidco/vocabulary/theidco-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/theidco-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/theidco/asyncapi/theidco-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/theidco-webhooks.yml
- group: design
  href: https://artifacts.apis.io/theidco/data-model/theidco-data-model.yml
  title: ''
  type: DataModel
  url: data-model/theidco-data-model.yml
- group: operate
  href: https://artifacts.apis.io/theidco/changelog/theidco-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/theidco-changelog.yml
- group: auth
  href: https://artifacts.apis.io/theidco/authentication/theidco-authentication.yml
  title: ''
  type: Authentication
  url: authentication/theidco-authentication.yml
- group: design
  href: https://artifacts.apis.io/theidco/conformance/theidco-conformance.yml
  title: ''
  type: Conformance
  url: conformance/theidco-conformance.yml
- group: other
  href: https://artifacts.apis.io/theidco/a2a/theidco-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/theidco-a2a.yml
- group: agent
  href: https://artifacts.apis.io/theidco/well-known/theidco-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/theidco-well-known.yml
- group: other
  href: https://artifacts.apis.io/theidco/hosts/theidco-hosts.yml
  title: ''
  type: Hosts
  url: hosts/theidco-hosts.yml
- group: other
  href: https://artifacts.apis.io/theidco/vendors/theidco-vendors.yml
  title: ''
  type: Vendors
  url: vendors/theidco-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TheIDCo
- group: auth
  href: https://artifacts.apis.io/theidco/security/theidco-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/theidco-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://theidco.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.atto.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.atto.co/
- group: operate
  title: ''
  type: Support
  url: https://www.atto.co/about/contact
- group: company
  title: ''
  type: Blog
  url: https://www.atto.co/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atto.co/policies/privacy-policy
coverage:
  checked: '2026-10-21'
  detail: Documentation at https://docs.atto.co renders a JavaScript shell with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://docs.atto.co
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: The ID Co. provides a fintech platform leveraging bank data to redefine credit risk. Through its Atto product, it offers open banking data integration for onboarding, collections, and risk assessment, serving businesses seeking to improve conversion and reduce risk. Registered with FCA and ICO, The ID Co. emphasizes data protection and compliance, delivering API-driven solutions for credit risk lifecycle management.
image: https://cdn.prod.website-files.com/5e4ab9466903578f21cc4e19/5e4be0c2030f2cb9371ceac1_Thumbnails%201200x630.png
json_schemas:
- name: GetConnectInvitationsV1InvitationidResponse
  property_count: 3
  slug: theidco-get-connect-invitations-v1-invitationid-response
- name: PostConnectInvitationsV1Response
  property_count: 1
  slug: theidco-post-connect-invitations-v1-response
jsonld:
- class_count: 2
  name: Theidco Context
  property_count: 3
  slug: theidco-context
layout: provider
modified: '2026-10-21'
name: The ID
nav: Providers
network: true
overview: 'The ID is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Credit Risk, Open Banking, and Data Protection.


  The The ID catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  The ID''s developer surface includes getting-started guide, changelog, authentication, documentation, support, engineering blog, and 16 more developer resources.'
random_paper: 16
rate_limits:
- limit_count: 2
  name: Theidco Rate Limits
  slug: theidco-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: The ID API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: theidco-rules
score:
  band: thin
  composite: 34.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 64.8
    catalog_earned_first_party: 8.0
    catalog_gap: 50.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 29.2
    developer_ergonomics: 50.0
    discoverability: 66.1
    operational_transparency: 50.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 13
      marker_coverage: 100.0
      total: 13
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 16.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Theidco Authentication
  slug: theidco-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Theidco Domain Security
  slug: theidco-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: theidco
tags:
- Company
- Fintech
- Credit Risk
- Open Banking
- Data Protection
website: https://theidco.com/
---
