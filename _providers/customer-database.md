---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 1.3
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 11
common:
- group: other
  title: ''
  type: Salesforce
  url: https://www.salesforce.com
- group: other
  title: ''
  type: HubSpot
  url: https://www.hubspot.com
- group: other
  title: ''
  type: Segment
  url: https://segment.com
- group: other
  title: ''
  type: Customer.io
  url: https://customer.io
- group: other
  title: ''
  type: Zendesk
  url: https://www.zendesk.com
- group: docs
  title: ''
  type: Schema.org Person
  url: https://schema.org/Person
- group: other
  title: ''
  type: vCard 4.0 (RFC 6350)
  url: https://datatracker.ietf.org/doc/html/rfc6350
- group: other
  title: ''
  type: SCIM 2.0
  url: https://datatracker.ietf.org/doc/html/rfc7643
- group: other
  title: ''
  type: SCIM 2.0 Protocol (RFC 7644)
  url: https://datatracker.ietf.org/doc/html/rfc7644
- group: docs
  title: ''
  type: Schema.org Vocabulary (JSON-LD)
  url: https://schema.org/version/latest/schemaorg-current-https.jsonld
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/customer-database-llms.txt
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/customer-database-vocabulary.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/customer-database-data-model.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/customer-record.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/customer-contact-point.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/customer-postal-address.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/customer-consent-record.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/customer-identity-link.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/customer-database-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/customer-database-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/customer-database-jsonschema-spectral-rules.yml
- group: build
  title: ''
  type: Examples
  url: examples/customer-record-example.json
- group: build
  title: ''
  type: Examples
  url: examples/customer-consent-record-example.json
- group: build
  title: ''
  type: Examples
  url: examples/customer-identity-link-example.json
coverage:
  checked: '2026-08-13'
  detail: 'Customer Database is an API Evangelist topic reference, not a company — apis.yml declares apis: [] and the profile exists to point at the vendors and open standards in the customer-data space, so there is no vendor, no host, and no API of its own to document. repair-api-bases.py returned "missing" and probe-domain-security.py returned "no-hosts" because no API entry names a base URL. The 14 artifacts added this pass are neutral, standards-grounded reference material (a vocabulary, a SCIM/vCard/Schema.org field crosswalk, five JSON Schemas, a JSON Structure, a JSON-LD context, a Spectral ruleset, examples and an llms.txt), not a vendor surface. See the individual vendor repositories — salesforce, hubspot, segment, customer-io, zendesk — for real APIs.'
  evidence:
  - status: 200
    url: https://raw.githubusercontent.com/api-evangelist/customer-database/refs/heads/main/apis.yml
  - status: 200
    url: https://schema.org/version/latest/schemaorg-current-https.jsonld
  - status: 200
    url: https://www.rfc-editor.org/rfc/rfc7643.txt
  reason: not-a-software-company
  state: none
created: '2024-01-15'
description: Customer Database is the topic dedicated to APIs, schemas, vocabularies, and reference designs for the systems of record that store customer identity, profile, contact, preference, consent, and account data. A customer database underpins CRM, marketing automation, customer data platforms (CDPs), customer service, billing, and analytics use cases, and is increasingly expected to support API-first access, schema-on-write data quality, real-time eventing, GDPR/CCPA consent and erasure workflows, and identity resolution across web, mobile, and offline channels. This repository tracks the vendors, standards, and patterns that make customer data accessible, governed, and portable.
examples:
- key_count: 12
  name: Customer Consent Record Example
  slug: customer-consent-record-example
- key_count: 10
  name: Customer Identity Link Example
  slug: customer-identity-link-example
- key_count: 22
  name: Customer Record Example
  slug: customer-record-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/customer-database.png
json_schemas:
- name: Customer Consent Record
  property_count: 13
  slug: customer-consent-record
- name: Customer Contact Point
  property_count: 10
  slug: customer-contact-point
- name: Customer Identity Link
  property_count: 10
  slug: customer-identity-link
- name: Customer Postal Address
  property_count: 10
  slug: customer-postal-address
- name: Customer Record
  property_count: 27
  slug: customer-record
json_structures:
- name: Customer Database Structure
  property_count: 25
  slug: customer-database-structure
jsonld:
- class_count: 52
  name: Customer Database Context
  property_count: 22
  slug: customer-database-context
layout: provider
modified: '2026-08-13'
name: Customer Database
nav: Providers
network: true
overview: 'Customer Database is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Account, Consent, Contacts, CRM, and Customer Data.


  The Customer Database catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Customer Database''s developer surface includes code examples and 23 more developer resources.'
random_paper: 5
rules:
- effective_rule_count: 15
  extends: []
  name: Customer Database API Rules
  rule_count: 15
  severity_counts:
    error: 9
    hint: 0
    info: 0
    warn: 6
  slug: customer-database-jsonschema-spectral-rules
score:
  band: emerging
  composite: 15.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 49.3
    catalog_earned_first_party: 0.0
    catalog_gap: 65.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 34.1
    contract_quality: 21.3
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 34.1
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 15.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/customer-database/refs/heads/main/screenshots/customer-database-2026-06-20T175347.png
slug: customer-database
tags:
- Account
- Consent
- Contacts
- CRM
- Customer Data
- Customer Data Platform
- Customers
- Database
- GDPR
- Identity
- Profiles
- Schema
---
