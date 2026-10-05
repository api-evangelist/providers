---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.1
  scored_at: '2026-10-04'
api_count: 4
apis:
- description: Netwrix provides a developer portal with documentation but no machine‑readable API contract was found.
  name: Netwrix API
  slug: netwrix-api-2
- baseURL: https://accessgovernance.company.com
  baseurl_source: declared
  description: The Data API from Netwrix — 1 operation(s) for data.
  name: Netwrix Data API
  slug: netwrix-data-api
- baseURL: https://accessgovernance.company.com
  baseurl_source: declared
  description: The Oauth API from Netwrix — 1 operation(s) for oauth.
  name: Netwrix OAuth API
  slug: netwrix-oauth-api
- baseURL: https://accessgovernance.company.com
  baseurl_source: declared
  description: The Token API from Netwrix — 2 operation(s) for token.
  name: Netwrix Token API
  slug: netwrix-token-api
artifact_total: 11
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/netwrix/refs/heads/main/well-known/netwrix-netwrix-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/netwrix-netwrix-security.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/netwrix/refs/heads/main/rules/netwrix-rules.yml
  title: ''
  type: Spectral
  url: rules/netwrix-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/netwrix/refs/heads/main/json-ld/netwrix-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/netwrix-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/netwrix/refs/heads/main/vocabulary/netwrix-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/netwrix-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/netwrix/refs/heads/main/data-model/netwrix-data-model.yml
  title: ''
  type: DataModel
  url: data-model/netwrix-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.netwrix.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/netwrix/refs/heads/main/security/netwrix-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/netwrix-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/netwrix/refs/heads/main/authentication/netwrix-authentication.yml
  title: ''
  type: Authentication
  url: authentication/netwrix-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/netwrix/refs/heads/main/conformance/netwrix-conformance.yml
  title: ''
  type: Conformance
  url: conformance/netwrix-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/netwrix/refs/heads/main/llms/netwrix-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/netwrix-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/netwrix/refs/heads/main/well-known/netwrix-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/netwrix-www-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/netwrix/refs/heads/main/well-known/netwrix-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/netwrix-status-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/netwrix/refs/heads/main/well-known/netwrix-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/netwrix-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/netwrix/refs/heads/main/well-known/netwrix-partner-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/netwrix-partner-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/netwrix/refs/heads/main/well-known/netwrix-customer-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/netwrix-customer-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/netwrix/refs/heads/main/well-known/netwrix-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/netwrix-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/netwrix/refs/heads/main/hosts/netwrix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/netwrix-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/netwrix/refs/heads/main/vendors/netwrix-vendors.yml
  title: ''
  type: Vendors
  url: vendors/netwrix-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.netwrix.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.netwrix.com/privacy.html
- group: company
  title: ''
  type: Newsroom
  url: https://netwrix.com/en/resources/news/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.netwrix.com/docs/1secure/configuration/registerconfig/1secure-classifier-setup-guide
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/netwrix
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/netwrix/refs/heads/main/security/netwrix-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/netwrix-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/netwrix/refs/heads/main/security/netwrix-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/netwrix-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/netwrix/refs/heads/main/security/netwrix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/netwrix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.netwrix.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.netwrix.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://netwrix.com/en/buy-now/
- group: operate
  title: ''
  type: Support
  url: https://netwrix.com/en/support/
- group: operate
  title: ''
  type: Contact
  url: https://netwrix.com/en/contact/
- group: company
  title: ''
  type: Blog
  url: https://netwrix.com/en/resources/blog/
coverage:
  detail: Documentation site uses Docusaurus JavaScript rendering, no machine‑readable spec found.
  evidence:
  - status: 200
    url: https://docs.netwrix.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-03'
description: Netwrix provides data security and governance solutions that help organizations protect, monitor, and manage their critical information assets. Their platform offers visibility into data usage, detects risky behavior, and ensures compliance with regulations such as GDPR, HIPAA, and PCI DSS. Netwrix serves enterprises across various industries, delivering tools for privileged access management, data loss prevention, and audit reporting, enabling IT teams to secure on-premises, cloud, and hybrid environments.
image: https://cdn.sanity.io/images/r09655ln/production/062d04e2794a7968846f6269de97062370fc5670-2400x1260.webp
json_schemas:
- name: PostTokenResponse
  property_count: 5
  slug: netwrix-post-token-response
jsonld:
- class_count: 1
  name: Netwrix Context
  property_count: 5
  slug: netwrix-context
layout: provider
modified: '2026-10-03'
name: Netwrix
nav: Providers
network: true
overview: 'Netwrix publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Data API, OAuth API, Token API, and 1 more. Tagged areas include Company, Data Security, Governance, Compliance, and Privileged Access.


  The Netwrix catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Netwrix''s developer surface includes authentication, getting-started guide, documentation, pricing, support, engineering blog, and 26 more developer resources.'
random_paper: 15
rules:
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Netwrix API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: netwrix-rules
score:
  band: thin
  composite: 35.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 51.2
    catalog_earned_first_party: 0.0
    catalog_gap: 63.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 19.3
    developer_ergonomics: 40.5
    discoverability: 71.4
    operational_transparency: 31.6
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
    score: 31.4
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Netwrix Authentication
  slug: netwrix-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Netwrix Domain Security
  slug: netwrix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Netwrix Vulnerability Disclosure
  slug: netwrix-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Netwrix Trust Center
  slug: netwrix-trust-center
  summary_line: SOC 2, GDPR
slug: netwrix
tags:
- Company
- Data Security
- Governance
- Compliance
- Privileged Access
website: https://www.netwrix.com
---
