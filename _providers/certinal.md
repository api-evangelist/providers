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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-10-17'
api_count: 2
apis:
- baseURL: https://esign-staging.certinal.com
  baseurl_source: declared
  description: The Auth API from Certinal — 1 operation(s) for auth.
  name: Certinal Auth API
  slug: certinal-auth-api
- baseURL: https://esign-staging.certinal.com
  baseurl_source: declared
  description: The Rssp API from Certinal — 1 operation(s) for rssp.
  name: Certinal Rssp API
  slug: certinal-rssp-api
artifact_total: 8
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/certinal/refs/heads/main/vendors/certinal-vendors.yml
  title: ''
  type: Vendors
  url: vendors/certinal-vendors.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/certinal/refs/heads/main/rules/certinal-rules.yml
  title: ''
  type: Spectral
  url: rules/certinal-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/certinal/refs/heads/main/json-ld/certinal-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/certinal-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/certinal/refs/heads/main/vocabulary/certinal-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/certinal-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/certinal/refs/heads/main/data-model/certinal-data-model.yml
  title: ''
  type: DataModel
  url: data-model/certinal-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/certinal/refs/heads/main/authentication/certinal-authentication.yml
  title: ''
  type: Authentication
  url: authentication/certinal-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/certinal/refs/heads/main/conformance/certinal-conformance.yml
  title: ''
  type: Conformance
  url: conformance/certinal-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/certinal/refs/heads/main/hosts/certinal-hosts.yml
  title: ''
  type: Hosts
  url: hosts/certinal-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.certinal.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.certinal.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.certinal.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.certinal.com/press
- group: docs
  title: ''
  type: Documentation
  url: https://certinal.stoplight.io/docs/api/72b66de24898e-introduction
- group: company
  title: ''
  type: Blog
  url: https://www.certinal.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/certinal/refs/heads/main/security/certinal-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/certinal-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://certinal.com/
coverage:
  checked: '2026-10-16'
  detail: Certinal documentation is rendered via JavaScript with no machine‑readable spec discovered.
  evidence:
  - status: 404
    url: https://certinal.stoplight.io/docs/api/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-16'
description: Certinal provides a Healthcare Consent & Compliance Platform that digitizes consent capture, electronic signatures, and patient intake, integrating directly with EHR systems such as Epic, Cerner, MEDITECH, and OpenEMR. The platform is designed for healthcare organizations to meet regulatory requirements including HIPAA, 21 CFR Part 11, CMS‑0053‑F, DPDP, and PDPA, and to automate consent workflows across surgical, clinical trial, telehealth, and general treatment contexts.
json_schemas:
- name: PutAuthV1UsersUseridRequest
  property_count: 10
  slug: certinal-put-auth-v1-users-userid-request
- name: PutAuthV1UsersUseridResponse
  property_count: 2
  slug: certinal-put-auth-v1-users-userid-response
jsonld:
- class_count: 2
  name: Certinal Context
  property_count: 10
  slug: certinal-context
layout: provider
modified: '2026-10-16'
name: Certinal
nav: Providers
network: true
overview: 'Certinal is listed with 2 APIs on the [APIs.io](https://apis.io/) network: Auth API and Rssp API. Tagged areas include Healthcare, Consent, Compliance, E-Signature, and EHR Integration.


  The Certinal catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Certinal''s developer surface includes authentication, pricing, documentation, engineering blog, and 12 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Certinal API Rules
  rule_count: 12
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 0
  slug: certinal-rules
score:
  band: thin
  composite: 26.2
  coverage:
    artifact_dirs: 14
    catalog_earned: 57.0
    catalog_earned_first_party: 0.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 19.7
    contract_quality: 23.5
    developer_ergonomics: 23.8
    discoverability: 64.3
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 19.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Certinal Authentication
  slug: certinal-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Certinal Domain Security
  slug: certinal-domain-security
  summary_line: TLSv1.3 · DMARC
slug: certinal
tags:
- Healthcare
- Consent
- Compliance
- E-Signature
- EHR Integration
- Regulatory
website: https://certinal.com/
---
