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
    openapi_examples: partial
    protected_resource_metadata: documented
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.8
  scored_at: '2026-10-17'
api_count: 6
apis:
- description: Sovos provides tax compliance, e‑invoicing, and filing APIs.
  name: Sovos API
  slug: sovos-api-2
- baseURL: https://api.sovos.com
  baseurl_source: declared
  description: The Configurations API from Sovos — 24 operation(s) for configurations.
  name: Sovos Configurations API
  slug: sovos-configurations-api
- baseURL: https://api.sovos.com
  baseurl_source: declared
  description: The Documents API from Sovos — 1 operation(s) for documents.
  name: Sovos Documents API
  slug: sovos-documents-api
- baseURL: https://api.sovos.com
  baseurl_source: declared
  description: The Notifications API from Sovos — 3 operation(s) for notifications.
  name: Sovos Notifications API
  slug: sovos-notifications-api
- baseURL: https://api.sovos.com
  baseurl_source: declared
  description: The Oauth API from Sovos — 2 operation(s) for oauth.
  name: Sovos OAuth API
  slug: sovos-oauth-api
- baseURL: https://api.sovos.com
  baseurl_source: declared
  description: The Taxid Checks API from Sovos — 1 operation(s) for taxid checks.
  name: Sovos Taxid Checks API
  slug: sovos-taxid-checks-api
artifact_total: 15
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sovos/refs/heads/main/rules/sovos-rules.yml
  title: ''
  type: Spectral
  url: rules/sovos-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sovos/refs/heads/main/json-ld/sovos-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sovos-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sovos/refs/heads/main/vocabulary/sovos-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sovos-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sovos/refs/heads/main/data-model/sovos-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sovos-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sovos/refs/heads/main/conformance/sovos-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sovos-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sovos/refs/heads/main/well-known/sovos-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sovos-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sovos/refs/heads/main/hosts/sovos-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sovos-hosts.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sovos.com/
- group: start
  title: ''
  type: SignUp
  url: https://sovos.com/blog/vat/registering-branches-for-insurance-premium-tax/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sovos.com/privacy-policy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.sovos.com/en/quick-links/release-notes
- group: company
  title: ''
  type: Blog
  url: https://sovos.com/blog/trr/p171069/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.sovos.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sovos/refs/heads/main/security/sovos-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sovos-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sovos.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://sovos.com
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: Sovos provides a global, cloud‑based platform for tax compliance, regulatory reporting, and e‑invoicing. It helps enterprises automate indirect tax calculations, filing, and information reporting across more than 200 jurisdictions. The platform integrates with ERP, finance, and e‑commerce systems, offering APIs for real‑time tax determination, filing, and compliance analytics. Sovos serves Fortune‑500 companies and midsize businesses, delivering solutions for sales tax, VAT, GST, customs duties, and specialized reporting such as 1099, crypto tax, and unclaimed property.
image: https://sovos.com/wp-content/uploads/2021/07/sovos-cloud-global-tax-determination.jpg
json_schemas:
- name: GetDocumentsCountrycodeDocumentidNotificationsResponse
  property_count: 10
  slug: sovos-get-documents-countrycode-documentid-notifications-response
- name: GetNotificationsCountrycodeNotificationidResponse
  property_count: 5
  slug: sovos-get-notifications-countrycode-notificationid-response
- name: GetNotificationsCountrycodeResponse
  property_count: 24
  slug: sovos-get-notifications-countrycode-response
- name: PostOauthClientCredentialAccesstokenResponse
  property_count: 14
  slug: sovos-post-oauth-client-credential-accesstoken-response
- name: PostOauthTokenResponse
  property_count: 14
  slug: sovos-post-oauth-token-response
- name: PutNotificationsCountrycodeResponse
  property_count: 4
  slug: sovos-put-notifications-countrycode-response
jsonld:
- class_count: 9
  name: Sovos Context
  property_count: 25
  slug: sovos-context
layout: provider
modified: '2026-10-13'
name: Sovos
nav: Providers
network: true
overview: 'Sovos is listed with 6 APIs on the [APIs.io](https://apis.io/) network, including Configurations API, Documents API, Notifications API, and 3 more. Tagged areas include Tax, Compliance, Cloud, and Global.


  The Sovos catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Sovos'' developer surface includes signup flow, changelog, engineering blog, documentation, and 11 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Sovos API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: sovos-rules
score:
  band: emerging
  composite: 25.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 22.0
    contract_quality: 25.7
    developer_ergonomics: 11.9
    discoverability: 62.5
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Sovos Domain Security
  slug: sovos-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sovos
tags:
- Tax
- Compliance
- Cloud
- Global
website: https://sovos.com
---
