---
agent_readiness:
  band: agent-aware
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-10-17'
api_count: 3
apis:
- baseURL: https://apiproxy.coreview.com
  baseurl_source: declared
  description: The Connect API from CoreView — 1 operation(s) for connect.
  name: CoreView Connect API
  slug: coreview-connect-api
- baseURL: https://apiproxy.coreview.com
  baseurl_source: declared
  description: The Public API from CoreView — 1 operation(s) for public.
  name: CoreView Public API
  slug: coreview-public-api
- baseURL: https://apiproxy.coreview.com
  baseurl_source: declared
  description: The Teams API from CoreView — 1 operation(s) for teams.
  name: CoreView Teams API
  slug: coreview-teams-api
artifact_total: 11
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/coreview/refs/heads/main/rate-limits/coreview-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/coreview-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coreview/refs/heads/main/rules/coreview-rules.yml
  title: ''
  type: Spectral
  url: rules/coreview-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coreview/refs/heads/main/json-ld/coreview-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/coreview-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coreview/refs/heads/main/vocabulary/coreview-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/coreview-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coreview/refs/heads/main/data-model/coreview-data-model.yml
  title: ''
  type: DataModel
  url: data-model/coreview-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.coreview.com/security
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coreview/refs/heads/main/conformance/coreview-conformance.yml
  title: ''
  type: Conformance
  url: conformance/coreview-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coreview/refs/heads/main/hosts/coreview-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coreview-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coreview/refs/heads/main/vendors/coreview-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coreview-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coreview.com/terms-conditions
- group: operate
  title: ''
  type: StatusPage
  url: https://status.coreview.com/
- group: auth
  title: ''
  type: Security
  url: https://www.coreview.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coreview.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.coreview.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.coreview.com/newsroom
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.coreview.com/en_US/release-notes
- group: company
  title: ''
  type: Blog
  url: https://www.coreview.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://help.coreview.com/en_US/onboarding-process/onboarding-registration
- group: docs
  title: ''
  type: Documentation
  url: https://help.coreview.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coreview/refs/heads/main/security/coreview-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/coreview-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coreview/refs/heads/main/security/coreview-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coreview-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.coreview.com/
coverage:
  checked: '2026-10-11'
  detail: Helpjuice knowledge base provides API documentation but no machine‑readable spec such as OpenAPI, GraphQL or AsyncAPI.
  evidence:
  - status: 200
    url: https://help.coreview.com/en_US/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-11'
description: CoreView provides Microsoft 365 cyber resilience solutions for enterprises, offering tools for policy enforcement, configuration resilience, privilege management, and tenant segmentation. Their platform helps organizations secure, manage, and automate Microsoft 365 environments, delivering risk insights, backup, and compliance across thousands of settings.
json_schemas:
- name: PostConnectTokenRequest
  property_count: 2
  slug: coreview-post-connect-token-request
- name: PostConnectTokenResponse
  property_count: 4
  slug: coreview-post-connect-token-response
- name: PostTeamsTeamidChannelsChannelidMessagesRequest
  property_count: 2
  slug: coreview-post-teams-teamid-channels-channelid-messages-request
jsonld:
- class_count: 3
  name: Coreview Context
  property_count: 7
  slug: coreview-context
layout: provider
modified: '2026-10-11'
name: CoreView
nav: Providers
network: true
overview: 'CoreView is listed with 3 APIs on the [APIs.io](https://apis.io/) network: Connect API, Public API, and Teams API. Tagged areas include Microsoft 365, Tenant Resilience, Configuration Management, Identity Security, and License Optimization.


  The CoreView catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CoreView''s developer surface includes pricing, changelog, engineering blog, getting-started guide, documentation, and 17 more developer resources.'
random_paper: 10
rate_limits:
- limit_count: 1
  name: Coreview Rate Limits
  slug: coreview-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: CoreView API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: coreview-rules
score:
  band: thin
  composite: 37.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 20.6
    developer_ergonomics: 23.8
    discoverability: 69.6
    operational_transparency: 63.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Coreview Domain Security
  slug: coreview-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Coreview Trust Center
  slug: coreview-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27018, GDPR
slug: coreview
tags:
- Microsoft 365
- Tenant Resilience
- Configuration Management
- Identity Security
- License Optimization
- SharePoint Control
- Enterprise Saas
website: https://www.coreview.com/
---
