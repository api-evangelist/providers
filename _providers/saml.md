---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Saml Agentic Access
  operation_count: 5
  slug: saml-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 1
apis:
- baseURL: https://idp.example.com
  baseurl_source: spec
  description: SAML 2.0 metadata retrieval.
  name: SAML Metadata API
  slug: saml-metadata-api
- baseURL: https://idp.example.com
  baseurl_source: spec
  description: SAML 2.0 Single Logout operations.
  name: SAML SLO API
  slug: saml-slo-api
- baseURL: https://idp.example.com
  baseurl_source: spec
  description: SAML 2.0 Single Sign-On operations.
  name: SAML SSO API
  slug: saml-sso-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SAML 2.0 SSO HTTP Bindings Metadata API
  slug: open-saml-metadata-api
- collection_type: open
  name: SAML 2.0 SSO HTTP Bindings Metadata SLO API
  slug: open-saml-slo-api
- collection_type: open
  name: SAML 2.0 HTTP Bindings Metadata SSO API
  slug: open-saml-sso-api
- collection_type: open
  name: SAML 2.0 SSO HTTP Bindings
  slug: open-saml-sso-bindings
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/saml-agentic-access.yml
- group: docs
  title: SAML 2.0 OASIS Standard
  type: Documentation
  url: https://www.oasis-open.org/standard/saml/
- group: docs
  title: SAML 2.0 Technical Overview
  type: Documentation
  url: https://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html
- group: docs
  title: SAML 2.0 Core Specification
  type: Documentation
  url: https://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf
- group: docs
  title: SAML 2.0 Bindings Specification
  type: Documentation
  url: https://docs.oasis-open.org/security/saml/v2.0/saml-bindings-2.0-os.pdf
- group: docs
  title: SAML 2.0 Profiles Specification
  type: Documentation
  url: https://docs.oasis-open.org/security/saml/v2.0/saml-profiles-2.0-os.pdf
- group: docs
  title: SAML 2.0 EntityDescriptor Metadata
  type: JSONSchema
  url: json-schema/saml-entity-descriptor.json
- group: docs
  title: SAML 2.0 AuthnRequest
  type: JSONSchema
  url: json-schema/saml-authn-request.json
- group: docs
  title: SAML 2.0 Assertion
  type: JSONSchema
  url: json-schema/saml-assertion.json
- group: design
  title: SAML 2.0 JSON-LD Context
  type: JSONLDContext
  url: json-ld/saml-context.jsonld
- group: design
  title: SAML 2.0 Assertion Structure
  type: JSONStructure
  url: json-structure/saml-assertion-structure.json
- group: design
  title: SAML API Spectral Rules
  type: SpectralRules
  url: rules/saml-rules.yml
- group: build
  title: SAML SSO HTTP Redirect Binding Example
  type: Examples
  url: examples/saml-sso-redirect-example.json
- group: design
  title: SAML 2.0 Vocabulary
  type: Vocabulary
  url: vocabulary/saml-vocabulary.yml
created: '2025-01-01'
description: SAML (Security Assertion Markup Language) is an XML-based open standard for exchanging authentication and authorization data between identity providers and service providers. Ratified as an OASIS Standard in March 2005, SAML 2.0 enables single sign-on (SSO) across different applications and domains, reducing the need for users to manage multiple sets of credentials. It uses XML digital signatures and encryption to secure assertions exchanged between Identity Providers (IdP) and Service Providers (SP).
examples:
- key_count: 4
  name: Saml Sso Redirect Example
  slug: saml-sso-redirect-example
finops:
- name: Saml Finops
  service_category: API
  slug: saml-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/saml.png
json_schemas:
- name: SAML 2.0 Assertion
  property_count: 8
  slug: saml-assertion
- name: SAML 2.0 AuthnRequest
  property_count: 13
  slug: saml-authn-request
- name: SAML 2.0 EntityDescriptor Metadata
  property_count: 8
  slug: saml-entity-descriptor
json_structures:
- name: Saml Assertion Structure
  property_count: 0
  slug: saml-assertion-structure
jsonld:
- class_count: 7
  name: Saml Context
  property_count: 35
  slug: saml-context
layout: provider
modified: '2026-05-19'
name: SAML
nav: Providers
network: true
overview: 'SAML publishes 3 APIs on the [APIs.io](https://apis.io/) network: Metadata API, SLO API, and SSO API. Tagged areas include Authentication, Authorization, Federation, Identity Management, and Open Standard.


  The SAML catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SAML''s developer surface includes documentation, code examples, and 12 more developer resources.'
plans:
- name: Saml Plans Pricing
  plan_count: 3
  slug: saml-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Saml Rate Limits
  slug: saml-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: SAML API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: saml-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: SAML API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 5
  slug: saml-rules
score:
  band: thin
  composite: 28.9
  coverage:
    artifact_dirs: 13
    catalog_gap: 61.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 56.8
    developer_ergonomics: 9.5
    discoverability: 51.9
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 28.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/saml/refs/heads/main/screenshots/saml-2026-06-20T193358.png
slug: saml
tags:
- Authentication
- Authorization
- Federation
- Identity Management
- Open Standard
- Security
- Single Sign-On
- SSO
- XML
website: https://www.oasis-open.org/standard/saml/
---
