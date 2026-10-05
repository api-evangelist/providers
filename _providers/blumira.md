---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.7
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 18
  human_in_the_loop: 18
  name: Blumira Agentic Access
  operation_count: 59
  slug: blumira-agentic-access
  summary_line: 59 operations · 18 acting · 18 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.blumira.com
  baseurl_source: declared
  description: The Health API from Blumira — 1 operation(s) for health.
  name: Blumira Health API
  slug: blumira-health-api
- baseURL: https://api.blumira.com
  baseurl_source: declared
  description: The Msp API from Blumira — 26 operation(s) for msp.
  name: Blumira Msp API
  slug: blumira-msp-api
- baseURL: https://api.blumira.com
  baseurl_source: declared
  description: The Org API from Blumira — 23 operation(s) for org.
  name: Blumira Org API
  slug: blumira-org-api
- baseURL: https://api.blumira.com
  baseurl_source: declared
  description: The Resolutions API from Blumira — 1 operation(s) for resolutions.
  name: Blumira Resolutions API
  slug: blumira-resolutions-api
artifact_total: 17
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blumira/refs/heads/main/agentic-access/blumira-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/blumira-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/blumira/refs/heads/main/plans/blumira-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/blumira-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blumira/refs/heads/main/rules/blumira-rules.yml
  title: ''
  type: Spectral
  url: rules/blumira-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blumira/refs/heads/main/json-ld/blumira-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/blumira-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blumira/refs/heads/main/vocabulary/blumira-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/blumira-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blumira/refs/heads/main/data-model/blumira-data-model.yml
  title: ''
  type: DataModel
  url: data-model/blumira-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/blumira/refs/heads/main/changelog/blumira-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/blumira-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blumira/refs/heads/main/conventions/blumira-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/blumira-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blumira/refs/heads/main/conventions/blumira-conventions.yml
  title: ''
  type: Conventions
  url: conventions/blumira-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://app.drata.com/trust/dec6cfdb-01d8-48e0-9aea-d34a48e20589
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blumira/refs/heads/main/errors/blumira-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/blumira-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blumira/refs/heads/main/conformance/blumira-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blumira-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blumira/refs/heads/main/well-known/blumira-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/blumira-app-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blumira/refs/heads/main/well-known/blumira-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blumira-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blumira/refs/heads/main/hosts/blumira-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blumira-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blumira/refs/heads/main/vendors/blumira-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blumira-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/blumira/refs/heads/main/packages/blumira-packages.yml
  title: ''
  type: SDKs
  url: packages/blumira-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/blumira/refs/heads/main/packages/blumira-packages.yml
  title: ''
  type: Packages
  url: packages/blumira-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blumira.com/terms-of-use
- group: operate
  title: ''
  type: StatusPage
  url: https://status.blumira.com/
- group: auth
  title: ''
  type: Security
  url: https://www.blumira.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blumira.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.blumira.com/news
- group: start
  title: ''
  type: GettingStarted
  url: https://www.blumira.com/blog/detect-and-respond-to-azure-threats-with-blumira-easy-cloud-siem-setup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Blumira
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blumira/refs/heads/main/authentication/blumira-authentication.yml
  title: ''
  type: Authentication
  url: authentication/blumira-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blumira/refs/heads/main/security/blumira-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/blumira-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blumira/refs/heads/main/security/blumira-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blumira-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.blumira.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.blumira.com/docs
- group: operate
  title: ''
  type: Support
  url: https://support.blumira.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.blumira.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.blumira.com/pricing
created: '2026-09-29'
description: Blumira provides a security operations platform that helps IT teams detect, investigate, and respond to threats across cloud, on‑premise, and hybrid environments. It offers features such as automated alerting, evidence‑rich case management, integrations with major cloud providers, and a developer‑friendly API for ingesting logs, managing detections, and automating response actions. The platform aims to simplify security operations while delivering comprehensive visibility and compliance reporting.
image: https://www.blumira.com/hubfs/Comprehensive%20Cybersecurity.png
json_schemas:
- name: action_catalog
  property_count: 1
  slug: blumira-action-catalog
- name: request_action_dispatch
  property_count: 4
  slug: blumira-request-action-dispatch
- name: response_command_record
  property_count: 8
  slug: blumira-response-command-record
- name: response_finding_evidence
  property_count: 5
  slug: blumira-response-finding-evidence
- name: webhook_endpoint_create_record
  property_count: 8
  slug: blumira-webhook-endpoint-create-record
- name: webhook_endpoint_update_record
  property_count: 9
  slug: blumira-webhook-endpoint-update-record
jsonld:
- class_count: 56
  name: Blumira Context
  property_count: 176
  slug: blumira-context
layout: provider
modified: '2026-09-29'
name: Blumira
nav: Providers
network: true
overview: 'Blumira publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Health API, Msp API, Org API, and 1 more. Tagged areas include Company, Security, Software-as-a-Service, Cloud, and IT.


  The Blumira catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Blumira''s developer surface includes changelog, getting-started guide, authentication, documentation, support, engineering blog, pricing, and 26 more developer resources.'
plans:
- name: Blumira Plans Pricing
  plan_count: 3
  slug: blumira-plans-pricing
random_paper: 0
rules:
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Blumira API Rules
  rule_count: 9
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 2
  slug: blumira-rules
score:
  band: strong
  composite: 59.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 22.0
    contract_quality: 59.6
    developer_ergonomics: 47.6
    discoverability: 67.9
    operational_transparency: 47.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: true
    score: 27.8
security:
- kind: authentication
  name: Blumira Authentication
  slug: blumira-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Blumira Domain Security
  slug: blumira-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Blumira Trust Center
  slug: blumira-trust-center
  summary_line: SOC 2, ISO 27001
slug: blumira
tags:
- Company
- Security
- Software-as-a-Service
- Cloud
- IT
website: https://www.blumira.com
---
