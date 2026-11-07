---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 28
  human_in_the_loop: 2
  name: Mail In A Box Agentic Access
  operation_count: 49
  slug: mail-in-a-box-agentic-access
  summary_line: 49 operations · 28 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://mailinabox.email/admin
  baseurl_source: declared
  description: DNS operations, which include adding custom records, adding a secondary nameserver and viewing all DNS records.
  name: Mail-in-a-Box DNS API
  slug: mail-in-a-box-dns-api
- baseURL: https://mailinabox.email/admin
  baseurl_source: declared
  description: Mail operations, which include getting all users, getting all aliases, adding/updating/removing users and aliases and getting all mail domains.
  name: Mail-in-a-Box Mail API
  slug: mail-in-a-box-mail-api
- baseURL: https://mailinabox.email/admin
  baseurl_source: declared
  description: Manage multi-factor authentication schemes. Currently, only TOTP is supported.
  name: Mail-in-a-Box MFA API
  slug: mail-in-a-box-mfa-api
- baseURL: https://mailinabox.email/admin
  baseurl_source: declared
  description: TLS (SSL) Certificates operations, which include checking certificate status and installing custom certificates.
  name: Mail-in-a-Box SSL API
  slug: mail-in-a-box-ssl-api
- baseURL: https://mailinabox.email/admin
  baseurl_source: declared
  description: System operations, which include system status checks, new version checks and reboot status.
  name: Mail-in-a-Box System API
  slug: mail-in-a-box-system-api
- baseURL: https://mailinabox.email/admin
  baseurl_source: declared
  description: Endpoints related to user authentication.
  name: Mail-in-a-Box User API
  slug: mail-in-a-box-user-api
- baseURL: https://mailinabox.email/admin
  baseurl_source: declared
  description: Static web hosting operations, which include getting domain information and updating domain root directories.
  name: Mail-in-a-Box Web API
  slug: mail-in-a-box-web-api
artifact_total: 23
common:
- group: agent
  href: https://artifacts.apis.io/mail-in-a-box/agentic-access/mail-in-a-box-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mail-in-a-box-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/mail-in-a-box/rules/mail-in-a-box-rules.yml
  title: ''
  type: Spectral
  url: rules/mail-in-a-box-rules.yml
- group: design
  href: https://artifacts.apis.io/mail-in-a-box/json-ld/mail-in-a-box-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mail-in-a-box-context.jsonld
- group: design
  href: https://artifacts.apis.io/mail-in-a-box/vocabulary/mail-in-a-box-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mail-in-a-box-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/mail-in-a-box/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/mail-in-a-box/data-model/mail-in-a-box-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mail-in-a-box-data-model.yml
- group: design
  href: https://artifacts.apis.io/mail-in-a-box/errors/mail-in-a-box-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mail-in-a-box-problem-types.yml
- group: design
  href: https://artifacts.apis.io/mail-in-a-box/conformance/mail-in-a-box-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mail-in-a-box-conformance.yml
- group: agent
  href: https://artifacts.apis.io/mail-in-a-box/llms/mail-in-a-box-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mail-in-a-box-llms.txt
- group: other
  href: https://artifacts.apis.io/mail-in-a-box/hosts/mail-in-a-box-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mail-in-a-box-hosts.yml
- group: build
  href: https://artifacts.apis.io/mail-in-a-box/packages/mail-in-a-box-packages.yml
  title: ''
  type: SDKs
  url: packages/mail-in-a-box-packages.yml
- group: build
  href: https://artifacts.apis.io/mail-in-a-box/packages/mail-in-a-box-packages.yml
  title: ''
  type: Packages
  url: packages/mail-in-a-box-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/JoshData
- group: auth
  href: https://artifacts.apis.io/mail-in-a-box/authentication/mail-in-a-box-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mail-in-a-box-authentication.yml
- group: auth
  href: https://artifacts.apis.io/mail-in-a-box/security/mail-in-a-box-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mail-in-a-box-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mailinabox.email/
created: '2026-10-27'
description: Mail-in-a-Box provides an easy-to-deploy, self-hosted mail server solution that includes a web-based control panel and a RESTful HTTP API for managing email accounts, DNS records, backups, and system monitoring. It aims to give users control over their email infrastructure while simplifying setup and maintenance.
json_schemas:
- name: MailAliasUpsertRequest
  property_count: 4
  slug: mail-in-a-box-mail-alias-upsert-request
- name: SSLCertificateInstallRequest
  property_count: 3
  slug: mail-in-a-box-sslcertificate-install-request
- name: SSLCSRGenerateResponse
  property_count: 0
  slug: mail-in-a-box-sslcsrgenerate-response
- name: SystemBackupConfigResponse
  property_count: 7
  slug: mail-in-a-box-system-backup-config-response
- name: SystemUpdatePackagesResponse
  property_count: 0
  slug: mail-in-a-box-system-update-packages-response
- name: WebDomain
  property_count: 5
  slug: mail-in-a-box-web-domain
jsonld:
- class_count: 43
  name: Mail In A Box Context
  property_count: 60
  slug: mail-in-a-box-context
layout: provider
modified: '2026-10-27'
name: Mail-in-a-Box
nav: Providers
network: true
overview: 'Mail-in-a-Box publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including DNS API, Mail API, MFA API, and 4 more. Tagged areas include Company, Email, Self-Hosted, Open Source, and Automation.


  The Mail-in-a-Box catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Mail-in-a-Box''s developer surface includes authentication and 15 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Mail-in-a-Box API Rules
  rule_count: 17
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 4
  slug: mail-in-a-box-rules
score:
  band: thin
  composite: 32.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 63.3
    developer_ergonomics: 20.8
    discoverability: 69.6
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 33.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/mail-in-a-box/mail-in-a-box-2026-11-03T135237.png
security:
- kind: authentication
  name: Mail In A Box Authentication
  slug: mail-in-a-box-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mail In A Box Domain Security
  slug: mail-in-a-box-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 5
skills:
- name: mail-in-a-box-add-dns-custom-record
  slug: mail-in-a-box-add-dns-custom-record
- name: mail-in-a-box-add-mail-user
  slug: mail-in-a-box-add-mail-user
- name: mail-in-a-box-check-and-reboot
  slug: mail-in-a-box-check-and-reboot
- name: mail-in-a-box-login-logout
  slug: mail-in-a-box-login-logout
- name: mail-in-a-box-web-manage-domains
  slug: mail-in-a-box-web-manage-domains
slug: mail-in-a-box
tags:
- Company
- Email
- Self-Hosted
- Open Source
- Automation
- Privacy
website: https://mailinabox.email/
---
